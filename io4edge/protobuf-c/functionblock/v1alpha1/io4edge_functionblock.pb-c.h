/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: io4edge_functionblock.proto */

#ifndef PROTOBUF_C_io4edge_5ffunctionblock_2eproto__INCLUDED
#define PROTOBUF_C_io4edge_5ffunctionblock_2eproto__INCLUDED

#include <protobuf-c/protobuf-c.h>

PROTOBUF_C__BEGIN_DECLS

#if PROTOBUF_C_VERSION_NUMBER < 1003000
# error This file was generated by a newer version of protoc-c which is incompatible with your libprotobuf-c headers. Please update your headers.
#elif 1003003 < PROTOBUF_C_MIN_COMPILER_VERSION
# error This file was generated by an older version of protoc-c which is incompatible with your libprotobuf-c headers. Please regenerate this file with a newer version of protoc-c.
#endif

#include "google/protobuf/any.pb-c.h"

typedef struct _Functionblock__Context Functionblock__Context;
typedef struct _Functionblock__Command Functionblock__Command;
typedef struct _Functionblock__Configuration Functionblock__Configuration;
typedef struct _Functionblock__FunctionControl Functionblock__FunctionControl;
typedef struct _Functionblock__StreamControlStart Functionblock__StreamControlStart;
typedef struct _Functionblock__StreamControlStop Functionblock__StreamControlStop;
typedef struct _Functionblock__StreamControl Functionblock__StreamControl;
typedef struct _Functionblock__Error Functionblock__Error;
typedef struct _Functionblock__ConfigurationResponse Functionblock__ConfigurationResponse;
typedef struct _Functionblock__FunctionControlResponse Functionblock__FunctionControlResponse;
typedef struct _Functionblock__StreamControlResponse Functionblock__StreamControlResponse;
typedef struct _Functionblock__StreamData Functionblock__StreamData;
typedef struct _Functionblock__Response Functionblock__Response;


/* --- enums --- */

/*
 * --------- Responses ------------
 */
typedef enum _Functionblock__Status {
  FUNCTIONBLOCK__STATUS__OK = 0,
  FUNCTIONBLOCK__STATUS__UNSPECIFIC_ERROR = 1,
  FUNCTIONBLOCK__STATUS__UNKNOWN_COMMAND = 2,
  FUNCTIONBLOCK__STATUS__NOT_IMPLEMENTED = 3,
  FUNCTIONBLOCK__STATUS__WRONG_CLIENT = 4,
  FUNCTIONBLOCK__STATUS__INVALID_PARAMETER = 5,
  FUNCTIONBLOCK__STATUS__HW_FAULT = 6
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(FUNCTIONBLOCK__STATUS)
} Functionblock__Status;

/* --- messages --- */

/*
 * -------- Meta ------------
 */
struct  _Functionblock__Context
{
  ProtobufCMessage base;
  /*
   * A message identifying key for a command-response pairs, e.g. an UUID the
   * clients sends on the request.
   */
  char *value;
};
#define FUNCTIONBLOCK__CONTEXT__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__context__descriptor) \
    , (char *)protobuf_c_empty_string }


typedef enum {
  FUNCTIONBLOCK__COMMAND__TYPE__NOT_SET = 0,
  FUNCTIONBLOCK__COMMAND__TYPE_CONFIGURATION = 2,
  FUNCTIONBLOCK__COMMAND__TYPE_FUNCTION_CONTROL = 3,
  FUNCTIONBLOCK__COMMAND__TYPE_STREAM_CONTROL = 4
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(FUNCTIONBLOCK__COMMAND__TYPE)
} Functionblock__Command__TypeCase;

/*
 * ------- Commands ---------
 */
struct  _Functionblock__Command
{
  ProtobufCMessage base;
  Functionblock__Context *context;
  Functionblock__Command__TypeCase type_case;
  union {
    Functionblock__Configuration *configuration;
    Functionblock__FunctionControl *functioncontrol;
    Functionblock__StreamControl *streamcontrol;
  };
};
#define FUNCTIONBLOCK__COMMAND__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__command__descriptor) \
    , NULL, FUNCTIONBLOCK__COMMAND__TYPE__NOT_SET, {0} }


