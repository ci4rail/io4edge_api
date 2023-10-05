/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: tracelet.proto */

#ifndef PROTOBUF_C_tracelet_2eproto__INCLUDED
#define PROTOBUF_C_tracelet_2eproto__INCLUDED

#include <protobuf-c/protobuf-c.h>

PROTOBUF_C__BEGIN_DECLS

#if PROTOBUF_C_VERSION_NUMBER < 1003000
# error This file was generated by a newer version of protoc-c which is incompatible with your libprotobuf-c headers. Please update your headers.
#elif 1003003 < PROTOBUF_C_MIN_COMPILER_VERSION
# error This file was generated by an older version of protoc-c which is incompatible with your libprotobuf-c headers. Please regenerate this file with a newer version of protoc-c.
#endif

#include "google/protobuf/timestamp.pb-c.h"

typedef struct _Tracelet__ServerToTracelet Tracelet__ServerToTracelet;
typedef struct _Tracelet__ServerToTracelet__LocationRequest Tracelet__ServerToTracelet__LocationRequest;
typedef struct _Tracelet__ServerToTracelet__StatusRequest Tracelet__ServerToTracelet__StatusRequest;
typedef struct _Tracelet__TraceletToServer Tracelet__TraceletToServer;
typedef struct _Tracelet__TraceletToServer__Location Tracelet__TraceletToServer__Location;
typedef struct _Tracelet__TraceletToServer__Location__Gnss Tracelet__TraceletToServer__Location__Gnss;
typedef struct _Tracelet__TraceletToServer__Location__Uwb Tracelet__TraceletToServer__Location__Uwb;
typedef struct _Tracelet__TraceletToServer__StatusResponse Tracelet__TraceletToServer__StatusResponse;


/* --- enums --- */

typedef enum _Tracelet__TraceletToServer__Location__Direction {
  /*
   * Invalid direction
   */
  TRACELET__TRACELET_TO_SERVER__LOCATION__DIRECTION__NO_DIRECTION = 0,
  /*
   * CAB A
   */
  TRACELET__TRACELET_TO_SERVER__LOCATION__DIRECTION__CAB_A_DIRECTION = 1,
  /*
   * CAB B
   */
  TRACELET__TRACELET_TO_SERVER__LOCATION__DIRECTION__CAB_B_DIRECTION = 2
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(TRACELET__TRACELET_TO_SERVER__LOCATION__DIRECTION)
} Tracelet__TraceletToServer__Location__Direction;

/* --- messages --- */

struct  _Tracelet__ServerToTracelet__LocationRequest
{
  ProtobufCMessage base;
};
#define TRACELET__SERVER_TO_TRACELET__LOCATION_REQUEST__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__server_to_tracelet__location_request__descriptor) \
     }


struct  _Tracelet__ServerToTracelet__StatusRequest
{
  ProtobufCMessage base;
};
#define TRACELET__SERVER_TO_TRACELET__STATUS_REQUEST__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__server_to_tracelet__status_request__descriptor) \
     }


typedef enum {
  TRACELET__SERVER_TO_TRACELET__TYPE__NOT_SET = 0,
  TRACELET__SERVER_TO_TRACELET__TYPE_LOCATION = 2,
  TRACELET__SERVER_TO_TRACELET__TYPE_STATUS = 3
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(TRACELET__SERVER_TO_TRACELET__TYPE)
} Tracelet__ServerToTracelet__TypeCase;

struct  _Tracelet__ServerToTracelet
{
  ProtobufCMessage base;
  /*
   * id of the request, will be echoed in StatusResponse
   */
  int32_t id;
  Tracelet__ServerToTracelet__TypeCase type_case;
  union {
    /*
     * request the location of the tracelet
     */
    Tracelet__ServerToTracelet__LocationRequest *location;
    /*
     * request the status of the tracelet
     */
    Tracelet__ServerToTracelet__StatusRequest *status;
  };
};
#define TRACELET__SERVER_TO_TRACELET__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__server_to_tracelet__descriptor) \
    , 0, TRACELET__SERVER_TO_TRACELET__TYPE__NOT_SET, {0} }


struct  _Tracelet__TraceletToServer__Location__Gnss
{
  ProtobufCMessage base;
  /*
   * GNSS location valid. If false, the other fields are not valid
   */
  protobuf_c_boolean valid;
  /*
   * WGS84 coordinates
   * latitude in [deg]
   */
  double latitude;
  /*
   * longitude in [deg]
   */
  double longitude;
  /*
   * altitude in [m]
   */
  double altitude;
  /*
   * horizontal accuracy in [m]
   */
  double eph;
  /*
   * vertical accuracy in [m]
   */
  double epv;
  /*
   * type of fix 
   * 0 = invalid, 1 = GPS fix, 2 = DGPS fix, 3 = PPS fix, 4 = Real Time Kinematic, 
   * 5 = Float RTK, 6 = estimated, 7 = Manual input mode, 8 = Simulation mode
   */
  int32_t fix_type;
};
#define TRACELET__TRACELET_TO_SERVER__LOCATION__GNSS__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__tracelet_to_server__location__gnss__descriptor) \
    , 0, 0, 0, 0, 0, 0, 0 }


