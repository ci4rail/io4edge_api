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

typedef struct _Tracelet__TraceletToServer Tracelet__TraceletToServer;
typedef struct _Tracelet__TraceletToServer__Location Tracelet__TraceletToServer__Location;
typedef struct _Tracelet__TraceletToServer__Location__Gnss Tracelet__TraceletToServer__Location__Gnss;
typedef struct _Tracelet__TraceletToServer__Location__Uwb Tracelet__TraceletToServer__Location__Uwb;
typedef struct _Tracelet__TraceletToServer__Location__Fused Tracelet__TraceletToServer__Location__Fused;
typedef struct _Tracelet__TraceletToServer__Location__Acceleration Tracelet__TraceletToServer__Location__Acceleration;


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
  /*
   * heading of motion in [deg]
   */
  double head_motion;
  /*
   * heading of vehicle in [deg]
   */
  double head_vehicle;
  /*
   * heading valid (bit 0=motion valid, 1=vehicle valid))
   */
  uint32_t head_valid;
  /*
   * speed in [m/s]
   */
  double ground_speed;
};
#define TRACELET__TRACELET_TO_SERVER__LOCATION__GNSS__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__tracelet_to_server__location__gnss__descriptor) \
    , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }


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
  /*
   * type of fix 
   * 0 = invalid, 1 = UWB/IMU, 2 - IMU only
   */
  int32_t fix_type;
  /*
   * heading of motion in [deg]
   */
  double head_motion;
  /*
   * heading of vehicle in [deg] - future extension
   */
  double head_vehicle;
  /*
   * heading valid (bit 0=motion valid, 1=vehicle valid))
   */
  uint32_t head_valid;
  /*
   * speed in [m/s]
   */
  double ground_speed;
};
#define TRACELET__TRACELET_TO_SERVER__LOCATION__UWB__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__tracelet_to_server__location__uwb__descriptor) \
    , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }


struct  _Tracelet__TraceletToServer__Location__Fused
{
  ProtobufCMessage base;
  /*
   * Fused location valid. If false, the other fields are not valid
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
   * altitude in [m] - future extension
   */
  double altitude;
  /*
   * horizontal accuracy in [m]
   */
  double eph;
  /*
   * heading of motion in [deg] - future extension
   */
  double head_motion;
  /*
   * heading of vehicle in [deg] - future extension
   */
  double head_vehicle;
  /*
   * heading valid (bit 0=motion valid, 1=vehicle valid)) - future extension
   */
  uint32_t head_valid;
  /*
   * speed in [m/s] - future extension
   */
  double ground_speed;
};
#define TRACELET__TRACELET_TO_SERVER__LOCATION__FUSED__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__tracelet_to_server__location__fused__descriptor) \
    , 0, 0, 0, 0, 0, 0, 0, 0, 0 }


/*
 * Acceleration data - all values in (m/s^2)
 */
struct  _Tracelet__TraceletToServer__Location__Acceleration
{
  ProtobufCMessage base;
  /*
   * Maximum acceleration in x direction in last period 
   */
  double x_max;
  double y_max;
  double z_max;
  /*
   * Minimum acceleration in x direction in last period
   */
  double x_min;
  double y_min;
  double z_min;
  /*
   * Average acceleration in x direction in last period
   */
  double x_avg;
  double y_avg;
  double z_avg;
};
#define TRACELET__TRACELET_TO_SERVER__LOCATION__ACCELERATION__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__tracelet_to_server__location__acceleration__descriptor) \
    , 0, 0, 0, 0, 0, 0, 0, 0, 0 }


/*
 * Sub-message sent periodically sent by the tracelet
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
   * Fused location
   */
  Tracelet__TraceletToServer__Location__Fused *fused;
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
  /*
   * Acceleration data
   */
  Tracelet__TraceletToServer__Location__Acceleration *acceleration;
};
#define TRACELET__TRACELET_TO_SERVER__LOCATION__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__tracelet_to_server__location__descriptor) \
    , NULL, NULL, NULL, TRACELET__TRACELET_TO_SERVER__LOCATION__DIRECTION__NO_DIRECTION, 0, 0, 0, NULL }


typedef enum {
  TRACELET__TRACELET_TO_SERVER__TYPE__NOT_SET = 0,
  TRACELET__TRACELET_TO_SERVER__TYPE_LOCATION = 5
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(TRACELET__TRACELET_TO_SERVER__TYPE)
} Tracelet__TraceletToServer__TypeCase;

struct  _Tracelet__TraceletToServer
{
  ProtobufCMessage base;
  /*
   * Currently not used, always 0
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
  };
};
#define TRACELET__TRACELET_TO_SERVER__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&tracelet__tracelet_to_server__descriptor) \
    , 0, NULL, (char *)protobuf_c_empty_string, 0, TRACELET__TRACELET_TO_SERVER__TYPE__NOT_SET, {0} }


/* Tracelet__TraceletToServer__Location__Gnss methods */
void   tracelet__tracelet_to_server__location__gnss__init
                     (Tracelet__TraceletToServer__Location__Gnss         *message);
/* Tracelet__TraceletToServer__Location__Uwb methods */
void   tracelet__tracelet_to_server__location__uwb__init
                     (Tracelet__TraceletToServer__Location__Uwb         *message);
/* Tracelet__TraceletToServer__Location__Fused methods */
void   tracelet__tracelet_to_server__location__fused__init
                     (Tracelet__TraceletToServer__Location__Fused         *message);
/* Tracelet__TraceletToServer__Location__Acceleration methods */
void   tracelet__tracelet_to_server__location__acceleration__init
                     (Tracelet__TraceletToServer__Location__Acceleration         *message);
/* Tracelet__TraceletToServer__Location methods */
void   tracelet__tracelet_to_server__location__init
                     (Tracelet__TraceletToServer__Location         *message);
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

typedef void (*Tracelet__TraceletToServer__Location__Gnss_Closure)
                 (const Tracelet__TraceletToServer__Location__Gnss *message,
                  void *closure_data);
typedef void (*Tracelet__TraceletToServer__Location__Uwb_Closure)
                 (const Tracelet__TraceletToServer__Location__Uwb *message,
                  void *closure_data);
typedef void (*Tracelet__TraceletToServer__Location__Fused_Closure)
                 (const Tracelet__TraceletToServer__Location__Fused *message,
                  void *closure_data);
typedef void (*Tracelet__TraceletToServer__Location__Acceleration_Closure)
                 (const Tracelet__TraceletToServer__Location__Acceleration *message,
                  void *closure_data);
typedef void (*Tracelet__TraceletToServer__Location_Closure)
                 (const Tracelet__TraceletToServer__Location *message,
                  void *closure_data);
typedef void (*Tracelet__TraceletToServer_Closure)
                 (const Tracelet__TraceletToServer *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCMessageDescriptor tracelet__tracelet_to_server__descriptor;
extern const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__descriptor;
extern const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__gnss__descriptor;
extern const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__uwb__descriptor;
extern const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__fused__descriptor;
extern const ProtobufCMessageDescriptor tracelet__tracelet_to_server__location__acceleration__descriptor;
extern const ProtobufCEnumDescriptor    tracelet__tracelet_to_server__location__direction__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_tracelet_2eproto__INCLUDED */
