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

### INR ###
def test_inr_basic(setup_and_cleanup):
    commands = retrieve_commands('inr')
    commands.extend([
        "write_mem(0x0001, 0x76)",
        ":run", 
        "write_reg8(0b000, 0b00000001)",
        ":run",
        "startup_test()", 
        ":run", 
        "main()", 
        ":run", 
        "print_b_reg()", 
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
        result = re.search(r'0x[0-9a-fA-F]+', output.split('\n')[-3]).group(0)
        assert result == "0x02" 
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")

def test_inr_zero(setup_and_cleanup):
    commands = retrieve_commands('inr')
    commands.extend([
        "write_mem(0x0001, 0x76)",
        ":run", 
        "write_reg8(0b000, 0b11111111)",
        ":run",
        "startup_test()", 
        ":run", 
        "main()", 
        ":run", 
        "print_b_reg()", 
        ":run", 
        "print_zero_bit()",
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
        result = re.search(r'0x[0-9a-fA-F]+', output.split('\n')[-6]).group(0)
        zero_flag = re.search(r'b(\d+)$', output.split('\n')[-3]).group(1)
        assert result == "0x00" 
        assert zero_flag == "1"
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")

def test_inr_sign_and_parity(setup_and_cleanup):
    commands = retrieve_commands('inr')
    commands.extend([
        "write_mem(0x0001, 0x76)",
        ":run", 
        "write_reg8(0b000, 0b01111111)",
        ":run",
        "startup_test()", 
        ":run", 
        "main()", 
        ":run", 
        "print_b_reg()", 
        ":run", 
        "print_sign_bit()",
        ":run",
        "print_parity_bit()",
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
        result = re.search(r'0x[0-9a-fA-F]+', output.split('\n')[-9]).group(0)
        sign_flag = re.search(r'b(\d+)$', output.split('\n')[-6]).group(1)
        parity_flag = re.search(r'b(\d+)$', output.split('\n')[-3]).group(1)
        assert result == "0x80" 
        assert parity_flag == "0"
        assert sign_flag == "1"
    
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")

