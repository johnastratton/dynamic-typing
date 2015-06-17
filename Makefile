
CFLAGS=-O3 -fno-inline

all: microbench

microbench : ISCodeSamples1.o
	g++ -o $@ $^ ${CFLAGS}

%.o : %.cpp %.h
	g++ -c -o $@ $< ${CFLAGS}

clean:
	rm ./*.o microbench

