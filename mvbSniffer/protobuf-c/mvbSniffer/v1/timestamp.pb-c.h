/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: timestamp.proto */

#ifndef PROTOBUF_C_timestamp_2eproto__INCLUDED
#define PROTOBUF_C_timestamp_2eproto__INCLUDED

#include <protobuf-c/protobuf-c.h>

PROTOBUF_C__BEGIN_DECLS

#if PROTOBUF_C_VERSION_NUMBER < 1003000
# error This file was generated by a newer version of protoc-c which is incompatible with your libprotobuf-c headers. Please update your headers.
#elif 1003003 < PROTOBUF_C_MIN_COMPILER_VERSION
# error This file was generated by an older version of protoc-c which is incompatible with your libprotobuf-c headers. Please regenerate this file with a newer version of protoc-c.
#endif


typedef struct _MvbSniffer__Timestamp MvbSniffer__Timestamp;


/* --- enums --- */


/* --- messages --- */

struct  _MvbSniffer__Timestamp
{
  ProtobufCMessage base;
  uint64_t seconds;
  uint64_t microseconds;
};
#define MVB_SNIFFER__TIMESTAMP__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_sniffer__timestamp__descriptor) \
    , 0, 0 }


/* MvbSniffer__Timestamp methods */
void   mvb_sniffer__timestamp__init
                     (MvbSniffer__Timestamp         *message);
size_t mvb_sniffer__timestamp__get_packed_size
                     (const MvbSniffer__Timestamp   *message);
size_t mvb_sniffer__timestamp__pack
                     (const MvbSniffer__Timestamp   *message,
                      uint8_t             *out);
size_t mvb_sniffer__timestamp__pack_to_buffer
                     (const MvbSniffer__Timestamp   *message,
                      ProtobufCBuffer     *buffer);
MvbSniffer__Timestamp *
       mvb_sniffer__timestamp__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_sniffer__timestamp__free_unpacked
                     (MvbSniffer__Timestamp *message,
                      ProtobufCAllocator *allocator);
/* --- per-message closures --- */

typedef void (*MvbSniffer__Timestamp_Closure)
                 (const MvbSniffer__Timestamp *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCMessageDescriptor mvb_sniffer__timestamp__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_timestamp_2eproto__INCLUDED */
