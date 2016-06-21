
CFLAGS=-O3 -fno-inline

all: microbench jmpbench

jmpbench : ISCodeSamples1_jmp.S
	g++ -o $@ $^ ${CFLAGS}

microbench : ISCodeSamples1.o
	g++ -o $@ $^ ${CFLAGS}

%.o : %.cpp %.h
	g++ -c -o $@ $< ${CFLAGS}

clean:
	rm ./*.o microbench jmpbench

