$include <prelude.sail>

type reg_8bit_num = bits(3)
type reg_16bit_num = bits(2)

type addr_size : Int = 16
type addr = bits(addr_size)

type word_size : Int = 8
type word = bits(word_size)

type dword_size : Int = 16
type dword = bits(dword_size)

/* 8-bit registers */
enum reg_8bit_enum = {
    B, //0
    C, //1
    D, //2
    E, //3
    H, //4
    L, //5
    A, //7
    M  //6
}

/* enum for 16-bit registers */
enum reg_16bit_enum = {
    BC, //0
    DE, //1
    HL, //2
    AF, //3
}

/* Mapping 8-bit register names to their binary representation */
bitfield reg16 : dword = {
    full : 15..0,
    high : 15..8,
    low : 7..0  
} 

register A_reg : word

register BC_reg : reg16
register DE_reg : reg16
register HL_reg : reg16
register AF_reg : reg16

register SP_reg : reg16
register PC_reg : reg16

register DE_addr : addr
register INTE : bits(1)

register input_output : vector(256, bits(8)) = vector_init(256, undefined)
