default Order dec
$include <prelude.sail>
$include "prelude.sail"

/* types for register names */
type regname_singles = bits(3);
type regname_pairs = bits(2);

/* enum for register names */
enum reg8_enum = {
    A,
    B,
    C,
    D,
    E,
    H,
    L
}

/* Mapping of register names to their binary representation */
mapping reg8_name : reg8_enum <-> regname_singles = {
    A <-> 0b000,
    B <-> 0b001,
    C <-> 0b010,
    D <-> 0b011,
    E <-> 0b100,
    H <-> 0b110,
    L <-> 0b111
};

/* enum for register pair names */
enum reg16_enum = {
    BC,
    DE,
    HL
}

/* Mapping of register pair names to their binary representation */
mapping reg16_name : reg16_enum <-> regname_pairs = {
    BC <-> 0b00,
    DE <-> 0b01,
    HL <-> 0b10
};

