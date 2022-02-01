/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: templateModule.proto */

#ifndef PROTOBUF_C_templateModule_2eproto__INCLUDED
#define PROTOBUF_C_templateModule_2eproto__INCLUDED

#include <protobuf-c/protobuf-c.h>

PROTOBUF_C__BEGIN_DECLS

#if PROTOBUF_C_VERSION_NUMBER < 1003000
# error This file was generated by a newer version of protoc-c which is incompatible with your libprotobuf-c headers. Please update your headers.
#elif 1003003 < PROTOBUF_C_MIN_COMPILER_VERSION
# error This file was generated by an older version of protoc-c which is incompatible with your libprotobuf-c headers. Please regenerate this file with a newer version of protoc-c.
#endif


typedef struct _TemplateModule__ConfigurationSet TemplateModule__ConfigurationSet;
typedef struct _TemplateModule__ConfigurationSetResponse TemplateModule__ConfigurationSetResponse;
typedef struct _TemplateModule__ConfigurationGet TemplateModule__ConfigurationGet;
typedef struct _TemplateModule__ConfigurationGetResponse TemplateModule__ConfigurationGetResponse;
typedef struct _TemplateModule__ConfigurationDescribe TemplateModule__ConfigurationDescribe;
typedef struct _TemplateModule__ConfigurationDescribeResponse TemplateModule__ConfigurationDescribeResponse;
typedef struct _TemplateModule__ConfigurationResponse TemplateModule__ConfigurationResponse;
typedef struct _TemplateModule__FunctionControlGet TemplateModule__FunctionControlGet;
typedef struct _TemplateModule__FunctionControlSet TemplateModule__FunctionControlSet;
typedef struct _TemplateModule__FunctionControlGetResponse TemplateModule__FunctionControlGetResponse;
typedef struct _TemplateModule__FunctionControlSetResponse TemplateModule__FunctionControlSetResponse;
typedef struct _TemplateModule__StreamControlStart TemplateModule__StreamControlStart;
typedef struct _TemplateModule__Sample TemplateModule__Sample;
typedef struct _TemplateModule__StreamData TemplateModule__StreamData;


/* --- enums --- */


/* --- messages --- */

/*
 * ConfigurationSet to pass to Functionblock.Configuration.functionSpecificConfigurationSet hook
 */
struct  _TemplateModule__ConfigurationSet
{
  ProtobufCMessage base;
};
#define TEMPLATE_MODULE__CONFIGURATION_SET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__configuration_set__descriptor) \
     }


/*
 * ConfigurationSetResponse to pass to Functionblock.Configuration.functionSpecificConfigurationSetResponse hook
 */
struct  _TemplateModule__ConfigurationSetResponse
{
  ProtobufCMessage base;
};
#define TEMPLATE_MODULE__CONFIGURATION_SET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__configuration_set_response__descriptor) \
     }


/*
 * ConfigurationGet to pass to Functionblock.Configuration.functionSpecificConfigurationGet hook
 */
struct  _TemplateModule__ConfigurationGet
{
  ProtobufCMessage base;
};
#define TEMPLATE_MODULE__CONFIGURATION_GET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__configuration_get__descriptor) \
     }


/*
 * ConfigurationGetResponse to pass to Functionblock.ConfigurationGetResponse.functionSpecificConfigurationGetResponse hook
 * Returns the current hardware configuration
 */
struct  _TemplateModule__ConfigurationGetResponse
{
  ProtobufCMessage base;
};
#define TEMPLATE_MODULE__CONFIGURATION_GET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__configuration_get_response__descriptor) \
     }


/*
 * ConfigurationDescribe to pass to Functionblock.Configuration.functionSpecificConfigurationDescribe hook
 */
struct  _TemplateModule__ConfigurationDescribe
{
  ProtobufCMessage base;
};
#define TEMPLATE_MODULE__CONFIGURATION_DESCRIBE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__configuration_describe__descriptor) \
     }


struct  _TemplateModule__ConfigurationDescribeResponse
{
  ProtobufCMessage base;
};
#define TEMPLATE_MODULE__CONFIGURATION_DESCRIBE_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__configuration_describe_response__descriptor) \
     }


