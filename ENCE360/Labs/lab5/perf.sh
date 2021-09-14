#!/bin/bash
set -v
dd if=/dev/urandom of=test.dat  bs=10M count=1

time ./mmap 20
diff -q -s test.dat output.dat

time ./read_write 20 8192
diff -q -s test.dat output.dat

time ./read_write 20 2048
diff -q -s test.dat output.dat

time ./read_write 20 512
diff -q -s test.dat output.dat

time ./read_write 20 128
diff -q -s test.dat output.dat

time ./read_write 20 32
diff -q -s test.dat output.dat



time ./fread_fwrite 20 8192
diff -q -s test.dat output.dat

time ./fread_fwrite 20 2048
diff -q -s test.dat output.dat

time ./fread_fwrite 20 512
diff -q -s test.dat output.dat

time ./fread_fwrite 20 128
diff -q -s test.dat output.dat

time ./fread_fwrite 20 32
diff -q -s test.dat output.dat


time ./realloc 20
diff -q -s test.dat output.dat