typedef enum {
  FUNCTIONBLOCK__CONFIGURATION__ACTION__NOT_SET = 0,
  FUNCTIONBLOCK__CONFIGURATION__ACTION_FUNCTION_SPECIFIC_CONFIGURATION_SET = 10,
  FUNCTIONBLOCK__CONFIGURATION__ACTION_FUNCTION_SPECIFIC_CONFIGURATION_GET = 20,
  FUNCTIONBLOCK__CONFIGURATION__ACTION_FUNCTION_SPECIFIC_CONFIGURATION_DESCRIBE = 30
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(FUNCTIONBLOCK__CONFIGURATION__ACTION)
} Functionblock__Configuration__ActionCase;

/*
 * Configuration contains the function blocks high level configuration
 */
struct  _Functionblock__Configuration
{
  ProtobufCMessage base;
  Functionblock__Configuration__ActionCase action_case;
  union {
    /*
     * Setting a new configuration
     */
    Google__Protobuf__Any *functionspecificconfigurationset;
    /*
     * Getting the current configuration
     */
    Google__Protobuf__Any *functionspecificconfigurationget;
    /*
     * Describe hardware capabilities
     */
    Google__Protobuf__Any *functionspecificconfigurationdescribe;
  };
};
#define FUNCTIONBLOCK__CONFIGURATION__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__configuration__descriptor) \
    , FUNCTIONBLOCK__CONFIGURATION__ACTION__NOT_SET, {0} }


typedef enum {
  FUNCTIONBLOCK__FUNCTION_CONTROL__ACTION__NOT_SET = 0,
  FUNCTIONBLOCK__FUNCTION_CONTROL__ACTION_FUNCTION_SPECIFIC_FUNCTION_CONTROL_SET = 1,
  FUNCTIONBLOCK__FUNCTION_CONTROL__ACTION_FUNCTION_SPECIFIC_FUNCTION_CONTROL_GET = 2
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(FUNCTIONBLOCK__FUNCTION_CONTROL__ACTION)
} Functionblock__FunctionControl__ActionCase;

/*
 * FunctionControl specifies the direct function control for getting and setting values
 */
struct  _Functionblock__FunctionControl
{
  ProtobufCMessage base;
  Functionblock__FunctionControl__ActionCase action_case;
  union {
    Google__Protobuf__Any *functionspecificfunctioncontrolset;
    Google__Protobuf__Any *functionspecificfunctioncontrolget;
  };
};
#define FUNCTIONBLOCK__FUNCTION_CONTROL__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__function_control__descriptor) \
    , FUNCTIONBLOCK__FUNCTION_CONTROL__ACTION__NOT_SET, {0} }


/*
 * StreamControlStart specifies the start of a stream.
 */
struct  _Functionblock__StreamControlStart
{
  ProtobufCMessage base;
  Google__Protobuf__Any *functionspecificstreamcontrolstart;
};
#define FUNCTIONBLOCK__STREAM_CONTROL_START__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__stream_control_start__descriptor) \
    , NULL }


/*
 * StreamControlStart specifies the stop of a stream.
 */
struct  _Functionblock__StreamControlStop
{
  ProtobufCMessage base;
};
#define FUNCTIONBLOCK__STREAM_CONTROL_STOP__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__stream_control_stop__descriptor) \
     }


typedef enum {
  FUNCTIONBLOCK__STREAM_CONTROL__ACTION__NOT_SET = 0,
  FUNCTIONBLOCK__STREAM_CONTROL__ACTION_START = 1,
  FUNCTIONBLOCK__STREAM_CONTROL__ACTION_STOP = 2
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(FUNCTIONBLOCK__STREAM_CONTROL__ACTION)
} Functionblock__StreamControl__ActionCase;

