import subprocess
import os
import sys

def retrieve_commands(instruction):
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    com_file_name = f'{instruction}.com'  # The .COM file to read
    asm_file_name = f'{instruction}.asm'  # The .ASM file to assemble

    # Ensure the stc.asm file exists in the script directory
    asm_file_path = os.path.join(script_dir, asm_file_name)
    if not os.path.exists(asm_file_path):
        print(f"Error: 'stc.asm' file does not exist in {script_dir}")
        sys.exit(1)

    # Assemble the .asm file
    try:
        subprocess.run(['asm80', 'stc.asm'], cwd=script_dir, check=True)
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
                commands.append(f"write_mem(0x{counter:04X}, 0x{int.from_bytes(byte, 'little'):02X})")
                commands.append(":run")
                byte = file.read(1)  
                counter += 1
        
        os.remove(file_path)

    except IOError as e:
        print(f"Error reading the file '{com_file_name}': {e}")
        sys.exit(1)
    
    return commands
