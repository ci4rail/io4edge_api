all: golang c

golang: proto-golang-binaryIoTypeA

c: proto-c-binaryIoTypeA

proto-c-binaryIoTypeA:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/binaryIoTypeA/v1alpha1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/binaryIoTypeA/v1alpha1/ && protoc --c_out=/out/binaryIoTypeA/v1alpha1 -I/proto/ /proto/binaryIoTypeA.proto"

proto-golang-binaryIoTypeA:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/binaryIoTypeA/v1alpha1 ./proto/binaryIoTypeA/v1alpha1/binaryIoTypeA.proto --go_out=go/

clean: clean-c clean-golang

clean-c:
	rm -rf protobuf-c/

clean-golang:
	rm -rf go/

.PHONY: all golang proto-golang-binaryIoTypeA c proto-c-binaryIoTypeA clean clean-c clean-golang
