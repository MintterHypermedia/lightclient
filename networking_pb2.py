# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: networking.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10networking.proto\x12\x1e\x63om.mintter.networking.v1alpha\"%\n\x12GetPeerInfoRequest\x12\x0f\n\x07peer_id\x18\x01 \x01(\t\"\x1f\n\x0e\x43onnectRequest\x12\r\n\x05\x61\x64\x64rs\x18\x01 \x03(\t\"\x11\n\x0f\x43onnectResponse\"z\n\x08PeerInfo\x12\r\n\x05\x61\x64\x64rs\x18\x01 \x03(\t\x12K\n\x11\x63onnection_status\x18\x02 \x01(\x0e\x32\x30.com.mintter.networking.v1alpha.ConnectionStatus\x12\x12\n\naccount_id\x18\x03 \x01(\t*Y\n\x10\x43onnectionStatus\x12\x11\n\rNOT_CONNECTED\x10\x00\x12\r\n\tCONNECTED\x10\x01\x12\x0f\n\x0b\x43\x41N_CONNECT\x10\x02\x12\x12\n\x0e\x43\x41NNOT_CONNECT\x10\x03\x32\xe5\x01\n\nNetworking\x12k\n\x0bGetPeerInfo\x12\x32.com.mintter.networking.v1alpha.GetPeerInfoRequest\x1a(.com.mintter.networking.v1alpha.PeerInfo\x12j\n\x07\x43onnect\x12..com.mintter.networking.v1alpha.ConnectRequest\x1a/.com.mintter.networking.v1alpha.ConnectResponseB8Z6mintter/backend/genproto/networking/v1alpha;networkingb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'networking_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6mintter/backend/genproto/networking/v1alpha;networking'
  _CONNECTIONSTATUS._serialized_start=267
  _CONNECTIONSTATUS._serialized_end=356
  _GETPEERINFOREQUEST._serialized_start=52
  _GETPEERINFOREQUEST._serialized_end=89
  _CONNECTREQUEST._serialized_start=91
  _CONNECTREQUEST._serialized_end=122
  _CONNECTRESPONSE._serialized_start=124
  _CONNECTRESPONSE._serialized_end=141
  _PEERINFO._serialized_start=143
  _PEERINFO._serialized_end=265
  _NETWORKING._serialized_start=359
  _NETWORKING._serialized_end=588
# @@protoc_insertion_point(module_scope)
