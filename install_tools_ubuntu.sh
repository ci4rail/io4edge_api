# define the versions of the tools to install
GO_VERSION='1.25.1'

PROTOC_VERSION=32.1
PROTOC_VERSION_WITH_DASH=32.1

PROTOCC_VERSION=1.4.1-1ubuntu4

PROTOCGO_VERSION=v1.36.9

# install go
wget -q https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz && \
    sudo rm -rf /usr/local/go && \
    sudo tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz &&\

rm -f go${GO_VERSION}.linux-amd64.tar.gz

go install google.golang.org/protobuf/cmd/protoc-gen-go@${PROTOCGO_VERSION}

# protoc
echo "https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION_WITH_DASH}-linux-x86_64.zip"
curl -Lo protoc.zip "https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION_WITH_DASH}-linux-x86_64.zip" && \
    sudo unzip -qo protoc.zip bin/protoc -d /usr/local && \
    sudo chmod a+x /usr/local/bin/protoc 

rm -f protoc.zip

sudo apt-get update && export DEBIAN_FRONTEND=noninteractive && sudo apt-get -y install --no-install-recommends \
    protobuf-c-compiler=${PROTOCC_VERSION}