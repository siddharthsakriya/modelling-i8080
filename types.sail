type addr_size : Int = 16
type addr = bits(addr_size)

type byte_size : Int = 8
type byte = bits(byte_size)

type dword_size : Int = 16
type dword = bits(dword_size)

/* registers */
bitfield dreg : dword = {
    lower: 7 .. 0,
    higher: 15 .. 8
}

register PC : dword
register SP : dword

register A : byte
register B : byte
register C : byte
register D : byte
register E : byte
register H : byte
register L : byte

register BC : dword
register DE : dword
register HL : dword


