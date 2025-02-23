# Compiler and flags
SAIL = sail
GCC = gcc
CFLAGS = -O3 -lgmp -lz -I /Users/siddharthsakriya/.opam/5.1.0/share/sail/lib/
COVFLAGS = -lpthread -ldl
SAILCOV = sailcov

# Source files
SAIL_SRC = main.sail
LIB_PATH = /Users/siddharthsakriya/.opam/5.1.0/share/sail/lib/*.c
LIBSAIL_COVERAGE = /Users/siddharthsakriya/.opam/5.1.0/share/sail/lib/coverage/libsail_coverage.a

# Output files
SAIL_OUT = out

# Default target
all: $(SAIL_OUT)

# Compile Sail source and C code
$(SAIL_OUT): $(SAIL_SRC)
	$(SAIL) -c $(SAIL_SRC) -o out -O
	$(GCC) out.c $(LIB_PATH) $(CFLAGS) -o $(SAIL_OUT)

# Clean up generated files
clean:
	rm -f out.c $(SAIL_OUT)
	rm -f z3_problems
	rm -f ./testing/output.txt
	rm -f commands.txt
	rm -f sail_coverage 
	rm -f all_branches

write:
	./out| tee ./testing/output.txt

coverage_bin: $(SAIL_SRC)
	$(SAIL) -c -c_coverage all_branches -c_include sail_coverage.h $(SAIL_SRC) -o $(SAIL_OUT) -O
	$(GCC) out.c $(LIBSAIL_COVERAGE) $(LIB_PATH) $(COVFLAGS) $(CFLAGS) -o $(SAIL_OUT)

coverage_gen: 
	$(SAILCOV) -a all_branches -t sail_coverage $(ARG1).sail



