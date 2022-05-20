all:
	cd binaryIoTypeA && make
	cd analogInTypeA && make
	cd mvbSniffer && make
	cd mvbDebug && make
	cd io4edge && make
	cd templateInterface && make

clean:
	cd binaryIoTypeA && make clean
	cd analogIn && make clean
	cd mvbSniffer && make clean
	cd mvbDebug && make clean
	cd io4edge && make clean
	cd templateInterface && make clean
