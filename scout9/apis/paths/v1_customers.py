from scout9.paths.v1_customers.get import ApiForget
from scout9.paths.v1_customers.put import ApiForput
from scout9.paths.v1_customers.post import ApiForpost
from scout9.paths.v1_customers.delete import ApiFordelete


class V1Customers(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