typedef enum {
  TEMPLATE_MODULE__CONFIGURATION_RESPONSE__TYPE__NOT_SET = 0,
  TEMPLATE_MODULE__CONFIGURATION_RESPONSE__TYPE_GET = 1,
  TEMPLATE_MODULE__CONFIGURATION_RESPONSE__TYPE_SET = 2,
  TEMPLATE_MODULE__CONFIGURATION_RESPONSE__TYPE_DESCRIBE = 3
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(TEMPLATE_MODULE__CONFIGURATION_RESPONSE__TYPE)
} TemplateModule__ConfigurationResponse__TypeCase;

/*
 * ConfigurationResponse to pass to Functionblock.ConfigurationResponse.functionSpecificConfigurationResponse hook
 */
struct  _TemplateModule__ConfigurationResponse
{
  ProtobufCMessage base;
  TemplateModule__ConfigurationResponse__TypeCase type_case;
  union {
    TemplateModule__ConfigurationGetResponse *get;
    TemplateModule__ConfigurationSetResponse *set;
    TemplateModule__ConfigurationDescribeResponse *describe;
  };
};
#define TEMPLATE_MODULE__CONFIGURATION_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__configuration_response__descriptor) \
    , TEMPLATE_MODULE__CONFIGURATION_RESPONSE__TYPE__NOT_SET, {0} }


/*
 * FunctionControlGet to pass to Functionblock.FunctionControl.functionSpecificFunctionControlGet hook
 */
struct  _TemplateModule__FunctionControlGet
{
  ProtobufCMessage base;
};
#define TEMPLATE_MODULE__FUNCTION_CONTROL_GET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__function_control_get__descriptor) \
     }


/*
 * FunctionControlSet to pass to Functionblock.FunctionControl.functionSpecificFunctionControlSet hook
 */
struct  _TemplateModule__FunctionControlSet
{
  ProtobufCMessage base;
  /*
   * Put here your function specific values
   * Example:
   */
  uint32_t value;
};
#define TEMPLATE_MODULE__FUNCTION_CONTROL_SET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__function_control_set__descriptor) \
    , 0 }


/*
 * FunctionControlGetResponse to pass to Functionblock.FunctionControlResponse.functionSpecificControlGet hook
 */
struct  _TemplateModule__FunctionControlGetResponse
{
  ProtobufCMessage base;
  /*
   * Put here your function specific values
   */
  uint32_t value;
};
#define TEMPLATE_MODULE__FUNCTION_CONTROL_GET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__function_control_get_response__descriptor) \
    , 0 }


/*
 * FunctionControlSetResponse to pass to Functionblock.FunctionControlResponse.functionSpecificControlSet hook
 */
struct  _TemplateModule__FunctionControlSetResponse
{
  ProtobufCMessage base;
};
#define TEMPLATE_MODULE__FUNCTION_CONTROL_SET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__function_control_set_response__descriptor) \
     }


/*
 * ============= StreamControl ==================
 * StreamControlStart to pass to Functionblock.StreamControlStart.functionSpecificStreamControlStart hook
 */
struct  _TemplateModule__StreamControlStart
{
  ProtobufCMessage base;
};
#define TEMPLATE_MODULE__STREAM_CONTROL_START__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__stream_control_start__descriptor) \
     }


struct  _TemplateModule__Sample
{
  ProtobufCMessage base;
  /*
   * Timestamp for that specific channels sample. This is the time the sample was taken.
   * This timestamp is in microseconds since the start of the device and does not get synchronized with the clients time.
   */
  uint64_t timestamp;
  /*
   * Specifies the binary channel value when the input value has changed.
   */
  uint32_t value;
};
#define TEMPLATE_MODULE__SAMPLE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__sample__descriptor) \
    , 0, 0 }


/*
 * StreamData to pass to Functionblock.StreamData.functionSpecificStreamData hook
 */
struct  _TemplateModule__StreamData
{
  ProtobufCMessage base;
  size_t n_samples;
  TemplateModule__Sample **samples;
};
#define TEMPLATE_MODULE__STREAM_DATA__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&template_module__stream_data__descriptor) \
    , 0,NULL }


