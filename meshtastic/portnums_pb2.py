# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/portnums.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19meshtastic/portnums.proto*\xa4\x03\n\x07PortNum\x12\x0f\n\x0bUNKNOWN_APP\x10\x00\x12\x14\n\x10TEXT_MESSAGE_APP\x10\x01\x12\x17\n\x13REMOTE_HARDWARE_APP\x10\x02\x12\x10\n\x0cPOSITION_APP\x10\x03\x12\x10\n\x0cNODEINFO_APP\x10\x04\x12\x0f\n\x0bROUTING_APP\x10\x05\x12\r\n\tADMIN_APP\x10\x06\x12\x1f\n\x1bTEXT_MESSAGE_COMPRESSED_APP\x10\x07\x12\x10\n\x0cWAYPOINT_APP\x10\x08\x12\r\n\tAUDIO_APP\x10\t\x12\r\n\tREPLY_APP\x10 \x12\x11\n\rIP_TUNNEL_APP\x10!\x12\x0e\n\nSERIAL_APP\x10@\x12\x15\n\x11STORE_FORWARD_APP\x10\x41\x12\x12\n\x0eRANGE_TEST_APP\x10\x42\x12\x11\n\rTELEMETRY_APP\x10\x43\x12\x0b\n\x07ZPS_APP\x10\x44\x12\x11\n\rSIMULATOR_APP\x10\x45\x12\x12\n\x0eTRACEROUTE_APP\x10\x46\x12\x10\n\x0bPRIVATE_APP\x10\x80\x02\x12\x13\n\x0e\x41TAK_FORWARDER\x10\x81\x02\x12\x08\n\x03MAX\x10\xff\x03\x42_\n\x13\x63om.geeksville.meshB\x08PortnumsH\x03Z\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_PORTNUM = DESCRIPTOR.enum_types_by_name['PortNum']
PortNum = enum_type_wrapper.EnumTypeWrapper(_PORTNUM)
UNKNOWN_APP = 0
TEXT_MESSAGE_APP = 1
REMOTE_HARDWARE_APP = 2
POSITION_APP = 3
NODEINFO_APP = 4
ROUTING_APP = 5
ADMIN_APP = 6
TEXT_MESSAGE_COMPRESSED_APP = 7
WAYPOINT_APP = 8
AUDIO_APP = 9
REPLY_APP = 32
IP_TUNNEL_APP = 33
SERIAL_APP = 64
STORE_FORWARD_APP = 65
RANGE_TEST_APP = 66
TELEMETRY_APP = 67
ZPS_APP = 68
SIMULATOR_APP = 69
TRACEROUTE_APP = 70
PRIVATE_APP = 256
ATAK_FORWARDER = 257
MAX = 511


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\010PortnumsH\003Z\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _PORTNUM._serialized_start=30
  _PORTNUM._serialized_end=450
# @@protoc_insertion_point(module_scope)
