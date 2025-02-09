import sys 

if len(sys.argv) != 3:
    print("Usage: python helper.py <path_to_hex> <path_to_res>")
    sys.exit(1)


input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        ascii_output = []

        for line in infile:
            if 'value:' in line.strip():
                hex_value = line.split(':')[1].strip().replace('0x', '')
                try:
                    ascii_char = bytes.fromhex(hex_value).decode('ascii')
                except ValueError:
                    ascii_char = '?'
                ascii_output.append(ascii_char)

        outfile.write("\nASCII Output:\n")
        outfile.write(''.join(ascii_output) + "\n")

    print(f"Lines containing 'value:' and the ASCII output have been written to {output_file}")
except FileNotFoundError:
    print(f"Error: The file {input_file} was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")