/* TemplateModule__ConfigurationSet methods */
void   template_module__configuration_set__init
                     (TemplateModule__ConfigurationSet         *message);
size_t template_module__configuration_set__get_packed_size
                     (const TemplateModule__ConfigurationSet   *message);
size_t template_module__configuration_set__pack
                     (const TemplateModule__ConfigurationSet   *message,
                      uint8_t             *out);
size_t template_module__configuration_set__pack_to_buffer
                     (const TemplateModule__ConfigurationSet   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__ConfigurationSet *
       template_module__configuration_set__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__configuration_set__free_unpacked
                     (TemplateModule__ConfigurationSet *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__ConfigurationSetResponse methods */
void   template_module__configuration_set_response__init
                     (TemplateModule__ConfigurationSetResponse         *message);
size_t template_module__configuration_set_response__get_packed_size
                     (const TemplateModule__ConfigurationSetResponse   *message);
size_t template_module__configuration_set_response__pack
                     (const TemplateModule__ConfigurationSetResponse   *message,
                      uint8_t             *out);
size_t template_module__configuration_set_response__pack_to_buffer
                     (const TemplateModule__ConfigurationSetResponse   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__ConfigurationSetResponse *
       template_module__configuration_set_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__configuration_set_response__free_unpacked
                     (TemplateModule__ConfigurationSetResponse *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__ConfigurationGet methods */
void   template_module__configuration_get__init
                     (TemplateModule__ConfigurationGet         *message);
size_t template_module__configuration_get__get_packed_size
                     (const TemplateModule__ConfigurationGet   *message);
size_t template_module__configuration_get__pack
                     (const TemplateModule__ConfigurationGet   *message,
                      uint8_t             *out);
size_t template_module__configuration_get__pack_to_buffer
                     (const TemplateModule__ConfigurationGet   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__ConfigurationGet *
       template_module__configuration_get__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__configuration_get__free_unpacked
                     (TemplateModule__ConfigurationGet *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__ConfigurationGetResponse methods */
void   template_module__configuration_get_response__init
                     (TemplateModule__ConfigurationGetResponse         *message);
size_t template_module__configuration_get_response__get_packed_size
                     (const TemplateModule__ConfigurationGetResponse   *message);
size_t template_module__configuration_get_response__pack
                     (const TemplateModule__ConfigurationGetResponse   *message,
                      uint8_t             *out);
size_t template_module__configuration_get_response__pack_to_buffer
                     (const TemplateModule__ConfigurationGetResponse   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__ConfigurationGetResponse *
       template_module__configuration_get_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__configuration_get_response__free_unpacked
                     (TemplateModule__ConfigurationGetResponse *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__ConfigurationDescribe methods */
void   template_module__configuration_describe__init
                     (TemplateModule__ConfigurationDescribe         *message);
size_t template_module__configuration_describe__get_packed_size
                     (const TemplateModule__ConfigurationDescribe   *message);
size_t template_module__configuration_describe__pack
                     (const TemplateModule__ConfigurationDescribe   *message,
                      uint8_t             *out);
size_t template_module__configuration_describe__pack_to_buffer
                     (const TemplateModule__ConfigurationDescribe   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__ConfigurationDescribe *
       template_module__configuration_describe__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__configuration_describe__free_unpacked
                     (TemplateModule__ConfigurationDescribe *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__ConfigurationDescribeResponse methods */
void   template_module__configuration_describe_response__init
                     (TemplateModule__ConfigurationDescribeResponse         *message);
size_t template_module__configuration_describe_response__get_packed_size
                     (const TemplateModule__ConfigurationDescribeResponse   *message);
size_t template_module__configuration_describe_response__pack
                     (const TemplateModule__ConfigurationDescribeResponse   *message,
                      uint8_t             *out);
size_t template_module__configuration_describe_response__pack_to_buffer
                     (const TemplateModule__ConfigurationDescribeResponse   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__ConfigurationDescribeResponse *
       template_module__configuration_describe_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__configuration_describe_response__free_unpacked
                     (TemplateModule__ConfigurationDescribeResponse *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__ConfigurationResponse methods */
void   template_module__configuration_response__init
                     (TemplateModule__ConfigurationResponse         *message);
size_t template_module__configuration_response__get_packed_size
                     (const TemplateModule__ConfigurationResponse   *message);
size_t template_module__configuration_response__pack
                     (const TemplateModule__ConfigurationResponse   *message,
                      uint8_t             *out);
size_t template_module__configuration_response__pack_to_buffer
                     (const TemplateModule__ConfigurationResponse   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__ConfigurationResponse *
       template_module__configuration_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__configuration_response__free_unpacked
                     (TemplateModule__ConfigurationResponse *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__FunctionControlGet methods */
void   template_module__function_control_get__init
                     (TemplateModule__FunctionControlGet         *message);
size_t template_module__function_control_get__get_packed_size
                     (const TemplateModule__FunctionControlGet   *message);
size_t template_module__function_control_get__pack
                     (const TemplateModule__FunctionControlGet   *message,
                      uint8_t             *out);
size_t template_module__function_control_get__pack_to_buffer
                     (const TemplateModule__FunctionControlGet   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__FunctionControlGet *
       template_module__function_control_get__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__function_control_get__free_unpacked
                     (TemplateModule__FunctionControlGet *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__FunctionControlSet methods */
void   template_module__function_control_set__init
                     (TemplateModule__FunctionControlSet         *message);
size_t template_module__function_control_set__get_packed_size
                     (const TemplateModule__FunctionControlSet   *message);
size_t template_module__function_control_set__pack
                     (const TemplateModule__FunctionControlSet   *message,
                      uint8_t             *out);
size_t template_module__function_control_set__pack_to_buffer
                     (const TemplateModule__FunctionControlSet   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__FunctionControlSet *
       template_module__function_control_set__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__function_control_set__free_unpacked
                     (TemplateModule__FunctionControlSet *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__FunctionControlGetResponse methods */
void   template_module__function_control_get_response__init
                     (TemplateModule__FunctionControlGetResponse         *message);
size_t template_module__function_control_get_response__get_packed_size
                     (const TemplateModule__FunctionControlGetResponse   *message);
size_t template_module__function_control_get_response__pack
                     (const TemplateModule__FunctionControlGetResponse   *message,
                      uint8_t             *out);
size_t template_module__function_control_get_response__pack_to_buffer
                     (const TemplateModule__FunctionControlGetResponse   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__FunctionControlGetResponse *
       template_module__function_control_get_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__function_control_get_response__free_unpacked
                     (TemplateModule__FunctionControlGetResponse *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__FunctionControlSetResponse methods */
void   template_module__function_control_set_response__init
                     (TemplateModule__FunctionControlSetResponse         *message);
size_t template_module__function_control_set_response__get_packed_size
                     (const TemplateModule__FunctionControlSetResponse   *message);
size_t template_module__function_control_set_response__pack
                     (const TemplateModule__FunctionControlSetResponse   *message,
                      uint8_t             *out);
size_t template_module__function_control_set_response__pack_to_buffer
                     (const TemplateModule__FunctionControlSetResponse   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__FunctionControlSetResponse *
       template_module__function_control_set_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__function_control_set_response__free_unpacked
                     (TemplateModule__FunctionControlSetResponse *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__StreamControlStart methods */
void   template_module__stream_control_start__init
                     (TemplateModule__StreamControlStart         *message);
size_t template_module__stream_control_start__get_packed_size
                     (const TemplateModule__StreamControlStart   *message);
size_t template_module__stream_control_start__pack
                     (const TemplateModule__StreamControlStart   *message,
                      uint8_t             *out);
size_t template_module__stream_control_start__pack_to_buffer
                     (const TemplateModule__StreamControlStart   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__StreamControlStart *
       template_module__stream_control_start__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__stream_control_start__free_unpacked
                     (TemplateModule__StreamControlStart *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__Sample methods */
void   template_module__sample__init
                     (TemplateModule__Sample         *message);
size_t template_module__sample__get_packed_size
                     (const TemplateModule__Sample   *message);
size_t template_module__sample__pack
                     (const TemplateModule__Sample   *message,
                      uint8_t             *out);
size_t template_module__sample__pack_to_buffer
                     (const TemplateModule__Sample   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__Sample *
       template_module__sample__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__sample__free_unpacked
                     (TemplateModule__Sample *message,
                      ProtobufCAllocator *allocator);
/* TemplateModule__StreamData methods */
void   template_module__stream_data__init
                     (TemplateModule__StreamData         *message);
size_t template_module__stream_data__get_packed_size
                     (const TemplateModule__StreamData   *message);
size_t template_module__stream_data__pack
                     (const TemplateModule__StreamData   *message,
                      uint8_t             *out);
size_t template_module__stream_data__pack_to_buffer
                     (const TemplateModule__StreamData   *message,
                      ProtobufCBuffer     *buffer);
TemplateModule__StreamData *
       template_module__stream_data__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   template_module__stream_data__free_unpacked
                     (TemplateModule__StreamData *message,
                      ProtobufCAllocator *allocator);
/* --- per-message closures --- */

typedef void (*TemplateModule__ConfigurationSet_Closure)
                 (const TemplateModule__ConfigurationSet *message,
                  void *closure_data);
typedef void (*TemplateModule__ConfigurationSetResponse_Closure)
                 (const TemplateModule__ConfigurationSetResponse *message,
                  void *closure_data);
typedef void (*TemplateModule__ConfigurationGet_Closure)
                 (const TemplateModule__ConfigurationGet *message,
                  void *closure_data);
typedef void (*TemplateModule__ConfigurationGetResponse_Closure)
                 (const TemplateModule__ConfigurationGetResponse *message,
                  void *closure_data);
typedef void (*TemplateModule__ConfigurationDescribe_Closure)
                 (const TemplateModule__ConfigurationDescribe *message,
                  void *closure_data);
typedef void (*TemplateModule__ConfigurationDescribeResponse_Closure)
                 (const TemplateModule__ConfigurationDescribeResponse *message,
                  void *closure_data);
typedef void (*TemplateModule__ConfigurationResponse_Closure)
                 (const TemplateModule__ConfigurationResponse *message,
                  void *closure_data);
typedef void (*TemplateModule__FunctionControlGet_Closure)
                 (const TemplateModule__FunctionControlGet *message,
                  void *closure_data);
typedef void (*TemplateModule__FunctionControlSet_Closure)
                 (const TemplateModule__FunctionControlSet *message,
                  void *closure_data);
typedef void (*TemplateModule__FunctionControlGetResponse_Closure)
                 (const TemplateModule__FunctionControlGetResponse *message,
                  void *closure_data);
typedef void (*TemplateModule__FunctionControlSetResponse_Closure)
                 (const TemplateModule__FunctionControlSetResponse *message,
                  void *closure_data);
typedef void (*TemplateModule__StreamControlStart_Closure)
                 (const TemplateModule__StreamControlStart *message,
                  void *closure_data);
typedef void (*TemplateModule__Sample_Closure)
                 (const TemplateModule__Sample *message,
                  void *closure_data);
typedef void (*TemplateModule__StreamData_Closure)
                 (const TemplateModule__StreamData *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCMessageDescriptor template_module__configuration_set__descriptor;
extern const ProtobufCMessageDescriptor template_module__configuration_set_response__descriptor;
extern const ProtobufCMessageDescriptor template_module__configuration_get__descriptor;
extern const ProtobufCMessageDescriptor template_module__configuration_get_response__descriptor;
extern const ProtobufCMessageDescriptor template_module__configuration_describe__descriptor;
extern const ProtobufCMessageDescriptor template_module__configuration_describe_response__descriptor;
extern const ProtobufCMessageDescriptor template_module__configuration_response__descriptor;
extern const ProtobufCMessageDescriptor template_module__function_control_get__descriptor;
extern const ProtobufCMessageDescriptor template_module__function_control_set__descriptor;
extern const ProtobufCMessageDescriptor template_module__function_control_get_response__descriptor;
extern const ProtobufCMessageDescriptor template_module__function_control_set_response__descriptor;
extern const ProtobufCMessageDescriptor template_module__stream_control_start__descriptor;
extern const ProtobufCMessageDescriptor template_module__sample__descriptor;
extern const ProtobufCMessageDescriptor template_module__stream_data__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_templateModule_2eproto__INCLUDED */
