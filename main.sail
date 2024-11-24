default Order dec
$include <prelude.sail>
$include "timing.sail"
$include "types.sail"
$include "utils.sail"
$include "memory.sail"
$include "instructions.sail"
$include "program.sail"


// /* Refer to page 13 of manual on deramp for startup, SP seems to be unspecified*/
// /* loads program into mem */
// function load_program(): unit -> unit = {
    
// }
//undefined keyword for SP

function startup() : unit -> unit = {
    PC_reg[full] = 0x0000;
    load_program();
}

function fetch_decode_execute(last_instruction) : bool -> bool = {
    var instruction = read_mem(PC_reg[full]);
    increment_pc();
    var decoded = decode8(instruction);
    var loop = execute(decoded);
    print_processor_state();
    loop
}

function main() : unit -> unit = {

    startup();
    while (fetch_decode_execute(true)) do ();

}
