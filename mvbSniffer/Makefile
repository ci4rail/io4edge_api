all: golang c

golang: proto-golang-mvbSniffer

c: proto-c-mvbSniffer

proto-c-mvbSniffer:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/mvbSniffer/v1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/mvbSniffer/v1/ && protoc --c_out=/out/mvbSniffer/v1 -I/proto/ /proto/mvbSniffer.proto /proto/telegram.proto /proto/timestamp.proto"

proto-golang-mvbSniffer:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I./proto -I=./proto/mvbSniffer/v1 ./proto/mvbSniffer/v1/mvbSniffer.proto ./proto/mvbSniffer/v1/telegram.proto --go_out=go/

clean: clean-c clean-golang

clean-c:
	rm -rf protobuf-c/

clean-golang:
	rm -rf go/

.PHONY: all golang proto-golang-mvbSniffer c proto-c-mvbSniffer clean clean-c clean-golang
