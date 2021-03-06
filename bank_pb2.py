# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bank.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bank.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nbank.proto\"J\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\naccount_no\x18\x02 \x01(\t\x12\x0e\n\x06pin_no\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x05\"\'\n\x0c\x42\x61nkAccounts\x12\x17\n\x06person\x18\x01 \x03(\x0b\x32\x07.Personb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Person.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='account_no', full_name='Person.account_no', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pin_no', full_name='Person.pin_no', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Person.amount', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=88,
)


_BANKACCOUNTS = _descriptor.Descriptor(
  name='BankAccounts',
  full_name='BankAccounts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='BankAccounts.person', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=129,
)

_BANKACCOUNTS.fields_by_name['person'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['BankAccounts'] = _BANKACCOUNTS

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(
  DESCRIPTOR = _PERSON,
  __module__ = 'bank_pb2'
  # @@protoc_insertion_point(class_scope:Person)
  ))
_sym_db.RegisterMessage(Person)

BankAccounts = _reflection.GeneratedProtocolMessageType('BankAccounts', (_message.Message,), dict(
  DESCRIPTOR = _BANKACCOUNTS,
  __module__ = 'bank_pb2'
  # @@protoc_insertion_point(class_scope:BankAccounts)
  ))
_sym_db.RegisterMessage(BankAccounts)


# @@protoc_insertion_point(module_scope)
