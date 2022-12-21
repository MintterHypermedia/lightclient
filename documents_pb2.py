# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: documents.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x64ocuments.proto\x12\x1d\x63om.mintter.documents.v1alpha\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"2\n\x12\x43reateDraftRequest\x12\x1c\n\x14\x65xisting_document_id\x18\x01 \x01(\t\")\n\x12\x44\x65leteDraftRequest\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\"&\n\x0fGetDraftRequest\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\"k\n\x14UpdateDraftRequestV2\x12\x13\n\x0b\x64ocument_id\x18\x03 \x01(\t\x12>\n\x07\x63hanges\x18\x04 \x03(\x0b\x32-.com.mintter.documents.v1alpha.DocumentChange\"\xae\x02\n\x0e\x44ocumentChange\x12\x13\n\tset_title\x18\x01 \x01(\tH\x00\x12\x16\n\x0cset_subtitle\x18\x02 \x01(\tH\x00\x12M\n\nmove_block\x18\x03 \x01(\x0b\x32\x37.com.mintter.documents.v1alpha.DocumentChange.MoveBlockH\x00\x12=\n\rreplace_block\x18\x04 \x01(\x0b\x32$.com.mintter.documents.v1alpha.BlockH\x00\x12\x16\n\x0c\x64\x65lete_block\x18\x05 \x01(\tH\x00\x1a\x43\n\tMoveBlock\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\x14\n\x0cleft_sibling\x18\x03 \x01(\tB\x04\n\x02op\":\n\x11ListDraftsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\"i\n\x12ListDraftsResponse\x12:\n\tdocuments\x18\x01 \x03(\x0b\x32\'.com.mintter.documents.v1alpha.Document\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"*\n\x13PublishDraftRequest\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\"Q\n\x15GetPublicationRequest\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x12\n\nlocal_only\x18\x03 \x01(\x08\"/\n\x18\x44\x65letePublicationRequest\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\"@\n\x17ListPublicationsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\"u\n\x18ListPublicationsResponse\x12@\n\x0cpublications\x18\x01 \x03(\x0b\x32*.com.mintter.documents.v1alpha.Publication\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\":\n\x14ListCitationsRequest\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\"K\n\x15ListCitationsResponse\x12\x32\n\x05links\x18\x01 \x03(\x0b\x32#.com.mintter.documents.v1alpha.Link\"Y\n\x0bPublication\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x39\n\x08\x64ocument\x18\x02 \x01(\x0b\x32\'.com.mintter.documents.v1alpha.Document\"\x97\x02\n\x08\x44ocument\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08subtitle\x18\x03 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x04 \x01(\t\x12:\n\x08\x63hildren\x18\t \x03(\x0b\x32(.com.mintter.documents.v1alpha.BlockNode\x12/\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0cpublish_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"|\n\tBlockNode\x12\x33\n\x05\x62lock\x18\x01 \x01(\x0b\x32$.com.mintter.documents.v1alpha.Block\x12:\n\x08\x63hildren\x18\x02 \x03(\x0b\x32(.com.mintter.documents.v1alpha.BlockNode\"\xec\x01\n\x05\x42lock\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12H\n\nattributes\x18\x04 \x03(\x0b\x32\x34.com.mintter.documents.v1alpha.Block.AttributesEntry\x12>\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32).com.mintter.documents.v1alpha.Annotation\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xba\x01\n\nAnnotation\x12\x0c\n\x04type\x18\x01 \x01(\t\x12M\n\nattributes\x18\x02 \x03(\x0b\x32\x39.com.mintter.documents.v1alpha.Annotation.AttributesEntry\x12\x0e\n\x06starts\x18\x03 \x03(\x05\x12\x0c\n\x04\x65nds\x18\x04 \x03(\x05\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"x\n\x04Link\x12\x37\n\x06source\x18\x01 \x01(\x0b\x32\'.com.mintter.documents.v1alpha.LinkNode\x12\x37\n\x06target\x18\x02 \x01(\x0b\x32\'.com.mintter.documents.v1alpha.LinkNode\"B\n\x08LinkNode\x12\x13\n\x0b\x64ocument_id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08\x62lock_id\x18\x03 \x01(\t2\xf3\x04\n\x06\x44rafts\x12i\n\x0b\x43reateDraft\x12\x31.com.mintter.documents.v1alpha.CreateDraftRequest\x1a\'.com.mintter.documents.v1alpha.Document\x12X\n\x0b\x44\x65leteDraft\x12\x31.com.mintter.documents.v1alpha.DeleteDraftRequest\x1a\x16.google.protobuf.Empty\x12\x63\n\x08GetDraft\x12..com.mintter.documents.v1alpha.GetDraftRequest\x1a\'.com.mintter.documents.v1alpha.Document\x12\\\n\rUpdateDraftV2\x12\x33.com.mintter.documents.v1alpha.UpdateDraftRequestV2\x1a\x16.google.protobuf.Empty\x12q\n\nListDrafts\x12\x30.com.mintter.documents.v1alpha.ListDraftsRequest\x1a\x31.com.mintter.documents.v1alpha.ListDraftsResponse\x12n\n\x0cPublishDraft\x12\x32.com.mintter.documents.v1alpha.PublishDraftRequest\x1a*.com.mintter.documents.v1alpha.Publication2\xee\x02\n\x0cPublications\x12r\n\x0eGetPublication\x12\x34.com.mintter.documents.v1alpha.GetPublicationRequest\x1a*.com.mintter.documents.v1alpha.Publication\x12\x64\n\x11\x44\x65letePublication\x12\x37.com.mintter.documents.v1alpha.DeletePublicationRequest\x1a\x16.google.protobuf.Empty\x12\x83\x01\n\x10ListPublications\x12\x36.com.mintter.documents.v1alpha.ListPublicationsRequest\x1a\x37.com.mintter.documents.v1alpha.ListPublicationsResponse2\x8a\x01\n\x0c\x43ontentGraph\x12z\n\rListCitations\x12\x33.com.mintter.documents.v1alpha.ListCitationsRequest\x1a\x34.com.mintter.documents.v1alpha.ListCitationsResponseB6Z4mintter/backend/genproto/documents/v1alpha;documentsb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'documents_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4mintter/backend/genproto/documents/v1alpha;documents'
  _BLOCK_ATTRIBUTESENTRY._options = None
  _BLOCK_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _ANNOTATION_ATTRIBUTESENTRY._options = None
  _ANNOTATION_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _CREATEDRAFTREQUEST._serialized_start=112
  _CREATEDRAFTREQUEST._serialized_end=162
  _DELETEDRAFTREQUEST._serialized_start=164
  _DELETEDRAFTREQUEST._serialized_end=205
  _GETDRAFTREQUEST._serialized_start=207
  _GETDRAFTREQUEST._serialized_end=245
  _UPDATEDRAFTREQUESTV2._serialized_start=247
  _UPDATEDRAFTREQUESTV2._serialized_end=354
  _DOCUMENTCHANGE._serialized_start=357
  _DOCUMENTCHANGE._serialized_end=659
  _DOCUMENTCHANGE_MOVEBLOCK._serialized_start=586
  _DOCUMENTCHANGE_MOVEBLOCK._serialized_end=653
  _LISTDRAFTSREQUEST._serialized_start=661
  _LISTDRAFTSREQUEST._serialized_end=719
  _LISTDRAFTSRESPONSE._serialized_start=721
  _LISTDRAFTSRESPONSE._serialized_end=826
  _PUBLISHDRAFTREQUEST._serialized_start=828
  _PUBLISHDRAFTREQUEST._serialized_end=870
  _GETPUBLICATIONREQUEST._serialized_start=872
  _GETPUBLICATIONREQUEST._serialized_end=953
  _DELETEPUBLICATIONREQUEST._serialized_start=955
  _DELETEPUBLICATIONREQUEST._serialized_end=1002
  _LISTPUBLICATIONSREQUEST._serialized_start=1004
  _LISTPUBLICATIONSREQUEST._serialized_end=1068
  _LISTPUBLICATIONSRESPONSE._serialized_start=1070
  _LISTPUBLICATIONSRESPONSE._serialized_end=1187
  _LISTCITATIONSREQUEST._serialized_start=1189
  _LISTCITATIONSREQUEST._serialized_end=1247
  _LISTCITATIONSRESPONSE._serialized_start=1249
  _LISTCITATIONSRESPONSE._serialized_end=1324
  _PUBLICATION._serialized_start=1326
  _PUBLICATION._serialized_end=1415
  _DOCUMENT._serialized_start=1418
  _DOCUMENT._serialized_end=1697
  _BLOCKNODE._serialized_start=1699
  _BLOCKNODE._serialized_end=1823
  _BLOCK._serialized_start=1826
  _BLOCK._serialized_end=2062
  _BLOCK_ATTRIBUTESENTRY._serialized_start=2013
  _BLOCK_ATTRIBUTESENTRY._serialized_end=2062
  _ANNOTATION._serialized_start=2065
  _ANNOTATION._serialized_end=2251
  _ANNOTATION_ATTRIBUTESENTRY._serialized_start=2013
  _ANNOTATION_ATTRIBUTESENTRY._serialized_end=2062
  _LINK._serialized_start=2253
  _LINK._serialized_end=2373
  _LINKNODE._serialized_start=2375
  _LINKNODE._serialized_end=2441
  _DRAFTS._serialized_start=2444
  _DRAFTS._serialized_end=3071
  _PUBLICATIONS._serialized_start=3074
  _PUBLICATIONS._serialized_end=3440
  _CONTENTGRAPH._serialized_start=3443
  _CONTENTGRAPH._serialized_end=3581
# @@protoc_insertion_point(module_scope)
