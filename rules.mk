#
# Makefile to be included by each module
#
# Expected variables:
# MODULE: subpath within the proto directory containing the proto files, e.g. "mvbSniffer/v1"
# PROTOS: List of all proto files

# search path for files
VPATH = ./proto/$(MODULE):./go/$(MODULE):./protobuf-c/$(MODULE)
WELLKNOWNTYPES_PROTO = ../google_wellknowntypes/proto

# GOLANG
%.pb.go ::  %.proto
	@mkdir -p go/
	@go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I./proto/$(MODULE) -I$(WELLKNOWNTYPES_PROTO) $< --go_out=go/

GO_TARGETS := $(PROTOS:.proto=.pb.go)

# C
%.pb-c.c ::  %.proto
	@mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(CURDIR)/proto/$(MODULE):/proto \
	-v $(CURDIR)/protobuf-c/:/out \
	-v $(realpath $(WELLKNOWNTYPES_PROTO)):/wellknowntypes \
	ixuan/protobuf-c \
	sh -c "mkdir -p /out/$(MODULE) && protoc --c_out=/out/$(MODULE)  -I/proto/ -I/wellknowntypes /proto/$(subst ./proto/$(MODULE),,$<)"

C_TARGETS := $(PROTOS:.proto=.pb-c.c)

# PYTHON
%_pb2.py ::  %.proto
	@mkdir -p python/
	protoc -I./proto -I$(WELLKNOWNTYPES_PROTO)  -I./proto/$(MODULE) $< --python_out=python/

PY_TARGETS := $(PROTOS:.proto=_pb2.py)


build: $(GO_TARGETS) $(C_TARGETS) $(PY_TARGETS)

clean:
	rm -rf go/ protobuf-c/ python/

.PHONY: build clean
