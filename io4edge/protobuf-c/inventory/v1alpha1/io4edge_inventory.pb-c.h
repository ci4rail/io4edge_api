/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: io4edge_inventory.proto */

#ifndef PROTOBUF_C_io4edge_5finventory_2eproto__INCLUDED
#define PROTOBUF_C_io4edge_5finventory_2eproto__INCLUDED

#include <protobuf-c/protobuf-c.h>

PROTOBUF_C__BEGIN_DECLS

#if PROTOBUF_C_VERSION_NUMBER < 1003000
# error This file was generated by a newer version of protoc-c which is incompatible with your libprotobuf-c headers. Please update your headers.
#elif 1003003 < PROTOBUF_C_MIN_COMPILER_VERSION
# error This file was generated by an older version of protoc-c which is incompatible with your libprotobuf-c headers. Please regenerate this file with a newer version of protoc-c.
#endif


typedef struct _Io4edgeInventory__Unit Io4edgeInventory__Unit;


/* --- enums --- */


/* --- messages --- */

struct  _Io4edgeInventory__Unit
{
  ProtobufCMessage base;
  char *root_article;
  uint32_t major_version;
  char *serial;
};
#define IO4EDGE_INVENTORY__UNIT__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&io4edge_inventory__unit__descriptor) \
    , (char *)protobuf_c_empty_string, 0, (char *)protobuf_c_empty_string }


/* Io4edgeInventory__Unit methods */
void   io4edge_inventory__unit__init
                     (Io4edgeInventory__Unit         *message);
size_t io4edge_inventory__unit__get_packed_size
                     (const Io4edgeInventory__Unit   *message);
size_t io4edge_inventory__unit__pack
                     (const Io4edgeInventory__Unit   *message,
                      uint8_t             *out);
size_t io4edge_inventory__unit__pack_to_buffer
                     (const Io4edgeInventory__Unit   *message,
                      ProtobufCBuffer     *buffer);
Io4edgeInventory__Unit *
       io4edge_inventory__unit__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   io4edge_inventory__unit__free_unpacked
                     (Io4edgeInventory__Unit *message,
                      ProtobufCAllocator *allocator);
/* --- per-message closures --- */

typedef void (*Io4edgeInventory__Unit_Closure)
                 (const Io4edgeInventory__Unit *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCMessageDescriptor io4edge_inventory__unit__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_io4edge_5finventory_2eproto__INCLUDED */
