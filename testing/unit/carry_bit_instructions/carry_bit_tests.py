import sys
import os
import subprocess
import re
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from asmfiles.assemble import retrieve_commands

three_dirs_back = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
commands_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../commands.txt'))

@pytest.fixture
def setup_and_cleanup():
    """Fixture to ensure cleanup is called after the test."""
    yield  # This is where the test function runs
    cleanup()  # Cleanup is executed after the test finishes


def cleanup():
    """Function to perform cleanup tasks."""
    subprocess.run(['make', 'clean'], cwd=three_dirs_back)
    if os.path.exists(commands_file_path):
        os.remove(commands_file_path)


def test_stc(setup_and_cleanup):
    commands = retrieve_commands('stc')
    commands.extend([
        "write_mem(0x0001, 0x76)",
        ":run", 
        "startup_test()", 
        ":run", 
        "main()", 
        ":run", 
        "print_carry_bit()", 
        ":run", 
        ":quit"
    ])
    
    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")    
    
    try:
        result = subprocess.run(
            ['sail', '-is', 'commands.txt', 'main.sail'],  # Use relative paths to the working directory
            cwd=three_dirs_back, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True,              
            check=True              
        )
        output = result.stdout
        carry_bit = re.search(r'b(\d+)$', output.split('\n')[-3]).group(1)
        assert carry_bit == '1' 
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")

# def test_cmc (setup_and_cleanup):
#     commands = retrieve_commands('cmc')
#     commands1 = commands.extend([
#         "write_mem(0x0002, 0x76)",
#         ":run", 
#         "startup_test()", 
#         ":run", 
#         "main()", 
#         ":run", 
#         "print_carry_bit()", 
#         ":run", 
#         ":quit"
#     ])
    
#     with open(commands_file_path, 'w') as file:
#         for command in commands1:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(
#             ['sail', '-is', 'commands.txt', 'main.sail'],  # Use relative paths to the working directory
#             cwd=three_dirs_back, 
#             stdout=subprocess.PIPE, 
#             stderr=subprocess.PIPE, 
#             text=True,              
#             check=True              
#         )
#         output = result.stdout
#         carry_bit = re.search(r'b(\d+)$', output.split('\n')[-3]).group(1)
#         assert carry_bit == '1' 
#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")

