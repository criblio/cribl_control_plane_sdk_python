"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from cribl_control_plane.types import BaseModel
from typing_extensions import TypedDict


class LoginInfoTypedDict(TypedDict):
    username: str
    password: str


class LoginInfo(BaseModel):
    username: str

    password: str
