from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sqlalchemy.sql.expression import extract
from app.models import Revenue, Customer
import datetime


class ReportTotalRevenue(Resource):
    """Report Total Revenue.

    ---
    post:
      tags:
        - Report
      summary: Report Total Revenue
      description: Report Total Revenue
      requestBody:
        content:
          application/json:
            schema:
              ReportSchema
    """

    method_decorators = [jwt_required()]

    @staticmethod
    def post():
        """The post report total revenue resource."""
        args = request.json
        fiscal_year = args.get("fiscal_year")
        query = Revenue.query.filter(
            extract("year", Revenue.transaction_date) == fiscal_year
        ).all()
        total_revenue = sum([getattr(x, "amount") for x in query])
        return {"report": {"total_revenue": total_revenue}}


class ReportRevenueByMonth(Resource):
    """Report Revenue By Month.

    ---
    post:
      tags:
        - Report
      summary: Report Revenue By Month
      description: Report Total Revenue by month
      requestBody:
        content:
          application/json:
            schema:
              ReportSchema
    """

    method_decorators = [jwt_required()]

    @staticmethod
    def post():
        """The post report total revenue by month resource."""
        args = request.json
        fiscal_year = args.get("fiscal_year")

        query = Revenue.query.filter(
            extract("year", Revenue.transaction_date) == fiscal_year
        ).all()

        from itertools import groupby

        def grouper(item):
            return item.transaction_date.month

        grouped_by_month = []
        for ((month), items) in groupby(query, grouper):
            grouped_by_month.append(
                {
                    "month_name": datetime.datetime.strptime(str(month), "%m").strftime(
                        "%B"
                    ),
                    "revenue": sum([getattr(x, "amount") for x in items]),
                }
            )
        return {
            "report": grouped_by_month
            if grouped_by_month
            else "nothing found on infomed fiscal year"
        }


class ReportRevenueByCustomer(Resource):
    """Report Revenue By Customer.

    ---
    post:
      tags:
        - Report
      summary: Report Revenue By Customer
      description: Report Total Revenue by Customer
      requestBody:
        content:
          application/json:
            schema:
              ReportSchema
    """

    method_decorators = [jwt_required()]

    @staticmethod
    def post():
        """The post report total revenue by customer resource."""
        args = request.json
        fiscal_year = args.get("fiscal_year")

        query = (
            Revenue.query.join(Customer)
            .filter(extract("year", Revenue.transaction_date) == fiscal_year)
            .all()
        )

        from itertools import groupby

        def grouper(item):
            return item.customer.legal_name

        grouped_by_customer = []
        for ((legal_name), items) in groupby(query, grouper):
            grouped_by_customer.append(
                {
                    "customer_name": legal_name,
                    "revenue": sum([getattr(x, "amount") for x in items]),
                }
            )

        return {
            "report": grouped_by_customer
            if grouped_by_customer
            else "nothing found on infomed fiscal year"
        }
