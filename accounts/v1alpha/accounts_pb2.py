# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accounts/v1alpha/accounts.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61\x63\x63ounts/v1alpha/accounts.proto\x12\x1c\x63om.mintter.accounts.v1alpha\"\x1f\n\x11GetAccountRequest\x12\n\n\x02id\x18\x01 \x01(\t\"<\n\x13ListAccountsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\"h\n\x14ListAccountsResponse\x12\x37\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32%.com.mintter.accounts.v1alpha.Account\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xe8\x01\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x07profile\x18\x02 \x01(\x0b\x32%.com.mintter.accounts.v1alpha.Profile\x12\x43\n\x07\x64\x65vices\x18\x03 \x03(\x0b\x32\x32.com.mintter.accounts.v1alpha.Account.DevicesEntry\x1aT\n\x0c\x44\x65vicesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.com.mintter.accounts.v1alpha.Device:\x02\x38\x01\"4\n\x07Profile\x12\r\n\x05\x61lias\x18\x01 \x01(\t\x12\x0b\n\x03\x62io\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"\x19\n\x06\x44\x65vice\x12\x0f\n\x07peer_id\x18\x01 \x01(\t2\xc6\x02\n\x08\x41\x63\x63ounts\x12\x64\n\nGetAccount\x12/.com.mintter.accounts.v1alpha.GetAccountRequest\x1a%.com.mintter.accounts.v1alpha.Account\x12]\n\rUpdateProfile\x12%.com.mintter.accounts.v1alpha.Profile\x1a%.com.mintter.accounts.v1alpha.Account\x12u\n\x0cListAccounts\x12\x31.com.mintter.accounts.v1alpha.ListAccountsRequest\x1a\x32.com.mintter.accounts.v1alpha.ListAccountsResponseB4Z2mintter/backend/genproto/accounts/v1alpha;accountsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'accounts.v1alpha.accounts_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2mintter/backend/genproto/accounts/v1alpha;accounts'
  _ACCOUNT_DEVICESENTRY._options = None
  _ACCOUNT_DEVICESENTRY._serialized_options = b'8\001'
  _GETACCOUNTREQUEST._serialized_start=65
  _GETACCOUNTREQUEST._serialized_end=96
  _LISTACCOUNTSREQUEST._serialized_start=98
  _LISTACCOUNTSREQUEST._serialized_end=158
  _LISTACCOUNTSRESPONSE._serialized_start=160
  _LISTACCOUNTSRESPONSE._serialized_end=264
  _ACCOUNT._serialized_start=267
  _ACCOUNT._serialized_end=499
  _ACCOUNT_DEVICESENTRY._serialized_start=415
  _ACCOUNT_DEVICESENTRY._serialized_end=499
  _PROFILE._serialized_start=501
  _PROFILE._serialized_end=553
  _DEVICE._serialized_start=555
  _DEVICE._serialized_end=580
  _ACCOUNTS._serialized_start=583
  _ACCOUNTS._serialized_end=909
# @@protoc_insertion_point(module_scope)