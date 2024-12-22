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
    AF <-> 0b11
}


/* read_reg16 function */
val read_reg16 : reg_16bit_num -> dword
function read_reg16(r) = {
    match r {
        0b00 => BC_reg[full], 
        0b01 => DE_reg[full],
        0b10 => HL_reg[full],
        0b11 => AF_reg[full]
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
        0b110 => read_mem(read_reg16(0b10)),
        0b111 => AF_reg[high]
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
        0b110 => write_mem(read_reg16(0b10), v),
        0b111 => AF_reg[high] = v
    }
}

/* string mappings for registers to asssist with printing */
mapping reg8_str_map : reg_8bit_enum <-> string = {
    B <-> "B",
    C <-> "C",
    D <-> "D",
    E <-> "E",
    H <-> "H",
    L <-> "L",
    M <-> "M",
    A <-> "A"
}

mapping reg16_str_map : reg_16bit_enum <-> string = {
    BC <-> "BC",
    DE <-> "DE",
    HL <-> "HL",
    AF <-> "AF"
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
union clause ast = STAX : (bits(1))
union clause ast = LDAX : (bits(1))
union clause ast = ADD : (reg_8bit_num)
union clause ast = ADC : (reg_8bit_num)
union clause ast = SUB : (reg_8bit_num)
union clause ast = SBB : (reg_8bit_num)
union clause ast = ANA : (reg_8bit_num)
union clause ast = XRA : (reg_8bit_num)
union clause ast = ORA : (reg_8bit_num)
union clause ast = CMP : (reg_8bit_num)
union clause ast = RLC : (unit)
union clause ast = RRC : (unit)
union clause ast = RAL : (unit)
union clause ast = RAR : (unit)
union clause ast = PUSH : (reg_16bit_num)
union clause ast = POP : (reg_16bit_num)
union clause ast = DAD : (reg_16bit_num)
union clause ast = INX : (reg_16bit_num)
union clause ast = DCX : (reg_16bit_num)
union clause ast = XCHG : (unit)
union clause ast = XTHL : (unit)
union clause ast = SPHL : (unit)
union clause ast = LXI : (reg_16bit_num, bits(8), bits(8))
union clause ast = MVI : (reg_8bit_num, bits(8))
union clause ast = ADI : (bits(8))
union clause ast = ACI : (bits(8))
union clause ast = SUI : (bits(8))
union clause ast = SBI : (bits(8))
union clause ast = ANI : (bits(8))
union clause ast = XRI : (bits(8))
union clause ast = ORI : (bits(8))
union clause ast = CPI : (bits(8))
union clause ast = STA : (bits(8), bits(8))
union clause ast = LDA : (bits(8), bits(8))
union clause ast = SHLD : (bits(8), bits(8))
union clause ast = LHLD : (bits(8), bits(8))
union clause ast = PCHL : (unit)
union clause ast = JMP : (bits(8), bits(8))
union clause ast = JC : (bits(8), bits(8))
union clause ast = JNC : (bits(8), bits(8))
union clause ast = JZ : (bits(8), bits(8))
union clause ast = JNZ : (bits(8), bits(8))
union clause ast = JM : (bits(8), bits(8))
union clause ast = JP : (bits(8), bits(8))
union clause ast = JPE : (bits(8), bits(8))
union clause ast = JPO : (bits(8), bits(8))
union clause ast = CALL : (bits(8), bits(8))
union clause ast = CC : (bits(8), bits(8))
union clause ast = CNC : (bits(8), bits(8))
union clause ast = CZ : (bits(8), bits(8))
union clause ast = CNZ : (bits(8), bits(8))
union clause ast = CM : (bits(8), bits(8))
union clause ast = CP : (bits(8), bits(8))
union clause ast = CPE : (bits(8), bits(8))
union clause ast = CPO : (bits(8), bits(8))
union clause ast = RET : (unit)
union clause ast = RC : (unit)
union clause ast = RNC : (unit)
union clause ast = RZ : (unit)
union clause ast = RNZ : (unit)
union clause ast = RM : (unit)
union clause ast = RP : (unit)
union clause ast = RPE : (unit)
union clause ast = RPO : (unit)
union clause ast = RST : (bits(3))
union clause ast = EI : (bits(1))
union clause ast = DI : (unit)
union clause ast = IN : (bits(8))
union clause ast = OUT: (bits(8))
union clause ast = HLT : (unit)

union clause ast = NOTFOUND8 : (bits(8))
union clause ast = NOTFOUND16 : (bits(16))
union clause ast = NOTFOUND24 : (bits(24))

type instruction8 = bits(8)
type instruction16 = bits(16)
type instruction24 = bits(24)

/* decode8 function: decodes 8-bit instructions */
val decode8 : instruction8 -> ast

function clause decode8 (0b00111111) 
    = CMC()
function clause decode8 (0b00110111) 
    = STC()
function clause decode8 (0b00 @ r:reg_8bit_num @ 0b100) 
    = INR(r)
function clause decode8 (0b01110110)
    = HLT()
function clause decode8 (0b00 @ r:reg_8bit_num @ 0b101) 
    = DCR(r)
function clause decode8 (0b00101111)
    = CMA()
function clause decode8 (0b00100111)
    = DAA()
function clause decode8 (0b00000000)
    = NOP()
function clause decode8 (0b01 @ dst:reg_8bit_num @ src:reg_8bit_num) 
    = MOV(dst, src)
function clause decode8 (0b000 @ reg_pair: bits(1) @ 0b0010)
    = STAX(reg_pair)
function clause decode8 (0b000 @ reg_pair: bits(1) @ 0b1010)
    = LDAX(reg_pair)
function clause decode8 (0b10000 @ r:reg_8bit_num)
    = ADD(r)
function clause decode8 (0b10001 @ r:reg_8bit_num)
    = ADC(r)
function clause decode8 (0b10010 @ r:reg_8bit_num)
    = SUB(r)
function clause decode8 (0b10011 @ r:reg_8bit_num)
    = SBB(r)
function clause decode8 (0b10100 @ r:reg_8bit_num)
    = ANA(r)
function clause decode8 (0b10101 @ r:reg_8bit_num)
    = XRA(r)
function clause decode8 (0b10110 @ r:reg_8bit_num)
    = ORA(r)
function clause decode8 (0b10111 @ r:reg_8bit_num)
    = CMP(r)
function clause decode8 (0b00000111) 
    = RLC()
function clause decode8 (0b00001111) 
    = RRC()
function clause decode8 (0b00010111)
    = RAL()
function clause decode8 (0b00011111)
    = RAR()
function clause decode8 (0b11001001)    
    = RET()
function clause decode8 (this: bits(8))
    = NOTFOUND8(this)
    
/* decode16 function: decodes 16-bit instructions */
val decode16 : bits(16) -> ast
function clause decode16 (0b00 @ r: reg_8bit_num @ 0b110 @ data: bits(8))
    = MVI(r, data)
function clause decode16(this: bits(16))
    = NOTFOUND16(this)


/* decode24 function: decodes 24-bit instructions */
val decode24 : bits(24) -> ast
function clause decode24(0b00 @ r: reg_16bit_num @ 0b0001 @ low_data: bits(8) @ high_data: bits(8))
    = LXI(r, low_data, high_data)
function clause decode24(0b11001101 @ low_data: bits(8) @ high_data: bits(8)) 
    = CALL(low_data, high_data)
function clause decode24(this: bits(24))
    = NOTFOUND24(this)

/* execute function */
val execute : ast -> bool
scattered function execute

/* CMC instruction */
function clause execute (CMC()) = {
    var c_flag = read_c_flag();
    c_flag = if c_flag == 0b1 then 0b0 else 0b1;  
    update_c_flag(c_flag);

    print_endline("Instruction completed: CMC");
    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

/* STC instruction */
function clause execute (STC()) = {
    update_c_flag(0b1);

    print_endline("Instruction completed: STC");    
    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

/* INR instruction */
function clause execute (INR(r)) = {
    var v = read_reg8(r);    
    update_a_flag(if v[3..0] == 0b1111 then 0b1 else 0b0); //if lower nibble is 0xf then auxillary flag should be 1 as there is a carry from lower nibble
    v = add_bits(v, 0b00000001);
    write_reg8(r, v);
    update_s_flag(if v[7..7] == 0b1 then 0b1 else 0b0); 
    update_z_flag(if v == 0b00000000 then 0b1 else 0b0); //if result is 0 then zero flag should be 1
    update_p_flag(if xor_reduce(v) == 0b0 then 0b1 else 0b0); //if number of 1s is even then parity flag should be 1
    
    print_endline(concat_str("Instruction completed: INR ", reg8_str_map(reg8_num_map(r))));
    if reg8_str_map(reg8_num_map(r)) == "M" then {
        print_bits("Value at M location: ", read_mem(read_reg16(0b10)));
    };
    
    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 10 else 5);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 5 else 1);

    true
}

/* HLT instruction */
function clause execute (HLT()) = {
    print_endline("Instruction completed: HLT ");
    false
}

// /* DCR instruction */
function clause execute (DCR(r)) = {
    var v = read_reg8(r);
    update_a_flag(if v[3..0] == 0b0000 then 0b1 else 0b0); //set auxilliary carry
    v = sub_bits(v, 0b00000001);
    write_reg8(r, v);
    update_s_flag(if v[7..7] == 0b1 then 0b1 else 0b0); //sign flag should be set whenever the most significant bit is 1
    update_z_flag(if v == 0b00000000 then 0b1 else 0b0); //if result is 0 then zero flag should be 1
    update_p_flag(if xor_reduce(v) == 0b0 then 0b1 else 0b0); //if number of 1s is even then parity flag should be 1

    print_endline(concat_str("Instruction completed: DCR ", reg8_str_map(reg8_num_map(r))));

    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 10 else 5);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 5 else 1);

    true
}

