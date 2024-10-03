$include <prelude.sail>

type addr_size : Int = 16
type addr = bits(addr_size)

type word_size : Int = 8
type word = bits(word_size)

type dword_size : Int = 16
type dword = bits(dword_size)

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

/* enum for register pair names */
enum reg16_enum = {
    BC,
    DE,
    HL
}

/* registers */
bitfield dreg : dword = {
    lower: 7 .. 0,
    higher: 15 .. 8
}

/* 16-bit registers */
register PC : dword
register SP : dword

/* 8-bit registers */
register A_reg : word
register B_reg : word
register C_reg : word
register D_reg : word
register E_reg : word
register H_reg : word
register L_reg : word

/* 16-bit registers */
register BC_reg : dword
register DE_reg : dword
register HL_reg : dword


