function load_program() : unit -> unit = {
write_mem(0x0000, 0xF9);
write_mem(0x0001, 0x76);
write_reg16(0b10, 0x1122);
}