// /* CMA instruction */
function clause execute (CMA()) = {
    var v = A_reg;
    v = xor_vec(v, 0b11111111);
    A_reg = v;

    print_endline("Instruction completed: CMA");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

// /* DAA instruction */ /* STILL TO BE DONE */
// function clause execute (DAA()) = {
//     var v = A_reg;
//     var lower_nibble: bits(4) = v[3..0];
//     var lower_value = signed(lower_nibble);

    // if lower_value > 9 | SFW_reg[A] == 0b1 then {
    //     v = add_bits(v, 0b00000110); //increment accumulator by 6
    // };
//     upper_nibble: bits(4) = v[7..4];
//     var upper_value = signed(upper_nibble);
//     if upper_value > 9 | SFW_reg[C] == 0b1 then {
//         upper_nibble = add_bits(upper_nibble, 0b0110);
//     };

//     true
// }   

// /* NOP instruction */
function clause execute (NOP()) = {
    /*false right no so it doesnt infinite loop in fetch_decode_execute*/
    print_endline("Instruction completed: NOP");
    
    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);
    print_bits("PC Value: ", PC_reg[full]); 
    false
}

// /* MOV instruction */
function clause execute (MOV(dst, src)) = {
    print_endline("MOV executed");
    write_reg8(dst, read_reg8(src));
    true 
}

