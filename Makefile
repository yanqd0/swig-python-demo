SRC := src/example

.DEFAULT_GOAL := ${SRC}/_example.so

${SRC}/_example.so : ${SRC}/example.o ${SRC}/example_wrap.o
	gcc -shared ${SRC}/example.o ${SRC}/example_wrap.o -o ${SRC}/_example.so -lpython3.5m

${SRC}/example.o : ${SRC}/example.c
	gcc -c -fPIC -I/usr/include/python3.5m ${SRC}/example.c -o ${SRC}/example.o

${SRC}/example_wrap.o : ${SRC}/example_wrap.c
	gcc -c -fPIC -I/usr/include/python3.5m ${SRC}/example_wrap.c -o ${SRC}/example_wrap.o

${SRC}/example_wrap.c ${SRC}/example.py : ${SRC}/example.i ${SRC}/example.h
	swig -python ${SRC}/example.i

clean:
	rm -f ${SRC}/*.o ${SRC}/*.so ${SRC}/example_wrap.* ${SRC}/example.py*

test:
	python setup.py test

.PHONY: clean test
