default Order dec
$include <prelude.sail>
$include "timing.sail"
$include "types.sail"
$include "memory.sail"
$include "utils.sail"
$include "instructions.sail"
$include "program.sail"


// /* Refer to page 13 of manual on deramp for startup, SP seems to be unspecified*/
// /* loads program into mem */
// function load_program(): unit -> unit = {
    
// }
//undefined keyword for SP

// function intercept_BDOS() : unit -> unit = {
//     if (read_reg8(0b001) == 0x09) then {
//         var start_addr = read_reg16(0b01);
//         while (read_mem(start_addr) != 0x24) do (
//             print_bits(read_mem(start_addr));
//             start_addr = add_bits(start_addr, 0x0001);
//         );
//     };
// }

// function read(prev, address) : bool, bits(16) -> unit = {
//     true
// }

function startup() : unit -> unit = {
    PC_reg[full] = 0x0100;
    SP_reg[full] = 0xFFEE;

}

function fetch_decode_execute(last_instruction) : bool -> bool = {
    var instruction = read_mem(PC_reg[full]);
    increment_pc();
    var decoded = decode8(instruction);
    var loop = execute(decoded);
    // print_processor_state();

    

    loop
}

function main() : unit -> unit = {

    startup();
    while (fetch_decode_execute(true)) do ();

}
