default Order dec
$include <prelude.sail>
$include "types.sail"
$include "utils.sail"
$include "memory.sail"

/* types for register names */
type reg_8bit_num = bits(3)
type reg_16bit_num = bits(2)

/* Mapping 8-bit register names to their binary representation */
mapping reg8_num_map : reg_8bit_enum <-> reg_8bit_num = {
    B <-> 0b000,
    C <-> 0b001,
    D <-> 0b010,
    E <-> 0b011,
    H <-> 0b100,
    L <-> 0b101,
    M <-> 0b110,
    A <-> 0b111
}

/* Mapping 16-bit register names to their binary representation */
mapping reg16_num_map : reg_16bit_enum <-> reg_16bit_num = {
    BC <-> 0b00,
    DE <-> 0b01,
    HL <-> 0b10,
    SP <-> 0b11
}

/* read_reg8 function */
val read_reg8 : reg_8bit_num -> word 
function read_reg8(r) = {
    match r {
        0b000 => BC_reg[high],
        0b001 => BC_reg[low],
        0b010 => DE_reg[high],
        0b011 => DE_reg[low],
        0b100 => HL_reg[high],
        0b101 => HL_reg[low],
        0b111 => A_reg
    }
}


/* write_reg8 function */
val write_reg8 : (reg_8bit_num, word) -> unit
function write_reg8(r, v) = {
    match r {
        0b000 => BC_reg[high] = v,
        0b001 => BC_reg[low] = v,
        0b010 => DE_reg[high] = v,
        0b011 => DE_reg[low] = v,
        0b100 => HL_reg[high] = v,
        0b101 => HL_reg[low] = v,
        0b111 => A_reg = v
    }
}

/* read_reg16 function */
val read_reg16 : reg_16bit_num -> dword
function read_reg16(r) = {
    match r {
        0b00 => BC_reg[full], 
        0b01 => DE_reg[full],
        0b10 => HL_reg[full],
        0b11 => SP_reg[full]
    }
}

/* write_reg16 function */
val write_reg16 : (reg_16bit_num, dword) -> unit
function write_reg16(r, v) = {
    match r {
        0b00 => BC_reg[full] = v,
        0b01 => DE_reg[full] = v,
        0b10 => HL_reg[full] = v,
        0b11 => SP_reg[full] = v
    }
}

scattered union ast 

union clause ast = CMC : (unit)
union clause ast = STC : (unit)
union clause ast = INR : (reg_8bit_num)
union clause ast = DCR : (reg_8bit_num)
union clause ast = CMA : (unit)
union clause ast = DAA : (unit)
union clause ast = NOP : (unit)
union clause ast = MOV : (reg_8bit_num, reg_8bit_num) 

type instruction8 = bits(8)
type instruction16 = bits(16)

/* decode8 function: decodes 8-bit instructions */
val decode8 : instruction8 -> ast
/* CMC instruction */
function clause decode8 (0b00111111) 
    = CMC()
/* STC instruction */
function clause decode8 (0b00110111) 
    = STC()
/* INR instruction */
function clause decode8 (0b00 @ r:reg_8bit_num @ 0b100) 
    = INR(r)
/* DCR instruction */
function clause decode8 (0b00 @ r:reg_8bit_num @ 0b101) 
    = DCR(r)
/* CMA instruction */
function clause decode8 (0b00101111)
    = CMA()
/* DAA instruction */
function clause decode8 (0b00100111)
    = DAA()
/* NOP instruction */
function clause decode8 (0b00000000)
    = NOP()
/* MOV instruction */
function clause decode8 (0b01 @ dst:reg_8bit_num @ src:reg_8bit_num) 
    = MOV(dst, src)

/* execute function */
val execute : ast -> bool
scattered function execute

/* CMC instruction */
function clause execute (CMC()) = {
    SFW_reg[C] = if SFW_reg[C] == 0b1 then 0b0 else 0b1;  
    true
}

/* STC instruction */
function clause execute (STC()) = {
    SFW_reg[C] = 0b1;
    true
}

/* INR instruction */
function clause execute (INR(r)) = {
    var v = read_reg8(r);    
    SFW_reg[A] = if v[3..0] == 0b1111 then 0b1 else 0b0; //if lower nibble is 0xf then auxillary flag should be 1 as there is a carry from lower nibble
    v = add_bits(v, 0b00000001);
    write_reg8(r, v);
    SFW_reg[S] = if v[7..7] == 0b1 then 0b1 else 0b0; //if D contains 0x80 then we need sign flag to be 1 
    SFW_reg[Z] = if v == 0b00000000 then 0b1 else 0b0; //if result is 0 then zero flag should be 1
    SFW_reg[P] = if xor_reduce(v) == 0b0 then 0b1 else 0b0; //if number of 1s in D is even then parity flag should be 1
    true
}

/* DCR instruction */
function clause execute (DCR(r)) = {
    var v = read_reg8(r);
    v_lsbs: bits(4)  = v[3..0];
    SFW_reg[A] = if v_lsbs == 0b0000 then 0b1 else 0b0; //set auxilliary carry 
    v = sub_bits(v, 0b00000001);
    write_reg8(r, v);
    SFW_reg[S] = if v[7..7] == 0b1 then 0b1 else 0b0; //sign flag should be set whenever the most significant bit is 1
    SFW_reg[Z] = if v == 0b00000000 then 0b1 else 0b0; //if result is 0 then zero flag should be 1
    SFW_reg[P] = if xor_reduce(v) == 0b0 then 0b1 else 0b0; //if number of 1s in D is even then parity flag should be 1
    true
}

/* CMA instruction */
function clause execute (CMA()) = {
    var v = A_reg;
    v = xor_vec(v, 0b11111111);
    A_reg = v;
    true
}

/* DAA instruction */
function clause execute (DAA()) = {
    var v = A_reg;
    var lower_nibble: bits(4) = v[3..0];
    var lower_value = signed(lower_nibble);

    if lower_value > 9 | SFW_reg[A] == 0b1 then {
        v = add_bits(v, 0b00000110); //increment accumulator by 6
    };
    upper_nibble: bits(4) = v[7..4];
    var upper_value = signed(upper_nibble);
    if upper_value > 9 | SFW_reg[C] == 0b1 then {
        upper_nibble = add_bits(upper_nibble, 0b0110);
    };
    true
}   

/* NOP instruction */
function clause execute (NOP()) = {
    true
}

/* MOV instruction */
function clause execute (MOV(dst, src)) = {
    write_reg8(dst, read_reg8(src));
    true
}


function main() : unit -> unit = {
    write_reg8(0b000, 0b00011110);
    let res = execute(decode8(0b00000101));
    let res = execute(decode8(0b00000101));
    print_int("B register after first cycle: ", signed(read_reg8(0b000)));
    // print_bits("flag reg before first cycle: ", SFW_reg[all]);
    // let res = execute(decode8(0b00000100));
    // print_bits("flag reg after first cycle: ", SFW_reg[all][7..7]);
    print_int("this is the int version of 0x00: ", signed(0x00));
    print_bits("memory: ", read_mem(0x0000));
    
}

