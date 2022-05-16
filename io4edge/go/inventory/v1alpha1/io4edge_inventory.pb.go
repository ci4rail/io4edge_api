//
//Copyright © 2021 Ci4Rail GmbH <engineering@ci4rail.com>
//
//Licensed under the Apache License, Version 2.0 (the "License");
//you may not use this file except in compliance with the License.
//You may obtain a copy of the License at
//
//http://www.apache.org/licenses/LICENSE-2.0
//
//Unless required by applicable law or agreed to in writing, software
//distributed under the License is distributed on an "AS IS" BASIS,
//WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//See the License for the specific language governing permissions and
//limitations under the License.

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.0
// 	protoc        v3.6.1
// source: io4edge_inventory.proto

package v1alpha1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Unit struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	RootArticle  string `protobuf:"bytes,1,opt,name=root_article,json=rootArticle,proto3" json:"root_article,omitempty"`
	MajorVersion uint32 `protobuf:"varint,2,opt,name=major_version,json=majorVersion,proto3" json:"major_version,omitempty"`
	Serial       string `protobuf:"bytes,3,opt,name=serial,proto3" json:"serial,omitempty"`
}

func (x *Unit) Reset() {
	*x = Unit{}
	if protoimpl.UnsafeEnabled {
		mi := &file_io4edge_inventory_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Unit) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Unit) ProtoMessage() {}

func (x *Unit) ProtoReflect() protoreflect.Message {
	mi := &file_io4edge_inventory_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Unit.ProtoReflect.Descriptor instead.
func (*Unit) Descriptor() ([]byte, []int) {
	return file_io4edge_inventory_proto_rawDescGZIP(), []int{0}
}

func (x *Unit) GetRootArticle() string {
	if x != nil {
		return x.RootArticle
	}
	return ""
}

func (x *Unit) GetMajorVersion() uint32 {
	if x != nil {
		return x.MajorVersion
	}
	return 0
}

func (x *Unit) GetSerial() string {
	if x != nil {
		return x.Serial
	}
	return ""
}

var File_io4edge_inventory_proto protoreflect.FileDescriptor

var file_io4edge_inventory_proto_rawDesc = []byte{
	0x0a, 0x17, 0x69, 0x6f, 0x34, 0x65, 0x64, 0x67, 0x65, 0x5f, 0x69, 0x6e, 0x76, 0x65, 0x6e, 0x74,
	0x6f, 0x72, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x10, 0x69, 0x6f, 0x34, 0x65, 0x64,
	0x67, 0x65, 0x49, 0x6e, 0x76, 0x65, 0x6e, 0x74, 0x6f, 0x72, 0x79, 0x22, 0x66, 0x0a, 0x04, 0x55,
	0x6e, 0x69, 0x74, 0x12, 0x21, 0x0a, 0x0c, 0x72, 0x6f, 0x6f, 0x74, 0x5f, 0x61, 0x72, 0x74, 0x69,
	0x63, 0x6c, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x72, 0x6f, 0x6f, 0x74, 0x41,
	0x72, 0x74, 0x69, 0x63, 0x6c, 0x65, 0x12, 0x23, 0x0a, 0x0d, 0x6d, 0x61, 0x6a, 0x6f, 0x72, 0x5f,
	0x76, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0d, 0x52, 0x0c, 0x6d,
	0x61, 0x6a, 0x6f, 0x72, 0x56, 0x65, 0x72, 0x73, 0x69, 0x6f, 0x6e, 0x12, 0x16, 0x0a, 0x06, 0x73,
	0x65, 0x72, 0x69, 0x61, 0x6c, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06, 0x73, 0x65, 0x72,
	0x69, 0x61, 0x6c, 0x42, 0x14, 0x5a, 0x12, 0x69, 0x6e, 0x76, 0x65, 0x6e, 0x74, 0x6f, 0x72, 0x79,
	0x2f, 0x76, 0x31, 0x61, 0x6c, 0x70, 0x68, 0x61, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x33,
}

var (
	file_io4edge_inventory_proto_rawDescOnce sync.Once
	file_io4edge_inventory_proto_rawDescData = file_io4edge_inventory_proto_rawDesc
)

func file_io4edge_inventory_proto_rawDescGZIP() []byte {
	file_io4edge_inventory_proto_rawDescOnce.Do(func() {
		file_io4edge_inventory_proto_rawDescData = protoimpl.X.CompressGZIP(file_io4edge_inventory_proto_rawDescData)
	})
	return file_io4edge_inventory_proto_rawDescData
}

var file_io4edge_inventory_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_io4edge_inventory_proto_goTypes = []interface{}{
	(*Unit)(nil), // 0: io4edgeInventory.Unit
}
var file_io4edge_inventory_proto_depIdxs = []int32{
	0, // [0:0] is the sub-list for method output_type
	0, // [0:0] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_io4edge_inventory_proto_init() }
func file_io4edge_inventory_proto_init() {
	if File_io4edge_inventory_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_io4edge_inventory_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Unit); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_io4edge_inventory_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_io4edge_inventory_proto_goTypes,
		DependencyIndexes: file_io4edge_inventory_proto_depIdxs,
		MessageInfos:      file_io4edge_inventory_proto_msgTypes,
	}.Build()
	File_io4edge_inventory_proto = out.File
	file_io4edge_inventory_proto_rawDesc = nil
	file_io4edge_inventory_proto_goTypes = nil
	file_io4edge_inventory_proto_depIdxs = nil
}
