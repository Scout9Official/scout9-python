import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.v1_customer import V1Customer
from openapi_client.apis.paths.v1_customers import V1Customers

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
