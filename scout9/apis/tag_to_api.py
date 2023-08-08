import typing_extensions

from scout9.apis.tags import TagValues
from scout9.apis.tags.scout9_api import Scout9Api

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
