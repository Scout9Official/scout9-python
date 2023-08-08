from openapi_client.paths.v1_customer.get import ApiForget
from openapi_client.paths.v1_customer.put import ApiForput
from openapi_client.paths.v1_customer.post import ApiForpost
from openapi_client.paths.v1_customer.delete import ApiFordelete


class V1Customer(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
