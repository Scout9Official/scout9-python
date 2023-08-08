# openapi_client.model.customer.Customer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**firstName** | str,  | str,  | The customers first name | [optional] 
**lastName** | str,  | str,  | The customers last name | [optional] 
**name** | str,  | str,  | The customers full name | [optional] 
**email** | None, str,  | NoneClass, str,  | The customers email address | [optional] 
**phone** | None, str,  | NoneClass, str,  | The customers phone number | [optional] 
**img** | None, str,  | NoneClass, str,  | The customers profile image | [optional] 
**neighborhood** | None, str,  | NoneClass, str,  | The customers neighborhood | [optional] 
**city** | None, str,  | NoneClass, str,  | The customers city | [optional] 
**country** | None, str,  | NoneClass, str,  | The customers 2-letter country code | [optional] 
**line1** | None, str,  | NoneClass, str,  | The customers street address | [optional] 
**line2** | None, str,  | NoneClass, str,  | The customers street address | [optional] 
**postal_code** | None, str,  | NoneClass, str,  | The customers postal code | [optional] 
**state** | None, str,  | NoneClass, str,  | The customers state, county, province, or region | [optional] 
**town** | None, str,  | NoneClass, str,  | The customers town (only used in Japan) | [optional] 
**blocked** | [**BlockInfo**](BlockInfo.md) | [**BlockInfo**](BlockInfo.md) |  | [optional] 
**phoneBlocked** | [**BlockInfo**](BlockInfo.md) | [**BlockInfo**](BlockInfo.md) |  | [optional] 
**emailBlocked** | [**BlockInfo**](BlockInfo.md) | [**BlockInfo**](BlockInfo.md) |  | [optional] 
**joined** | None, str, datetime,  | NoneClass, str,  | The date the customer joined the business | [optional] value must conform to RFC-3339 date-time
**stripe** | None, str,  | NoneClass, str,  | The customers stripe ID | [optional] 
**stripeDev** | None, str,  | NoneClass, str,  | The customers stripe ID in the dev environment | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

