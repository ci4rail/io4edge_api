all: golang c

golang: proto-golang-motionSensor

c: proto-c-motionSensor

proto-c-motionSensor:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/motionSensor/v1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/motionSensor/v1/ && protoc --c_out=/out/motionSensor/v1 -I/proto/ /proto/motionSensor.proto"

proto-golang-motionSensor:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/motionSensor/v1 ./proto/motionSensor/v1/motionSensor.proto --go_out=go/

clean: clean-c clean-golang

clean-c:
	rm -rf protobuf-c/

clean-golang:
	rm -rf go/

.PHONY: all golang proto-golang-motionSensor c proto-c-motionSensor clean clean-c clean-golang
