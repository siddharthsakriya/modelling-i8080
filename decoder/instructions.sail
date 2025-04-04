
/* execute function */
val execute : ast -> bool
scattered function execute

/* STC instruction */
function clause execute (STC()) = {
    update_c_flag(0b1);

    // print_endline("Instruction completed: STC");    
    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

/* CMC instruction */
function clause execute (CMC()) = {
    var c_flag = read_c_flag();
    c_flag = xor_vec(c_flag, 0b1);
    update_c_flag(c_flag);

    // print_endline("Instruction completed: CMC");
    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

/* INR instruction */
function clause execute (INR(r)) = {
    var v = read_reg8(r);    
    //if lower nibble is 0b1111 it means when we add one theres going to be an auxillary carry
    update_a_flag(bool_to_bit_converter(v[3..0] == 0b1111)); 
    v = add_bits(v, 0x01);
    write_reg8(r, v);
    update_s_flag(bool_to_bit_converter(v[7..7] == 0b1));
    update_z_flag(bool_to_bit_converter(v == 0b00000000)); //if result is 0 then zero flag should be 1
    update_p_flag(bool_to_bit_converter(xor_reduce(v) == 0b0));//if number of 1s is even then parity flag should be 1
    
    // print_endline(concat_str("Instruction completed: INR ", reg8_str_map(reg8_num_map(r))));
    
    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 10 else 5);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 5 else 1);

    true
}

// /* DCR instruction */
function clause execute (DCR(r)) = {
    var v = read_reg8(r);
    update_a_flag(bool_to_bit_converter(v[3..0] != 0b0000));
    v = sub_bits(v, 0b00000001);
    write_reg8(r, v);
    update_s_flag(bool_to_bit_converter(v[7..7] == 0b1)); 
    update_z_flag(bool_to_bit_converter(v == 0b00000000)); 
    update_p_flag(bool_to_bit_converter(xor_reduce(v) == 0b0));

    // print_endline(concat_str("Instruction completed: DCR ", reg8_str_map(reg8_num_map(r))));

    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 10 else 5);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 5 else 1);

    true
}

// /* CMA instruction */
function clause execute (CMA()) = {
    var v = read_reg8(0b111);
    v = xor_vec(v, 0b11111111);
    write_reg8(0b111, v);

    // print_endline("Instruction completed: CMA");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

// /* DAA instruction */
function clause execute (DAA()) = {
    var v : word = read_reg8(0b111);
    var correction : word = 0x00;
    var cy : bits(1) = read_c_flag();

    var msb : bits(4) = v[7..4];
    var lsb : bits(4) = v[3..0];

    if (read_a_flag() == 0b1 | unsigned(lsb) > 9) then {
        correction = add_bits(correction, 0x06);
    };

    if (read_c_flag() == 0b1 | unsigned(msb) > 9 | (unsigned(msb) >= 9 & unsigned(lsb) > 9)) then {
        correction = add_bits(correction, 0x60);
        cy = 0b1;
    };

    write_reg8(0b111, perform_add(v, correction, 0b0));
    update_c_flag(cy);

    // print_endline("Instruction completed: DAA");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}   

// /* NOP instruction */
function clause execute (NOP()) = {
    // print_endline("Instruction completed: NOP");
    
    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);
    true
}

// /* MOV instruction */
function clause execute (MOV(dst, src)) = {
    write_reg8(dst, read_reg8(src));

    // print_endline(concat_str("Instruction completed: MOV ", concat_str(reg8_str_map(reg8_num_map(dst)), concat_str(" ", reg8_str_map(reg8_num_map(src))))));

    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(dst)) == "M" | reg8_str_map(reg8_num_map(src)) == "M" then 7 else 5);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(dst)) == "M" | reg8_str_map(reg8_num_map(src)) == "M" then 2 else 1);

    true 
}

/* STAX instruction */
function clause execute (STAX(reg_pair)) = {
    var addr: addr = read_reg16(0b0 @ reg_pair);
    var v = read_reg8(0b111);
    write_mem(addr, v);

    // print_endline(concat_str("Instruction completed: STAX ", reg16_str_map(reg16_num_map(sail_zero_extend(reg_pair, 2))))); 

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    true
}

