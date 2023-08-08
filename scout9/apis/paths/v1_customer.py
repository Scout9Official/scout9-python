from scout9.paths.v1_customer.get import ApiForget
from scout9.paths.v1_customer.put import ApiForput
from scout9.paths.v1_customer.post import ApiForpost
from scout9.paths.v1_customer.delete import ApiFordelete


class V1Customer(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
