/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: pixelDisplay.proto */

#ifndef PROTOBUF_C_pixelDisplay_2eproto__INCLUDED
#define PROTOBUF_C_pixelDisplay_2eproto__INCLUDED

#include <protobuf-c/protobuf-c.h>

PROTOBUF_C__BEGIN_DECLS

#if PROTOBUF_C_VERSION_NUMBER < 1003000
# error This file was generated by a newer version of protoc-c which is incompatible with your libprotobuf-c headers. Please update your headers.
#elif 1003003 < PROTOBUF_C_MIN_COMPILER_VERSION
# error This file was generated by an older version of protoc-c which is incompatible with your libprotobuf-c headers. Please regenerate this file with a newer version of protoc-c.
#endif


typedef struct _PixelDisplay__ConfigurationSet PixelDisplay__ConfigurationSet;
typedef struct _PixelDisplay__ConfigurationSetResponse PixelDisplay__ConfigurationSetResponse;
typedef struct _PixelDisplay__ConfigurationGet PixelDisplay__ConfigurationGet;
typedef struct _PixelDisplay__ConfigurationGetResponse PixelDisplay__ConfigurationGetResponse;
typedef struct _PixelDisplay__ConfigurationDescribe PixelDisplay__ConfigurationDescribe;
typedef struct _PixelDisplay__ConfigurationDescribeResponse PixelDisplay__ConfigurationDescribeResponse;
typedef struct _PixelDisplay__ConfigurationResponse PixelDisplay__ConfigurationResponse;
typedef struct _PixelDisplay__FunctionControlGet PixelDisplay__FunctionControlGet;
typedef struct _PixelDisplay__SetPixelArea PixelDisplay__SetPixelArea;
typedef struct _PixelDisplay__SetDisplayOn PixelDisplay__SetDisplayOn;
typedef struct _PixelDisplay__FunctionControlSet PixelDisplay__FunctionControlSet;
typedef struct _PixelDisplay__FunctionControlGetResponse PixelDisplay__FunctionControlGetResponse;
typedef struct _PixelDisplay__SetPixelAreaResponse PixelDisplay__SetPixelAreaResponse;
typedef struct _PixelDisplay__SetDisplayOnResponse PixelDisplay__SetDisplayOnResponse;
typedef struct _PixelDisplay__FunctionControlSetResponse PixelDisplay__FunctionControlSetResponse;
typedef struct _PixelDisplay__StreamControlStart PixelDisplay__StreamControlStart;
typedef struct _PixelDisplay__StreamData PixelDisplay__StreamData;


/* --- enums --- */


/* --- messages --- */

/*
 * ConfigurationSet to pass to Functionblock.Configuration.functionSpecificConfigurationSet hook
 */
struct  _PixelDisplay__ConfigurationSet
{
  ProtobufCMessage base;
};
#define PIXEL_DISPLAY__CONFIGURATION_SET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__configuration_set__descriptor) \
     }


/*
 * ConfigurationSetResponse to pass to Functionblock.Configuration.functionSpecificConfigurationSetResponse hook
 */
struct  _PixelDisplay__ConfigurationSetResponse
{
  ProtobufCMessage base;
};
#define PIXEL_DISPLAY__CONFIGURATION_SET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__configuration_set_response__descriptor) \
     }


/*
 * ConfigurationGet to pass to Functionblock.Configuration.functionSpecificConfigurationGet hook
 */
struct  _PixelDisplay__ConfigurationGet
{
  ProtobufCMessage base;
};
#define PIXEL_DISPLAY__CONFIGURATION_GET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__configuration_get__descriptor) \
     }


/*
 * ConfigurationGetResponse to pass to Functionblock.ConfigurationGetResponse.functionSpecificConfigurationGetResponse hook
 * Returns the current hardware configuration
 */
struct  _PixelDisplay__ConfigurationGetResponse
{
  ProtobufCMessage base;
};
#define PIXEL_DISPLAY__CONFIGURATION_GET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__configuration_get_response__descriptor) \
     }


/*
 * ConfigurationDescribe to pass to Functionblock.Configuration.functionSpecificConfigurationDescribe hook
 */
struct  _PixelDisplay__ConfigurationDescribe
{
  ProtobufCMessage base;
};
#define PIXEL_DISPLAY__CONFIGURATION_DESCRIBE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__configuration_describe__descriptor) \
     }


