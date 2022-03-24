all: golang c

golang: proto-golang-canL2

c: proto-c-canL2

proto-c-canL2:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/canL2/v1alpha1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/canL2/v1alpha1/ && protoc --c_out=/out/canL2/v1alpha1 -I/proto/ /proto/canL2.proto"

proto-golang-canL2:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/canL2/v1alpha1 ./proto/canL2/v1alpha1/canL2.proto --go_out=go/

clean: clean-c clean-golang

clean-c:
	rm -rf protobuf-c/

clean-golang:
	rm -rf go/

.PHONY: all golang proto-golang-canL2 c proto-c-canL2 clean clean-c clean-golang
