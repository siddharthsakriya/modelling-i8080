# Modern Modelling of the Intel 8080 - Achieved 80% (A2)
A formal specification of the Intel 8080 CPU written in [Sail](https://github.com/rems-project/sail "Sail Github Page").
## Project Structure
```
├── compile_coverage.py                  # generates coverage report for custom test suite
├── coverage_results/                    # html coverage reports
├── decoder/                             # decode and instructions sail files
│   ├── decode.sail                      # sail code to decode instruction
│   └── instructions.sail                # instruction semantics for execution
├── helper.py                            # helper script to convert hex to ascii
├── main.sail                            # main control loop/ fetch-decode-execute loop
├── makefile                             # makefile with different build options
├── mem&reg/                             # memory and type file
│   ├── memory.sail                      # memory and functions to interface it
│   └── types.sail                       # custom type synonyms
├── programs8080/                        # existing intel 8080 binaries 
├── run.sh                               # bash script for automating build + run process
├── runner_binary.py                     # script to run existing 8080 code on model via binary
├── runner_interactive.py                # script to run existing 8080 code via sail interactive mode
├── test/                                # contains asm files and custom test suites for each instruction
└── utility/                             # contains utility sail files
    ├── timing.sail                      # contails sail functions for counting cycles
    └── utils.sail                       # additional utility functions 
```

## Requirements
This project requires 3.10.10+, Pytest, and Sail.

## How to Run
I have provided a `makefile` that compiles the Sail code to C, and then compiles the C into an executable file (binary). This project can also be run via Sails Interactive Mode. 

To run a test suite, use `runner_binary.py`, specify Intel 8080 binary and specify if you want execution or coverage mode. Example usage from root directory to run in execution mode:
```
> python3 runner_binary.py programs8080/TST8080.COM e
```
Pytest is used to run the unit tests, this is simply enabled by typing out the following command from the **root** directory of the project:
```
> pytest testing/unit
```
## Test Results
The external tests used and their respective owners:
- `CPUTEST.COM` © 1981 Supersoft Associates - Passed
- `TEST.COM` © 1980 Microcosm Associates - Passed
- `8080PRE.COM` (GPLv3) © 1994 Frank D. Cringle © 2009 Ian Bartholomew - Passed
- `8080EXM.COM` (GPLv3) © 1994 Frank D. Cringle © 2009 Ian Bartholomew - Passed

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
8080 instruction exerciser

dad <b,d,h,sp>................  PASS! crc is:14474ba6

aluop nn......................  PASS! crc is:9e922f9e

aluop <b,c,d,e,h,l,m,a>.......  PASS! crc is:cf762c86

<daa,cma,stc,cmc>.............  PASS! crc is:bb3f030c

<inr,dcr> a...................  PASS! crc is:adb6460e

<inr,dcr> b...................  PASS! crc is:83ed1345

<inx,dcx> b...................  PASS! crc is:f79287cd

<inr,dcr> c...................  PASS! crc is:e5f6721b

<inr,dcr> d...................  PASS! crc is:15b5579a

<inx,dcx> d...................  PASS! crc is:7f4e2501

<inr,dcr> e...................  PASS! crc is:cf2ab396

<inr,dcr> h...................  PASS! crc is:12b2952c

<inx,dcx> h...................  PASS! crc is:9f2b23c0

<inr,dcr> l...................  PASS! crc is:ff57d356

<inr,dcr> m...................  PASS! crc is:92e963bd

<inx,dcx> sp..................  PASS! crc is:d5702fab

lhld nnnn.....................  PASS! crc is:a9c3d5cb

shld nnnn.....................  PASS! crc is:e8864f26

lxi <b,d,h,sp>,nnnn...........  PASS! crc is:fcf46e12

ldax <b,d>....................  PASS! crc is:2b821d5f

mvi <b,c,d,e,h,l,m,a>,nn......  PASS! crc is:eaa72044

mov <bcdehla>,<bcdehla>.......  PASS! crc is:10b58cee

sta nnnn / lda nnnn...........  PASS! crc is:ed57af72

<rlc,rrc,ral,rar>.............  PASS! crc is:e0d89235

stax <b,d>....................  PASS! crc is:2b0471e9

Tests complete
```

<!-- ## MISC notes
- HLT and MOV M M opcode was clashing, caused MOV M M to be executed rather than HLT, MOV M M is invalid
- Was calculating Auxillary flag in the wrong place in ANA
- Remove startup_cpm from main when running tests
- Add startup_cpm when running an assembly file
- Pydrofoil compiler
- Presentation: 
    - Spend more time time discussing SAIL.
    - c_include filename.c
    - can run interrupt from  -->
