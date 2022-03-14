all:
	cd binaryIoTypeA && make
	cd analogInTypeA && make
	cd mvbSniffer && make
	cd io4edge && make
	cd templateModule && make

clean:
	cd binaryIoTypeA && make clean
	cd analogIn && make clean
	cd mvbSniffer && make clean
	cd io4edge && make clean
	cd templateModule && make clean
