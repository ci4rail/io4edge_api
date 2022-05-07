all: golang c

golang: proto-golang-mvbDebug

c: proto-c-mvbDebug

proto-c-mvbDebug:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/mvbDebug/v1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/mvbDebug/v1/ && protoc --c_out=/out/mvbDebug/v1 -I/proto/ /proto/mvbDebug.proto"

proto-golang-mvbDebug:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/mvbDebug/v1 ./proto/mvbDebug/v1/mvbDebug.proto --go_out=go/

clean: clean-c clean-golang

clean-c:
	rm -rf protobuf-c/

clean-golang:
	rm -rf go/

.PHONY: all golang proto-golang-mvbDebug c proto-c-mvbDebug clean clean-c clean-golang
