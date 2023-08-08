import typing_extensions

from scout9.paths import PathValues
from scout9.apis.paths.v1_customer import V1Customer
from scout9.apis.paths.v1_customers import V1Customers

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_CUSTOMER: V1Customer,
        PathValues.V1_CUSTOMERS: V1Customers,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_CUSTOMER: V1Customer,
        PathValues.V1_CUSTOMERS: V1Customers,
    }
)
