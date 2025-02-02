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

## MISC notes
- HLT and MOV M M opcode was clashing 
- Was calculating Auxillary flag in the wrong place in ANA
- Remove startup_cpm from main when running tests
- Add startup_cpm when running an assembly file
- Pydrofoil compiler
- Presentation: 
    - Spend more time time discussing SAIL.
    - c_include filename.c
    - can run interrupt from 