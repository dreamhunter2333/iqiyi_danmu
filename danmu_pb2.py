# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: danmu.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x64\x61nmu.proto\x12\x05\x64\x61nmu\"\x1d\n\nBulletInfo\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\".\n\x05\x45ntry\x12%\n\nbulletInfo\x18\x02 \x03(\x0b\x32\x11.danmu.BulletInfo\"$\n\x05\x44\x61nmu\x12\x1b\n\x05\x65ntry\x18\x06 \x03(\x0b\x32\x0c.danmu.Entry')



_BULLETINFO = DESCRIPTOR.message_types_by_name['BulletInfo']
_ENTRY = DESCRIPTOR.message_types_by_name['Entry']
_DANMU = DESCRIPTOR.message_types_by_name['Danmu']
BulletInfo = _reflection.GeneratedProtocolMessageType('BulletInfo', (_message.Message,), {
  'DESCRIPTOR' : _BULLETINFO,
  '__module__' : 'danmu_pb2'
  # @@protoc_insertion_point(class_scope:danmu.BulletInfo)
  })
_sym_db.RegisterMessage(BulletInfo)

Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
  'DESCRIPTOR' : _ENTRY,
  '__module__' : 'danmu_pb2'
  # @@protoc_insertion_point(class_scope:danmu.Entry)
  })
_sym_db.RegisterMessage(Entry)

Danmu = _reflection.GeneratedProtocolMessageType('Danmu', (_message.Message,), {
  'DESCRIPTOR' : _DANMU,
  '__module__' : 'danmu_pb2'
  # @@protoc_insertion_point(class_scope:danmu.Danmu)
  })
_sym_db.RegisterMessage(Danmu)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BULLETINFO._serialized_start=22
  _BULLETINFO._serialized_end=51
  _ENTRY._serialized_start=53
  _ENTRY._serialized_end=99
  _DANMU._serialized_start=101
  _DANMU._serialized_end=137
# @@protoc_insertion_point(module_scope)
