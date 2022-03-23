all: golang c

golang: proto-golang-templateInterface

c: proto-c-templateInterface

proto-c-templateInterface:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/templateInterface/v1alpha1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/templateInterface/v1alpha1/ && protoc --c_out=/out/templateInterface/v1alpha1 -I/proto/ /proto/templateInterface.proto"

proto-golang-templateInterface:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/templateInterface/v1alpha1 ./proto/templateInterface/v1alpha1/templateInterface.proto --go_out=go/

clean: clean-c clean-golang

clean-c:
	rm -rf protobuf-c/

clean-golang:
	rm -rf go/

.PHONY: all golang proto-golang-templateInterface c proto-c-templateInterface clean clean-c clean-golang