/* LDAX instruction */
function clause execute (LDAX(reg_pair)) = {
    write_reg8(0b111, read_mem(read_reg16(0b0 @ reg_pair)));

    // print_endline(concat_str("Instruction completed: LDAX ", reg16_str_map(reg16_num_map(sail_zero_extend(reg_pair, 2)))));

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    true
}

/* ADD instruction */
function clause execute (ADD(r)) = {
    var a: word = read_reg8(0b111);
    var b: word = read_reg8(r);

    result = perform_add(a, b, 0b0);

    write_reg8(0b111, result);
    // print_endline(concat_str("Instruction completed: ADD ", reg8_str_map(reg8_num_map(r))));
    
    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);

    true
}

/* ADC instruction */
function clause execute (ADC(r)) = {
    var v: bits(8) = read_reg8(r);
    var acc: bits(8) = read_reg8(0b111);

    var result: bits(8) = perform_add(acc, v, read_c_flag());
    
    write_reg8(0b111, result);

    // print_endline(concat_str("Instruction completed: ADC ", reg8_str_map(reg8_num_map(r))));
    
    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);

    true
}

// /* SUB instruction
function clause execute (SUB(r)) = {
    
    var a_value = read_reg8(0b111);
    var data = read_reg8(r);

    var res = perform_sub(a_value, data, 0b0);

    write_reg8(0b111, res);

    // print_endline(concat_str("Instruction completed: SUB ", reg8_str_map(reg8_num_map(r))));

    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);

    true
}

// /* SBB instruction 
function clause execute (SBB(r)) = {

    var a_value = read_reg8(0b111); 
    var data = read_reg8(r);
    var carry = read_c_flag(); 

    var result = perform_sub(a_value, data, carry);
    
    write_reg8(0b111, result);

    //print_endline("Instruction completed: SBB");

    if reg8_str_map(reg8_num_map(r)) == "M" then increment_clock_cycle_count(7) else increment_clock_cycle_count(4);
    if reg8_str_map(reg8_num_map(r)) == "M" then increment_machine_cycle_count(2) else increment_machine_cycle_count(1);
    
    true
}

/* ANA instruction */
function clause execute (ANA(r)) = {
    var v: word = read_reg8(r);
    update_a_flag(or_vec(read_reg8(0b111)[3..3], v[3..3]));

    write_reg8(0b111, and_vec(read_reg8(0b111), v));
    
    update_c_flag(0b0);
    update_p_flag(bool_to_bit_converter(xor_reduce(read_reg8(0b111)) == 0b0));
    update_s_flag(bool_to_bit_converter(read_reg8(0b111)[7..7] == 0b1));
    update_z_flag(bool_to_bit_converter(read_reg8(0b111) == 0b00000000));

    // print_endline(concat_str("Instruction completed: ANA ", reg8_str_map(reg8_num_map(r))));
    
    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);

    true
}

// /* XRA instruction */
function clause execute (XRA(r)) = {
    var v: word = read_reg8(r);
    write_reg8(0b111, xor_vec(read_reg8(0b111), v));

    update_c_flag(0b0);
    update_a_flag(0b0);
    update_p_flag(bool_to_bit_converter(xor_reduce(read_reg8(0b111)) == 0b0));
    update_s_flag(bool_to_bit_converter(read_reg8(0b111)[7..7] == 0b1));
    update_z_flag(bool_to_bit_converter(read_reg8(0b111) == 0b00000000));

    // print_endline(concat_str("Instruction completed: XRA ", reg8_str_map(reg8_num_map(r))));

    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);

    true
}

// /* ORA instruction */
function clause execute (ORA(r)) = {
    var v: word = read_reg8(r);
    write_reg8(0b111, or_vec(read_reg8(0b111), v));

    update_c_flag(0b0);
    update_a_flag(0b0);
    update_p_flag(bool_to_bit_converter(xor_reduce(read_reg8(0b111)) == 0b0));
    update_s_flag(bool_to_bit_converter(read_reg8(0b111)[7..7] == 0b1));
    update_z_flag(bool_to_bit_converter(read_reg8(0b111) == 0b00000000));

    // print_endline(concat_str("Instruction completed: ORA ", reg8_str_map(reg8_num_map(r))));

    increment_clock_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 7 else 4);
    increment_machine_cycle_count(if reg8_str_map(reg8_num_map(r)) == "M" then 2 else 1);
    
    true
}

