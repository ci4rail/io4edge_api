all: golang c

golang: proto-golang-analogInTypeA

c: proto-c-analogInTypeA

proto-c-analogInTypeA:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/analogInTypeA/v1alpha1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/analogInTypeA/v1alpha1/ && protoc --c_out=/out/analogInTypeA/v1alpha1 -I/proto/ /proto/analogInTypeA.proto"

proto-golang-analogInTypeA:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/analogInTypeA/v1alpha1 ./proto/analogInTypeA/v1alpha1/analogInTypeA.proto --go_out=go/

clean: clean-c clean-golang

clean-c:
	rm -rf protobuf-c/

clean-golang:
	rm -rf go/

.PHONY: all golang proto-golang-analogInTypeA c proto-c-analogInTypeA clean clean-c clean-golang
