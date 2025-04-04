/* 
REGISTER MAPPINGS
*/
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

/* 
ALL REGISTER HELPER FUNCTIONS
*/

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

val read_reg16_sp : reg_16bit_num -> dword
function read_reg16_sp(r) = {
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
        0b11 => AF_reg[full] = v
    }
}

val write_reg16_sp : (reg_16bit_num, dword) -> unit
function write_reg16_sp(r, v) = {
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

/* 
ALL PSW HELPER FUNCTIONS
*/

val read_flag_reg : unit -> word
function read_flag_reg() = {
    var flag_reg : word = AF_reg[low];
    flag_reg
}

val update_s_flag : bits(1) -> unit
function update_s_flag(s_flag) = {
    var flag_reg : word = AF_reg[low];
    flag_reg[7..7] = s_flag;
    AF_reg[low] = flag_reg;
}

val update_z_flag : bits(1) -> unit
function update_z_flag(z_flag) = {
    var flag_reg : word = AF_reg[low];
    flag_reg[6..6] = z_flag;
    AF_reg[low] = flag_reg;
}

val update_a_flag : bits(1) -> unit
function update_a_flag(a_flag) = {
    var flag_reg : word = AF_reg[low];
    flag_reg[4..4] = a_flag;
    AF_reg[low] = flag_reg;
}

val update_p_flag : bits(1) -> unit
function update_p_flag(p_flag) = {
    var flag_reg : word = AF_reg[low];
    flag_reg[2..2] = p_flag;
    AF_reg[low] = flag_reg;
}

val update_c_flag : bits(1) -> unit
function update_c_flag(c_flag) = {
    var flag_reg : word = AF_reg[low];
    flag_reg[0..0] = c_flag;
    AF_reg[low] = flag_reg;
}

val read_s_flag : unit -> bits(1)
function read_s_flag() = {
    var flag_reg : word = AF_reg[low];
    flag_reg[7..7];
}

val read_z_flag : unit -> bits(1)
function read_z_flag() = {
    var flag_reg : word = AF_reg[low];
    flag_reg[6..6];
}

val read_a_flag : unit -> bits(1)
function read_a_flag() = {
    var flag_reg : word = AF_reg[low];
    flag_reg[4..4];
}

val read_p_flag : unit -> bits(1)
function read_p_flag() = {
    var flag_reg : word = AF_reg[low];
    flag_reg[2..2]
}

val read_c_flag : unit -> bits(1)
function read_c_flag() = {
    var flag_reg : word = AF_reg[low];
    flag_reg[0..0]
}

/* 
ALL PC & STACK HELPER FUNCTIONS
*/

val increment_pc : unit -> unit
function increment_pc() = {
    PC_reg[full] = add_bits(PC_reg[full], 0x0001)
}

val push_stack : bits(16) -> unit
function push_stack(data: bits(16)) = {
    SP_reg[full] = sub_bits(SP_reg[full], 0x0001);
    write_mem(SP_reg[full], data[15..8]);
    SP_reg[full] = sub_bits(SP_reg[full], 0x0001);
    write_mem(SP_reg[full], data[7..0]);
}

val pop_stack : unit -> bits(16)
function pop_stack() = {
    var low_bits: bits(8) = read_mem(SP_reg[full]);
    SP_reg[full] = add_bits(SP_reg[full], 0x0001);
    var high_bits: bits(8) = read_mem(SP_reg[full]);
    SP_reg[full] = add_bits(SP_reg[full], 0x0001);
    high_bits @ low_bits;
}

val increment_stack_pointer : unit -> unit
function increment_stack_pointer() = {
    SP_reg[full] = add_bits(SP_reg[full], 0x0001);
}

/* ALL PRINT STATE HELPER FUNCTIONS */
val print_processor_state : unit -> unit
function print_processor_state() = {
    print_bits("PSW: ", AF_reg[full]);
    print_bits("HL: ", HL_reg[full]);
    print_bits("DE: ", DE_reg[full]);
    print_bits("BC: ", BC_reg[full]);
    print_bits("SP: ", SP_reg[full]);
    print_bits("PC: ", PC_reg[full]);
    print_int("Clock Cycles: ",clock_cycle_count);
    print_int("Machine Cycles: ", machine_cycle_count);
}

val print_h_reg : unit -> unit
function print_h_reg() = {
    print_bits("H Reg: ", read_reg8(0b100))
}
val print_l_reg : unit -> unit
function print_l_reg() = {
    print_bits("L Reg: ", read_reg8(0b101))
}

val print_d_reg : unit -> unit
function print_d_reg() = {
    print_bits("D Reg: ", read_reg8(0b010))
}

val print_e_reg : unit -> unit
function print_e_reg() = {
    print_bits("E Reg: ", read_reg8(0b011))
}

val print_b_reg : unit -> unit
function print_b_reg() = {
    print_bits("B Reg: ", read_reg8(0b000))
}

val print_c_reg : unit -> unit
function print_c_reg() = {
    print_bits("C Reg: ", read_reg8(0b001))
}

val print_a_reg : unit -> unit
function print_a_reg() = {
    print_bits("A Reg: ", read_reg8(0b111))
}

val print_sp_reg : unit -> unit
function print_sp_reg() = {
    print_bits("SP Reg: ", SP_reg[full])
}

val print_pc_reg : unit -> unit
function print_pc_reg() = {
    print_bits("PC Reg: ", PC_reg[full])
}

val print_carry_bit : unit -> unit
function print_carry_bit() = {
    print_bits("CarryFlag: ", read_c_flag())
}

val print_parity_bit : unit -> unit
function print_parity_bit() = {
    print_bits("ParityFlag: ", read_p_flag())
}

val print_aux_carry_bit : unit -> unit
function print_aux_carry_bit() = {
    print_bits("AuxCarryFlag: ", read_a_flag())
}

val print_zero_bit : unit -> unit
function print_zero_bit() = {
    print_bits("ZeroFlag: ", read_z_flag())
}

val print_sign_bit : unit -> unit
function print_sign_bit() = {
    print_bits("SignFlag: ", read_s_flag())
}

val print_m_reg : unit -> unit
function print_m_reg() = {
    print_bits("M Reg: ", read_reg8(0b110))
}

/*
MISC FUNCTIONS
*/

val write_devacc : bits(8) -> unit 
function write_devacc(port) = {
    input_output[unsigned(port)] = read_reg8(0b111);
}

val read_devacc : bits(8) -> unit
function read_devacc(port) = {
    write_reg8(0b111, input_output[unsigned(port)]);
}

val set_interrupt_enable: bits(1) -> unit   
function set_interrupt_enable(ie) = {
    INTE = ie;
}

val EXTZ : forall 'n 'm, 'm >= 'n. (implicit('m), bits('n)) -> bits('m)
function EXTZ(m, v) = sail_zero_extend(v, m)

val EXTS : forall 'n 'm, 'm >= 'n. (implicit('m), bits('n)) -> bits('m)
function EXTS(m, v) = sail_sign_extend(v, m)

val xor_reduce : word -> bits(1)
function xor_reduce(v) = {
    var x: bits(1) = [v[0]];
    foreach (i from 1 to 7) {
        let y : bits(1) = x;
        let z : bits(1) = [v[i]]; 
        x = xor_vec(y, z);
    };
    x
}

val bool_to_bit_converter : bool -> bits(1)
function bool_to_bit_converter(b) = {
    if b == true then 0b1 else 0b0;
}

val perform_sub : (bits(8), bits(8), bits(1)) -> bits(8)
function perform_sub(minuend, subtrahend, carry) = {
    var ones_comp_sub = xor_vec(subtrahend, 0b11111111);
    
    var carry_extended = if carry == 0b1 then 0b00000000 else 0b00000001;
    
    var result: bits(9) = add_bits(0b0 @ minuend, add_bits(0b0 @ ones_comp_sub, 0b0 @ carry_extended)); 
    var carry_out = result[8..8];
    var result_8bit = result[7..0];
    
    update_c_flag(if (carry_out == 0b1) then 0b0 else 0b1);
    update_s_flag(result_8bit[7..7]);
    update_z_flag(bool_to_bit_converter(result_8bit == 0b00000000));
    update_p_flag(bool_to_bit_converter(xor_reduce(result_8bit) == 0b0));
    update_a_flag(add_bits(0b0 @ minuend[3..0], add_bits(0b0 @ ones_comp_sub[3..0], carry_extended[4..0]))[4..4]);     

    result_8bit
}

val perform_add : (bits(8), bits(8), bits(1)) -> bits(8)
function perform_add(a, b, carry) = {
    var carry_extended = if carry == 0b1 then 0b00000001 else 0b00000000;
    
    var results: bits(9) = add_bits(0b0 @ a, add_bits(0b0 @ b, 0b0 @ carry_extended));
    var carry_out = results[8..8];
    var result_8bit = results[7..0];

    var half_carry = add_bits(0b0 @ a[3..0], add_bits(0b0 @ b[3..0], carry_extended[4..0]))[4..4];

    update_c_flag(if (carry_out == 0b1) then 0b1 else 0b0);
    update_s_flag(result_8bit[7..7]);
    update_z_flag(bool_to_bit_converter(result_8bit == 0b00000000));
    update_p_flag(bool_to_bit_converter(xor_reduce(result_8bit) == 0b0));
    update_a_flag(half_carry);

    result_8bit
}

val print_test : unit -> unit
function print_test() = {
    print_m_reg();
    print_b_reg();
    print_c_reg();
    print_d_reg();
    print_e_reg();
    print_h_reg();
    print_l_reg();
    print_a_reg();
    print_carry_bit();
    print_parity_bit();
    print_aux_carry_bit();
    print_zero_bit();
    print_sign_bit();
    
}

val "shiftl" : forall 'm 'n, 'n >= 0. (bits('m), atom('n)) -> bits('m)
val "shiftr" : forall 'm 'n, 'n >= 0. (bits('m), atom('n)) -> bits('m)
val "putchar" : int -> unit


register flag1: bool = true
register flag2: bool = true
register flag3: bool = true
register flag4: bool = true
register flag5: bool = true
register flag6: bool = true