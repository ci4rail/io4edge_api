/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: tracelet.proto */

/* Do not generate deprecated warnings for self */
#ifndef PROTOBUF_C__NO_DEPRECATED
#define PROTOBUF_C__NO_DEPRECATED
#endif

#include "tracelet.pb-c.h"
void   tracelet__tracelet_to_server__location__gnss__init
                     (Tracelet__TraceletToServer__Location__Gnss         *message)
{
  static const Tracelet__TraceletToServer__Location__Gnss init_value = TRACELET__TRACELET_TO_SERVER__LOCATION__GNSS__INIT;
  *message = init_value;
}
void   tracelet__tracelet_to_server__location__uwb__init
                     (Tracelet__TraceletToServer__Location__Uwb         *message)
{
  static const Tracelet__TraceletToServer__Location__Uwb init_value = TRACELET__TRACELET_TO_SERVER__LOCATION__UWB__INIT;
  *message = init_value;
}
void   tracelet__tracelet_to_server__location__fused__init
                     (Tracelet__TraceletToServer__Location__Fused         *message)
{
  static const Tracelet__TraceletToServer__Location__Fused init_value = TRACELET__TRACELET_TO_SERVER__LOCATION__FUSED__INIT;
  *message = init_value;
}
void   tracelet__tracelet_to_server__location__acceleration__init
                     (Tracelet__TraceletToServer__Location__Acceleration         *message)
{
  static const Tracelet__TraceletToServer__Location__Acceleration init_value = TRACELET__TRACELET_TO_SERVER__LOCATION__ACCELERATION__INIT;
  *message = init_value;
}
void   tracelet__tracelet_to_server__location__init
                     (Tracelet__TraceletToServer__Location         *message)
{
  static const Tracelet__TraceletToServer__Location init_value = TRACELET__TRACELET_TO_SERVER__LOCATION__INIT;
  *message = init_value;
}
void   tracelet__tracelet_to_server__init
                     (Tracelet__TraceletToServer         *message)
{
  static const Tracelet__TraceletToServer init_value = TRACELET__TRACELET_TO_SERVER__INIT;
  *message = init_value;
}
size_t tracelet__tracelet_to_server__get_packed_size
                     (const Tracelet__TraceletToServer *message)
{
  assert(message->base.descriptor == &tracelet__tracelet_to_server__descriptor);
  return protobuf_c_message_get_packed_size ((const ProtobufCMessage*)(message));
}
size_t tracelet__tracelet_to_server__pack
                     (const Tracelet__TraceletToServer *message,
                      uint8_t       *out)
{
  assert(message->base.descriptor == &tracelet__tracelet_to_server__descriptor);
  return protobuf_c_message_pack ((const ProtobufCMessage*)message, out);
}
size_t tracelet__tracelet_to_server__pack_to_buffer
                     (const Tracelet__TraceletToServer *message,
                      ProtobufCBuffer *buffer)
{
  assert(message->base.descriptor == &tracelet__tracelet_to_server__descriptor);
  return protobuf_c_message_pack_to_buffer ((const ProtobufCMessage*)message, buffer);
}
Tracelet__TraceletToServer *
       tracelet__tracelet_to_server__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data)
{
  return (Tracelet__TraceletToServer *)
     protobuf_c_message_unpack (&tracelet__tracelet_to_server__descriptor,
                                allocator, len, data);
}
void   tracelet__tracelet_to_server__free_unpacked
                     (Tracelet__TraceletToServer *message,
                      ProtobufCAllocator *allocator)
{
  if(!message)
    return;
  assert(message->base.descriptor == &tracelet__tracelet_to_server__descriptor);
  protobuf_c_message_free_unpacked ((ProtobufCMessage*)message, allocator);
}
static const ProtobufCFieldDescriptor tracelet__tracelet_to_server__location__gnss__field_descriptors[11] =
{
  {
    "valid",
    1,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_BOOL,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Gnss, valid),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "latitude",
    2,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Gnss, latitude),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "longitude",
    3,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Gnss, longitude),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "altitude",
    4,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Gnss, altitude),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "eph",
    5,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Gnss, eph),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "epv",
    6,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Gnss, epv),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "fix_type",
    7,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_INT32,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Gnss, fix_type),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "head_motion",
    8,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Gnss, head_motion),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "head_vehicle",
    9,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Gnss, head_vehicle),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "head_valid",
    10,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Gnss, head_valid),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "ground_speed",
    11,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Gnss, ground_speed),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned tracelet__tracelet_to_server__location__gnss__field_indices_by_name[] = {
  3,   /* field[3] = altitude */
  4,   /* field[4] = eph */
  5,   /* field[5] = epv */
  6,   /* field[6] = fix_type */
  10,   /* field[10] = ground_speed */
  7,   /* field[7] = head_motion */
  9,   /* field[9] = head_valid */
  8,   /* field[8] = head_vehicle */
  1,   /* field[1] = latitude */
  2,   /* field[2] = longitude */
  0,   /* field[0] = valid */
};
static const ProtobufCIntRange tracelet__tracelet_to_server__location__gnss__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 11 }
};
const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__gnss__descriptor =
{
  PROTOBUF_C__MESSAGE_DESCRIPTOR_MAGIC,
  "tracelet.TraceletToServer.Location.Gnss",
  "Gnss",
  "Tracelet__TraceletToServer__Location__Gnss",
  "tracelet",
  sizeof(Tracelet__TraceletToServer__Location__Gnss),
  11,
  tracelet__tracelet_to_server__location__gnss__field_descriptors,
  tracelet__tracelet_to_server__location__gnss__field_indices_by_name,
  1,  tracelet__tracelet_to_server__location__gnss__number_ranges,
  (ProtobufCMessageInit) tracelet__tracelet_to_server__location__gnss__init,
  NULL,NULL,NULL    /* reserved[123] */
};
static const ProtobufCFieldDescriptor tracelet__tracelet_to_server__location__uwb__field_descriptors[7] =
{
  {
    "valid",
    1,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_BOOL,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Uwb, valid),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "x",
    2,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Uwb, x),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "y",
    3,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Uwb, y),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "z",
    4,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Uwb, z),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "site_id",
    5,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_UINT32,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Uwb, site_id),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "location_signature",
    6,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_FIXED64,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Uwb, location_signature),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "eph",
    7,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Uwb, eph),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned tracelet__tracelet_to_server__location__uwb__field_indices_by_name[] = {
  6,   /* field[6] = eph */
  5,   /* field[5] = location_signature */
  4,   /* field[4] = site_id */
  0,   /* field[0] = valid */
  1,   /* field[1] = x */
  2,   /* field[2] = y */
  3,   /* field[3] = z */
};
static const ProtobufCIntRange tracelet__tracelet_to_server__location__uwb__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 7 }
};
const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__uwb__descriptor =
{
  PROTOBUF_C__MESSAGE_DESCRIPTOR_MAGIC,
  "tracelet.TraceletToServer.Location.Uwb",
  "Uwb",
  "Tracelet__TraceletToServer__Location__Uwb",
  "tracelet",
  sizeof(Tracelet__TraceletToServer__Location__Uwb),
  7,
  tracelet__tracelet_to_server__location__uwb__field_descriptors,
  tracelet__tracelet_to_server__location__uwb__field_indices_by_name,
  1,  tracelet__tracelet_to_server__location__uwb__number_ranges,
  (ProtobufCMessageInit) tracelet__tracelet_to_server__location__uwb__init,
  NULL,NULL,NULL    /* reserved[123] */
};
static const ProtobufCFieldDescriptor tracelet__tracelet_to_server__location__fused__field_descriptors[4] =
{
  {
    "valid",
    1,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_BOOL,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Fused, valid),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "latitude",
    2,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Fused, latitude),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "longitude",
    3,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Fused, longitude),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "eph",
    5,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Fused, eph),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned tracelet__tracelet_to_server__location__fused__field_indices_by_name[] = {
  3,   /* field[3] = eph */
  1,   /* field[1] = latitude */
  2,   /* field[2] = longitude */
  0,   /* field[0] = valid */
};
static const ProtobufCIntRange tracelet__tracelet_to_server__location__fused__number_ranges[2 + 1] =
{
  { 1, 0 },
  { 5, 3 },
  { 0, 4 }
};
const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__fused__descriptor =
{
  PROTOBUF_C__MESSAGE_DESCRIPTOR_MAGIC,
  "tracelet.TraceletToServer.Location.Fused",
  "Fused",
  "Tracelet__TraceletToServer__Location__Fused",
  "tracelet",
  sizeof(Tracelet__TraceletToServer__Location__Fused),
  4,
  tracelet__tracelet_to_server__location__fused__field_descriptors,
  tracelet__tracelet_to_server__location__fused__field_indices_by_name,
  2,  tracelet__tracelet_to_server__location__fused__number_ranges,
  (ProtobufCMessageInit) tracelet__tracelet_to_server__location__fused__init,
  NULL,NULL,NULL    /* reserved[123] */
};
static const ProtobufCFieldDescriptor tracelet__tracelet_to_server__location__acceleration__field_descriptors[9] =
{
  {
    "x_max",
    1,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Acceleration, x_max),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "y_max",
    2,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Acceleration, y_max),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "z_max",
    3,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Acceleration, z_max),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "x_min",
    4,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Acceleration, x_min),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "y_min",
    5,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Acceleration, y_min),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "z_min",
    6,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Acceleration, z_min),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "x_avg",
    7,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Acceleration, x_avg),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "y_avg",
    8,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Acceleration, y_avg),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "z_avg",
    9,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location__Acceleration, z_avg),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned tracelet__tracelet_to_server__location__acceleration__field_indices_by_name[] = {
  6,   /* field[6] = x_avg */
  0,   /* field[0] = x_max */
  3,   /* field[3] = x_min */
  7,   /* field[7] = y_avg */
  1,   /* field[1] = y_max */
  4,   /* field[4] = y_min */
  8,   /* field[8] = z_avg */
  2,   /* field[2] = z_max */
  5,   /* field[5] = z_min */
};
static const ProtobufCIntRange tracelet__tracelet_to_server__location__acceleration__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 9 }
};
const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__acceleration__descriptor =
{
  PROTOBUF_C__MESSAGE_DESCRIPTOR_MAGIC,
  "tracelet.TraceletToServer.Location.Acceleration",
  "Acceleration",
  "Tracelet__TraceletToServer__Location__Acceleration",
  "tracelet",
  sizeof(Tracelet__TraceletToServer__Location__Acceleration),
  9,
  tracelet__tracelet_to_server__location__acceleration__field_descriptors,
  tracelet__tracelet_to_server__location__acceleration__field_indices_by_name,
  1,  tracelet__tracelet_to_server__location__acceleration__number_ranges,
  (ProtobufCMessageInit) tracelet__tracelet_to_server__location__acceleration__init,
  NULL,NULL,NULL    /* reserved[123] */
};
static const ProtobufCEnumValue tracelet__tracelet_to_server__location__direction__enum_values_by_number[3] =
{
  { "NO_DIRECTION", "TRACELET__TRACELET_TO_SERVER__LOCATION__DIRECTION__NO_DIRECTION", 0 },
  { "CAB_A_DIRECTION", "TRACELET__TRACELET_TO_SERVER__LOCATION__DIRECTION__CAB_A_DIRECTION", 1 },
  { "CAB_B_DIRECTION", "TRACELET__TRACELET_TO_SERVER__LOCATION__DIRECTION__CAB_B_DIRECTION", 2 },
};
static const ProtobufCIntRange tracelet__tracelet_to_server__location__direction__value_ranges[] = {
{0, 0},{0, 3}
};
static const ProtobufCEnumValueIndex tracelet__tracelet_to_server__location__direction__enum_values_by_name[3] =
{
  { "CAB_A_DIRECTION", 1 },
  { "CAB_B_DIRECTION", 2 },
  { "NO_DIRECTION", 0 },
};
const ProtobufCEnumDescriptor tracelet__tracelet_to_server__location__direction__descriptor =
{
  PROTOBUF_C__ENUM_DESCRIPTOR_MAGIC,
  "tracelet.TraceletToServer.Location.Direction",
  "Direction",
  "Tracelet__TraceletToServer__Location__Direction",
  "tracelet",
  3,
  tracelet__tracelet_to_server__location__direction__enum_values_by_number,
  3,
  tracelet__tracelet_to_server__location__direction__enum_values_by_name,
  1,
  tracelet__tracelet_to_server__location__direction__value_ranges,
  NULL,NULL,NULL,NULL   /* reserved[1234] */
};
static const ProtobufCFieldDescriptor tracelet__tracelet_to_server__location__field_descriptors[8] =
{
  {
    "gnss",
    1,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_MESSAGE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location, gnss),
    &tracelet__tracelet_to_server__location__gnss__descriptor,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "uwb",
    2,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_MESSAGE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location, uwb),
    &tracelet__tracelet_to_server__location__uwb__descriptor,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "direction",
    3,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_ENUM,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location, direction),
    &tracelet__tracelet_to_server__location__direction__descriptor,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "speed",
    4,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location, speed),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "mileage",
    5,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_INT32,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location, mileage),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "temperature",
    6,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_DOUBLE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location, temperature),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "fused",
    7,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_MESSAGE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location, fused),
    &tracelet__tracelet_to_server__location__fused__descriptor,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "acceleration",
    8,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_MESSAGE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer__Location, acceleration),
    &tracelet__tracelet_to_server__location__acceleration__descriptor,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned tracelet__tracelet_to_server__location__field_indices_by_name[] = {
  7,   /* field[7] = acceleration */
  2,   /* field[2] = direction */
  6,   /* field[6] = fused */
  0,   /* field[0] = gnss */
  4,   /* field[4] = mileage */
  3,   /* field[3] = speed */
  5,   /* field[5] = temperature */
  1,   /* field[1] = uwb */
};
static const ProtobufCIntRange tracelet__tracelet_to_server__location__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 8 }
};
const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__descriptor =
{
  PROTOBUF_C__MESSAGE_DESCRIPTOR_MAGIC,
  "tracelet.TraceletToServer.Location",
  "Location",
  "Tracelet__TraceletToServer__Location",
  "tracelet",
  sizeof(Tracelet__TraceletToServer__Location),
  8,
  tracelet__tracelet_to_server__location__field_descriptors,
  tracelet__tracelet_to_server__location__field_indices_by_name,
  1,  tracelet__tracelet_to_server__location__number_ranges,
  (ProtobufCMessageInit) tracelet__tracelet_to_server__location__init,
  NULL,NULL,NULL    /* reserved[123] */
};
static const ProtobufCFieldDescriptor tracelet__tracelet_to_server__field_descriptors[5] =
{
  {
    "id",
    1,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_INT32,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer, id),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "delivery_ts",
    2,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_MESSAGE,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer, delivery_ts),
    &google__protobuf__timestamp__descriptor,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "tracelet_id",
    3,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_STRING,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer, tracelet_id),
    NULL,
    &protobuf_c_empty_string,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "ignition",
    4,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_BOOL,
    0,   /* quantifier_offset */
    offsetof(Tracelet__TraceletToServer, ignition),
    NULL,
    NULL,
    0,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
  {
    "location",
    5,
    PROTOBUF_C_LABEL_NONE,
    PROTOBUF_C_TYPE_MESSAGE,
    offsetof(Tracelet__TraceletToServer, type_case),
    offsetof(Tracelet__TraceletToServer, location),
    &tracelet__tracelet_to_server__location__descriptor,
    NULL,
    0 | PROTOBUF_C_FIELD_FLAG_ONEOF,             /* flags */
    0,NULL,NULL    /* reserved1,reserved2, etc */
  },
};
static const unsigned tracelet__tracelet_to_server__field_indices_by_name[] = {
  1,   /* field[1] = delivery_ts */
  0,   /* field[0] = id */
  3,   /* field[3] = ignition */
  4,   /* field[4] = location */
  2,   /* field[2] = tracelet_id */
};
static const ProtobufCIntRange tracelet__tracelet_to_server__number_ranges[1 + 1] =
{
  { 1, 0 },
  { 0, 5 }
};
const ProtobufCMessageDescriptor tracelet__tracelet_to_server__descriptor =
{
  PROTOBUF_C__MESSAGE_DESCRIPTOR_MAGIC,
  "tracelet.TraceletToServer",
  "TraceletToServer",
  "Tracelet__TraceletToServer",
  "tracelet",
  sizeof(Tracelet__TraceletToServer),
  5,
  tracelet__tracelet_to_server__field_descriptors,
  tracelet__tracelet_to_server__field_indices_by_name,
  1,  tracelet__tracelet_to_server__number_ranges,
  (ProtobufCMessageInit) tracelet__tracelet_to_server__init,
  NULL,NULL,NULL    /* reserved[123] */
};
