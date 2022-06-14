"""The init resource file."""
from app.api.resources.user import UserResource, UserList
from app.api.resources.customer import CustomerResource, CustomerList
from app.api.resources.revenue import (
    RevenueResource,
    RevenueList,
    RevenueCategoryResource,
    RevenueCategoryList,
)
from app.api.resources.report import (
    ReportTotalRevenue,
    ReportRevenueByMonth,
    ReportRevenueByCustomer,
)

__all__ = [
    "UserResource",
    "UserList",
    "CustomerList",
    "CustomerResource",
    "RevenueResource",
    "RevenueList",
    "RevenueCategoryResource",
    "RevenueCategoryList",
    "ReportTotalRevenue",
    "ReportRevenueByMonth",
    "ReportRevenueByCustomer",
]
