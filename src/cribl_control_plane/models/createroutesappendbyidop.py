"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .routeconf import RouteConf, RouteConfTypedDict
from cribl_control_plane.types import BaseModel
from cribl_control_plane.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateRoutesAppendByIDRequestTypedDict(TypedDict):
    id: str
    r"""the route table to be appended to - currently default is the only supported value"""
    request_body: List[RouteConfTypedDict]
    r"""RouteDefinitions object"""


class CreateRoutesAppendByIDRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""the route table to be appended to - currently default is the only supported value"""

    request_body: Annotated[
        List[RouteConf],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""RouteDefinitions object"""


class CreateRoutesAppendByIDResponseTypedDict(TypedDict):
    r"""a list of any objects"""

    count: NotRequired[int]
    r"""number of items present in the items array"""
    items: NotRequired[List[Dict[str, Any]]]


class CreateRoutesAppendByIDResponse(BaseModel):
    r"""a list of any objects"""

    count: Optional[int] = None
    r"""number of items present in the items array"""

    items: Optional[List[Dict[str, Any]]] = None
