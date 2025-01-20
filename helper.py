# Define the input and output file paths
input_file = "out2.txt"  # Replace with the path to your input file
output_file = "out3.txt"  # Replace with the path to your output file

try:
    # Open the input and output files
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Initialize a list to accumulate ASCII output
        ascii_output = []

        # Iterate through each line in the input file
        for line in infile:
            # Strip any leading/trailing whitespace and check if the line contains 'value:'
            if 'value:' in line.strip():
                # Extract the hex value after 'value:' and strip leading '0x'
                hex_value = line.split(':')[1].strip().replace('0x', '')
                try:
                    # Convert the hex value to ASCII
                    ascii_char = bytes.fromhex(hex_value).decode('ascii')
                except ValueError:
                    # Handle invalid hex values gracefully
                    ascii_char = '?'  # Use '?' for non-convertible values

                # Append the ASCII character to the accumulator
                ascii_output.append(ascii_char)

                # Write the original line to the output file
                outfile.write(line)

        # After processing all lines, write the accumulated ASCII output
        outfile.write("\nASCII Output:\n")
        outfile.write(''.join(ascii_output) + "\n")

    print(f"Lines containing 'value:' and the ASCII output have been written to {output_file}")
except FileNotFoundError:
    print(f"Error: The file {input_file} was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")