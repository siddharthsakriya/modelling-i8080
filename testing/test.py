import os
import subprocess
import sys

test_files = ["./tests/CMC.txt", "./tests/STC.txt"]

def test(verbose=False):
    for file in test_files:
        if verbose:
            print(f"Running tests for {file}")
        expected_output = extract_program_and_expected(file, verbose)
        if expected_output is not None:
            run_make_command(expected_output, verbose)

def extract_program_and_expected(test_files, verbose=False):
    with open(test_files, "r") as file:
        lines = file.readlines()
        print(test_files)
        
        if "TEST\n" not in lines or "EXPECTED\n" not in lines:
            if verbose:
                print("TEST or EXPECTED section not found.")
            return None
        
        start = lines.index("TEST\n")
        end = lines.index("EXPECTED\n")
        
        program_section = lines[start + 1:end]
        expected_section = lines[end + 1:]
        
        with open("../program.sail", "w") as new_file:
            new_file.writelines(program_section)
        
        if verbose:
            print("Program section written to program.sail successfully.")
        
        return expected_section

def run_make_command(expected_output, verbose=False):
    try:
        root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        result = subprocess.run(['make'], cwd=root_directory, check=True, capture_output=True, text=True)
        
        if verbose:
            print("Output from 'make':")
            print(result.stdout)

        out_result = subprocess.run(['./out'], cwd=root_directory, check=True, capture_output=True, text=True)
        actual_output = out_result.stdout.strip()
        
        expected_output = ''.join(expected_output).strip()
        
        if actual_output == expected_output:
            print("\033[92mSuccess: The actual output matches the expected output.\033[0m")
            print("")
        else:
            print("\033[91mFailure: The actual output does not match the expected output.\033[0m")
            print("")
            if verbose:
                print("Expected output:")
                print(expected_output)
                print("Actual output:")
                print(actual_output)

        subprocess.run(['make', 'clean'], cwd=root_directory, check=True, capture_output=True, text=True)

    except subprocess.CalledProcessError as e:
        if verbose:
            print("Error:")
            print(e.stderr)

if __name__ == "__main__":
    verbose_flag = '--verbose' in sys.argv
    test(verbose=verbose_flag)
