/* Generated by the protocol buffer compiler.  DO NOT EDIT! */
/* Generated from: telegram.proto */

#ifndef PROTOBUF_C_telegram_2eproto__INCLUDED
#define PROTOBUF_C_telegram_2eproto__INCLUDED

#include <protobuf-c/protobuf-c.h>

PROTOBUF_C__BEGIN_DECLS

#if PROTOBUF_C_VERSION_NUMBER < 1003000
# error This file was generated by a newer version of protoc-c which is incompatible with your libprotobuf-c headers. Please update your headers.
#elif 1003003 < PROTOBUF_C_MIN_COMPILER_VERSION
# error This file was generated by an older version of protoc-c which is incompatible with your libprotobuf-c headers. Please regenerate this file with a newer version of protoc-c.
#endif


typedef struct _MvbSniffer__Telegram MvbSniffer__Telegram;
typedef struct _MvbSniffer__TelegramCollection MvbSniffer__TelegramCollection;


/* --- enums --- */

/*
 * Values for "state" field. Multiple bits may be set at the same time.
 */
typedef enum _MvbSniffer__Telegram__State {
  /*
   * No errors
   */
  MVB_SNIFFER__TELEGRAM__STATE__kSuccessful = 0,
  /*
   * No slave frame has been received to a master frame
   * Only the master information is valid (timestamp, type, address, line), data is empty
   */
  MVB_SNIFFER__TELEGRAM__STATE__kTimedOut = 1,
  /*
   * one or more MVB frames are lost in the device since the last telegram.
   * however, this telegram is valid.
   */
  MVB_SNIFFER__TELEGRAM__STATE__kMissedMVBFrames = 2,
  /*
   * one or more telegrams are lost
   * however, this telegram is valid.
   */
  MVB_SNIFFER__TELEGRAM__STATE__kMissedTelegrams = 4
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(MVB_SNIFFER__TELEGRAM__STATE)
} MvbSniffer__Telegram__State;
typedef enum _MvbSniffer__Telegram__Type {
  MVB_SNIFFER__TELEGRAM__TYPE__kProcessData16Bit = 0,
  MVB_SNIFFER__TELEGRAM__TYPE__kProcessData32Bit = 1,
  MVB_SNIFFER__TELEGRAM__TYPE__kProcessData64Bit = 2,
  MVB_SNIFFER__TELEGRAM__TYPE__kProcessData128Bit = 3,
  MVB_SNIFFER__TELEGRAM__TYPE__kProcessData256Bit = 4,
  MVB_SNIFFER__TELEGRAM__TYPE__kReserved_1 = 5,
  MVB_SNIFFER__TELEGRAM__TYPE__kReserved_2 = 6,
  MVB_SNIFFER__TELEGRAM__TYPE__kReserved_3 = 7,
  MVB_SNIFFER__TELEGRAM__TYPE__kMastershipTransfer = 8,
  MVB_SNIFFER__TELEGRAM__TYPE__kGeneralEvent = 9,
  MVB_SNIFFER__TELEGRAM__TYPE__kReserved_4 = 10,
  MVB_SNIFFER__TELEGRAM__TYPE__kReserved_5 = 11,
  MVB_SNIFFER__TELEGRAM__TYPE__kMessageData = 12,
  MVB_SNIFFER__TELEGRAM__TYPE__kGroupEvent = 13,
  MVB_SNIFFER__TELEGRAM__TYPE__kSingleEvent = 14,
  MVB_SNIFFER__TELEGRAM__TYPE__kDeviceStatus = 15
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(MVB_SNIFFER__TELEGRAM__TYPE)
} MvbSniffer__Telegram__Type;
typedef enum _MvbSniffer__Telegram__Line {
  MVB_SNIFFER__TELEGRAM__LINE__kA = 0,
  MVB_SNIFFER__TELEGRAM__LINE__kB = 1
    PROTOBUF_C__FORCE_ENUM_TO_BE_INT_SIZE(MVB_SNIFFER__TELEGRAM__LINE)
} MvbSniffer__Telegram__Line;

/* --- messages --- */

/*
 * Telegram represents a single information from an MVB device
 */
