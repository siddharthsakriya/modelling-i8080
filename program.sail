function load_program() : unit -> unit = {
write_mem(0x0000, 0xD3);
write_mem(0x0001, 0x24);
write_mem(0x0002, 0x76);
write_reg8(0b111, 0x69);
}