/*
 * StreamControl specifies if the stream shall be started or stopped
 */
struct  _Functionblock__StreamControl
{
  ProtobufCMessage base;
  Functionblock__StreamControl__ActionCase action_case;
  union {
    Functionblock__StreamControlStart *start;
    Functionblock__StreamControlStop *stop;
  };
};
#define FUNCTIONBLOCK__STREAM_CONTROL__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__stream_control__descriptor) \
    , FUNCTIONBLOCK__STREAM_CONTROL__ACTION__NOT_SET, {0} }


struct  _Functionblock__Error
{
  ProtobufCMessage base;
  char *error;
};
#define FUNCTIONBLOCK__ERROR__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__error__descriptor) \
    , (char *)protobuf_c_empty_string }


typedef enum {
  FUNCTIONBLOCK__CONFIGURATION_RESPONSE__ACTION__NOT_SET = 0,
  FUNCTIONBLOCK__CONFIGURATION_RESPONSE__ACTION_FUNCTION_SPECIFIC_CONFIGURATION_SET = 10,
  FUNCTIONBLOCK__CONFIGURATION_RESPONSE__ACTION_FUNCTION_SPECIFIC_CONFIGURATION_GET = 20,
  FUNCTIONBLOCK__CONFIGURATION_RESPONSE__ACTION_FUNCTION_SPECIFIC_CONFIGURATION_DESCRIBE = 30
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(FUNCTIONBLOCK__CONFIGURATION_RESPONSE__ACTION)
} Functionblock__ConfigurationResponse__ActionCase;

struct  _Functionblock__ConfigurationResponse
{
  ProtobufCMessage base;
  Functionblock__ConfigurationResponse__ActionCase action_case;
  union {
    /*
     * Setting a new configuration
     */
    Google__Protobuf__Any *functionspecificconfigurationset;
    /*
     * Getting the current configuration
     */
    Google__Protobuf__Any *functionspecificconfigurationget;
    /*
     * Describe hardware capabilities
     */
    Google__Protobuf__Any *functionspecificconfigurationdescribe;
  };
};
#define FUNCTIONBLOCK__CONFIGURATION_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__configuration_response__descriptor) \
    , FUNCTIONBLOCK__CONFIGURATION_RESPONSE__ACTION__NOT_SET, {0} }


typedef enum {
  FUNCTIONBLOCK__FUNCTION_CONTROL_RESPONSE__ACTION__NOT_SET = 0,
  FUNCTIONBLOCK__FUNCTION_CONTROL_RESPONSE__ACTION_FUNCTION_SPECIFIC_FUNCTION_CONTROL_SET = 1,
  FUNCTIONBLOCK__FUNCTION_CONTROL_RESPONSE__ACTION_FUNCTION_SPECIFIC_FUNCTION_CONTROL_GET = 2
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(FUNCTIONBLOCK__FUNCTION_CONTROL_RESPONSE__ACTION)
} Functionblock__FunctionControlResponse__ActionCase;

struct  _Functionblock__FunctionControlResponse
{
  ProtobufCMessage base;
  Functionblock__FunctionControlResponse__ActionCase action_case;
  union {
    Google__Protobuf__Any *functionspecificfunctioncontrolset;
    Google__Protobuf__Any *functionspecificfunctioncontrolget;
  };
};
#define FUNCTIONBLOCK__FUNCTION_CONTROL_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__function_control_response__descriptor) \
    , FUNCTIONBLOCK__FUNCTION_CONTROL_RESPONSE__ACTION__NOT_SET, {0} }


struct  _Functionblock__StreamControlResponse
{
  ProtobufCMessage base;
};
#define FUNCTIONBLOCK__STREAM_CONTROL_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__stream_control_response__descriptor) \
     }


