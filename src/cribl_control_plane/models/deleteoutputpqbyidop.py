"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from cribl_control_plane.types import BaseModel
from cribl_control_plane.utils import FieldMetadata, PathParamMetadata
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DeleteOutputPqByIDRequestTypedDict(TypedDict):
    id: str
    r"""Destination Id"""


class DeleteOutputPqByIDRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Destination Id"""


class DeleteOutputPqByIDResponseTypedDict(TypedDict):
    r"""a list of any objects"""

    count: NotRequired[int]
    r"""number of items present in the items array"""
    items: NotRequired[List[Dict[str, Any]]]


class DeleteOutputPqByIDResponse(BaseModel):
    r"""a list of any objects"""

    count: Optional[int] = None
    r"""number of items present in the items array"""

    items: Optional[List[Dict[str, Any]]] = None
