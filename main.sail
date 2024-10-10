default Order dec
$include <prelude.sail>
$include "types.sail"
$include "utils.sail"
$include "memory.sail"
$include "instructions.sail"


function main() : unit -> unit = {
    // write_reg8(0b000, 0b00011110);
    // let res = execute(decode8(0b00000101));
    // let res = execute(decode8(0b00000101));
    // print_int("B register after first cycle: ", signed(read_reg8(0b000)));
    // print_bits("flag reg before first cycle: ", SFW_reg[all]);
    // let res = execute(decode8(0b00000100));
    // print_bits("flag reg after first cycle: ", SFW_reg[all][7..7]);
    // print_int("this is the int version of 0x00: ", signed(0x00));
    // print_bits("memory: ", read_mem(0x0000));
    // SFW_reg[C] = 0b1;
    // A_reg = 0b00000100;
    // write_reg8(0b000, 0b00000010);
    // let res = execute(decode8(0b10011000));
    // print_bits("B register after first cycle: ", A_reg);
    // A_reg = 0b11111100;
    // write_reg8(0b000, 0b00001111);
    // let res = execute(decode8(0b10100000));
    // print_bits("A register after first cycle: ", A_reg);
    // write_reg8(0b000, 0b11111111);
    // write_reg8(0b111, 0b11111111);
    // let res = execute(decode8(0b10000000));
    // print_bits("flag register ", SFW_reg[all]);
    // write_reg8(0b000, 0b00000011);
    // write_reg8(0b111, 0b00000010);
    // let res = execute(decode8(0b10010000));
    // print_bits("flag register ", SFW_reg[all]);
    // print_bits("A register after first cycle: ", A_reg);
    // write_reg8(0b111, 0b11110010);
    // let res = execute(decode8(0b00001111));
    // print_bits("A register after first cycle: ", A_reg);
    // print_bits("flag register ", SFW_reg[all]);
    print_bits("memory: ", 0b00000000);
}