struct  _PixelDisplay__ConfigurationDescribeResponse
{
  ProtobufCMessage base;
  uint32_t height_pixel;
  uint32_t width_pixel;
  /*
   * maximum number of pixels to set transmit at once
   */
  uint32_t max_num_of_pixel;
};
#define PIXEL_DISPLAY__CONFIGURATION_DESCRIBE_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__configuration_describe_response__descriptor) \
    , 0, 0, 0 }


typedef enum {
  PIXEL_DISPLAY__CONFIGURATION_RESPONSE__TYPE__NOT_SET = 0,
  PIXEL_DISPLAY__CONFIGURATION_RESPONSE__TYPE_GET = 1,
  PIXEL_DISPLAY__CONFIGURATION_RESPONSE__TYPE_SET = 2,
  PIXEL_DISPLAY__CONFIGURATION_RESPONSE__TYPE_DESCRIBE = 3
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(PIXEL_DISPLAY__CONFIGURATION_RESPONSE__TYPE)
} PixelDisplay__ConfigurationResponse__TypeCase;

/*
 * ConfigurationResponse to pass to Functionblock.ConfigurationResponse.functionSpecificConfigurationResponse hook
 */
struct  _PixelDisplay__ConfigurationResponse
{
  ProtobufCMessage base;
  PixelDisplay__ConfigurationResponse__TypeCase type_case;
  union {
    PixelDisplay__ConfigurationGetResponse *get;
    PixelDisplay__ConfigurationSetResponse *set;
    PixelDisplay__ConfigurationDescribeResponse *describe;
  };
};
#define PIXEL_DISPLAY__CONFIGURATION_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__configuration_response__descriptor) \
    , PIXEL_DISPLAY__CONFIGURATION_RESPONSE__TYPE__NOT_SET, {0} }


/*
 * FunctionControlGet to pass to Functionblock.FunctionControl.functionSpecificFunctionControlGet hook
 */
struct  _PixelDisplay__FunctionControlGet
{
  ProtobufCMessage base;
};
#define PIXEL_DISPLAY__FUNCTION_CONTROL_GET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__function_control_get__descriptor) \
     }


/*
 * Upload a pixel image to display on a specific screen area
 * Start and end coordinates are inclusive
 */
struct  _PixelDisplay__SetPixelArea
{
  ProtobufCMessage base;
  uint32_t start_x;
  uint32_t start_y;
  uint32_t end_x;
  ProtobufCBinaryData image;
};
#define PIXEL_DISPLAY__SET_PIXEL_AREA__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__set_pixel_area__descriptor) \
    , 0, 0, 0, {0,NULL} }


struct  _PixelDisplay__SetDisplayOn
{
  ProtobufCMessage base;
  protobuf_c_boolean on;
};
#define PIXEL_DISPLAY__SET_DISPLAY_ON__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__set_display_on__descriptor) \
    , 0 }


typedef enum {
  PIXEL_DISPLAY__FUNCTION_CONTROL_SET__TYPE__NOT_SET = 0,
  PIXEL_DISPLAY__FUNCTION_CONTROL_SET__TYPE_SET_PIXEL_AREA = 1,
  PIXEL_DISPLAY__FUNCTION_CONTROL_SET__TYPE_DISPLAY_ON = 2
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(PIXEL_DISPLAY__FUNCTION_CONTROL_SET__TYPE)
} PixelDisplay__FunctionControlSet__TypeCase;

/*
 * FunctionControlSet to pass to Functionblock.FunctionControl.functionSpecificFunctionControlSet hook
 */
struct  _PixelDisplay__FunctionControlSet
{
  ProtobufCMessage base;
  PixelDisplay__FunctionControlSet__TypeCase type_case;
  union {
    PixelDisplay__SetPixelArea *set_pixel_area;
    PixelDisplay__SetDisplayOn *display_on;
  };
};
#define PIXEL_DISPLAY__FUNCTION_CONTROL_SET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__function_control_set__descriptor) \
    , PIXEL_DISPLAY__FUNCTION_CONTROL_SET__TYPE__NOT_SET, {0} }


/*
 * FunctionControlGetResponse to pass to Functionblock.FunctionControlResponse.functionSpecificControlGet hook
 */
struct  _PixelDisplay__FunctionControlGetResponse
{
  ProtobufCMessage base;
};
#define PIXEL_DISPLAY__FUNCTION_CONTROL_GET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__function_control_get_response__descriptor) \
     }


