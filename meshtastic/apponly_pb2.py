# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/apponly.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from meshtastic import channel_pb2 as meshtastic_dot_channel__pb2
from meshtastic import config_pb2 as meshtastic_dot_config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18meshtastic/apponly.proto\x1a\x18meshtastic/channel.proto\x1a\x17meshtastic/config.proto\"Y\n\nChannelSet\x12\"\n\x08settings\x18\x01 \x03(\x0b\x32\x10.ChannelSettings\x12\'\n\x0blora_config\x18\x02 \x01(\x0b\x32\x12.Config.LoRaConfigBd\n\x13\x63om.geeksville.meshB\rAppOnlyProtosH\x03Z\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')



_CHANNELSET = DESCRIPTOR.message_types_by_name['ChannelSet']
ChannelSet = _reflection.GeneratedProtocolMessageType('ChannelSet', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELSET,
  '__module__' : 'meshtastic.apponly_pb2'
  # @@protoc_insertion_point(class_scope:ChannelSet)
  })
_sym_db.RegisterMessage(ChannelSet)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\rAppOnlyProtosH\003Z\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _CHANNELSET._serialized_start=79
  _CHANNELSET._serialized_end=168
# @@protoc_insertion_point(module_scope)