struct  _Functionblock__StreamData
{
  ProtobufCMessage base;
  /*
   * timestamp when the message has been sent out
   */
  uint64_t deliverytimestampus;
  /*
   * sample series sequence number (counted from 0, rolls over)
   */
  uint32_t sequence;
  /*
   * Function specific data type
   */
  Google__Protobuf__Any *functionspecificstreamdata;
};
#define FUNCTIONBLOCK__STREAM_DATA__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__stream_data__descriptor) \
    , 0, 0, NULL }


typedef enum {
  FUNCTIONBLOCK__RESPONSE__TYPE__NOT_SET = 0,
  FUNCTIONBLOCK__RESPONSE__TYPE_CONFIGURATION = 4,
  FUNCTIONBLOCK__RESPONSE__TYPE_FUNCTION_CONTROL = 5,
  FUNCTIONBLOCK__RESPONSE__TYPE_STREAM_CONTROL = 6,
  FUNCTIONBLOCK__RESPONSE__TYPE_STREAM = 7
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(FUNCTIONBLOCK__RESPONSE__TYPE)
} Functionblock__Response__TypeCase;

struct  _Functionblock__Response
{
  ProtobufCMessage base;
  Functionblock__Context *context;
  Functionblock__Status status;
  Functionblock__Error *error;
  Functionblock__Response__TypeCase type_case;
  union {
    Functionblock__ConfigurationResponse *configuration;
    Functionblock__FunctionControlResponse *functioncontrol;
    Functionblock__StreamControlResponse *streamcontrol;
    Functionblock__StreamData *stream;
  };
};
#define FUNCTIONBLOCK__RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&functionblock__response__descriptor) \
    , NULL, FUNCTIONBLOCK__STATUS__OK, NULL, FUNCTIONBLOCK__RESPONSE__TYPE__NOT_SET, {0} }


/* Functionblock__Context methods */
void   functionblock__context__init
                     (Functionblock__Context         *message);
size_t functionblock__context__get_packed_size
                     (const Functionblock__Context   *message);
size_t functionblock__context__pack
                     (const Functionblock__Context   *message,
                      uint8_t             *out);
