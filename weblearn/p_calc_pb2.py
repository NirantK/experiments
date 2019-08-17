# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: p_calc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='p_calc.proto',
  package='services.smartreply',
  syntax='proto3',
  serialized_options=_b('Z-github.com/verloop/api/go/services/smartreply'),
  serialized_pb=_b('\n\x0cp_calc.proto\x12\x13services.smartreply\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x02\"\x89\x01\n\x0fTrainSmartReply\x12\n\n\x02id\x18\x01 \x01(\t\x12\x33\n\x06status\x18\x02 \x01(\x0e\x32#.services.smartreply.TrainingStatus\x12\x18\n\x10percent_complete\x18\x14 \x01(\x05\x12\x0b\n\x03\x65ta\x18\x15 \x01(\x03\x12\x0e\n\x06tenant\x18\x05 \x01(\t\"F\n\x08Response\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\treplytext\x18\x02 \x01(\t\x12\x0b\n\x03rid\x18\x03 \x01(\t\x12\x0e\n\x06tenant\x18\x05 \x01(\t\"C\n\x05Query\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tquerytext\x18\x02 \x01(\t\x12\x0b\n\x03rid\x18\x03 \x01(\t\x12\x0e\n\x06tenant\x18\x05 \x01(\t\"t\n\x19ReferenceTimeWithTimezone\x12\x17\n\x0futcMilliSeconds\x18\x01 \x01(\x03\x12\x1a\n\x10utcOffsetMinutes\x18\x02 \x01(\x11H\x00\x12\x16\n\x0ctimezoneName\x18\x03 \x01(\tH\x00\x42\n\n\x08timezone*}\n\x0eTrainingStatus\x12\x14\n\x10TRAINING_UNKNOWN\x10\x00\x12\x13\n\x0fTRAINING_QUEUED\x10\x01\x12\x14\n\x10TRAINING_STARTED\x10\x02\x12\x14\n\x10TRAINING_SUCCESS\x10\x03\x12\x14\n\x10TRAINING_FAILURE\x10\x04\x32V\n\nCalculator\x12H\n\nSquareRoot\x12\x1b.services.smartreply.Number\x1a\x1b.services.smartreply.Number\"\x00\x32\\\n\x0eSuggestReponse\x12J\n\rGetSmartReply\x12\x1a.services.smartreply.Query\x1a\x1d.services.smartreply.Response2q\n\x12SmartReplyTraining\x12[\n\rBeginTraining\x12$.services.smartreply.TrainSmartReply\x1a$.services.smartreply.TrainSmartReplyB/Z-github.com/verloop/api/go/services/smartreplyb\x06proto3')
)

_TRAININGSTATUS = _descriptor.EnumDescriptor(
  name='TrainingStatus',
  full_name='services.smartreply.TrainingStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRAINING_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAINING_QUEUED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAINING_STARTED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAINING_SUCCESS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAINING_FAILURE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=461,
  serialized_end=586,
)
_sym_db.RegisterEnumDescriptor(_TRAININGSTATUS)

TrainingStatus = enum_type_wrapper.EnumTypeWrapper(_TRAININGSTATUS)
TRAINING_UNKNOWN = 0
TRAINING_QUEUED = 1
TRAINING_STARTED = 2
TRAINING_SUCCESS = 3
TRAINING_FAILURE = 4



_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='services.smartreply.Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='services.smartreply.Number.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=37,
  serialized_end=60,
)


_TRAINSMARTREPLY = _descriptor.Descriptor(
  name='TrainSmartReply',
  full_name='services.smartreply.TrainSmartReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='services.smartreply.TrainSmartReply.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='services.smartreply.TrainSmartReply.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percent_complete', full_name='services.smartreply.TrainSmartReply.percent_complete', index=2,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eta', full_name='services.smartreply.TrainSmartReply.eta', index=3,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenant', full_name='services.smartreply.TrainSmartReply.tenant', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=63,
  serialized_end=200,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='services.smartreply.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='services.smartreply.Response.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replytext', full_name='services.smartreply.Response.replytext', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rid', full_name='services.smartreply.Response.rid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenant', full_name='services.smartreply.Response.tenant', index=3,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=202,
  serialized_end=272,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='services.smartreply.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='services.smartreply.Query.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='querytext', full_name='services.smartreply.Query.querytext', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rid', full_name='services.smartreply.Query.rid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tenant', full_name='services.smartreply.Query.tenant', index=3,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=274,
  serialized_end=341,
)


