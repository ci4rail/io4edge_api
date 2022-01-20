all:
	cd binaryIoTypeA && make
	cd io4edge && make
	cd templateModule && make

clean:
	cd binaryIoTypeA && make clean
	cd io4edge && make clean
	cd templateModule && make clean