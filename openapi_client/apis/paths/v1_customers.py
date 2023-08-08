from openapi_client.paths.v1_customers.get import ApiForget
from openapi_client.paths.v1_customers.put import ApiForput
from openapi_client.paths.v1_customers.post import ApiForpost
from openapi_client.paths.v1_customers.delete import ApiFordelete


class V1Customers(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