_REFERENCETIMEWITHTIMEZONE = _descriptor.Descriptor(
  name='ReferenceTimeWithTimezone',
  full_name='services.smartreply.ReferenceTimeWithTimezone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='utcMilliSeconds', full_name='services.smartreply.ReferenceTimeWithTimezone.utcMilliSeconds', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='utcOffsetMinutes', full_name='services.smartreply.ReferenceTimeWithTimezone.utcOffsetMinutes', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timezoneName', full_name='services.smartreply.ReferenceTimeWithTimezone.timezoneName', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='timezone', full_name='services.smartreply.ReferenceTimeWithTimezone.timezone',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=343,
  serialized_end=459,
)

_TRAINSMARTREPLY.fields_by_name['status'].enum_type = _TRAININGSTATUS
_REFERENCETIMEWITHTIMEZONE.oneofs_by_name['timezone'].fields.append(
  _REFERENCETIMEWITHTIMEZONE.fields_by_name['utcOffsetMinutes'])
_REFERENCETIMEWITHTIMEZONE.fields_by_name['utcOffsetMinutes'].containing_oneof = _REFERENCETIMEWITHTIMEZONE.oneofs_by_name['timezone']
_REFERENCETIMEWITHTIMEZONE.oneofs_by_name['timezone'].fields.append(
  _REFERENCETIMEWITHTIMEZONE.fields_by_name['timezoneName'])
_REFERENCETIMEWITHTIMEZONE.fields_by_name['timezoneName'].containing_oneof = _REFERENCETIMEWITHTIMEZONE.oneofs_by_name['timezone']
DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
DESCRIPTOR.message_types_by_name['TrainSmartReply'] = _TRAINSMARTREPLY
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['ReferenceTimeWithTimezone'] = _REFERENCETIMEWITHTIMEZONE
DESCRIPTOR.enum_types_by_name['TrainingStatus'] = _TRAININGSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'p_calc_pb2'
  # @@protoc_insertion_point(class_scope:services.smartreply.Number)
  })
_sym_db.RegisterMessage(Number)

TrainSmartReply = _reflection.GeneratedProtocolMessageType('TrainSmartReply', (_message.Message,), {
  'DESCRIPTOR' : _TRAINSMARTREPLY,
  '__module__' : 'p_calc_pb2'
  # @@protoc_insertion_point(class_scope:services.smartreply.TrainSmartReply)
  })
_sym_db.RegisterMessage(TrainSmartReply)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'p_calc_pb2'
  # @@protoc_insertion_point(class_scope:services.smartreply.Response)
  })
_sym_db.RegisterMessage(Response)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'p_calc_pb2'
  # @@protoc_insertion_point(class_scope:services.smartreply.Query)
  })
_sym_db.RegisterMessage(Query)

ReferenceTimeWithTimezone = _reflection.GeneratedProtocolMessageType('ReferenceTimeWithTimezone', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCETIMEWITHTIMEZONE,
  '__module__' : 'p_calc_pb2'
  # @@protoc_insertion_point(class_scope:services.smartreply.ReferenceTimeWithTimezone)
  })
_sym_db.RegisterMessage(ReferenceTimeWithTimezone)


DESCRIPTOR._options = None

_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='services.smartreply.Calculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=588,
  serialized_end=674,
  methods=[
  _descriptor.MethodDescriptor(
    name='SquareRoot',
    full_name='services.smartreply.Calculator.SquareRoot',
    index=0,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR


_SUGGESTREPONSE = _descriptor.ServiceDescriptor(
  name='SuggestReponse',
  full_name='services.smartreply.SuggestReponse',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=676,
  serialized_end=768,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSmartReply',
    full_name='services.smartreply.SuggestReponse.GetSmartReply',
    index=0,
    containing_service=None,
    input_type=_QUERY,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SUGGESTREPONSE)

DESCRIPTOR.services_by_name['SuggestReponse'] = _SUGGESTREPONSE


_SMARTREPLYTRAINING = _descriptor.ServiceDescriptor(
  name='SmartReplyTraining',
  full_name='services.smartreply.SmartReplyTraining',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=770,
  serialized_end=883,
  methods=[
  _descriptor.MethodDescriptor(
    name='BeginTraining',
    full_name='services.smartreply.SmartReplyTraining.BeginTraining',
    index=0,
    containing_service=None,
    input_type=_TRAINSMARTREPLY,
    output_type=_TRAINSMARTREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SMARTREPLYTRAINING)

DESCRIPTOR.services_by_name['SmartReplyTraining'] = _SMARTREPLYTRAINING

# @@protoc_insertion_point(module_scope)