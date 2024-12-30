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
        # Open the .COM file in binary mode
        with open(file_path, 'rb') as file:
            byte = file.read(1)  # Read the first byte
            byte_count = 0       # Counter to keep track of the byte number

            while byte:
                # Format counter as 4-digit hex with leading zeros
                commands.append(f"write_mem(0x{counter:04X}, 0x{int.from_bytes(byte, 'little'):02X})") 
                commands.append(":run")       
                print(commands[byte_count])
                byte = file.read(1)  # Read the next byte
                byte_count += 1
                counter += 1

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'TST8080.COM'
read_com_file(file_path)
commands.append("main()")
commands.append(":run")
commands.append(":quit")

# Write the commands to the file
with open('commands.txt', 'w') as file:
    file.write('\n'.join(commands))

# Fix subprocess.run by passing a list of arguments
result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], capture_output=True)

# Check and print the output or error
if result.returncode == 0:
    print(result.stdout.decode())  # Print the standard output
else:
    print(result.stderr.decode())  # Print the error output