/* STAX instruction */
function clause execute (STAX(reg_pair)) = {
    if reg_pair == 0b0 then {
        var addr: addr = read_reg16(0b00);
        var v = A_reg;
        write_mem(addr, v);
    } else {
        var addr: addr = read_reg16(0b01);
        var v = A_reg;
        write_mem(addr, v);
    };

    print_endline(concat_str("Instruction completed: STAX ", reg16_str_map(reg16_num_map(sail_zero_extend(reg_pair, 2))))); 

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    true
}

/* LDAX instruction */
function clause execute (LDAX(reg_pair)) = {
    if reg_pair == 0b0 then {
        var addr: addr = read_reg16(0b00);
        A_reg = read_mem(addr);
    } else {
        var addr: addr = read_reg16(0b01);
        A_reg = read_mem(addr);
    };

    print_endline(concat_str("Instruction completed: LDAX ", reg16_str_map(reg16_num_map(sail_zero_extend(reg_pair, 2)))));

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    true
}

/* ADD instruction */
function clause execute (ADD(r)) = {
    var v: word = read_reg8(r);

    //update flag to take boolean
    update_c_flag(if add_bits(sail_zero_extend(A_reg, 9), sail_zero_extend(v, 9))[8..8] == 0b1 then 0b1 else 0b0);
    update_a_flag(if add_bits(sail_zero_extend(A_reg[3..0], 5), sail_zero_extend(v[3..0], 5))[4..4] == 0b1 then 0b1 else 0b0); //if there is a carry from the 4th bit then auxillary flag should be 1
    A_reg = add_bits(A_reg, v);
    update_p_flag(if xor_reduce(A_reg) == 0b0 then 0b1 else 0b0); //if number of 1s is even then parity flag should be 1
    update_s_flag(if A_reg[7..7] == 0b1 then 0b1 else 0b0); //sign flag should be set whenever the most significant bit is 1
    update_z_flag(if A_reg == 0b00000000 then 0b1 else 0b0); //if result is 0 then zero flag should be 1
    
    print_endline(concat_str("Instruction completed: ADD ", reg8_str_map(reg8_num_map(r))));
    
    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);

    true
}

