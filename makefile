# Compiler and flags
SAIL = sail
GCC = gcc
CFLAGS = -lgmp -lz -I /Users/siddharthsakriya/.opam/5.1.0/share/sail/lib/

# Source files
SAIL_SRC = instructions.sail
LIB_PATH = /Users/siddharthsakriya/.opam/5.1.0/share/sail/lib/*.c

# Output files
SAIL_OUT = out

# Default target
all: $(SAIL_OUT)

# Compile Sail source and C code
$(SAIL_OUT): $(SAIL_SRC)
	$(SAIL) -c $(SAIL_SRC) -o out
	$(GCC) out.c $(LIB_PATH) $(CFLAGS) -o $(SAIL_OUT)

# Clean up generated files
clean:
	rm -f out.c $(SAIL_OUT)
