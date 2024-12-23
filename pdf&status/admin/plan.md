TODO:

- Look into cycle counts, and if there is any pipelining:
https://pastebin.com/sFANRuYr :
Seems to just be decrementing the cycles by instruction
https://github.com/GunshipPenguin/lib8080/blob/master/src/i8080.c
Seems to just increment the count as is
If it is similar to Z80 then maybe we would decrement by 2

Page 2-20: The results of these arithmetic, logical or rotate in- structions are not moved into the accumulator (A) until state T2 of the next instruction cycle. That is, A is loaded while the next instruction is being fetched; this overlapping of operations allows for faster processing. 

Remaining Work

- Write code for all the instructions

- Write code for interrupts, I/O

- Write code for defining processor state on startup

- Need to fix XOR reduce

- Look into python intel hex library for testing 

- https://github.com/begoon/asm8080?tab=readme-ov-file




Todo:

- Fix testing framework:
    -
    -

- Finish Instructions 
    - 
    - 



mvi     c, WSTRF
lxi     d, message
call    BDOS
ret