struct  _PixelDisplay__SetPixelAreaResponse
{
  ProtobufCMessage base;
};
#define PIXEL_DISPLAY__SET_PIXEL_AREA_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__set_pixel_area_response__descriptor) \
     }


struct  _PixelDisplay__SetDisplayOnResponse
{
  ProtobufCMessage base;
};
#define PIXEL_DISPLAY__SET_DISPLAY_ON_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__set_display_on_response__descriptor) \
     }


typedef enum {
  PIXEL_DISPLAY__FUNCTION_CONTROL_SET_RESPONSE__TYPE__NOT_SET = 0,
  PIXEL_DISPLAY__FUNCTION_CONTROL_SET_RESPONSE__TYPE_SET_PIXEL_AREA = 1,
  PIXEL_DISPLAY__FUNCTION_CONTROL_SET_RESPONSE__TYPE_DISPLAY_ON = 2
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(PIXEL_DISPLAY__FUNCTION_CONTROL_SET_RESPONSE__TYPE)
} PixelDisplay__FunctionControlSetResponse__TypeCase;

/*
 * FunctionControlSetResponse to pass to Functionblock.FunctionControlResponse.functionSpecificControlSet hook
 */
struct  _PixelDisplay__FunctionControlSetResponse
{
  ProtobufCMessage base;
  PixelDisplay__FunctionControlSetResponse__TypeCase type_case;
  union {
    PixelDisplay__SetPixelAreaResponse *set_pixel_area;
    PixelDisplay__SetDisplayOnResponse *display_on;
  };
};
#define PIXEL_DISPLAY__FUNCTION_CONTROL_SET_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__function_control_set_response__descriptor) \
    , PIXEL_DISPLAY__FUNCTION_CONTROL_SET_RESPONSE__TYPE__NOT_SET, {0} }


/*
 * ============= StreamControl ==================
 * StreamControlStart to pass to Functionblock.StreamControlStart.functionSpecificStreamControlStart hook
 */
struct  _PixelDisplay__StreamControlStart
{
  ProtobufCMessage base;
};
#define PIXEL_DISPLAY__STREAM_CONTROL_START__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__stream_control_start__descriptor) \
     }


/*
 * StreamData to pass to Functionblock.StreamData.functionSpecificStreamData hook
 */
struct  _PixelDisplay__StreamData
{
  ProtobufCMessage base;
};
#define PIXEL_DISPLAY__STREAM_DATA__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&pixel_display__stream_data__descriptor) \
     }


/* PixelDisplay__ConfigurationSet methods */
void   pixel_display__configuration_set__init
                     (PixelDisplay__ConfigurationSet         *message);
size_t pixel_display__configuration_set__get_packed_size
                     (const PixelDisplay__ConfigurationSet   *message);
size_t pixel_display__configuration_set__pack
                     (const PixelDisplay__ConfigurationSet   *message,
                      uint8_t             *out);
