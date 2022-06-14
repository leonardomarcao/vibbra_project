"""The Revenue Resource File."""
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from app.api.schemas import RevenueSchema, RevenueCategorySchema
from app.models import Revenue, RevenueCategory, Customer
from app.extensions import db
from app.commons.pagination import paginate


class RevenueResource(Resource):
    """Single object resource.

    ---
    get:
      tags:
        - Revenue
      summary: Get a revenue
      description: Get a single revenue by ID
      parameters:
        - in: path
          name: revenue_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  revenue: RevenueSchema
        404:
          description: revenue does not exists
    put:
      tags:
        - Revenue
      summary: Update a revenue
      description: Update a single revenue by ID
      parameters:
        - in: path
          name: revenue_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              RevenueSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: revenue updated
                  revenue: RevenueSchema
        404:
          description: revenue does not exists
    delete:
      tags:
        - Revenue
      summary: Delete a revenue
      description: Delete a single revenue by ID
      parameters:
        - in: path
          name: revenue_id
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
                    example: revenue deleted
        404:
          description: revenue does not exists
    """

    method_decorators = [jwt_required()]

    @staticmethod
    def get(revenue_id):
        """The get method revenue resource."""
        schema = RevenueSchema()
        revenue = Revenue.query.get_or_404(revenue_id)
        return {"revenue": schema.dump(revenue)}

    @staticmethod
    def put(revenue_id):
        """The put method revenue resource."""
        schema = RevenueSchema(partial=True)
        revenue = Revenue.query.get_or_404(revenue_id)
        revenue = schema.load(request.json, instance=revenue)

        db.session.commit()

        return {"msg": "revenue updated", "revenue": schema.dump(revenue)}

    @staticmethod
    def delete(revenue_id):
        """The delete method revenue resource."""
        revenue = Revenue.query.get_or_404(revenue_id)
        db.session.delete(revenue)
        db.session.commit()

        return {"msg": "revenue deleted"}


class RevenueList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - Revenue
      summary: Get a list of revenues
      description: Get a list of paginated revenues
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
                          $ref: '#/components/schemas/RevenueSchema'
    post:
      tags:
        - Revenue
      summary: Create a revenue
      description: Create a new revenue
      requestBody:
        content:
          application/json:
            schema:
              RevenueSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: revenue created
                  revenue: RevenueSchema
    """

    method_decorators = [jwt_required()]

    @staticmethod
    def get():
        """The get revenue list resource."""
        schema = RevenueSchema(many=True)
        query = Revenue.query
        return paginate(query, schema)

    @staticmethod
    def post():
        """The post revenue list resource."""
        schema = RevenueSchema()
        revenue = schema.load(request.json)

        # check if customer id informed exists
        if not Customer.query.filter_by(id=request.json["customer_id"]).one_or_none():
            return {"error": "informed customer id dont exist"}

        # check if revenue category id informed exists
        if not RevenueCategory.query.filter_by(
            id=request.json["category_id"]
        ).one_or_none():
            return {"error": "informed category id dont exist"}

        db.session.add(revenue)
        db.session.commit()

        return {"msg": "revenue created", "revenue": schema.dump(revenue)}, 201


class RevenueCategoryResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - Revenue Category
      summary: Get a revenue_category
      description: Get a single revenue_category by ID
      parameters:
        - in: path
          name: revenue_category_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  revenue_category: RevenueCategorySchema
        404:
          description: revenue_category does not exists
    put:
      tags:
        - Revenue Category
      summary: Update a revenue_category
      description: Update a single revenue_category by ID
      parameters:
        - in: path
          name: revenue_category_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              RevenueCategorySchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: revenue_category updated
                  revenue_category: RevenueCategorySchema
        404:
          description: revenue_category does not exists
    delete:
      tags:
        - Revenue Category
      summary: Delete a revenue_category
      description: Delete a single revenue_category by ID
      parameters:
        - in: path
          name: revenue_category_id
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
                    example: revenue_category deleted
        404:
          description: revenue_category does not exists
    """

    method_decorators = [jwt_required()]

    @staticmethod
    def get(revenue_category_id):
        """The get revenue category resource."""
        schema = RevenueCategorySchema()
        revenue_category = RevenueCategory.query.get_or_404(revenue_category_id)
        return {"revenue_category": schema.dump(revenue_category)}

    @staticmethod
    def put(revenue_category_id):
        """The put revenue category resource."""
        schema = RevenueCategorySchema(partial=True)
        revenue_category = RevenueCategory.query.get_or_404(revenue_category_id)
        revenue_category = schema.load(request.json, instance=revenue_category)

        db.session.commit()

        return {
            "msg": "revenue_category updated",
            "revenue_category": schema.dump(revenue_category),
        }

    @staticmethod
    def delete(revenue_category_id):
        """The method delete revenue category resource."""
        revenue_category = RevenueCategory.query.get_or_404(revenue_category_id)
        db.session.delete(revenue_category)
        db.session.commit()

        return {"msg": "revenue_category deleted"}


class RevenueCategoryList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - Revenue Category
      summary: Get a list of revenue_categorys
      description: Get a list of paginated revenue_categorys
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
                          $ref: '#/components/schemas/RevenueCategorySchema'
    post:
      tags:
        - Revenue Category
      summary: Create a revenue_category
      description: Create a new revenue_category
      requestBody:
        content:
          application/json:
            schema:
              RevenueCategorySchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: revenue_category created
                  revenue_category: RevenueCategorySchema
    """

    method_decorators = [jwt_required()]

    @staticmethod
    def get():
        """The get method revenue category list resource."""
        schema = RevenueCategorySchema(many=True)
        query = RevenueCategory.query
        return paginate(query, schema)

    @staticmethod
    def post():
        """The post method revenue category list resource."""
        schema = RevenueCategorySchema()
        revenue_category = schema.load(request.json)

        db.session.add(revenue_category)
        db.session.commit()

        return {
            "msg": "revenue_category created",
            "revenue_category": schema.dump(revenue_category),
        }, 201
