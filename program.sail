function load_program() : unit -> unit = {
write_mem(0x0000, 0x3F);
write_mem(0x0001, 0x76);
update_c_flag(0b1);
}
