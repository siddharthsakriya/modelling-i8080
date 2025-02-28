function load_program() : unit -> unit = {
write_mem(0x0000, 0x1A);
write_mem(0x0001, 0x76);
write_mem(0x1111, 0x22);
write_reg16(0b01, 0x1111);
}
