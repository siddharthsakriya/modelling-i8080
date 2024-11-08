function load_program(): unit -> unit = {
    //B reg being used to test carry is set
    write_reg8(0b000, 0b11111111);
    write_mem(0x0000, 0b00000100);
    write_mem(0x0001, 0b01110110);
}
