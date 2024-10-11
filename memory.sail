// 65536 bytes of memory
register main_memory : vector(65536, bits(8)) = vector_init(65536, 0x00)

//memory read function
val read_mem : addr -> word
function read_mem(addr) = {
    main_memory[unsigned(addr)]
}


val write_mem : (addr, word) -> unit
function write_mem(addr, data) = {
    main_memory[unsigned(addr)] = data
}