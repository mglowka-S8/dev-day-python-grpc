# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapi.proto\x12\x03\x61pi\"\x1f\n\x10\x43onfigGetRequest\x12\x0b\n\x03tmp\x18\x01 \x01(\t\"4\n\x11\x43onfigGetResponse\x12\x1f\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x10.api.ConfigEntry\")\n\x0b\x43onfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t2K\n\nApiService\x12=\n\nget_config\x12\x15.api.ConfigGetRequest\x1a\x16.api.ConfigGetResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGGETREQUEST._serialized_start=18
  _CONFIGGETREQUEST._serialized_end=49
  _CONFIGGETRESPONSE._serialized_start=51
  _CONFIGGETRESPONSE._serialized_end=103
  _CONFIGENTRY._serialized_start=105
  _CONFIGENTRY._serialized_end=146
  _APISERVICE._serialized_start=148
  _APISERVICE._serialized_end=223
# @@protoc_insertion_point(module_scope)