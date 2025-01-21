# Modern Modelling of the Intel 8080
A formal specification of the Intel 8080 CPU written in  [Sail](https://github.com/rems-project/sail "Sail Github Page") .
## Files
There are several folders for different parts/areas of the processor, the main Fetch-Decode-Execute cycle can be found in `main.sail`. I have done my best to keep function and variable names very clear, and to keep some commenting to allow for readable code.

## How to Run

I have provided a `makefile` that compiles the Sail code to C, and then compiles the C into an executable file (binary). This project can also be run via Sails Interactive Mode. 
The python script `runner.py` allows for a `.COM` file to be loaded in and executed. I have mocked CP/M syscalls using the information provided, and the logic for that can be found [here](https://retrocomputing.stackexchange.com/questions/9361/test-emulated-8080-cpu-without-an-os "cp/m syscall mocking") .
Pytest is used to run the unit tests, this is simply enabled by typing out the following command from the **root** directory of the project:
```
> pytest testing/unit
```
## Test Results

The external tests used and their respective owners:
- `CPUTEST.COM` © 1981 Supersoft Associates - Passed
- `TEST.COM` © 1980 Microcosm Associates - Passed
- `8080PRE.COM` (GPLv3) © 1994 Frank D. Cringle © 2009 Ian Bartholomew - Passed
- `8080EXM.COM` (GPLv3) © 1994 Frank D. Cringle © 2009 Ian Bartholomew - TBC (takes extremely long to run)

Notably with the generated emulator, `CPUTEST` takes roughly 35-40 minutes to run, and completes around 250 million cycles.

```
#CPUTEST.COM output:

DIAGNOSTICS II V1.2 - CPU TEST
COPYRIGHT (C) 1981 - SUPERSOFT ASSOCIATES

ABCDEFGHIJKLMNOPQRSTUVWXYZ
CPU IS 8080/8085
BEGIN TIMING TEST
END TIMING TEST
CPU TESTS OK
```
```
#TEST.COM output:

MICROCOSM ASSOCIATES 8080/8085 CPU DIAGNOSTIC VERSION 1.0  (C) 1980

CPU IS OPERATIONAL
```
```
#8080PRE.COM output:

8080 Preliminary tests complete
```
``` 
#8080EXM.COM output:
TBC
```

## MISC notes
- HLT and MOV M M opcode was clashing 
- Was calculating Auxillary flag in the wrong place in ANA
- Remove startup_cpm from main when running tests
- Add startup_cpm when running an assembly file
