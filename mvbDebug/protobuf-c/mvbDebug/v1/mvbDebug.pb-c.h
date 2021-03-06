/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: mvbDebug.proto */

#ifndef PROTOBUF_C_mvbDebug_2eproto__INCLUDED
#define PROTOBUF_C_mvbDebug_2eproto__INCLUDED

#include <protobuf-c/protobuf-c.h>

PROTOBUF_C__BEGIN_DECLS

#if PROTOBUF_C_VERSION_NUMBER < 1003000
# error This file was generated by a newer version of protoc-c which is incompatible with your libprotobuf-c headers. Please update your headers.
#elif 1003003 < PROTOBUF_C_MIN_COMPILER_VERSION
# error This file was generated by an older version of protoc-c which is incompatible with your libprotobuf-c headers. Please regenerate this file with a newer version of protoc-c.
#endif


typedef struct _MvbDebug__ConfigurationSet MvbDebug__ConfigurationSet;
typedef struct _MvbDebug__ConfigurationSetResponse MvbDebug__ConfigurationSetResponse;
typedef struct _MvbDebug__ConfigurationGet MvbDebug__ConfigurationGet;
typedef struct _MvbDebug__ConfigurationGetResponse MvbDebug__ConfigurationGetResponse;
typedef struct _MvbDebug__ConfigurationDescribe MvbDebug__ConfigurationDescribe;
typedef struct _MvbDebug__ConfigurationDescribeResponse MvbDebug__ConfigurationDescribeResponse;
typedef struct _MvbDebug__FunctionControlGet MvbDebug__FunctionControlGet;
typedef struct _MvbDebug__FunctionControlSet MvbDebug__FunctionControlSet;
typedef struct _MvbDebug__FunctionControlGetResponse MvbDebug__FunctionControlGetResponse;
typedef struct _MvbDebug__FunctionControlSetResponse MvbDebug__FunctionControlSetResponse;
typedef struct _MvbDebug__StreamControlStart MvbDebug__StreamControlStart;
typedef struct _MvbDebug__Sample MvbDebug__Sample;
typedef struct _MvbDebug__StreamData MvbDebug__StreamData;


/* --- enums --- */


/* --- messages --- */

/*
 * ConfigurationSet to pass to Functionblock.Configuration.functionSpecificConfigurationSet hook
 */
struct  _MvbDebug__ConfigurationSet
{
  ProtobufCMessage base;
};
#define MVB_DEBUG__CONFIGURATION_SET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__configuration_set__descriptor) \
     }


/*
 * ConfigurationSetResponse to pass to Functionblock.Configuration.functionSpecificConfigurationSetResponse hook
 */
struct  _MvbDebug__ConfigurationSetResponse
{
  ProtobufCMessage base;
};
#define MVB_DEBUG__CONFIGURATION_SET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__configuration_set_response__descriptor) \
     }


/*
 * ConfigurationGet to pass to Functionblock.Configuration.functionSpecificConfigurationGet hook
 */
struct  _MvbDebug__ConfigurationGet
{
  ProtobufCMessage base;
};
#define MVB_DEBUG__CONFIGURATION_GET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__configuration_get__descriptor) \
     }


/*
 * ConfigurationGetResponse to pass to Functionblock.ConfigurationGetResponse.functionSpecificConfigurationGetResponse hook
 * Returns the current hardware configuration
 */
struct  _MvbDebug__ConfigurationGetResponse
{
  ProtobufCMessage base;
};
#define MVB_DEBUG__CONFIGURATION_GET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__configuration_get_response__descriptor) \
     }


/*
 * ConfigurationDescribe to pass to Functionblock.Configuration.functionSpecificConfigurationDescribe hook
 */
struct  _MvbDebug__ConfigurationDescribe
{
  ProtobufCMessage base;
};
#define MVB_DEBUG__CONFIGURATION_DESCRIBE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__configuration_describe__descriptor) \
     }


struct  _MvbDebug__ConfigurationDescribeResponse
{
  ProtobufCMessage base;
};
#define MVB_DEBUG__CONFIGURATION_DESCRIBE_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__configuration_describe_response__descriptor) \
     }


/*
 * FunctionControlGet to pass to Functionblock.FunctionControl.functionSpecificFunctionControlGet hook
 */
struct  _MvbDebug__FunctionControlGet
{
  ProtobufCMessage base;
};
#define MVB_DEBUG__FUNCTION_CONTROL_GET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__function_control_get__descriptor) \
     }


/*
 * FunctionControlSet to pass to
 * Functionblock.FunctionControl.functionSpecificFunctionControlSet hookmessage FunctionControlSet {
 */