struct  _Tracelet__TraceletToServer__Location__Uwb
{
  ProtobufCMessage base;
  /*
   * UWB location valid. If false, the other fields are not valid
   */
  protobuf_c_boolean valid;
  /*
   * location of tracelet in space
   * Units: [m], can be negative. Resolution 0.1m
   */
  double x;
  double y;
  double z;
  /*
   * Site ID
   * a 16 bit unsigned value
   */
  uint32_t site_id;
  /*
   * Location signature
   * can be used to validate the received location
   */
  uint64_t location_signature;
  /*
   * horizontal accuracy in [m]
   */
  double eph;
};
#define TRACELET__TRACELET_TO_SERVER__LOCATION__UWB__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__tracelet_to_server__location__uwb__descriptor) \
    , 0, 0, 0, 0, 0, 0, 0 }


/*
 * Sub-message sent in response to a location request OR
 * periodically sent by the tracelet
 */
struct  _Tracelet__TraceletToServer__Location
{
  ProtobufCMessage base;
  /*
   * Data from GNSS subsystem
   */
  Tracelet__TraceletToServer__Location__Gnss *gnss;
  /*
   * Data from UWB subsystem
   */
  Tracelet__TraceletToServer__Location__Uwb *uwb;
  /*
   * Driving direction of the vehicle
   */
  Tracelet__TraceletToServer__Location__Direction direction;
  /*
   * Vehicle Speed in [m/s]
   */
  double speed;
  /*
   * Vehicle Mileage in [km]
   */
  int32_t mileage;
  /*
   * Current Tracelet Temperature in [°C]
   */
  double temperature;
};
#define TRACELET__TRACELET_TO_SERVER__LOCATION__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__tracelet_to_server__location__descriptor) \
    , NULL, NULL, TRACELET__TRACELET_TO_SERVER__LOCATION__DIRECTION__NO_DIRECTION, 0, 0, 0 }


/*
 * Sub-message sent in response to a status request
 */
struct  _Tracelet__TraceletToServer__StatusResponse
{
  ProtobufCMessage base;
  /*
   * number of tracelet power Ups
   */
  int32_t power_up_count;
  /*
   * Tracelet has a valid time
   */
  protobuf_c_boolean has_time;
  /*
   * Status of the UWB module (0=OK, error code otherwise)
   */
  int32_t uwb_module_status;
  /*
   * Status of the GNSS module (0=OK, error code otherwise)
   */
  int32_t gnss_module_status;
  /*
   * Status of Main processor IMU (0=OK, error code otherwise)
   */
  int32_t imu1_status;
  /*
   * Status of tachometer signal (0=OK, error code otherwise)
   */
  int32_t tacho_status;
};
#define TRACELET__TRACELET_TO_SERVER__STATUS_RESPONSE__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__tracelet_to_server__status_response__descriptor) \
    , 0, 0, 0, 0, 0, 0 }


typedef enum {
  TRACELET__TRACELET_TO_SERVER__TYPE__NOT_SET = 0,
  TRACELET__TRACELET_TO_SERVER__TYPE_LOCATION = 5,
  TRACELET__TRACELET_TO_SERVER__TYPE_STATUS = 6
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(TRACELET__TRACELET_TO_SERVER__TYPE)
} Tracelet__TraceletToServer__TypeCase;

struct  _Tracelet__TraceletToServer
{
  ProtobufCMessage base;
  /*
   * Tracelet will echo the ID of the request here.
   * For messages sent without a request, the ID is 0
   */
  int32_t id;
  /*
   * timestamp when the message was sent by the tracelet
   * If the Tracelet has no valid time, receive_ts is set to 1970-Jan-1 00:00
   * UTC
   */
  Google__Protobuf__Timestamp *delivery_ts;
  /*
   * tracelet ID as provisioned in tracelet. Could be a vehicle ID
   */
  char *tracelet_id;
  /*
   * status of the tracelet ignition signal
   */
  protobuf_c_boolean ignition;
  Tracelet__TraceletToServer__TypeCase type_case;
  union {
    /*
     * periodically sent by the tracelet or in
     */
    Tracelet__TraceletToServer__Location *location;
    /*
     * response to a location request
     */
    /*
     * sent in response to the status request
     */
    Tracelet__TraceletToServer__StatusResponse *status;
  };
};
#define TRACELET__TRACELET_TO_SERVER__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__tracelet_to_server__descriptor) \
    , 0, NULL, (char *)protobuf_c_empty_string, 0, TRACELET__TRACELET_TO_SERVER__TYPE__NOT_SET, {0} }


