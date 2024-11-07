
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
val read_z_flag : unit -> bits(1)
val read_a_flag : unit -> bits(1)
val read_p_flag : unit -> bits(1)
val read_c_flag : unit -> bits(1)


val increment_pc : unit -> unit
function increment_pc() = {
    PC_reg[full] = add_bits(PC_reg[full], 0x0001)
}


//sail_shiftleft 
//sail_shiftright 
//look into overloading the shift operators 

val "shiftl" : forall 'm 'n, 'n >= 0. (bits('m), atom('n)) -> bits('m)
val "shiftr" : forall 'm 'n, 'n >= 0. (bits('m), atom('n)) -> bits('m)

