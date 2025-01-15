# Define the input and output file paths
input_file = "res2.txt"  # Replace with the path to your input file
output_file = "out1.txt"  # Replace with the path to your output file

try:
    # Open the input and output files
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Iterate through each line in the input file
        for line in infile:
            # Strip any leading/trailing whitespace and check if the line contains 'value:'
            if 'value:' in line.strip():
                # Write the line to the output file
                outfile.write(line)

    print(f"Lines containing 'value:' have been written to {output_file}")
except FileNotFoundError:
    print(f"Error: The file {input_file} was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
