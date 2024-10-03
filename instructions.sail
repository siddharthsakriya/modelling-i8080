default Order dec
$include <prelude.sail>
$include "types.sail"

/* types for register names */
type regname_singles = bits(3)
type regname_pairs = bits(2)

/* Mapping of register names to their binary representation */
mapping reg8_num : reg8_enum <-> regname_singles = {
    A <-> 0b000,
    B <-> 0b001,
    C <-> 0b010,
    D <-> 0b011,
    E <-> 0b100,
    H <-> 0b110,
    L <-> 0b111
}

/* Mapping of register pair names to their binary representation */
mapping reg16_num : reg16_enum <-> regname_pairs = {
    BC <-> 0b00,
    DE <-> 0b01,
    HL <-> 0b10
}

/* Mapping of bit values to their string representation */
mapping reg8_to_string : reg8_enum <-> string = {
    A <-> "A",
    B <-> "B",
    C <-> "C",
    D <-> "D",
    E <-> "E",
    H <-> "H",
    L <-> "L"
}

/* Mapping of bit values to their string representation */
mapping reg16_to_string : reg16_enum <-> string = {
    BC <-> "BC",
    DE <-> "DE",
    HL <-> "HL"
}

/* read_reg8 function */
val read_reg8 : regname_singles -> word 
function read_reg8(r) = {
    match r {
        0b000 => A_reg,
        0b001 => B_reg,
        0b010 => C_reg,
        0b011 => D_reg,
        0b100 => E_reg,
        0b110 => H_reg,
        0b111 => L_reg
    }
}

/* write_reg8 function */
val write_reg8 : (regname_singles, word) -> unit
function write_reg8(r, w) = {
    match r {
        0b000 => A_reg = w,
        0b001 => B_reg = w,
        0b010 => C_reg = w,
        0b011 => D_reg = w,
        0b100 => E_reg = w,
        0b110 => H_reg = w,
        0b111 => L_reg = w
    }
}


function main() : unit -> unit = {
    write_reg8(0b000, 0b00000000);

    print_bits("the bits are: ", read_reg8(0b000));

}