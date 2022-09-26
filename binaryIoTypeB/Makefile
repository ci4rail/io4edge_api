all: golang c

golang: proto-golang-binaryIoTypeB

c: proto-c-binaryIoTypeB

proto-c-binaryIoTypeB:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/binaryIoTypeB/v1alpha1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/binaryIoTypeB/v1alpha1/ && protoc --c_out=/out/binaryIoTypeB/v1alpha1 -I/proto/ /proto/binaryIoTypeB.proto"

proto-golang-binaryIoTypeB:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/binaryIoTypeB/v1alpha1 ./proto/binaryIoTypeB/v1alpha1/binaryIoTypeB.proto --go_out=go/

clean: clean-c clean-golang

clean-c:
	rm -rf protobuf-c/

clean-golang:
	rm -rf go/

.PHONY: all golang proto-golang-binaryIoTypeB c proto-c-binaryIoTypeB clean clean-c clean-golang
