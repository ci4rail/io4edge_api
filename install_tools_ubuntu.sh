# define the versions of the tools to install
# GO_VERSION='1.25.1' - Go is installed via devcontainer feature

PROTOC_VERSION=32.1
PROTOC_VERSION_WITH_DASH=32.1

PROTOCC_VERSION=1.4.1-1ubuntu4

PROTOCGO_VERSION=v1.36.9

# Detect architecture
ARCH=$(uname -m)
case $ARCH in
    x86_64)
        GO_ARCH="amd64"
        ;;
    aarch64|arm64)
        GO_ARCH="arm64"
        ;;
    *)
        echo "Unsupported architecture: $ARCH"
        exit 1
        ;;
esac

# Skip Go installation - already handled by devcontainer feature
echo "Skipping Go installation (handled by devcontainer feature)"

# Install protoc-gen-go (uses the Go installation from devcontainer feature)
echo "Installing protoc-gen-go..."
go install google.golang.org/protobuf/cmd/protoc-gen-go@${PROTOCGO_VERSION}

# protoc
PROTOC_ARCH=$GO_ARCH
if [ "$GO_ARCH" = "arm64" ]; then
    PROTOC_ARCH="aarch_64"
elif [ "$GO_ARCH" = "amd64" ]; then
    PROTOC_ARCH="x86_64"
fi

echo "https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION_WITH_DASH}-linux-${PROTOC_ARCH}.zip"
curl -Lo protoc.zip "https://github.com/protocolbuffers/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION_WITH_DASH}-linux-${PROTOC_ARCH}.zip" && \
    sudo unzip -qo protoc.zip bin/protoc -d /usr/local && \
    sudo chmod a+x /usr/local/bin/protoc 

rm -f protoc.zip

sudo apt-get update && export DEBIAN_FRONTEND=noninteractive && sudo apt-get -y install --no-install-recommends \
    protobuf-c-compiler=${PROTOCC_VERSION}