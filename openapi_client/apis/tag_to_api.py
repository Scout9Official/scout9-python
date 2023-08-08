import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.scout9_api import Scout9Api

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SCOUT9: Scout9Api,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SCOUT9: Scout9Api,
    }
)
