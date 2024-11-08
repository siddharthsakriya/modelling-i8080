function load_program(): unit -> unit = {
    //B reg
    write_mem(0x0000, 0b00000100);

    //C reg
    write_mem(0x0001, 0b00001100);

    //D reg
    write_mem(0x0002, 0b00010100);

    //E reg
    write_mem(0x0003, 0b00011100);

    //H reg
    write_mem(0x0004, 0b00100100);

    //L reg
    write_mem(0x0005, 0b00101100);

    //M reference (location in HL)
    write_mem(0x0006, 0b00110100);

    //A reg
    write_mem(0x0007, 0b00111100);
    write_mem(0x0008, 0b01110110);
}
