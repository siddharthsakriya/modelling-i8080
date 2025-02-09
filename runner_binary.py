import subprocess
import sys

def read_com_file(file_path):
    commands = []
    commands.append("    write_mem(0x0005, 0b11001001);")

    counter = 0x0100 
    try:
        with open(file_path, 'rb') as file:
            byte = file.read(1) 

            while byte:
                
                commands.append(f"    write_mem(0x{counter:04X}, 0x{int.from_bytes(byte, 'little'):02X});") 
                byte = file.read(1) 
                counter += 1

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    return commands

def generate_sail_program(commands):
    sail_code = """function load_program() : unit -> unit = {
"""
    sail_code += "\n".join(commands) + "\n"
    sail_code += "}\n"

    with open('program.sail', 'w') as file:
        file.write(sail_code)

    print("Generated program.sail successfully.")

if len(sys.argv) != 2:
    print("Usage: python runner_binary.py <path_to_com_file>")
    sys.exit(1)

file_path = sys.argv[1]
commands = read_com_file(file_path)
generate_sail_program(commands)

make_result = subprocess.run(['make'], capture_output=True, text=True)

if make_result.returncode != 0:
    print("Make failed:")
    print(make_result.stderr)
    sys.exit(1)

run_result = subprocess.run(['./out'], capture_output=True, text=True)

if run_result.returncode == 0:
    print(run_result.stdout)
else:
    print("Execution failed:")
    print(run_result.stderr)
    subprocess.run(['make', 'clean'], capture_output=True, text=True)

make_clean_result = subprocess.run(['make', 'clean'], capture_output=True, text=True)

if make_clean_result.returncode == 0:
    print(make_clean_result.stdout)
else:
    print("Make clean failed:")
    print(make_clean_result.stderr)
