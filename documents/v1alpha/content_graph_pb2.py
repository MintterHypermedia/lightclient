# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: documents/v1alpha/content_graph.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%documents/v1alpha/content_graph.proto\x12\x1d\x63om.mintter.documents.v1alpha\"+\n\x14ListCitationsRequest\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\"K\n\x15ListCitationsResponse\x12\x32\n\x05links\x18\x01 \x03(\x0b\x32#.com.mintter.documents.v1alpha.Link\"\x8b\x01\n\x04Link\x12\x37\n\x06source\x18\x01 \x01(\x0b\x32\'.com.mintter.documents.v1alpha.LinkNode\x12\x37\n\x06target\x18\x02 \x01(\x0b\x32\'.com.mintter.documents.v1alpha.LinkNode\x12\x11\n\tis_latest\x18\x03 \x01(\x08\"B\n\x08LinkNode\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08\x62lock_id\x18\x03 \x01(\t2\x8a\x01\n\x0c\x43ontentGraph\x12z\n\rListCitations\x12\x33.com.mintter.documents.v1alpha.ListCitationsRequest\x1a\x34.com.mintter.documents.v1alpha.ListCitationsResponseB6Z4mintter/backend/genproto/documents/v1alpha;documentsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'documents.v1alpha.content_graph_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4mintter/backend/genproto/documents/v1alpha;documents'
  _LISTCITATIONSREQUEST._serialized_start=72
  _LISTCITATIONSREQUEST._serialized_end=115
  _LISTCITATIONSRESPONSE._serialized_start=117
  _LISTCITATIONSRESPONSE._serialized_end=192
  _LINK._serialized_start=195
  _LINK._serialized_end=334
  _LINKNODE._serialized_start=336
  _LINKNODE._serialized_end=402
  _CONTENTGRAPH._serialized_start=405
  _CONTENTGRAPH._serialized_end=543
# @@protoc_insertion_point(module_scope)