size_t functionblock__context__pack_to_buffer
                     (const Functionblock__Context   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__Context *
       functionblock__context__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__context__free_unpacked
                     (Functionblock__Context *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__Command methods */
void   functionblock__command__init
                     (Functionblock__Command         *message);
size_t functionblock__command__get_packed_size
                     (const Functionblock__Command   *message);
size_t functionblock__command__pack
                     (const Functionblock__Command   *message,
                      uint8_t             *out);
size_t functionblock__command__pack_to_buffer
                     (const Functionblock__Command   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__Command *
       functionblock__command__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__command__free_unpacked
                     (Functionblock__Command *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__Configuration methods */
void   functionblock__configuration__init
                     (Functionblock__Configuration         *message);
size_t functionblock__configuration__get_packed_size
                     (const Functionblock__Configuration   *message);
size_t functionblock__configuration__pack
                     (const Functionblock__Configuration   *message,
                      uint8_t             *out);
size_t functionblock__configuration__pack_to_buffer
                     (const Functionblock__Configuration   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__Configuration *
       functionblock__configuration__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__configuration__free_unpacked
                     (Functionblock__Configuration *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__FunctionControl methods */
void   functionblock__function_control__init
                     (Functionblock__FunctionControl         *message);
size_t functionblock__function_control__get_packed_size
                     (const Functionblock__FunctionControl   *message);
size_t functionblock__function_control__pack
                     (const Functionblock__FunctionControl   *message,
                      uint8_t             *out);
size_t functionblock__function_control__pack_to_buffer
                     (const Functionblock__FunctionControl   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__FunctionControl *
       functionblock__function_control__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__function_control__free_unpacked
                     (Functionblock__FunctionControl *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__StreamControlStart methods */
void   functionblock__stream_control_start__init
                     (Functionblock__StreamControlStart         *message);
size_t functionblock__stream_control_start__get_packed_size
                     (const Functionblock__StreamControlStart   *message);
size_t functionblock__stream_control_start__pack
                     (const Functionblock__StreamControlStart   *message,
                      uint8_t             *out);
size_t functionblock__stream_control_start__pack_to_buffer
                     (const Functionblock__StreamControlStart   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__StreamControlStart *
       functionblock__stream_control_start__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__stream_control_start__free_unpacked
                     (Functionblock__StreamControlStart *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__StreamControlStop methods */
void   functionblock__stream_control_stop__init
                     (Functionblock__StreamControlStop         *message);
size_t functionblock__stream_control_stop__get_packed_size
                     (const Functionblock__StreamControlStop   *message);
size_t functionblock__stream_control_stop__pack
                     (const Functionblock__StreamControlStop   *message,
                      uint8_t             *out);
size_t functionblock__stream_control_stop__pack_to_buffer
                     (const Functionblock__StreamControlStop   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__StreamControlStop *
       functionblock__stream_control_stop__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__stream_control_stop__free_unpacked
                     (Functionblock__StreamControlStop *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__StreamControl methods */
void   functionblock__stream_control__init
                     (Functionblock__StreamControl         *message);
size_t functionblock__stream_control__get_packed_size
                     (const Functionblock__StreamControl   *message);
size_t functionblock__stream_control__pack
                     (const Functionblock__StreamControl   *message,
                      uint8_t             *out);
size_t functionblock__stream_control__pack_to_buffer
                     (const Functionblock__StreamControl   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__StreamControl *
       functionblock__stream_control__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__stream_control__free_unpacked
                     (Functionblock__StreamControl *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__Error methods */
void   functionblock__error__init
                     (Functionblock__Error         *message);
size_t functionblock__error__get_packed_size
                     (const Functionblock__Error   *message);
size_t functionblock__error__pack
                     (const Functionblock__Error   *message,
                      uint8_t             *out);
size_t functionblock__error__pack_to_buffer
                     (const Functionblock__Error   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__Error *
       functionblock__error__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__error__free_unpacked
                     (Functionblock__Error *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__ConfigurationResponse methods */
void   functionblock__configuration_response__init
                     (Functionblock__ConfigurationResponse         *message);
size_t functionblock__configuration_response__get_packed_size
                     (const Functionblock__ConfigurationResponse   *message);
size_t functionblock__configuration_response__pack
                     (const Functionblock__ConfigurationResponse   *message,
                      uint8_t             *out);
size_t functionblock__configuration_response__pack_to_buffer
                     (const Functionblock__ConfigurationResponse   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__ConfigurationResponse *
       functionblock__configuration_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__configuration_response__free_unpacked
                     (Functionblock__ConfigurationResponse *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__FunctionControlResponse methods */
void   functionblock__function_control_response__init
                     (Functionblock__FunctionControlResponse         *message);
size_t functionblock__function_control_response__get_packed_size
                     (const Functionblock__FunctionControlResponse   *message);
size_t functionblock__function_control_response__pack
                     (const Functionblock__FunctionControlResponse   *message,
                      uint8_t             *out);
size_t functionblock__function_control_response__pack_to_buffer
                     (const Functionblock__FunctionControlResponse   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__FunctionControlResponse *
       functionblock__function_control_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__function_control_response__free_unpacked
                     (Functionblock__FunctionControlResponse *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__StreamControlResponse methods */
void   functionblock__stream_control_response__init
                     (Functionblock__StreamControlResponse         *message);
size_t functionblock__stream_control_response__get_packed_size
                     (const Functionblock__StreamControlResponse   *message);
size_t functionblock__stream_control_response__pack
                     (const Functionblock__StreamControlResponse   *message,
                      uint8_t             *out);
size_t functionblock__stream_control_response__pack_to_buffer
                     (const Functionblock__StreamControlResponse   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__StreamControlResponse *
       functionblock__stream_control_response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__stream_control_response__free_unpacked
                     (Functionblock__StreamControlResponse *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__StreamData methods */
void   functionblock__stream_data__init
                     (Functionblock__StreamData         *message);
size_t functionblock__stream_data__get_packed_size
                     (const Functionblock__StreamData   *message);
size_t functionblock__stream_data__pack
                     (const Functionblock__StreamData   *message,
                      uint8_t             *out);
size_t functionblock__stream_data__pack_to_buffer
                     (const Functionblock__StreamData   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__StreamData *
       functionblock__stream_data__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__stream_data__free_unpacked
                     (Functionblock__StreamData *message,
                      ProtobufCAllocator *allocator);
/* Functionblock__Response methods */
void   functionblock__response__init
                     (Functionblock__Response         *message);
size_t functionblock__response__get_packed_size
                     (const Functionblock__Response   *message);
size_t functionblock__response__pack
                     (const Functionblock__Response   *message,
                      uint8_t             *out);
size_t functionblock__response__pack_to_buffer
                     (const Functionblock__Response   *message,
                      ProtobufCBuffer     *buffer);
Functionblock__Response *
       functionblock__response__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   functionblock__response__free_unpacked
                     (Functionblock__Response *message,
                      ProtobufCAllocator *allocator);
/* --- per-message closures --- */

typedef void (*Functionblock__Context_Closure)
                 (const Functionblock__Context *message,
                  void *closure_data);
typedef void (*Functionblock__Command_Closure)
                 (const Functionblock__Command *message,
                  void *closure_data);
typedef void (*Functionblock__Configuration_Closure)
                 (const Functionblock__Configuration *message,
                  void *closure_data);
typedef void (*Functionblock__FunctionControl_Closure)
                 (const Functionblock__FunctionControl *message,
                  void *closure_data);
typedef void (*Functionblock__StreamControlStart_Closure)
                 (const Functionblock__StreamControlStart *message,
                  void *closure_data);
typedef void (*Functionblock__StreamControlStop_Closure)
                 (const Functionblock__StreamControlStop *message,
                  void *closure_data);
typedef void (*Functionblock__StreamControl_Closure)
                 (const Functionblock__StreamControl *message,
                  void *closure_data);
typedef void (*Functionblock__Error_Closure)
                 (const Functionblock__Error *message,
                  void *closure_data);
typedef void (*Functionblock__ConfigurationResponse_Closure)
                 (const Functionblock__ConfigurationResponse *message,
                  void *closure_data);
typedef void (*Functionblock__FunctionControlResponse_Closure)
                 (const Functionblock__FunctionControlResponse *message,
                  void *closure_data);
typedef void (*Functionblock__StreamControlResponse_Closure)
                 (const Functionblock__StreamControlResponse *message,
                  void *closure_data);
typedef void (*Functionblock__StreamData_Closure)
                 (const Functionblock__StreamData *message,
                  void *closure_data);
typedef void (*Functionblock__Response_Closure)
                 (const Functionblock__Response *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCEnumDescriptor    functionblock__status__descriptor;
extern const ProtobufCMessageDescriptor functionblock__context__descriptor;
extern const ProtobufCMessageDescriptor functionblock__command__descriptor;
extern const ProtobufCMessageDescriptor functionblock__configuration__descriptor;
extern const ProtobufCMessageDescriptor functionblock__function_control__descriptor;
extern const ProtobufCMessageDescriptor functionblock__stream_control_start__descriptor;
extern const ProtobufCMessageDescriptor functionblock__stream_control_stop__descriptor;
extern const ProtobufCMessageDescriptor functionblock__stream_control__descriptor;
extern const ProtobufCMessageDescriptor functionblock__error__descriptor;
extern const ProtobufCMessageDescriptor functionblock__configuration_response__descriptor;
extern const ProtobufCMessageDescriptor functionblock__function_control_response__descriptor;
extern const ProtobufCMessageDescriptor functionblock__stream_control_response__descriptor;
extern const ProtobufCMessageDescriptor functionblock__stream_data__descriptor;
extern const ProtobufCMessageDescriptor functionblock__response__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_io4edge_5ffunctionblock_2eproto__INCLUDED */
