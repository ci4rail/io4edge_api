all: golang c

golang: proto-golang-templateModule

c: proto-c-templateModule

proto-c-templateModule:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/templateModule/v1alpha1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/templateModule/v1alpha1/ && protoc --c_out=/out/templateModule/v1alpha1 -I/proto/ /proto/templateModule.proto"

proto-golang-templateModule:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/templateModule/v1alpha1 ./proto/templateModule/v1alpha1/templateModule.proto --go_out=go/

clean: clean-c clean-golang

clean-c:
	rm -rf protobuf-c/

clean-golang:
	rm -rf go/

.PHONY: all golang proto-golang-templateModule c proto-c-templateModule clean clean-c clean-golang
