import os
import subprocess
import sys

commands = []

# inject ret address for BDOS call
commands.append("write_mem(0x0005, 0b11001001)")
commands.append(":run") 
def read_com_file(file_path):
    counter = 256
    try:
        with open(file_path, 'rb') as file:
            byte = file.read(1) 
            byte_count = 0      

            while byte:
                commands.append(f"write_mem(0x{counter:04X}, 0x{int.from_bytes(byte, 'little'):02X})") 
                commands.append(":run")       
                print(commands[byte_count])
                byte = file.read(1)
                byte_count += 1
                counter += 1

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if len(sys.argv) != 2:
    print("Usage: python runner_binary.py <path_to_com_file>")
    sys.exit(1)

file_path = sys.argv[1]

read_com_file(file_path)
commands.append("main()")
commands.append(":run")
commands.append(":quit")

with open('commands.txt', 'w') as file:
    file.write('\n'.join(commands))

result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], capture_output=True)

if result.returncode == 0:
    print(result.stdout.decode())  
else:
    print(result.stderr.decode())  

make_clean_result = subprocess.run(['make', 'clean'], capture_output=True, text=True)

if make_clean_result.returncode == 0:
    print(make_clean_result.stdout)
else:
    print("Make clean failed:")
    print(make_clean_result.stderr)

