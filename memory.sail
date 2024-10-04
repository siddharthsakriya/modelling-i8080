// 65536 bytes of memory
register main_memory : vector(65536, bits(8)) = vector_init(65536, 0b00000000)

// read_mem function
val read_mem : dword -> word
function read_mem(addr) = {
    main_memory[signed(addr)]
}

val write_mem : (dword, word) -> unit
function write_mem(addr, v) = {
    main_memory[signed(addr)] = v
}