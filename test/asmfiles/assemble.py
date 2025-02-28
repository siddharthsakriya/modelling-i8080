import subprocess
import os
import sys

def retrieve_commands(instruction):
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    com_file_name = f'{instruction}.com'  
    asm_file_name = f'{instruction}.asm'  

    # Ensure the stc.asm file exists in the script directory
    asm_file_path = os.path.join(script_dir, asm_file_name)
    if not os.path.exists(asm_file_path):
        print(f"Error: the file does not exist in {script_dir}")
        sys.exit(1)

    # Assemble the .asm file
    try:
        subprocess.run(['asm80', asm_file_name], cwd=script_dir, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running asm80: {e}")
        sys.exit(1)
    file_path = os.path.join(script_dir, com_file_name)
    if not os.path.exists(file_path):
        print(f"Error: '{com_file_name}' was not created by the assembler.")
        sys.exit(1)
    try:
        commands = []
        counter = 0

        with open(file_path, 'rb') as file:
            byte = file.read(1) 
            while byte:
                commands.append(f"write_mem(0x{counter:04X}, 0x{int.from_bytes(byte, 'little'):02X});")                
                byte = file.read(1)  
                counter += 1
        
        commands.append(f"write_mem(0x{counter:04X}, 0x76);")
        os.remove(file_path)

    except IOError as e:
        print(f"Error reading the file '{com_file_name}': {e}")
        sys.exit(1)
    
    
    return commands

def create_program_and_main(commands_program, commands_main):
    program_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../program.sail'))
    program_sail_code = """function load_program() : unit -> unit = {
"""
    program_sail_code  += "\n".join(commands_program) + "\n"
    program_sail_code  += "}\n"

    with open(program_file_path, 'w') as file:
        file.write(program_sail_code)

    main_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../main.sail'))
    main_sail_code = """default Order dec
$include <prelude.sail>
$include "./utility/timing.sail"
$include "./mem&reg/types.sail"
$include "./mem&reg/memory.sail"
$include "./utility/utils.sail"
$include "./decoder/decode.sail"
$include "./decoder/instructions.sail"
$include "program.sail"

function bdos_9(value) : bool -> bool = {
    var looped = if (read_mem(DE_addr) == 0x24) then { false } else { print_bits("value: ", read_mem(DE_addr)); DE_addr = DE_addr + 1; true;}; 
    looped
}

function intercept_BDOS() : unit -> unit = {
    if (read_reg8(0b001) == 0x09) then {
        DE_addr = read_reg16(0b01);
        while (bdos_9(true)) do ();
    };

    if (read_reg8(0b001) == 0x02) then {
        if (read_reg8(0b011) != 0x00) then {
            print_bits("value: ", read_reg8(0b011));
        };
    };
}

function startup_cpm() : unit -> unit = {
    PC_reg[full] = 0x0100;
    SP_reg[full] = 0x0000;
}

function startup_test() : unit -> unit = {
    PC_reg[full] = 0x0000;
}

function fetch_decode_execute(last_instruction) : bool -> bool = {
    var instruction = read_mem(PC_reg[full]);
    increment_pc();
    
    var decoded = decode8(instruction);

    var loop = execute(decoded);
    if (PC_reg[full] == 0x0005) then {
        intercept_BDOS();
    };
    if( PC_reg[full] == 0x0000) then {
        loop = false;
    };

    loop
}

function main() : unit -> unit = {
    load_program();
    while (fetch_decode_execute(true)) do ();
"""

    main_sail_code += "\n".join(commands_main) + "\n"
    main_sail_code += "}\n"
    with open(main_file_path, 'w') as file:
        file.write(main_sail_code)

def build_sail():
    three_dirs_back = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    subprocess.run(['make', 'coverage_bin'], 
                   cwd = three_dirs_back)
    
def run_sail():
    three_dirs_back = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

    run_result = subprocess.run(['./out'], 
                                cwd = three_dirs_back,          
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True,
                                check=True
                                )
    
    
    return run_result.stdout
    
def save_coverage_info(name):
    three_dirs_back = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    #rename sail_coverage to name
    subprocess.run(['mv', 'sail_coverage', name], cwd=three_dirs_back)
    #move into a directory called coverage files
    subprocess.run(['mkdir', 'coverage_files'], cwd=three_dirs_back)
    subprocess.run(['mv', name, 'coverage_files'], cwd=three_dirs_back)
    

    
    