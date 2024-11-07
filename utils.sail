
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
function 
val update_z_flag : bits(1) -> unit
val update_a_flag : bits(1) -> unit
val update_p_flag : bits(1) -> unit
val update_c_flag : bits(1) -> unit

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