// /* ADC instruction */ Need to double check the logic of this 
// function clause execute (ADC(r)) = {
//     var v: word = read_reg8(r);
//     SFW_reg[C] = if add_bits(sail_zero_extend(A_reg, 9), add_bits(sail_zero_extend(v, 9), sail_zero_extend(SFW_reg[C], 9)))[8..8] == 0b1 then 0b1 else 0b0;
//     SFW_reg[A] = if add_bits(sail_zero_extend(A_reg[3..0], 5), add_bits(sail_zero_extend(v[3..0], 5), sail_zero_extend(SFW_reg[C], 5)))[4..4] == 0b1 then 0b1 else 0b0;
//     A_reg = add_bits(A_reg, add_bits(v, sail_zero_extend(SFW_reg[C], 8)));
//     SFW_reg[P] = if xor_reduce(A_reg) == 0b0 then 0b1 else 0b0;
//     SFW_reg[S] = if A_reg[7..7] == 0b1 then 0b1 else 0b0;
//     SFW_reg[Z] = if A_reg == 0b00000000 then 0b1 else 0b0;
    
//     print_endline(concat_str("Instruction completed: ADC ", reg8_str_map(reg8_num_map(r))));
//     true
// }

// /* SUB instruction */
function clause execute (SUB(r)) = {
    var v: word = read_reg8(r);
    update_c_flag(if signed(A_reg) < signed(v) then 0b1 else 0b0);
    update_a_flag(if signed(A_reg[3..0]) < signed(v[3..0]) then 0b1 else 0b0);
    A_reg = sub_bits(A_reg, v);
    update_p_flag(if xor_reduce(A_reg) == 0b0 then 0b1 else 0b0);
    update_s_flag(if A_reg[7..7] == 0b1 then 0b1 else 0b0);
    update_z_flag(if A_reg == 0b00000000 then 0b1 else 0b0);
    
    print_endline(concat_str("Instruction completed: SUB ", reg8_str_map(reg8_num_map(r))));

    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);

    true
}

// /* SBB instruction */ NEED TO DOUBLE CHECK THE LOGIC OF THIS
// function clause execute (SBB(r)) = {
//     var v: word = read_reg8(r);
//     var v_lower_with_carry = add_bits(v[3..0], sail_zero_extend(SFW_reg[C], 4));
//     SFW_reg[A] = if signed(A_reg[3..0]) < signed(v_lower_with_carry) then 0b1 else 0b0;    
//     v = add_bits(v, sail_zero_extend(SFW_reg[C], 8));
//     SFW_reg[C] = if signed(A_reg) < signed(v) then 0b1 else 0b0; 
//     A_reg = sub_bits(A_reg, v);
//     SFW_reg[P] = if xor_reduce(A_reg) == 0b0 then 0b1 else 0b0;
//     SFW_reg[S] = if A_reg[7..7] == 0b1 then 0b1 else 0b0;
//     SFW_reg[Z] = if A_reg == 0b00000000 then 0b1 else 0b0;

//     print_endline(concat_str("Instruction completed: SBB ", reg8_str_map(reg8_num_map(r))));
//     true
// }

/* ANA instruction */
function clause execute (ANA(r)) = {
    var v: word = read_reg8(r);
    A_reg = and_vec(A_reg, v);
    update_c_flag(0b0);
    update_p_flag(if xor_reduce(A_reg) == 0b0 then 0b1 else 0b0);
    update_s_flag(if A_reg[7..7] == 0b1 then 0b1 else 0b0);
    update_z_flag(if A_reg == 0b00000000 then 0b1 else 0b0);

    print_endline(concat_str("Instruction completed: ANA ", reg8_str_map(reg8_num_map(r))));
    
    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);

    true
}

