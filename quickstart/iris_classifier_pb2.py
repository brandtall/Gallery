# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iris_classifier.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15iris_classifier.proto\"\x19\n\ninputArray\x12\x0b\n\x03\x61rr\x18\x01 \x01(\t\"\x1a\n\x0boutputArray\x12\x0b\n\x03\x61rr\x18\x01 \x01(\t25\n\x0c\x43lassifyIris\x12%\n\x08\x63lassify\x12\x0b.inputArray\x1a\x0c.outputArrayb\x06proto3')



_INPUTARRAY = DESCRIPTOR.message_types_by_name['inputArray']
_OUTPUTARRAY = DESCRIPTOR.message_types_by_name['outputArray']
inputArray = _reflection.GeneratedProtocolMessageType('inputArray', (_message.Message,), {
  'DESCRIPTOR' : _INPUTARRAY,
  '__module__' : 'iris_classifier_pb2'
  # @@protoc_insertion_point(class_scope:inputArray)
  })
_sym_db.RegisterMessage(inputArray)

outputArray = _reflection.GeneratedProtocolMessageType('outputArray', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTARRAY,
  '__module__' : 'iris_classifier_pb2'
  # @@protoc_insertion_point(class_scope:outputArray)
  })
_sym_db.RegisterMessage(outputArray)

_CLASSIFYIRIS = DESCRIPTOR.services_by_name['ClassifyIris']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INPUTARRAY._serialized_start=25
  _INPUTARRAY._serialized_end=50
  _OUTPUTARRAY._serialized_start=52
  _OUTPUTARRAY._serialized_end=78
  _CLASSIFYIRIS._serialized_start=80
  _CLASSIFYIRIS._serialized_end=133
# @@protoc_insertion_point(module_scope)