size_t pixel_display__configuration_set__pack_to_buffer
                     (const PixelDisplay__ConfigurationSet   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__ConfigurationSet *
       pixel_display__configuration_set__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__configuration_set__free_unpacked
                     (PixelDisplay__ConfigurationSet *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__ConfigurationSetResponse methods */
void   pixel_display__configuration_set_response__init
                     (PixelDisplay__ConfigurationSetResponse         *message);
size_t pixel_display__configuration_set_response__get_packed_size
                     (const PixelDisplay__ConfigurationSetResponse   *message);
size_t pixel_display__configuration_set_response__pack
                     (const PixelDisplay__ConfigurationSetResponse   *message,
                      uint8_t             *out);
size_t pixel_display__configuration_set_response__pack_to_buffer
                     (const PixelDisplay__ConfigurationSetResponse   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__ConfigurationSetResponse *
       pixel_display__configuration_set_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__configuration_set_response__free_unpacked
                     (PixelDisplay__ConfigurationSetResponse *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__ConfigurationGet methods */
void   pixel_display__configuration_get__init
                     (PixelDisplay__ConfigurationGet         *message);
size_t pixel_display__configuration_get__get_packed_size
                     (const PixelDisplay__ConfigurationGet   *message);
size_t pixel_display__configuration_get__pack
                     (const PixelDisplay__ConfigurationGet   *message,
                      uint8_t             *out);
size_t pixel_display__configuration_get__pack_to_buffer
                     (const PixelDisplay__ConfigurationGet   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__ConfigurationGet *
       pixel_display__configuration_get__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__configuration_get__free_unpacked
                     (PixelDisplay__ConfigurationGet *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__ConfigurationGetResponse methods */
void   pixel_display__configuration_get_response__init
                     (PixelDisplay__ConfigurationGetResponse         *message);
size_t pixel_display__configuration_get_response__get_packed_size
                     (const PixelDisplay__ConfigurationGetResponse   *message);
size_t pixel_display__configuration_get_response__pack
                     (const PixelDisplay__ConfigurationGetResponse   *message,
                      uint8_t             *out);
size_t pixel_display__configuration_get_response__pack_to_buffer
                     (const PixelDisplay__ConfigurationGetResponse   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__ConfigurationGetResponse *
       pixel_display__configuration_get_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__configuration_get_response__free_unpacked
                     (PixelDisplay__ConfigurationGetResponse *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__ConfigurationDescribe methods */
void   pixel_display__configuration_describe__init
                     (PixelDisplay__ConfigurationDescribe         *message);
size_t pixel_display__configuration_describe__get_packed_size
                     (const PixelDisplay__ConfigurationDescribe   *message);
size_t pixel_display__configuration_describe__pack
                     (const PixelDisplay__ConfigurationDescribe   *message,
                      uint8_t             *out);
size_t pixel_display__configuration_describe__pack_to_buffer
                     (const PixelDisplay__ConfigurationDescribe   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__ConfigurationDescribe *
       pixel_display__configuration_describe__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__configuration_describe__free_unpacked
                     (PixelDisplay__ConfigurationDescribe *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__ConfigurationDescribeResponse methods */
void   pixel_display__configuration_describe_response__init
                     (PixelDisplay__ConfigurationDescribeResponse         *message);
size_t pixel_display__configuration_describe_response__get_packed_size
                     (const PixelDisplay__ConfigurationDescribeResponse   *message);
size_t pixel_display__configuration_describe_response__pack
                     (const PixelDisplay__ConfigurationDescribeResponse   *message,
                      uint8_t             *out);
size_t pixel_display__configuration_describe_response__pack_to_buffer
                     (const PixelDisplay__ConfigurationDescribeResponse   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__ConfigurationDescribeResponse *
       pixel_display__configuration_describe_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__configuration_describe_response__free_unpacked
                     (PixelDisplay__ConfigurationDescribeResponse *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__ConfigurationResponse methods */
void   pixel_display__configuration_response__init
                     (PixelDisplay__ConfigurationResponse         *message);
size_t pixel_display__configuration_response__get_packed_size
                     (const PixelDisplay__ConfigurationResponse   *message);
size_t pixel_display__configuration_response__pack
                     (const PixelDisplay__ConfigurationResponse   *message,
                      uint8_t             *out);
size_t pixel_display__configuration_response__pack_to_buffer
                     (const PixelDisplay__ConfigurationResponse   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__ConfigurationResponse *
       pixel_display__configuration_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__configuration_response__free_unpacked
                     (PixelDisplay__ConfigurationResponse *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__FunctionControlGet methods */
void   pixel_display__function_control_get__init
                     (PixelDisplay__FunctionControlGet         *message);
size_t pixel_display__function_control_get__get_packed_size
                     (const PixelDisplay__FunctionControlGet   *message);
size_t pixel_display__function_control_get__pack
                     (const PixelDisplay__FunctionControlGet   *message,
                      uint8_t             *out);
size_t pixel_display__function_control_get__pack_to_buffer
                     (const PixelDisplay__FunctionControlGet   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__FunctionControlGet *
       pixel_display__function_control_get__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__function_control_get__free_unpacked
                     (PixelDisplay__FunctionControlGet *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__SetPixelArea methods */
void   pixel_display__set_pixel_area__init
                     (PixelDisplay__SetPixelArea         *message);
size_t pixel_display__set_pixel_area__get_packed_size
                     (const PixelDisplay__SetPixelArea   *message);
size_t pixel_display__set_pixel_area__pack
                     (const PixelDisplay__SetPixelArea   *message,
                      uint8_t             *out);
size_t pixel_display__set_pixel_area__pack_to_buffer
                     (const PixelDisplay__SetPixelArea   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__SetPixelArea *
       pixel_display__set_pixel_area__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__set_pixel_area__free_unpacked
                     (PixelDisplay__SetPixelArea *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__SetDisplayOn methods */
void   pixel_display__set_display_on__init
                     (PixelDisplay__SetDisplayOn         *message);
size_t pixel_display__set_display_on__get_packed_size
                     (const PixelDisplay__SetDisplayOn   *message);
size_t pixel_display__set_display_on__pack
                     (const PixelDisplay__SetDisplayOn   *message,
                      uint8_t             *out);
size_t pixel_display__set_display_on__pack_to_buffer
                     (const PixelDisplay__SetDisplayOn   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__SetDisplayOn *
       pixel_display__set_display_on__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__set_display_on__free_unpacked
                     (PixelDisplay__SetDisplayOn *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__FunctionControlSet methods */
void   pixel_display__function_control_set__init
                     (PixelDisplay__FunctionControlSet         *message);
size_t pixel_display__function_control_set__get_packed_size
                     (const PixelDisplay__FunctionControlSet   *message);
size_t pixel_display__function_control_set__pack
                     (const PixelDisplay__FunctionControlSet   *message,
                      uint8_t             *out);
size_t pixel_display__function_control_set__pack_to_buffer
                     (const PixelDisplay__FunctionControlSet   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__FunctionControlSet *
       pixel_display__function_control_set__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__function_control_set__free_unpacked
                     (PixelDisplay__FunctionControlSet *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__FunctionControlGetResponse methods */
void   pixel_display__function_control_get_response__init
                     (PixelDisplay__FunctionControlGetResponse         *message);
size_t pixel_display__function_control_get_response__get_packed_size
                     (const PixelDisplay__FunctionControlGetResponse   *message);
size_t pixel_display__function_control_get_response__pack
                     (const PixelDisplay__FunctionControlGetResponse   *message,
                      uint8_t             *out);
size_t pixel_display__function_control_get_response__pack_to_buffer
                     (const PixelDisplay__FunctionControlGetResponse   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__FunctionControlGetResponse *
       pixel_display__function_control_get_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__function_control_get_response__free_unpacked
                     (PixelDisplay__FunctionControlGetResponse *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__SetPixelAreaResponse methods */
void   pixel_display__set_pixel_area_response__init
                     (PixelDisplay__SetPixelAreaResponse         *message);
size_t pixel_display__set_pixel_area_response__get_packed_size
                     (const PixelDisplay__SetPixelAreaResponse   *message);
size_t pixel_display__set_pixel_area_response__pack
                     (const PixelDisplay__SetPixelAreaResponse   *message,
                      uint8_t             *out);
size_t pixel_display__set_pixel_area_response__pack_to_buffer
                     (const PixelDisplay__SetPixelAreaResponse   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__SetPixelAreaResponse *
       pixel_display__set_pixel_area_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__set_pixel_area_response__free_unpacked
                     (PixelDisplay__SetPixelAreaResponse *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__SetDisplayOnResponse methods */
void   pixel_display__set_display_on_response__init
                     (PixelDisplay__SetDisplayOnResponse         *message);
size_t pixel_display__set_display_on_response__get_packed_size
                     (const PixelDisplay__SetDisplayOnResponse   *message);
size_t pixel_display__set_display_on_response__pack
                     (const PixelDisplay__SetDisplayOnResponse   *message,
                      uint8_t             *out);
size_t pixel_display__set_display_on_response__pack_to_buffer
                     (const PixelDisplay__SetDisplayOnResponse   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__SetDisplayOnResponse *
       pixel_display__set_display_on_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__set_display_on_response__free_unpacked
                     (PixelDisplay__SetDisplayOnResponse *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__FunctionControlSetResponse methods */
void   pixel_display__function_control_set_response__init
                     (PixelDisplay__FunctionControlSetResponse         *message);
size_t pixel_display__function_control_set_response__get_packed_size
                     (const PixelDisplay__FunctionControlSetResponse   *message);
size_t pixel_display__function_control_set_response__pack
                     (const PixelDisplay__FunctionControlSetResponse   *message,
                      uint8_t             *out);
size_t pixel_display__function_control_set_response__pack_to_buffer
                     (const PixelDisplay__FunctionControlSetResponse   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__FunctionControlSetResponse *
       pixel_display__function_control_set_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__function_control_set_response__free_unpacked
                     (PixelDisplay__FunctionControlSetResponse *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__StreamControlStart methods */
void   pixel_display__stream_control_start__init
                     (PixelDisplay__StreamControlStart         *message);
size_t pixel_display__stream_control_start__get_packed_size
                     (const PixelDisplay__StreamControlStart   *message);
size_t pixel_display__stream_control_start__pack
                     (const PixelDisplay__StreamControlStart   *message,
                      uint8_t             *out);
size_t pixel_display__stream_control_start__pack_to_buffer
                     (const PixelDisplay__StreamControlStart   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__StreamControlStart *
       pixel_display__stream_control_start__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__stream_control_start__free_unpacked
                     (PixelDisplay__StreamControlStart *message,
                      ProtobufCAllocator *allocator);
/* PixelDisplay__StreamData methods */
void   pixel_display__stream_data__init
                     (PixelDisplay__StreamData         *message);
size_t pixel_display__stream_data__get_packed_size
                     (const PixelDisplay__StreamData   *message);
size_t pixel_display__stream_data__pack
                     (const PixelDisplay__StreamData   *message,
                      uint8_t             *out);
size_t pixel_display__stream_data__pack_to_buffer
                     (const PixelDisplay__StreamData   *message,
                      ProtobufCBuffer     *buffer);
PixelDisplay__StreamData *
       pixel_display__stream_data__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   pixel_display__stream_data__free_unpacked
                     (PixelDisplay__StreamData *message,
                      ProtobufCAllocator *allocator);
/* --- per-message closures --- */

typedef void (*PixelDisplay__ConfigurationSet_Closure)
                 (const PixelDisplay__ConfigurationSet *message,
                  void *closure_data);
typedef void (*PixelDisplay__ConfigurationSetResponse_Closure)
                 (const PixelDisplay__ConfigurationSetResponse *message,
                  void *closure_data);
typedef void (*PixelDisplay__ConfigurationGet_Closure)
                 (const PixelDisplay__ConfigurationGet *message,
                  void *closure_data);
typedef void (*PixelDisplay__ConfigurationGetResponse_Closure)
                 (const PixelDisplay__ConfigurationGetResponse *message,
                  void *closure_data);
typedef void (*PixelDisplay__ConfigurationDescribe_Closure)
                 (const PixelDisplay__ConfigurationDescribe *message,
                  void *closure_data);
typedef void (*PixelDisplay__ConfigurationDescribeResponse_Closure)
                 (const PixelDisplay__ConfigurationDescribeResponse *message,
                  void *closure_data);
typedef void (*PixelDisplay__ConfigurationResponse_Closure)
                 (const PixelDisplay__ConfigurationResponse *message,
                  void *closure_data);
typedef void (*PixelDisplay__FunctionControlGet_Closure)
                 (const PixelDisplay__FunctionControlGet *message,
                  void *closure_data);
typedef void (*PixelDisplay__SetPixelArea_Closure)
                 (const PixelDisplay__SetPixelArea *message,
                  void *closure_data);
typedef void (*PixelDisplay__SetDisplayOn_Closure)
                 (const PixelDisplay__SetDisplayOn *message,
                  void *closure_data);
typedef void (*PixelDisplay__FunctionControlSet_Closure)
                 (const PixelDisplay__FunctionControlSet *message,
                  void *closure_data);
typedef void (*PixelDisplay__FunctionControlGetResponse_Closure)
                 (const PixelDisplay__FunctionControlGetResponse *message,
                  void *closure_data);
typedef void (*PixelDisplay__SetPixelAreaResponse_Closure)
                 (const PixelDisplay__SetPixelAreaResponse *message,
                  void *closure_data);
typedef void (*PixelDisplay__SetDisplayOnResponse_Closure)
                 (const PixelDisplay__SetDisplayOnResponse *message,
                  void *closure_data);
typedef void (*PixelDisplay__FunctionControlSetResponse_Closure)
                 (const PixelDisplay__FunctionControlSetResponse *message,
                  void *closure_data);
typedef void (*PixelDisplay__StreamControlStart_Closure)
                 (const PixelDisplay__StreamControlStart *message,
                  void *closure_data);
typedef void (*PixelDisplay__StreamData_Closure)
                 (const PixelDisplay__StreamData *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCMessageDescriptor pixel_display__configuration_set__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__configuration_set_response__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__configuration_get__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__configuration_get_response__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__configuration_describe__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__configuration_describe_response__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__configuration_response__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__function_control_get__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__set_pixel_area__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__set_display_on__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__function_control_set__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__function_control_get_response__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__set_pixel_area_response__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__set_display_on_response__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__function_control_set_response__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__stream_control_start__descriptor;
extern const ProtobufCMessageDescriptor pixel_display__stream_data__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_pixelDisplay_2eproto__INCLUDED */
