all:
	cd binaryIoTypeA && make
	cd analogInTypeA && make
	cd mvbSniffer && make
	cd mvbDebug && make
	cd canL2 && make
	cd motionSensor && make
	cd io4edge && make
	cd templateInterface && make

clean:
	cd binaryIoTypeA && make clean
	cd analogIn && make clean
	cd mvbSniffer && make clean
	cd mvbDebug && make clean
	cd canL2 && make clean
	cd motionSensor && make clean
	cd io4edge && make clean
	cd templateInterface && make clean