/* Tracelet__ServerToTracelet__LocationRequest methods */
void   tracelet__server_to_tracelet__location_request__init
                     (Tracelet__ServerToTracelet__LocationRequest         *message);
/* Tracelet__ServerToTracelet__StatusRequest methods */
void   tracelet__server_to_tracelet__status_request__init
                     (Tracelet__ServerToTracelet__StatusRequest         *message);
/* Tracelet__ServerToTracelet methods */
void   tracelet__server_to_tracelet__init
                     (Tracelet__ServerToTracelet         *message);
size_t tracelet__server_to_tracelet__get_packed_size
                     (const Tracelet__ServerToTracelet   *message);
size_t tracelet__server_to_tracelet__pack
                     (const Tracelet__ServerToTracelet   *message,
                      uint8_t             *out);
size_t tracelet__server_to_tracelet__pack_to_buffer
                     (const Tracelet__ServerToTracelet   *message,
                      ProtobufCBuffer     *buffer);
Tracelet__ServerToTracelet *
       tracelet__server_to_tracelet__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   tracelet__server_to_tracelet__free_unpacked
                     (Tracelet__ServerToTracelet *message,
                      ProtobufCAllocator *allocator);
/* Tracelet__TraceletToServer__Location__Gnss methods */
void   tracelet__tracelet_to_server__location__gnss__init
                     (Tracelet__TraceletToServer__Location__Gnss         *message);
/* Tracelet__TraceletToServer__Location__Uwb methods */
void   tracelet__tracelet_to_server__location__uwb__init
                     (Tracelet__TraceletToServer__Location__Uwb         *message);
/* Tracelet__TraceletToServer__Location methods */
void   tracelet__tracelet_to_server__location__init
                     (Tracelet__TraceletToServer__Location         *message);
/* Tracelet__TraceletToServer__StatusResponse methods */
void   tracelet__tracelet_to_server__status_response__init
                     (Tracelet__TraceletToServer__StatusResponse         *message);
/* Tracelet__TraceletToServer methods */
void   tracelet__tracelet_to_server__init
                     (Tracelet__TraceletToServer         *message);
size_t tracelet__tracelet_to_server__get_packed_size
                     (const Tracelet__TraceletToServer   *message);
size_t tracelet__tracelet_to_server__pack
                     (const Tracelet__TraceletToServer   *message,
                      uint8_t             *out);
size_t tracelet__tracelet_to_server__pack_to_buffer
                     (const Tracelet__TraceletToServer   *message,
                      ProtobufCBuffer     *buffer);
Tracelet__TraceletToServer *
       tracelet__tracelet_to_server__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   tracelet__tracelet_to_server__free_unpacked
                     (Tracelet__TraceletToServer *message,
                      ProtobufCAllocator *allocator);
/* --- per-message closures --- */

typedef void (*Tracelet__ServerToTracelet__LocationRequest_Closure)
                 (const Tracelet__ServerToTracelet__LocationRequest *message,
                  void *closure_data);
typedef void (*Tracelet__ServerToTracelet__StatusRequest_Closure)
                 (const Tracelet__ServerToTracelet__StatusRequest *message,
                  void *closure_data);
typedef void (*Tracelet__ServerToTracelet_Closure)
                 (const Tracelet__ServerToTracelet *message,
                  void *closure_data);
typedef void (*Tracelet__TraceletToServer__Location__Gnss_Closure)
                 (const Tracelet__TraceletToServer__Location__Gnss *message,
                  void *closure_data);
typedef void (*Tracelet__TraceletToServer__Location__Uwb_Closure)
                 (const Tracelet__TraceletToServer__Location__Uwb *message,
                  void *closure_data);
typedef void (*Tracelet__TraceletToServer__Location_Closure)
                 (const Tracelet__TraceletToServer__Location *message,
                  void *closure_data);
typedef void (*Tracelet__TraceletToServer__StatusResponse_Closure)
                 (const Tracelet__TraceletToServer__StatusResponse *message,
                  void *closure_data);
typedef void (*Tracelet__TraceletToServer_Closure)
                 (const Tracelet__TraceletToServer *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCMessageDescriptor tracelet__server_to_tracelet__descriptor;
extern const ProtobufCMessageDescriptor tracelet__server_to_tracelet__location_request__descriptor;
extern const ProtobufCMessageDescriptor tracelet__server_to_tracelet__status_request__descriptor;
extern const ProtobufCMessageDescriptor tracelet__tracelet_to_server__descriptor;
extern const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__descriptor;
extern const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__gnss__descriptor;
extern const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__uwb__descriptor;
extern const ProtobufCEnumDescriptor    tracelet__tracelet_to_server__location__direction__descriptor;
extern const ProtobufCMessageDescriptor tracelet__tracelet_to_server__status_response__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_tracelet_2eproto__INCLUDED */
