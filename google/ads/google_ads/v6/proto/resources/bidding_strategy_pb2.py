# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/resources/bidding_strategy.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.common import bidding_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_bidding__pb2
from google.ads.google_ads.v6.proto.enums import bidding_strategy_status_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_bidding__strategy__status__pb2
from google.ads.google_ads.v6.proto.enums import bidding_strategy_type_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_bidding__strategy__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/resources/bidding_strategy.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\024BiddingStrategyProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>google/ads/googleads_v6/proto/resources/bidding_strategy.proto\x12!google.ads.googleads.v6.resources\x1a\x32google/ads/googleads_v6/proto/common/bidding.proto\x1a\x41google/ads/googleads_v6/proto/enums/bidding_strategy_status.proto\x1a?google/ads/googleads_v6/proto/enums/bidding_strategy_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xb5\t\n\x0f\x42iddingStrategy\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0\x41\x05\xfa\x41*\n(googleads.googleapis.com/BiddingStrategy\x12\x14\n\x02id\x18\x10 \x01(\x03\x42\x03\xe0\x41\x03H\x01\x88\x01\x01\x12\x11\n\x04name\x18\x11 \x01(\tH\x02\x88\x01\x01\x12\x63\n\x06status\x18\x0f \x01(\x0e\x32N.google.ads.googleads.v6.enums.BiddingStrategyStatusEnum.BiddingStrategyStatusB\x03\xe0\x41\x03\x12]\n\x04type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v6.enums.BiddingStrategyTypeEnum.BiddingStrategyTypeB\x03\xe0\x41\x03\x12)\n\x17\x65\x66\x66\x65\x63tive_currency_code\x18\x14 \x01(\tB\x03\xe0\x41\x03H\x03\x88\x01\x01\x12 \n\x0e\x63\x61mpaign_count\x18\x12 \x01(\x03\x42\x03\xe0\x41\x03H\x04\x88\x01\x01\x12,\n\x1anon_removed_campaign_count\x18\x13 \x01(\x03\x42\x03\xe0\x41\x03H\x05\x88\x01\x01\x12\x43\n\x0c\x65nhanced_cpc\x18\x07 \x01(\x0b\x32+.google.ads.googleads.v6.common.EnhancedCpcH\x00\x12\\\n\x19maximize_conversion_value\x18\x15 \x01(\x0b\x32\x37.google.ads.googleads.v6.common.MaximizeConversionValueH\x00\x12S\n\x14maximize_conversions\x18\x16 \x01(\x0b\x32\x33.google.ads.googleads.v6.common.MaximizeConversionsH\x00\x12?\n\ntarget_cpa\x18\t \x01(\x0b\x32).google.ads.googleads.v6.common.TargetCpaH\x00\x12X\n\x17target_impression_share\x18\x30 \x01(\x0b\x32\x35.google.ads.googleads.v6.common.TargetImpressionShareH\x00\x12\x41\n\x0btarget_roas\x18\x0b \x01(\x0b\x32*.google.ads.googleads.v6.common.TargetRoasH\x00\x12\x43\n\x0ctarget_spend\x18\x0c \x01(\x0b\x32+.google.ads.googleads.v6.common.TargetSpendH\x00:n\xea\x41k\n(googleads.googleapis.com/BiddingStrategy\x12?customers/{customer_id}/biddingStrategies/{bidding_strategy_id}B\x08\n\x06schemeB\x05\n\x03_idB\x07\n\x05_nameB\x1a\n\x18_effective_currency_codeB\x11\n\x0f_campaign_countB\x1d\n\x1b_non_removed_campaign_countB\x81\x02\n%com.google.ads.googleads.v6.resourcesB\x14\x42iddingStrategyProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_bidding__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_bidding__strategy__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_bidding__strategy__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_BIDDINGSTRATEGY = _descriptor.Descriptor(
  name='BiddingStrategy',
  full_name='google.ads.googleads.v6.resources.BiddingStrategy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.BiddingStrategy.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A*\n(googleads.googleapis.com/BiddingStrategy', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v6.resources.BiddingStrategy.id', index=1,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v6.resources.BiddingStrategy.name', index=2,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v6.resources.BiddingStrategy.status', index=3,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v6.resources.BiddingStrategy.type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='effective_currency_code', full_name='google.ads.googleads.v6.resources.BiddingStrategy.effective_currency_code', index=5,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign_count', full_name='google.ads.googleads.v6.resources.BiddingStrategy.campaign_count', index=6,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='non_removed_campaign_count', full_name='google.ads.googleads.v6.resources.BiddingStrategy.non_removed_campaign_count', index=7,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enhanced_cpc', full_name='google.ads.googleads.v6.resources.BiddingStrategy.enhanced_cpc', index=8,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maximize_conversion_value', full_name='google.ads.googleads.v6.resources.BiddingStrategy.maximize_conversion_value', index=9,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maximize_conversions', full_name='google.ads.googleads.v6.resources.BiddingStrategy.maximize_conversions', index=10,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_cpa', full_name='google.ads.googleads.v6.resources.BiddingStrategy.target_cpa', index=11,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_impression_share', full_name='google.ads.googleads.v6.resources.BiddingStrategy.target_impression_share', index=12,
      number=48, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_roas', full_name='google.ads.googleads.v6.resources.BiddingStrategy.target_roas', index=13,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_spend', full_name='google.ads.googleads.v6.resources.BiddingStrategy.target_spend', index=14,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Ak\n(googleads.googleapis.com/BiddingStrategy\022?customers/{customer_id}/biddingStrategies/{bidding_strategy_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='scheme', full_name='google.ads.googleads.v6.resources.BiddingStrategy.scheme',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_id', full_name='google.ads.googleads.v6.resources.BiddingStrategy._id',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_name', full_name='google.ads.googleads.v6.resources.BiddingStrategy._name',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_effective_currency_code', full_name='google.ads.googleads.v6.resources.BiddingStrategy._effective_currency_code',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_campaign_count', full_name='google.ads.googleads.v6.resources.BiddingStrategy._campaign_count',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_non_removed_campaign_count', full_name='google.ads.googleads.v6.resources.BiddingStrategy._non_removed_campaign_count',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=376,
  serialized_end=1581,
)

_BIDDINGSTRATEGY.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_bidding__strategy__status__pb2._BIDDINGSTRATEGYSTATUSENUM_BIDDINGSTRATEGYSTATUS
_BIDDINGSTRATEGY.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_bidding__strategy__type__pb2._BIDDINGSTRATEGYTYPEENUM_BIDDINGSTRATEGYTYPE
_BIDDINGSTRATEGY.fields_by_name['enhanced_cpc'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_bidding__pb2._ENHANCEDCPC
_BIDDINGSTRATEGY.fields_by_name['maximize_conversion_value'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_bidding__pb2._MAXIMIZECONVERSIONVALUE
_BIDDINGSTRATEGY.fields_by_name['maximize_conversions'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_bidding__pb2._MAXIMIZECONVERSIONS
_BIDDINGSTRATEGY.fields_by_name['target_cpa'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_bidding__pb2._TARGETCPA
_BIDDINGSTRATEGY.fields_by_name['target_impression_share'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_bidding__pb2._TARGETIMPRESSIONSHARE
_BIDDINGSTRATEGY.fields_by_name['target_roas'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_bidding__pb2._TARGETROAS
_BIDDINGSTRATEGY.fields_by_name['target_spend'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_bidding__pb2._TARGETSPEND
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['enhanced_cpc'])
_BIDDINGSTRATEGY.fields_by_name['enhanced_cpc'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['maximize_conversion_value'])
_BIDDINGSTRATEGY.fields_by_name['maximize_conversion_value'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['maximize_conversions'])
_BIDDINGSTRATEGY.fields_by_name['maximize_conversions'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['target_cpa'])
_BIDDINGSTRATEGY.fields_by_name['target_cpa'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['target_impression_share'])
_BIDDINGSTRATEGY.fields_by_name['target_impression_share'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['target_roas'])
_BIDDINGSTRATEGY.fields_by_name['target_roas'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['scheme'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['target_spend'])
_BIDDINGSTRATEGY.fields_by_name['target_spend'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['scheme']
_BIDDINGSTRATEGY.oneofs_by_name['_id'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['id'])
_BIDDINGSTRATEGY.fields_by_name['id'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['_id']
_BIDDINGSTRATEGY.oneofs_by_name['_name'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['name'])
_BIDDINGSTRATEGY.fields_by_name['name'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['_name']
_BIDDINGSTRATEGY.oneofs_by_name['_effective_currency_code'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['effective_currency_code'])
_BIDDINGSTRATEGY.fields_by_name['effective_currency_code'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['_effective_currency_code']
_BIDDINGSTRATEGY.oneofs_by_name['_campaign_count'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['campaign_count'])
_BIDDINGSTRATEGY.fields_by_name['campaign_count'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['_campaign_count']
_BIDDINGSTRATEGY.oneofs_by_name['_non_removed_campaign_count'].fields.append(
  _BIDDINGSTRATEGY.fields_by_name['non_removed_campaign_count'])
_BIDDINGSTRATEGY.fields_by_name['non_removed_campaign_count'].containing_oneof = _BIDDINGSTRATEGY.oneofs_by_name['_non_removed_campaign_count']
DESCRIPTOR.message_types_by_name['BiddingStrategy'] = _BIDDINGSTRATEGY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BiddingStrategy = _reflection.GeneratedProtocolMessageType('BiddingStrategy', (_message.Message,), {
  'DESCRIPTOR' : _BIDDINGSTRATEGY,
  '__module__' : 'google.ads.googleads_v6.proto.resources.bidding_strategy_pb2'
  ,
  '__doc__': """A bidding strategy.
  
  Attributes:
      resource_name:
          Immutable. The resource name of the bidding strategy. Bidding
          strategy resource names have the form:  ``customers/{customer_
          id}/biddingStrategies/{bidding_strategy_id}``
      id:
          Output only. The ID of the bidding strategy.
      name:
          The name of the bidding strategy. All bidding strategies
          within an account must be named distinctly.  The length of
          this string should be between 1 and 255, inclusive, in UTF-8
          bytes, (trimmed).
      status:
          Output only. The status of the bidding strategy.  This field
          is read-only.
      type:
          Output only. The type of the bidding strategy. Create a
          bidding strategy by setting the bidding scheme.  This field is
          read-only.
      effective_currency_code:
          Output only. The currency used by the bidding strategy (ISO
          4217 three-letter code).  For bidding strategies in manager
          customers, this is the currency set by the advertiser when
          creating the strategy. For serving customers, this is the
          customer's currency\_code.  Bidding strategy metrics are
          reported in this currency.  This field is read-only.
      campaign_count:
          Output only. The number of campaigns attached to this bidding
          strategy.  This field is read-only.
      non_removed_campaign_count:
          Output only. The number of non-removed campaigns attached to
          this bidding strategy.  This field is read-only.
      scheme:
          The bidding scheme.  Only one can be set.
      enhanced_cpc:
          A bidding strategy that raises bids for clicks that seem more
          likely to lead to a conversion and lowers them for clicks
          where they seem less likely.
      maximize_conversion_value:
          An automated bidding strategy to help get the most conversion
          value for your campaigns while spending your budget.
      maximize_conversions:
          An automated bidding strategy to help get the most conversions
          for your campaigns while spending your budget.
      target_cpa:
          A bidding strategy that sets bids to help get as many
          conversions as possible at the target cost-per-acquisition
          (CPA) you set.
      target_impression_share:
          A bidding strategy that automatically optimizes towards a
          desired percentage of impressions.
      target_roas:
          A bidding strategy that helps you maximize revenue while
          averaging a specific target Return On Ad Spend (ROAS).
      target_spend:
          A bid strategy that sets your bids to help get as many clicks
          as possible within your budget.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.BiddingStrategy)
  })
_sym_db.RegisterMessage(BiddingStrategy)


DESCRIPTOR._options = None
_BIDDINGSTRATEGY.fields_by_name['resource_name']._options = None
_BIDDINGSTRATEGY.fields_by_name['id']._options = None
_BIDDINGSTRATEGY.fields_by_name['status']._options = None
_BIDDINGSTRATEGY.fields_by_name['type']._options = None
_BIDDINGSTRATEGY.fields_by_name['effective_currency_code']._options = None
_BIDDINGSTRATEGY.fields_by_name['campaign_count']._options = None
_BIDDINGSTRATEGY.fields_by_name['non_removed_campaign_count']._options = None
_BIDDINGSTRATEGY._options = None
# @@protoc_insertion_point(module_scope)
