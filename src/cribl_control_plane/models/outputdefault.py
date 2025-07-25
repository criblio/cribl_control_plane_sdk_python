"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from cribl_control_plane import utils
from cribl_control_plane.types import BaseModel
from cribl_control_plane.utils import validate_open_enum
from enum import Enum
import pydantic
from pydantic.functional_validators import PlainValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class OutputDefaultType(str, Enum, metaclass=utils.OpenEnumMeta):
    DEFAULT = "default"


class OutputDefaultTypedDict(TypedDict):
    type: OutputDefaultType
    default_id: str
    r"""ID of the default output. This will be used whenever a nonexistent/deleted output is referenced."""
    id: NotRequired[str]
    r"""Unique ID for this output"""
    pipeline: NotRequired[str]
    r"""Pipeline to process data before sending out to this output"""
    system_fields: NotRequired[List[str]]
    r"""Fields to automatically add to events, such as cribl_pipe. Supports wildcards."""
    environment: NotRequired[str]
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    streamtags: NotRequired[List[str]]
    r"""Tags for filtering and grouping in @{product}"""


class OutputDefault(BaseModel):
    type: Annotated[OutputDefaultType, PlainValidator(validate_open_enum(False))]

    default_id: Annotated[str, pydantic.Field(alias="defaultId")]
    r"""ID of the default output. This will be used whenever a nonexistent/deleted output is referenced."""

    id: Optional[str] = None
    r"""Unique ID for this output"""

    pipeline: Optional[str] = None
    r"""Pipeline to process data before sending out to this output"""

    system_fields: Annotated[
        Optional[List[str]], pydantic.Field(alias="systemFields")
    ] = None
    r"""Fields to automatically add to events, such as cribl_pipe. Supports wildcards."""

    environment: Optional[str] = None
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""

    streamtags: Optional[List[str]] = None
    r"""Tags for filtering and grouping in @{product}"""
