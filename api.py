# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: api.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto
import grpclib


@dataclass
class ConfigGetRequest(betterproto.Message):
    tmp: str = betterproto.string_field(1)


@dataclass
class ConfigGetResponse(betterproto.Message):
    entry: List["ConfigEntry"] = betterproto.message_field(1)


@dataclass
class ConfigEntry(betterproto.Message):
    key: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)


class ApiServiceStub(betterproto.ServiceStub):
    async def get_config(self, *, tmp: str = "") -> ConfigGetResponse:
        request = ConfigGetRequest()
        request.tmp = tmp

        return await self._unary_unary(
            "/api.ApiService/get_config",
            request,
            ConfigGetResponse,
        )