struct  _MvbSniffer__Telegram
{
  ProtobufCMessage base;
  /*
   * timestamp respresenting the start of the slave response
   * in microseconds since the start of the device
   */
  uint64_t timestamp;
  /*
   * State of that telegram. Contains ORed values from State enum
   */
  uint32_t state;
  /*
   * Type corresponds to the MVB f_code
   */
  MvbSniffer__Telegram__Type type;
  /*
   * address as sent by the master
   */
  int32_t address;
  /*
   * mvb data from the bus; CRCs removed
   */
  ProtobufCBinaryData data;
  /*
   * telegram number, increased with each telegram generated (global, not per stream)
   */
  uint64_t telegram_nr;
  /*
   * line used to receive the data of this telegram
   */
  MvbSniffer__Telegram__Line line;
};
#define MVB_SNIFFER__TELEGRAM__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_sniffer__telegram__descriptor) \
    , 0, 0, MVB_SNIFFER__TELEGRAM__TYPE__kProcessData16Bit, 0, {0,NULL}, 0, MVB_SNIFFER__TELEGRAM__LINE__kA }


struct  _MvbSniffer__TelegramCollection
{
  ProtobufCMessage base;
  size_t n_entry;
  MvbSniffer__Telegram **entry;
};
#define MVB_SNIFFER__TELEGRAM_COLLECTION__INIT \
 { PROTOBUF_C_MESSAGE_INIT (&mvb_sniffer__telegram_collection__descriptor) \
    , 0,NULL }


/* MvbSniffer__Telegram methods */
void   mvb_sniffer__telegram__init
                     (MvbSniffer__Telegram         *message);
size_t mvb_sniffer__telegram__get_packed_size
                     (const MvbSniffer__Telegram   *message);
size_t mvb_sniffer__telegram__pack
                     (const MvbSniffer__Telegram   *message,
                      uint8_t             *out);
size_t mvb_sniffer__telegram__pack_to_buffer
                     (const MvbSniffer__Telegram   *message,
                      ProtobufCBuffer     *buffer);
MvbSniffer__Telegram *
       mvb_sniffer__telegram__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_sniffer__telegram__free_unpacked
                     (MvbSniffer__Telegram *message,
                      ProtobufCAllocator *allocator);
/* MvbSniffer__TelegramCollection methods */
void   mvb_sniffer__telegram_collection__init
                     (MvbSniffer__TelegramCollection         *message);
size_t mvb_sniffer__telegram_collection__get_packed_size
                     (const MvbSniffer__TelegramCollection   *message);
size_t mvb_sniffer__telegram_collection__pack
                     (const MvbSniffer__TelegramCollection   *message,
                      uint8_t             *out);
size_t mvb_sniffer__telegram_collection__pack_to_buffer
                     (const MvbSniffer__TelegramCollection   *message,
                      ProtobufCBuffer     *buffer);
MvbSniffer__TelegramCollection *
       mvb_sniffer__telegram_collection__unpack
                     (ProtobufCAllocator  *allocator,
                      size_t               len,
                      const uint8_t       *data);
void   mvb_sniffer__telegram_collection__free_unpacked
                     (MvbSniffer__TelegramCollection *message,
                      ProtobufCAllocator *allocator);
/* --- per-message closures --- */

typedef void (*MvbSniffer__Telegram_Closure)
                 (const MvbSniffer__Telegram *message,
                  void *closure_data);
typedef void (*MvbSniffer__TelegramCollection_Closure)
                 (const MvbSniffer__TelegramCollection *message,
                  void *closure_data);

/* --- services --- */


/* --- descriptors --- */

extern const ProtobufCMessageDescriptor mvb_sniffer__telegram__descriptor;
extern const ProtobufCEnumDescriptor    mvb_sniffer__telegram__state__descriptor;
extern const ProtobufCEnumDescriptor    mvb_sniffer__telegram__type__descriptor;
extern const ProtobufCEnumDescriptor    mvb_sniffer__telegram__line__descriptor;
extern const ProtobufCMessageDescriptor mvb_sniffer__telegram_collection__descriptor;

PROTOBUF_C__END_DECLS


#endif  /* PROTOBUF_C_telegram_2eproto__INCLUDED */
