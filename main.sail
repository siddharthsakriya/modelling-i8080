default Order dec
$include <prelude.sail>
$include "./utility/timing.sail"
$include "./mem&reg/types.sail"
$include "./mem&reg/memory.sail"
$include "./utility/utils.sail"
$include "./decoder/decode.sail"
$include "./decoder/instructions.sail"
$include "program.sail"
// /* Refer to page 13 of manual on deramp for startup, SP seems to be unspecified*/
// /* loads program into mem */
//undefined keyword for SP


function bdos_9(value) : bool -> bool = {
    var looped = if (read_mem(DE_addr) == 0x24) then { false } else { print_bits("value: ", read_mem(DE_addr)); DE_addr = DE_addr + 1; true;}; 
    looped
}

function intercept_BDOS() : unit -> unit = {
    if (read_reg8(0b001) == 0x09) then {
        DE_addr = read_reg16(0b01);
        while (bdos_9(true)) do ();
    };

    if (read_reg8(0b001) == 0x02) then {
        if (read_reg8(0b011) != 0x00) then {
            print_bits("value: ", read_reg8(0b011));
        };
    };
}

function startup_cpm() : unit -> unit = {
    PC_reg[full] = 0x0100;
    SP_reg[full] = 0x0000;
}

function startup_test() : unit -> unit = {
    PC_reg[full] = 0x0000;
}

//call a c function for interrupt handling
function fetch_decode_execute(last_instruction) : bool -> bool = {
    var instruction = read_mem(PC_reg[full]);
    increment_pc();

    
    if (fdiv_int(clock_cycle_count, 10000000) == 1) then {
        print_int("cycles: ", clock_cycle_count);
    };

    if (fdiv_int(clock_cycle_count, 100000000) == 1) then {
        print_int("cycles: ", clock_cycle_count);
    };

    if (fdiv_int(clock_cycle_count, 100000000) == 10) then {
        print_int("cycles: ", clock_cycle_count);
    };

    if (fdiv_int(clock_cycle_count, 100000000) == 30) then {
        print_int("cycles: ", clock_cycle_count);
    };

    if (fdiv_int(clock_cycle_count, 100000000) == 50) then {
        print_int("cycles: ", clock_cycle_count);
    };

    if (fdiv_int(clock_cycle_count, 100000000) == 80) then {
        print_int("cycles: ", clock_cycle_count);
    };

    if (fdiv_int(clock_cycle_count, 100000000) == 100) then {
        print_int("cycles: ", clock_cycle_count);
    };

    if (fdiv_int(clock_cycle_count, 100000000) == 130) then {
        print_int("cycles: ", clock_cycle_count);
    };

    if (fdiv_int(clock_cycle_count, 100000000) == 170) then {
        print_int("cycles: ", clock_cycle_count);
    };

    if (fdiv_int(clock_cycle_count, 100000000) == 230) then {
        print_int("cycles: ", clock_cycle_count);
    };

    var decoded = decode8(instruction);

    var loop = execute(decoded);
    if (PC_reg[full] == 0x0005) then {
        intercept_BDOS();
    };
    if( PC_reg[full] == 0x0000) then {
        loop = false;
    };

    loop
}

function main() : unit -> unit = {
    load_program();
    startup_cpm();
    while (fetch_decode_execute(true)) do ();
}