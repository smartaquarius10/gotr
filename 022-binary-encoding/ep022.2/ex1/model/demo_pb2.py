# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='demo.proto',
  package='model.other.thing',
  syntax='proto3',
  serialized_options=_b('Z\005model'),
  serialized_pb=_b('\n\ndemo.proto\x12\x11model.other.thing\"\x16\n\tSearchReq\x12\t\n\x01q\x18\x01 \x01(\tB\x07Z\x05modelb\x06proto3')
)




_SEARCHREQ = _descriptor.Descriptor(
  name='SearchReq',
  full_name='model.other.thing.SearchReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='q', full_name='model.other.thing.SearchReq.q', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=55,
)

DESCRIPTOR.message_types_by_name['SearchReq'] = _SEARCHREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchReq = _reflection.GeneratedProtocolMessageType('SearchReq', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHREQ,
  __module__ = 'demo_pb2'
  # @@protoc_insertion_point(class_scope:model.other.thing.SearchReq)
  ))
_sym_db.RegisterMessage(SearchReq)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)