struct  _MvbDebug__FunctionControlSet
{
  ProtobufCMessage base;
  /*
   * pattern to send to the stimulus generator within the MVB sniffer for self-test
   */
  char *generator_pattern;
};
#define MVB_DEBUG__FUNCTION_CONTROL_SET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__function_control_set__descriptor) \
    , (char *)protobuf_c_empty_string }


/*
 * FunctionControlGetResponse to pass to Functionblock.FunctionControlResponse.functionSpecificControlGet hook
 */
struct  _MvbDebug__FunctionControlGetResponse
{
  ProtobufCMessage base;
  float value;
};
#define MVB_DEBUG__FUNCTION_CONTROL_GET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__function_control_get_response__descriptor) \
    , 0 }


/*
 * FunctionControlSetResponse to pass to Functionblock.FunctionControlResponse.functionSpecificControlSet hook
 */
struct  _MvbDebug__FunctionControlSetResponse
{
  ProtobufCMessage base;
};
#define MVB_DEBUG__FUNCTION_CONTROL_SET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__function_control_set_response__descriptor) \
     }


/*
 * ============= StreamControl ==================
 * StreamControlStart to pass to Functionblock.StreamControlStart.functionSpecificStreamControlStart hook
 */
struct  _MvbDebug__StreamControlStart
{
  ProtobufCMessage base;
};
#define MVB_DEBUG__STREAM_CONTROL_START__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__stream_control_start__descriptor) \
     }


struct  _MvbDebug__Sample
{
  ProtobufCMessage base;
  /*
   * raw data block from FPGA in debug mode
   */
  ProtobufCBinaryData transitions_block;
};
#define MVB_DEBUG__SAMPLE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__sample__descriptor) \
    , {0,NULL} }


/*
 * StreamData to pass to Functionblock.StreamData.functionSpecificStreamData hook
 */
struct  _MvbDebug__StreamData
{
  ProtobufCMessage base;
  size_t n_samples;
  MvbDebug__Sample **samples;
};
#define MVB_DEBUG__STREAM_DATA__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_debug__stream_data__descriptor) \
    , 0,NULL }


/* MvbDebug__ConfigurationSet methods */
void   mvb_debug__configuration_set__init
                     (MvbDebug__ConfigurationSet         *message);
size_t mvb_debug__configuration_set__get_packed_size
                     (const MvbDebug__ConfigurationSet   *message);
size_t mvb_debug__configuration_set__pack
                     (const MvbDebug__ConfigurationSet   *message,
                      uint8_t             *out);
