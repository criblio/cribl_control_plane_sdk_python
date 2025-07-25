"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .routesroute import RoutesRoute, RoutesRouteTypedDict
from .routesroute_input import RoutesRouteInput, RoutesRouteInputTypedDict
from cribl_control_plane.types import BaseModel
import pydantic
from pydantic import ConfigDict
from typing import Any, Dict, List, Optional
from typing_extensions import NotRequired, TypedDict


class RoutesGroupsTypedDict(TypedDict):
    name: str
    description: NotRequired[str]
    r"""Short description of this group"""
    disabled: NotRequired[bool]
    r"""Whether this group is disabled"""


class RoutesGroups(BaseModel):
    name: str

    description: Optional[str] = None
    r"""Short description of this group"""

    disabled: Optional[bool] = None
    r"""Whether this group is disabled"""


class CommentTypedDict(TypedDict):
    comment: NotRequired[str]
    r"""Optional, short description of this Route's purpose"""


class Comment(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, extra="allow"
    )
    __pydantic_extra__: Dict[str, Any] = pydantic.Field(init=False)

    comment: Optional[str] = None
    r"""Optional, short description of this Route's purpose"""

    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value  # pyright: ignore[reportIncompatibleVariableOverride]


class RoutesTypedDict(TypedDict):
    routes: List[RoutesRouteTypedDict]
    r"""Pipeline routing rules"""
    id: NotRequired[str]
    r"""Routes ID"""
    groups: NotRequired[Dict[str, RoutesGroupsTypedDict]]
    comments: NotRequired[List[CommentTypedDict]]
    r"""Comments"""


class Routes(BaseModel):
    routes: List[RoutesRoute]
    r"""Pipeline routing rules"""

    id: Optional[str] = None
    r"""Routes ID"""

    groups: Optional[Dict[str, RoutesGroups]] = None

    comments: Optional[List[Comment]] = None
    r"""Comments"""


class RoutesInputTypedDict(TypedDict):
    routes: List[RoutesRouteInputTypedDict]
    r"""Pipeline routing rules"""
    id: NotRequired[str]
    r"""Routes ID"""
    groups: NotRequired[Dict[str, RoutesGroupsTypedDict]]
    comments: NotRequired[List[CommentTypedDict]]
    r"""Comments"""


class RoutesInput(BaseModel):
    routes: List[RoutesRouteInput]
    r"""Pipeline routing rules"""

    id: Optional[str] = None
    r"""Routes ID"""

    groups: Optional[Dict[str, RoutesGroups]] = None

    comments: Optional[List[Comment]] = None
    r"""Comments"""
