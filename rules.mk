#
# Makefile to be included by each module
#
# Expected variables:
# MODULE: subpath within the proto directory containing the proto files, e.g. "mvbSniffer/v1"
# PROTOS: List of all proto files

# search path for files
VPATH ?= ./proto/$(MODULE):./go/$(MODULE):./protobuf-c/$(MODULE):./python/$(MODULE)
WELLKNOWNTYPES_PROTO = ../google_wellknowntypes/proto

# GOLANG
%.pb.go ::  %.proto
	@mkdir -p go/
	@echo " generating $@"
	@protoc -I./proto/$(MODULE) -I$(WELLKNOWNTYPES_PROTO) $(EXTRA_PROTO_PATHS) $< --go_out=go/

GO_TARGETS := $(PROTOS:.proto=.pb.go)

# C
%.pb-c.c ::  %.proto
	@mkdir -p protobuf-c/$(MODULE)
	@echo " generating $@"
	@protoc -I./proto/$(MODULE) -I$(WELLKNOWNTYPES_PROTO) $(EXTRA_PROTO_PATHS) $< --c_out=protobuf-c/$(MODULE)

C_TARGETS := $(PROTOS:.proto=.pb-c.c)

# PYTHON
%_pb2.py ::  %.proto
	@mkdir -p python/
	@echo " generating $@"
	@protoc -I./proto -I./proto/$(MODULE) -I$(WELLKNOWNTYPES_PROTO) $(EXTRA_PROTO_PATHS) $< --python_out=python/

PY_TARGETS := $(PROTOS:.proto=_pb2.py)


build: $(GO_TARGETS) $(C_TARGETS) $(PY_TARGETS)

clean:
	rm -rf go/ protobuf-c/ python/

.PHONY: build clean