// /* CMP instruction */ 
function clause execute (CMP(r)) = {
    
    var a_value = read_reg8(0b111);
    var data_value = read_reg8(r);
    var data = read_reg8(r);

    var res = perform_sub(a_value, data_value, 0b0);



    // print_endline("Instruction completed: CMP");

    if reg8_str_map(reg8_num_map(r)) == "M" then increment_clock_cycle_count(7) else increment_clock_cycle_count(4);
    if reg8_str_map(reg8_num_map(r)) == "M" then increment_machine_cycle_count(2) else increment_machine_cycle_count(1);    
        
    true
}

// /* RLC instruction */
function clause execute (RLC()) = {
    var v = read_reg8(0b111);
    var msb = v[7..7];
    v = shiftl(v, 1);
    v[0..0] = msb;
    write_reg8(0b111, v);
    update_c_flag(msb);

    // print_endline("Instruction completed: RLC");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

// /* RRC instruction */
function clause execute(RRC()) = {
    var v = read_reg8(0b111);
    var lsb = v[0..0];
    v = shiftr(v, 1);
    v[7..7] = lsb;
    write_reg8(0b111, v);
    update_c_flag(lsb);

    // print_endline("Instruction completed: RRC");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

// /* RAL instruction */
function clause execute(RAL()) = {
    var v = read_reg8(0b111);
    var msb = v[7..7];
    v = shiftl(v, 1);
    v[0..0] = read_c_flag();
    write_reg8(0b111, v);
    update_c_flag(msb);

    // print_endline("Instruction completed: RAL");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

/* RAR instruction */
function clause execute(RAR()) = {
    var v = read_reg8(0b111);
    var lsb = v[0..0];
    v = shiftr(v, 1);
    v[7..7] = read_c_flag();
    write_reg8(0b111, v);
    update_c_flag(lsb);

    // print_endline("Instruction completed: RAR");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

/* PUSH instruction */
function clause execute(PUSH(r)) = {
    var data = read_reg16(r);
    push_stack(data);
    
    // print_endline(concat_str("Instruction completed: PUSH ", reg16_str_map(reg16_num_map(r))));
    increment_clock_cycle_count(11);
    increment_machine_cycle_count(4);

    true
}

/* POP instruction */ 
function clause execute(POP(r)) = {
    var stack_data = pop_stack();
    
    if reg16_str_map(reg16_num_map(r)) == "AF" then {
        stack_data[5..5] = 0b0;
        stack_data[3..3] = 0b0;
        stack_data[1..1] = 0b1;
    };
    
    write_reg16(r, stack_data);
    
    // print_endline(concat_str("Instruction completed: POP ", reg16_str_map(reg16_num_map(r))));
    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* DAD instruction */
function clause execute(DAD(r)) = {
    var v = 0b0 @ read_reg16_sp(r);
    var hl = 0b0 @ read_reg16_sp(0b10);
    var res = add_bits(hl, v);

    write_reg16_sp(0b10, res[15..0]);
    update_c_flag(res[16..16]);

    // print_endline(concat_str("Instruction completed: DAD ", reg16_str_map(reg16_num_map(r))));

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* INX instruction */
function clause execute(INX(r)) = {
    var v = read_reg16_sp(r);
    v = add_bits(v, 0x0001);
    write_reg16_sp(r, v);

    // print_endline(concat_str("Instruction completed: INX ", reg16_str_map(reg16_num_map(r))));
    increment_clock_cycle_count(5);
    increment_machine_cycle_count(1);

    true
}

/* DCX instruction */
function clause execute(DCX(r)) = {
    var v = read_reg16_sp(r);
    v = sub_bits(v, 0x0001);
    write_reg16_sp(r, v);

    // print_endline(concat_str("Instruction completed: DCX ", reg16_str_map(reg16_num_map(r))));
    increment_clock_cycle_count(5);
    increment_machine_cycle_count(1);

    true
}

/* XCHG instruction */
function clause execute(XCHG()) = {
    var de = read_reg16_sp(0b01);
    var hl = read_reg16_sp(0b10);
    
    write_reg16_sp(0b01, hl);
    write_reg16_sp(0b10, de);

    // print_endline("Instruction completed: XCHG");
    increment_clock_cycle_count(5);
    increment_machine_cycle_count(1);

    true
}

/* XTHL instruction */
function clause execute(XTHL()) = {
    var sp = read_reg16_sp(0b11);
    var hl = read_reg16_sp(0b10);
    
    
    var h = read_mem(sp);
    var l = read_mem(sp + 0x0001);

    write_mem(sp, hl[7..0]);
    write_mem(sp + 0x0001, hl[15..8]);

    write_reg16_sp(0b10, l @ h);

    // print_endline("Instruction completed: XTHL");
    increment_clock_cycle_count(18);
    increment_machine_cycle_count(5);

    true
}

/* SPHL instruction */
function clause execute(SPHL()) = {
    var hl = read_reg16_sp(0b10);
    write_reg16_sp(0b11, hl);

    // print_endline("Instruction completed: SPHL");
    increment_clock_cycle_count(5);
    increment_machine_cycle_count(1);

    true
}

/* LXI instruction */
function clause execute(LXI(r, low_data, high_data)) = {
    write_reg16_sp(r, high_data @ low_data);
    // print_endline(concat_str("Instruction completed: LXI ", reg16_str_map(reg16_num_map(r))));

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* MVI instruction */
function clause execute(MVI(r, data)) = {
    write_reg8(r, data);
    // print_endline(concat_str("Instruction completed: MVI ", reg8_str_map(reg8_num_map(r))));

    if reg8_str_map(reg8_num_map(r)) == "M" then increment_clock_cycle_count(10) else increment_clock_cycle_count(7);

    true
}

/* ADI instruction */
function clause execute(ADI(data)) = {
    var v = read_reg8(0b111);
    var result = perform_add(v, data, 0b0);
    write_reg8(0b111, result);

    // print_endline("Instruction completed: ADI");

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    true
}

/* ACI instruction */
function clause execute(ACI(data)) = {
    var acc: bits(8) = read_reg8(0b111);
    var result: bits(8) = perform_add(acc, data, read_c_flag());

    write_reg8(0b111, result);
    // print_endline("Instruction completed: ACI");

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    true
}

/* SUI instruction */
function clause execute(SUI(data)) = {
    
    var a_value = read_reg8(0b111); // Read accumulator (A)
    var res = perform_sub(a_value, data, 0b0); // Perform subtraction

    write_reg8(0b111, res);

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    // print_endline("Instruction completed: SUI");

    true
}

/* SBI instruction */
function clause execute(SBI(data)) = {
    var a_value = read_reg8(0b111); 
    var carry = read_c_flag(); 
    

    var result = perform_sub(a_value, data, carry);

    write_reg8(0b111, result);

    // print_endline("Instruction completed: SBI");

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    true
}


/* ANI instruction */
function clause execute(ANI(data)) = {
    var v: word = data;
    update_a_flag(or_vec(read_reg8(0b111)[3..3], v[3..3]));
    write_reg8(0b111, and_vec(read_reg8(0b111), v));
    update_c_flag(0b0);
    update_p_flag(bool_to_bit_converter(xor_reduce(read_reg8(0b111)) == 0b0));
    update_s_flag(bool_to_bit_converter(read_reg8(0b111)[7..7] == 0b1));
    update_z_flag(bool_to_bit_converter(read_reg8(0b111) == 0b00000000));

    // print_endline("Instruction completed: ANI");

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    true
}

/* XRI instruction */
function clause execute(XRI(data)) = {
    var v: word = data;
    write_reg8(0b111, xor_vec(read_reg8(0b111), v));
    update_c_flag(0b0);
    update_a_flag(0b0);
    update_p_flag(bool_to_bit_converter(xor_reduce(read_reg8(0b111)) == 0b0));
    update_s_flag(bool_to_bit_converter(read_reg8(0b111)[7..7] == 0b1));
    update_z_flag(bool_to_bit_converter(read_reg8(0b111) == 0b00000000));

    // print_endline("Instruction completed: XRI");

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    true
}

/* ORI instruction */
function clause execute(ORI(data)) = {
    var v: word = data;
    write_reg8(0b111, or_vec(read_reg8(0b111), v));
    update_c_flag(0b0);
    update_a_flag(0b0);
    update_p_flag(bool_to_bit_converter(xor_reduce(read_reg8(0b111)) == 0b0));
    update_s_flag(bool_to_bit_converter(read_reg8(0b111)[7..7] == 0b1));
    update_z_flag(bool_to_bit_converter(read_reg8(0b111) == 0b00000000));

    // print_endline("Instruction completed: ORI");

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    true
}

/* CPI instruction */
function clause execute(CPI(data)) = {

    var result = perform_sub(read_reg8(0b111), data, 0b0);
    
    // print_endline("Instruction completed: CPI");

    increment_clock_cycle_count(7);
    increment_machine_cycle_count(2);

    true
}

/* STA instruction */
function clause execute(STA(low_data, high_data)) = {
    var addr: addr = high_data @ low_data;
    write_mem(addr, read_reg8(0b111));

    // print_endline("Instruction completed: STA");

    increment_clock_cycle_count(13);
    increment_machine_cycle_count(4);

    true
}

/* LDA instruction */
function clause execute(LDA(low_data, high_data)) = {
    var addr: addr = high_data @ low_data;
    write_reg8(0b111, read_mem(addr));

    // print_endline("Instruction completed: LDA");

    increment_clock_cycle_count(13);
    increment_machine_cycle_count(4);

    true
}

/* SHLD instruction */
function clause execute(SHLD(low_data, high_data)) = {
    var addr: addr = high_data @ low_data;
    write_mem(addr, read_reg8(0b101));
    write_mem(add_bits(addr, 0x0001), read_reg8(0b100));

    // print_endline("Instruction completed: SHLD");

    increment_clock_cycle_count(16);
    increment_machine_cycle_count(5);

    true
}

/* LHLD instruction */
function clause execute(LHLD(low_data, high_data)) = {
    var addr: addr = high_data @ low_data;
    write_reg8(0b101, read_mem(addr));
    write_reg8(0b100, read_mem(add_bits(addr, 0x0001)));

    // print_endline("Instruction completed: LHLD");

    increment_clock_cycle_count(16);
    increment_machine_cycle_count(5);

    true
}

/* PCHL instruction */
function clause execute(PCHL()) = {
    PC_reg[full] = read_reg16_sp(0b10);

    // print_endline("Instruction completed: PCHL");

    increment_clock_cycle_count(5);
    increment_machine_cycle_count(1);

    true
}

/* JMP instruction */
function clause execute(JMP(low_data, high_data)) = {
    PC_reg[full] = high_data @ low_data;

    // print_endline("Instruction completed: JMP");

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* JC instruction */
function clause execute(JC(low_data, high_data)) = {
    if read_c_flag() == 0b1 then {
        PC_reg[full] = high_data @ low_data;
    };

    // print_endline("Instruction completed: JC");

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* JNC instruction */
function clause execute(JNC(low_data, high_data)) = {
    if read_c_flag() == 0b0 then {
        PC_reg[full] = high_data @ low_data;
    };

    // print_endline("Instruction completed: JNC");

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* JZ instruction */
function clause execute(JZ(low_data, high_data)) = {
    if read_z_flag() == 0b1 then {
        PC_reg[full] = high_data @ low_data;
    };

    // print_endline("Instruction completed: JZ");

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* JNZ instruction */
function clause execute(JNZ(low_data, high_data)) = {
    if read_z_flag() == 0b0 then {
        PC_reg[full] = high_data @ low_data;
    };

    // print_endline("Instruction completed: JNZ");

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* JM instruction */
function clause execute(JM(low_data, high_data)) = {
    if read_s_flag() == 0b1 then {
        PC_reg[full] = high_data @ low_data;
    };

    // print_endline("Instruction completed: JM");

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* JP instruction */
function clause execute(JP(low_data, high_data)) = {
    if read_s_flag() == 0b0 then {
        PC_reg[full] = high_data @ low_data;
    };

    // print_endline("Instruction completed: JP");

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* JPE instruction */
function clause execute(JPE(low_data, high_data)) = {
    if read_p_flag() == 0b1 then {
        PC_reg[full] = high_data @ low_data;
    };

    // print_endline("Instruction completed: JPE");

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* JPO instruction */
function clause execute(JPO(low_data, high_data)) = {
    if read_p_flag() == 0b0 then {
        PC_reg[full] = high_data @ low_data;
    };

    // print_endline("Instruction completed: JPO");

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* CALL instruction */
function clause execute(CALL(low_data, high_data)) = {
    push_stack(PC_reg[full]);
    PC_reg[full] = high_data @ low_data;
    // print_endline("Instruction completed: CALL");

    increment_clock_cycle_count(17);
    increment_machine_cycle_count(5);

    true
}

/* CC instruction */
function clause execute(CC(low_data, high_data)) = {
    if read_c_flag() == 0b1 then {
        push_stack(PC_reg[full]);
        PC_reg[full] = high_data @ low_data;
        increment_clock_cycle_count(17);
        increment_machine_cycle_count(5);
    } else {
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    };

    // print_endline("Instruction completed: CC");

    true
}

/* CNC instruction */
function clause execute(CNC(low_data, high_data)) = {
    if read_c_flag() == 0b0 then {
        push_stack(PC_reg[full]);
        PC_reg[full] = high_data @ low_data;
        increment_clock_cycle_count(17);
        increment_machine_cycle_count(5);
    } else {
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    };

    // print_endline("Instruction completed: CNC");

    true
}

/* CZ instruction */
function clause execute(CZ(low_data, high_data)) = {
    if read_z_flag() == 0b1 then {
        push_stack(PC_reg[full]);
        PC_reg[full] = high_data @ low_data;
        increment_clock_cycle_count(17);
        increment_machine_cycle_count(5);
    } else {
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    };

    // print_endline("Instruction completed: CZ");

    true
}

/* CNZ instruction */
function clause execute(CNZ(low_data, high_data)) = {
    if read_z_flag() == 0b0 then {
        push_stack(PC_reg[full]);
        PC_reg[full] = high_data @ low_data;
        increment_clock_cycle_count(17);
        increment_machine_cycle_count(5);
    } else {
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    };

    // print_endline("Instruction completed: CNZ");

    true
}

/* CM instruction */
function clause execute(CM(low_data, high_data)) = {
    if read_s_flag() == 0b1 then {
        push_stack(PC_reg[full]);
        PC_reg[full] = high_data @ low_data;
        increment_clock_cycle_count(17);
        increment_machine_cycle_count(5);
    } else {
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    };

    // print_endline("Instruction completed: CM");

    true
}

/* CP instruction */
function clause execute(CP(low_data, high_data)) = {
    if read_s_flag() == 0b0 then {
        push_stack(PC_reg[full]);
        PC_reg[full] = high_data @ low_data;
        increment_clock_cycle_count(17);
        increment_machine_cycle_count(5);
    } else {
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    };

    // print_endline("Instruction completed: CP");

    true
}

/* CPE instruction */
function clause execute(CPE(low_data, high_data)) = {
    if read_p_flag() == 0b1 then {
        push_stack(PC_reg[full]);
        PC_reg[full] = high_data @ low_data;
        increment_clock_cycle_count(17);
        increment_machine_cycle_count(5);
    } else {
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    };

    // print_endline("Instruction completed: CPE");

    true
}

/* CPO instruction */
function clause execute(CPO(low_data, high_data)) = {
    if read_p_flag() == 0b0 then {
        push_stack(PC_reg[full]);
        PC_reg[full] = high_data @ low_data;
        increment_clock_cycle_count(17);
        increment_machine_cycle_count(5);
    } else {
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    };

    // print_endline("Instruction completed: CPO");

    true
}

/* RET instruction */
function clause execute(RET()) = {
    PC_reg[full] = pop_stack();

    // print_endline("Instruction completed: RET");


    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);
    true
}

/* RC instruction */
function clause execute(RC()) = {
    if read_c_flag() == 0b1 then {
        PC_reg[full] = pop_stack();
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    } else {
        increment_clock_cycle_count(5);
        increment_machine_cycle_count(1);
    };

    // print_endline("Instruction completed: RC");

    true
}

/* RNC instruction */
function clause execute(RNC()) = {
    if read_c_flag() == 0b0 then {
        PC_reg[full] = pop_stack();
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    } else {
        increment_clock_cycle_count(5);
        increment_machine_cycle_count(1);
    };

    // print_endline("Instruction completed: RNC");

    true
}

/* RZ instruction */
function clause execute(RZ()) = {
    if read_z_flag() == 0b1 then {
        PC_reg[full] = pop_stack();
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    } else {
        increment_clock_cycle_count(5);
        increment_machine_cycle_count(1);
    };

    // print_endline("Instruction completed: RZ");

    true
}

/* RNZ instruction */
function clause execute(RNZ()) = {
    if read_z_flag() == 0b0 then {
        PC_reg[full] = pop_stack();
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    } else {
        increment_clock_cycle_count(5);
        increment_machine_cycle_count(1);
    };

    // print_endline("Instruction completed: RNZ");

    true
}

/* RM instruction */
function clause execute(RM()) = {
    if read_s_flag() == 0b1 then {
        PC_reg[full] = pop_stack();
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    } else {
        increment_clock_cycle_count(5);
        increment_machine_cycle_count(1);
    };

    // print_endline("Instruction completed: RM");

    true
}

/* RP instruction */
function clause execute(RP()) = {
    if read_s_flag() == 0b0 then {
        PC_reg[full] = pop_stack();
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    } else {
        increment_clock_cycle_count(5);
        increment_machine_cycle_count(1);
    };

    // print_endline("Instruction completed: RP");

    true
}

/* RPE instruction */   
function clause execute(RPE()) = {
    if read_p_flag() == 0b1 then {
        PC_reg[full] = pop_stack();
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    } else {
        increment_clock_cycle_count(5);
        increment_machine_cycle_count(1);
    };

    // print_endline("Instruction completed: RPE");

    true
}

/* RPO instruction */
function clause execute(RPO()) = {
    if read_p_flag() == 0b0 then {
        PC_reg[full] = pop_stack();
        increment_clock_cycle_count(11);
        increment_machine_cycle_count(3);
    } else {
        increment_clock_cycle_count(5);
        increment_machine_cycle_count(1);
    };

    // print_endline("Instruction completed: RPO");

    true
}

/* RST instruction */
function clause execute(RST(exp)) = {
    push_stack(PC_reg[full]);
    PC_reg[full] = 0b0000000000 @ exp @ 0b000;

    // print_endline("Instruction completed: RST");

    increment_clock_cycle_count(11);
    increment_machine_cycle_count(3);

    true
}

/* EI instruction */
function clause execute(EI()) = {
    set_interrupt_enable(0b1);
    // print_endline("Instruction completed: EI");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

/* DI instruction */
function clause execute(DI()) = {
    set_interrupt_enable(0b0);
    // print_endline("Instruction completed: DI");

    increment_clock_cycle_count(4);
    increment_machine_cycle_count(1);

    true
}

/* IN instruction */
function clause execute(IN(port)) = {
    
    read_devacc(port);
    // print_endline("Instruction completed: IN");

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* OUT instruction */
function clause execute(OUT(port)) = {
    
    write_devacc(port);
    // print_endline("Instruction completed: OUT");

    increment_clock_cycle_count(10);
    increment_machine_cycle_count(3);

    true
}

/* HLT instruction */
function clause execute (HLT()) = {
    // print_endline("Instruction completed: HLT ");
    
    increment_clock_cycle_count(7);
    increment_machine_cycle_count(1);
    
    false
}

function clause execute(NOTFOUND8(this)) = {
    // print_endline("not found, try 16");
    let next_byte: bitvector(8) = read_mem(PC_reg[full]);
    increment_pc();
    execute(decode16(this @ next_byte));
}

function clause execute(NOTFOUND16(this)) = {
    // print_endline("not found, try 24");
    let next_byte: bitvector(8) = read_mem(PC_reg[full]);
    increment_pc();
    execute(decode24(this @ next_byte))
}

function clause execute(NOTFOUND24(this)) = {
    print_endline("invalid instruction");
    print_bits("this: ", this);
    false
}

