from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.api.schemas import CustomerSchema
from app.models import Customer
from app.extensions import db
from app.commons.pagination import paginate


class CustomerResource(Resource):
    """Single object resource.

    ---
    get:
      tags:
        - Customer
      summary: Get a customer
      description: Get a single customer by ID
      parameters:
        - in: query
          name: id
          description: the id of customer
          required: false
          schema:
            type: integer
        - in: query
          name: name
          description: the legal name of customer
          required: false
          schema:
            type: string
        - in: query
          name: cnpj
          description: the cnpj of customer
          required: false
          schema:
            type: string
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  customer: CustomerSchema
        404:
          description: customer does not exists
    put:
      tags:
        - Customer
      summary: Update a customer
      description: Update a single customer by ID
      parameters:
        - in: path
          name: customer_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              CustomerSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: customer updated
                  customer: CustomerSchema
        404:
          description: customer does not exists
    delete:
      tags:
        - Customer
      summary: Delete a customer
      description: Delete a single customer by ID
      parameters:
        - in: path
          name: customer_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: customer deleted
        404:
          description: customer does not exists
    """

    method_decorators = [jwt_required()]

    @staticmethod
    def get():
        """The get revenue resource."""
        args = request.args
        cnpj = args.get("cnpj")
        id = args.get("id")
        name = args.get("name")
        schema = CustomerSchema()
        query = Customer.query
        if cnpj:
            query = query.filter_by(cnpj=cnpj)
        if id:
            query = query.filter_by(id=id)
        if name:
            query = query.filter_by(legal_name=name)
        customer = query.one_or_none()
        if not customer:
            return {"error": "customer not found"}
        return {"customer": schema.dump(customer)}

    @staticmethod
    def put(customer_id):
        """The put revenue resource."""
        schema = CustomerSchema(partial=True)
        customer = Customer.query.get_or_404(customer_id)
        customer = schema.load(request.json, instance=customer)

        db.session.commit()

        return {"msg": "customer updated", "customer": schema.dump(customer)}

    @staticmethod
    def delete(customer_id):
        """The delete revenue resource."""
        customer = Customer.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()

        return {"msg": "customer deleted"}


class CustomerList(Resource):
    """Creation and get_all.

    ---
    get:
      tags:
        - Customer
      summary: Get a list of customers
      description: Get a list of paginated customers
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/CustomerSchema'
    post:
      tags:
        - Customer
      summary: Create a customer
      description: Create a new customer
      requestBody:
        content:
          application/json:
            schema:
              CustomerSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: customer created
                  customer: CustomerSchema
    """

    method_decorators = [jwt_required()]

    @staticmethod
    def get():
        """The get of revenue list resource."""
        schema = CustomerSchema(many=True)
        query = Customer.query
        return paginate(query, schema)

    @staticmethod
    def post():
        """The post of revenue list resource."""
        schema = CustomerSchema()
        customer = schema.load(request.json)

        db.session.add(customer)
        db.session.commit()

        return {"msg": "customer created", "customer": schema.dump(customer)}, 201