// /* XRA instruction */
function clause execute (XRA(r)) = {
    var v: word = read_reg8(r);
    A_reg = xor_vec(A_reg, v);
    update_c_flag(0b0);
    update_a_flag(0b0);
    update_p_flag(if xor_reduce(A_reg) == 0b0 then 0b1 else 0b0);
    update_s_flag(if A_reg[7..7] == 0b1 then 0b1 else 0b0);
    update_z_flag(if A_reg == 0b00000000 then 0b1 else 0b0);

    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);

    print_endline(concat_str("Instruction completed: XRA ", reg8_str_map(reg8_num_map(r))));
    true
}

// /* ORA instruction */
function clause execute (ORA(r)) = {
    var v: word = read_reg8(r);
    A_reg = or_vec(A_reg, v);
    update_c_flag(0b0);
    update_p_flag(if xor_reduce(A_reg) == 0b0 then 0b1 else 0b0);
    update_s_flag(if A_reg[7..7] == 0b1 then 0b1 else 0b0);
    update_z_flag(if A_reg == 0b00000000 then 0b1 else 0b0);

    print_endline(concat_str("Instruction completed: ORA ", reg8_str_map(reg8_num_map(r))));

    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);
    
    true
}

// /* CMP instruction */
function clause execute (CMP(r)) = {
    var v: word = read_reg8(r);
    update_c_flag(if signed(A_reg) < signed(v) then 0b1 else 0b0);
    update_a_flag(if signed(A_reg[3..0]) < signed(v[3..0]) then 0b1 else 0b0);
    var res = sub_bits(A_reg, v);
    update_p_flag(if xor_reduce(res) == 0b0 then 0b1 else 0b0);
    update_s_flag(if res[7..7] == 0b1 then 0b1 else 0b0);
    update_z_flag(if res == 0b00000000 then 0b1 else 0b0);

    print_endline(concat_str("Instruction completed: CMP ", reg8_str_map(reg8_num_map(r))));    

    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);
    
    true
}

// /* RLC instruction */
function clause execute (RLC()) = {
    var v = A_reg;
    var msb = v[7..7];
    v = shiftl(v, 1);
    v[0..0] = msb;
    A_reg = v;
    update_c_flag(msb);

    print_endline("Instruction completed: RLC");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

// /* RRC instruction */
function clause execute(RRC()) = {
    var v = A_reg;
    var lsb = v[0..0];
    v = shiftr(v, 1);
    v[7..7] = lsb;
    A_reg = v;
    update_c_flag(lsb);

    print_endline("Instruction completed: RRC");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

// /* RAL instruction */
function clause execute(RAL()) = {
    var v = A_reg;
    var msb = v[7..7];
    v = shiftl(v, 1);
    v[0..0] = read_c_flag();
    A_reg = v;
    update_c_flag(msb);

    print_endline("Instruction completed: RAL");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

// /* RAR instruction */
function clause execute(RAR()) = {
    var v = A_reg;
    var lsb = v[0..0];
    v = shiftr(v, 1);
    v[7..7] = read_c_flag();
    A_reg = v;
    update_c_flag(lsb);

    print_endline("Instruction completed: RAR");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

function clause execute(CALL(low_data, high_data)) = {
    push_stack(PC_reg[full]);
    print_endline("CALL Executed");
    PC_reg[full] = high_data @ low_data;
    true
}

function clause execute(MVI(r, data)) = {
    write_reg8(r, data);
    print_endline("MVI Executed");
    true
}

function clause execute(LXI(r, low_data, high_data)) = {
    write_reg16(r, high_data @ low_data);
    print_endline("LXI Executed");
    true
}

function clause execute(NOTFOUND8(this)) = {
    print_endline("not found, try 16");
    let next_byte: bitvector(8) = read_mem(PC_reg[full]);
    increment_pc();
    execute(decode16(this @ next_byte));
}

function clause execute(NOTFOUND16(this)) = {
    print_endline("not found, try 24");
    let next_byte: bitvector(8) = read_mem(PC_reg[full]);
    increment_pc();
    execute(decode24(this @ next_byte))
}

function clause execute(RET()) = {
    print_endline("RET executed");
    PC_reg[full] = pop_stack();
    true
}

function clause execute(NOTFOUND24(this)) = {
    print_endline("invalid instruction");
    print_bits("this: ", this);
    false
}

