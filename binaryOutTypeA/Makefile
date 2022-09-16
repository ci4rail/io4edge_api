all: golang c

golang: proto-golang-binaryOutTypeA

c: proto-c-binaryOutTypeA

proto-c-binaryOutTypeA:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/binaryOutTypeA/v1alpha1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/binaryOutTypeA/v1alpha1/ && protoc --c_out=/out/binaryOutTypeA/v1alpha1 -I/proto/ /proto/binaryOutTypeA.proto"

proto-golang-binaryOutTypeA:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/binaryOutTypeA/v1alpha1 ./proto/binaryOutTypeA/v1alpha1/binaryOutTypeA.proto --go_out=go/

clean: clean-c clean-golang

clean-c:
	rm -rf protobuf-c/

clean-golang:
	rm -rf go/

.PHONY: all golang proto-golang-binaryOutTypeA c proto-c-binaryOutTypeA clean clean-c clean-golang
