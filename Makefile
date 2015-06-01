
CFLAGS=-O3 -fno-inline -I /home/lpentecost/Documents/sniper-6.1/include

all: microbench

microbench : ISCodeSamples1.o
	g++ -o $@ $^ ${CFLAGS}

%.o : %.cpp %.h
	g++ -c -o $@ $< ${CFLAGS}

clean:
	rm ./*.o microbench

