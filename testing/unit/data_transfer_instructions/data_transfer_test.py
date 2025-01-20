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


def extract_results(output):
    res = []
    for i in range(len(output) - 3, len(output) - 16, -1):
        res.append(output[i])
    res.reverse()
    register_dict = {item.split(': ')[0].replace(' Reg', ''): item.split(': ')[1] for item in res}
    return register_dict

"""MOV tests"""

def test_mov_basic():
    commands = retrieve_commands('mov')
    commands.extend(["write_mem(0x0006, 0x76)", ":run", "write_reg8(0b111, 0x22)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")    
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)
        assert results['B'] == '0x22'
        assert results['C'] == '0x22'
        assert results['D'] == '0x22'
        assert results['E'] == '0x22'
        assert results['H'] == '0x22'
        assert results['L'] == '0x22'
        assert results['A'] == '0x22'


    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")


def test_mov_mem():
    commands = retrieve_commands('mov_m')
    commands.extend(["write_mem(0x0003, 0x76)", ":run", "write_reg16(0b10, 0x1111)", ":run", "write_reg8(0b111, 0x22)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])


    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")    
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)
        assert results['A'] == '0x22'
        assert results['B'] == '0x22'
        assert results['M'] == '0x22'


    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")


""" STAX tests """
def test_stax_b():
    commands = retrieve_commands('stax_b')
    commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg16(0b00, 0x1111)", ":run", "write_reg8(0b111, 0x22)", ":run", "startup_test()", ":run", "main()", ":run", "read_mem(read_reg16(0b00))", ":run", ":quit"])
    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")    
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        res = output[-2].replace(" ", "").split("=")[-1]
        assert res == '0x22'

    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")    

def test_stax_d():
    commands = retrieve_commands('stax_d')
    commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg16(0b01, 0x1111)", ":run", "write_reg8(0b111, 0x22)", ":run", "startup_test()", ":run", "main()", ":run", "read_mem(read_reg16(0b01))", ":run", ":quit"])
    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")    
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        res = output[-2].replace(" ", "").split("=")[-1]
        assert res == '0x22'

    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")    

"""LDAX tests"""
def test_ldax_b():
    commands = retrieve_commands('ldax_b')
    commands.extend(["write_mem(0x0001, 0x76)", ":run","write_mem(0x1111, 0x22)", ":run", "write_reg16(0b00, 0x1111)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")    
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)
        assert results['A'] == '0x22'

    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")

def test_ldax_d():
    commands = retrieve_commands('ldax_d')
    commands.extend(["write_mem(0x0001, 0x76)", ":run","write_mem(0x1111, 0x22)", ":run", "write_reg16(0b01, 0x1111)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)
        assert results['A'] == '0x22'
    
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")
