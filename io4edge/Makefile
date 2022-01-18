all: golang c

golang: proto-golang-functionblock proto-golang-core proto-golang-inventory
 
c: proto-c-functionblock proto-c-core proto-c-inventory

proto-c-functionblock:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/functionblock/v1alpha1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/functionblock/v1alpha1/ && protoc --c_out=/out/functionblock/v1alpha1 -I/proto/ /proto/io4edge_functionblock.proto"

proto-golang-functionblock:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/functionblock/v1alpha1 ./proto/functionblock/v1alpha1/io4edge_functionblock.proto --go_out=go/

proto-c-core:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/core/v1alpha2:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/core/v1alpha2/ && protoc --c_out=/out/core/v1alpha2 -I/proto/ /proto/io4edge_core.proto"

proto-golang-core:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/core/v1alpha2 ./proto/core/v1alpha2/io4edge_core.proto --go_out=go/

proto-c-inventory:
	mkdir -p protobuf-c
	docker run --rm --user "$(shell id -u):$(shell id -g)" \
	-v $(shell pwd)/proto/inventory/v1alpha1:/proto \
	-v $(shell pwd)/protobuf-c/:/out ixuan/protobuf-c \
	sh -c "mkdir -p /out/inventory/v1alpha1/ && protoc --c_out=/out/inventory/v1alpha1 -I/proto/ /proto/io4edge_inventory.proto"

proto-golang-inventory:
	mkdir -p go/
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
	protoc -I=./proto/inventory/v1alpha1 ./proto/inventory/v1alpha1/io4edge_inventory.proto --go_out=go/

clean: clean-c clean-golang

clean-c:
	rm -rf protobuf-c/

clean-golang:
	rm -rf go/

.PHONY: all golang proto-golang-functionblock c proto-c-functionblock proto-golang-inventory proto-c-inventory proto-golang-core proto-c-core clean clean-c clean-golang
