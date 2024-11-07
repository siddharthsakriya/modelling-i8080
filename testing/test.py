import os
import subprocess

test_files = ["./tests/CMC.txt"] 

def test():
    for file in test_files:
        expected_output = extract_program_and_expected(file)
        run_make_command(expected_output)

def extract_program_and_expected(test_files):
    
    with open("./tests/CMC.txt", "r") as file:
        lines = file.readlines()
        
        if "TEST\n" not in lines or "EXPECTED\n" not in lines:
            print("TEST or EXPECTED section not found.")
            return None, None
        
        start = lines.index("TEST\n")
        end = lines.index("EXPECTED\n")
        
        program_section = lines[start + 1:end]
        
        expected_section = lines[end + 1:]
        
        with open("../program.sail", "w") as new_file:
            new_file.writelines(program_section)
        
        print("Program section written to program.sail successfully.")
        
        return expected_section

def run_make_command(expected_output):
    try:
        root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        result = subprocess.run(['make'], cwd=root_directory, check=True, capture_output=True, text=True)
        print("Output from 'make':")
        print(result.stdout)

        out_result = subprocess.run(['./out'], cwd=root_directory, check=True, capture_output=True, text=True)
        actual_output = out_result.stdout.strip()
        
        # Convert the expected output to a single string for comparison
        expected_output = ''.join(expected_output).strip()
        
        # Compare actual output with expected output
        if actual_output == expected_output:
            print("Success: The actual output matches the expected output.")
        else:
            print("Failure: The actual output does not match the expected output.")
            print("Expected output:")
            print(expected_output)
            print("Actual output:")
            print(actual_output)

        subprocess.run(['make', 'clean'], cwd=root_directory, check=True, capture_output=True, text=True)


    except subprocess.CalledProcessError as e:
        print("Error:")
        print(e.stderr)

if __name__ == "__main__":
    test()
    