size_t mvb_debug__configuration_set__pack_to_buffer
                     (const MvbDebug__ConfigurationSet   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__ConfigurationSet *
       mvb_debug__configuration_set__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__configuration_set__free_unpacked
                     (MvbDebug__ConfigurationSet *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__ConfigurationSetResponse methods */
void   mvb_debug__configuration_set_response__init
                     (MvbDebug__ConfigurationSetResponse         *message);
size_t mvb_debug__configuration_set_response__get_packed_size
                     (const MvbDebug__ConfigurationSetResponse   *message);
size_t mvb_debug__configuration_set_response__pack
                     (const MvbDebug__ConfigurationSetResponse   *message,
                      uint8_t             *out);
size_t mvb_debug__configuration_set_response__pack_to_buffer
                     (const MvbDebug__ConfigurationSetResponse   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__ConfigurationSetResponse *
       mvb_debug__configuration_set_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__configuration_set_response__free_unpacked
                     (MvbDebug__ConfigurationSetResponse *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__ConfigurationGet methods */
void   mvb_debug__configuration_get__init
                     (MvbDebug__ConfigurationGet         *message);
size_t mvb_debug__configuration_get__get_packed_size
                     (const MvbDebug__ConfigurationGet   *message);
size_t mvb_debug__configuration_get__pack
                     (const MvbDebug__ConfigurationGet   *message,
                      uint8_t             *out);
size_t mvb_debug__configuration_get__pack_to_buffer
                     (const MvbDebug__ConfigurationGet   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__ConfigurationGet *
       mvb_debug__configuration_get__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__configuration_get__free_unpacked
                     (MvbDebug__ConfigurationGet *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__ConfigurationGetResponse methods */
void   mvb_debug__configuration_get_response__init
                     (MvbDebug__ConfigurationGetResponse         *message);
size_t mvb_debug__configuration_get_response__get_packed_size
                     (const MvbDebug__ConfigurationGetResponse   *message);
size_t mvb_debug__configuration_get_response__pack
                     (const MvbDebug__ConfigurationGetResponse   *message,
                      uint8_t             *out);
size_t mvb_debug__configuration_get_response__pack_to_buffer
                     (const MvbDebug__ConfigurationGetResponse   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__ConfigurationGetResponse *
       mvb_debug__configuration_get_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__configuration_get_response__free_unpacked
                     (MvbDebug__ConfigurationGetResponse *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__ConfigurationDescribe methods */
void   mvb_debug__configuration_describe__init
                     (MvbDebug__ConfigurationDescribe         *message);
size_t mvb_debug__configuration_describe__get_packed_size
                     (const MvbDebug__ConfigurationDescribe   *message);
size_t mvb_debug__configuration_describe__pack
                     (const MvbDebug__ConfigurationDescribe   *message,
                      uint8_t             *out);
size_t mvb_debug__configuration_describe__pack_to_buffer
                     (const MvbDebug__ConfigurationDescribe   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__ConfigurationDescribe *
       mvb_debug__configuration_describe__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__configuration_describe__free_unpacked
                     (MvbDebug__ConfigurationDescribe *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__ConfigurationDescribeResponse methods */
void   mvb_debug__configuration_describe_response__init
                     (MvbDebug__ConfigurationDescribeResponse         *message);
size_t mvb_debug__configuration_describe_response__get_packed_size
                     (const MvbDebug__ConfigurationDescribeResponse   *message);
size_t mvb_debug__configuration_describe_response__pack
                     (const MvbDebug__ConfigurationDescribeResponse   *message,
                      uint8_t             *out);
size_t mvb_debug__configuration_describe_response__pack_to_buffer
                     (const MvbDebug__ConfigurationDescribeResponse   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__ConfigurationDescribeResponse *
       mvb_debug__configuration_describe_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__configuration_describe_response__free_unpacked
                     (MvbDebug__ConfigurationDescribeResponse *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__FunctionControlGet methods */
void   mvb_debug__function_control_get__init
                     (MvbDebug__FunctionControlGet         *message);
size_t mvb_debug__function_control_get__get_packed_size
                     (const MvbDebug__FunctionControlGet   *message);
size_t mvb_debug__function_control_get__pack
                     (const MvbDebug__FunctionControlGet   *message,
                      uint8_t             *out);
size_t mvb_debug__function_control_get__pack_to_buffer
                     (const MvbDebug__FunctionControlGet   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__FunctionControlGet *
       mvb_debug__function_control_get__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__function_control_get__free_unpacked
                     (MvbDebug__FunctionControlGet *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__FunctionControlSet methods */
void   mvb_debug__function_control_set__init
                     (MvbDebug__FunctionControlSet         *message);
size_t mvb_debug__function_control_set__get_packed_size
                     (const MvbDebug__FunctionControlSet   *message);
size_t mvb_debug__function_control_set__pack
                     (const MvbDebug__FunctionControlSet   *message,
                      uint8_t             *out);
size_t mvb_debug__function_control_set__pack_to_buffer
                     (const MvbDebug__FunctionControlSet   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__FunctionControlSet *
       mvb_debug__function_control_set__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__function_control_set__free_unpacked
                     (MvbDebug__FunctionControlSet *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__FunctionControlGetResponse methods */
void   mvb_debug__function_control_get_response__init
                     (MvbDebug__FunctionControlGetResponse         *message);
size_t mvb_debug__function_control_get_response__get_packed_size
                     (const MvbDebug__FunctionControlGetResponse   *message);
size_t mvb_debug__function_control_get_response__pack
                     (const MvbDebug__FunctionControlGetResponse   *message,
                      uint8_t             *out);
size_t mvb_debug__function_control_get_response__pack_to_buffer
                     (const MvbDebug__FunctionControlGetResponse   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__FunctionControlGetResponse *
       mvb_debug__function_control_get_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__function_control_get_response__free_unpacked
                     (MvbDebug__FunctionControlGetResponse *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__FunctionControlSetResponse methods */
void   mvb_debug__function_control_set_response__init
                     (MvbDebug__FunctionControlSetResponse         *message);
size_t mvb_debug__function_control_set_response__get_packed_size
                     (const MvbDebug__FunctionControlSetResponse   *message);
size_t mvb_debug__function_control_set_response__pack
                     (const MvbDebug__FunctionControlSetResponse   *message,
                      uint8_t             *out);
size_t mvb_debug__function_control_set_response__pack_to_buffer
                     (const MvbDebug__FunctionControlSetResponse   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__FunctionControlSetResponse *
       mvb_debug__function_control_set_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__function_control_set_response__free_unpacked
                     (MvbDebug__FunctionControlSetResponse *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__StreamControlStart methods */
void   mvb_debug__stream_control_start__init
                     (MvbDebug__StreamControlStart         *message);
size_t mvb_debug__stream_control_start__get_packed_size
                     (const MvbDebug__StreamControlStart   *message);
size_t mvb_debug__stream_control_start__pack
                     (const MvbDebug__StreamControlStart   *message,
                      uint8_t             *out);
size_t mvb_debug__stream_control_start__pack_to_buffer
                     (const MvbDebug__StreamControlStart   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__StreamControlStart *
       mvb_debug__stream_control_start__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__stream_control_start__free_unpacked
                     (MvbDebug__StreamControlStart *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__Sample methods */
void   mvb_debug__sample__init
                     (MvbDebug__Sample         *message);
size_t mvb_debug__sample__get_packed_size
                     (const MvbDebug__Sample   *message);
size_t mvb_debug__sample__pack
                     (const MvbDebug__Sample   *message,
                      uint8_t             *out);
size_t mvb_debug__sample__pack_to_buffer
                     (const MvbDebug__Sample   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__Sample *
       mvb_debug__sample__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__sample__free_unpacked
                     (MvbDebug__Sample *message,
                      ProtobufCAllocator *allocator);
/* MvbDebug__StreamData methods */
void   mvb_debug__stream_data__init
                     (MvbDebug__StreamData         *message);
size_t mvb_debug__stream_data__get_packed_size
                     (const MvbDebug__StreamData   *message);
size_t mvb_debug__stream_data__pack
                     (const MvbDebug__StreamData   *message,
                      uint8_t             *out);
size_t mvb_debug__stream_data__pack_to_buffer
                     (const MvbDebug__StreamData   *message,
                      ProtobufCBuffer     *buffer);
MvbDebug__StreamData *
       mvb_debug__stream_data__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_debug__stream_data__free_unpacked
                     (MvbDebug__StreamData *message,
                      ProtobufCAllocator *allocator);
/* --- per-message closures --- */

typedef void (*MvbDebug__ConfigurationSet_Closure)
                 (const MvbDebug__ConfigurationSet *message,
                  void *closure_data);
typedef void (*MvbDebug__ConfigurationSetResponse_Closure)
                 (const MvbDebug__ConfigurationSetResponse *message,
                  void *closure_data);
typedef void (*MvbDebug__ConfigurationGet_Closure)
                 (const MvbDebug__ConfigurationGet *message,
                  void *closure_data);
typedef void (*MvbDebug__ConfigurationGetResponse_Closure)
                 (const MvbDebug__ConfigurationGetResponse *message,
                  void *closure_data);
typedef void (*MvbDebug__ConfigurationDescribe_Closure)
                 (const MvbDebug__ConfigurationDescribe *message,
                  void *closure_data);
typedef void (*MvbDebug__ConfigurationDescribeResponse_Closure)
                 (const MvbDebug__ConfigurationDescribeResponse *message,
                  void *closure_data);
typedef void (*MvbDebug__FunctionControlGet_Closure)
                 (const MvbDebug__FunctionControlGet *message,
                  void *closure_data);
typedef void (*MvbDebug__FunctionControlSet_Closure)
                 (const MvbDebug__FunctionControlSet *message,
                  void *closure_data);
typedef void (*MvbDebug__FunctionControlGetResponse_Closure)
                 (const MvbDebug__FunctionControlGetResponse *message,
                  void *closure_data);
typedef void (*MvbDebug__FunctionControlSetResponse_Closure)
                 (const MvbDebug__FunctionControlSetResponse *message,
                  void *closure_data);
typedef void (*MvbDebug__StreamControlStart_Closure)
                 (const MvbDebug__StreamControlStart *message,
                  void *closure_data);
typedef void (*MvbDebug__Sample_Closure)
                 (const MvbDebug__Sample *message,
                  void *closure_data);
typedef void (*MvbDebug__StreamData_Closure)
                 (const MvbDebug__StreamData *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCMessageDescriptor mvb_debug__configuration_set__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__configuration_set_response__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__configuration_get__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__configuration_get_response__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__configuration_describe__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__configuration_describe_response__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__function_control_get__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__function_control_set__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__function_control_get_response__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__function_control_set_response__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__stream_control_start__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__sample__descriptor;
extern const ProtobufCMessageDescriptor mvb_debug__stream_data__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_mvbDebug_2eproto__INCLUDED */
