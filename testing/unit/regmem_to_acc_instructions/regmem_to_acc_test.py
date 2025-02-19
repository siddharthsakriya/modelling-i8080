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
    for i in range(len(output) - 3, len(output) - 15, -1):
        res.append(output[i])
    res.reverse()
    register_dict = {item.split(': ')[0].replace(' Reg', ''): item.split(': ')[1] for item in res}
    return register_dict

""" ADD TESTS """
def test_add_reg_to_acc(setup_and_cleanup):
    commands = retrieve_commands('add_r')
    commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b111, 0x6C)", ":run", "write_reg8(0b010, 0x2E)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")    
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)
        
        assert results['A'] == '0x9A'
        assert results['CarryFlag'] == '0b0'
        assert results['AuxCarryFlag'] == '0b1'
        assert results['ZeroFlag'] == '0b0'
        assert results['SignFlag'] == '0b1'
        assert results['ParityFlag'] == '0b1'

    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")

def test_add_mem_to_acc(setup_and_cleanup):
    commands = retrieve_commands('add_m')
    commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_mem(0x0002, 0x2E)", ":run", "write_reg8(0b111, 0x6C)", ":run", "write_reg16(0b10, 0x0002)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)

        assert results['A'] == '0x9A'
        assert results['CarryFlag'] == '0b0'
        assert results['AuxCarryFlag'] == '0b1'
        assert results['ZeroFlag'] == '0b0'
        assert results['SignFlag'] == '0b1'
        assert results['ParityFlag'] == '0b1'
        
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")

""" ADC TESTS """
def test_adc_withcarry_reg_to_acc(setup_and_cleanup):
    commands = retrieve_commands('adc_m')
    commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b111, 0x42)", ":run", "write_mem(0x0002, 0x3D)", ":run", "write_reg16(0b10, 0x0002)", ":run", "update_c_flag(0b1)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)

        assert results['A'] == '0x80'
        assert results['CarryFlag'] == '0b0'
        assert results['AuxCarryFlag'] == '0b1'
        assert results['ZeroFlag'] == '0b0'
        assert results['SignFlag'] == '0b1'
        assert results['ParityFlag'] == '0b0'
    
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")


def test_adc_withcarry_mem_to_acc(setup_and_cleanup):
    commands = retrieve_commands('adc_r')
    commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b111, 0x42)", ":run", "write_reg8(0b010, 0x3D)", ":run", "update_c_flag(0b1)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)

        assert results['A'] == '0x80'
        assert results['CarryFlag'] == '0b0'
        assert results['AuxCarryFlag'] == '0b1'
        assert results['ZeroFlag'] == '0b0'
        assert results['SignFlag'] == '0b1'
        assert results['ParityFlag'] == '0b0'
    
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")

def test_adc_woutcarry_reg_to_acc(setup_and_cleanup):
    commands = retrieve_commands('adc_r')
    commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b111, 0x42)", ":run", "write_reg8(0b010, 0x3D)", ":run", "update_c_flag(0b0)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)

        assert results['A'] == '0x7F'
        assert results['CarryFlag'] == '0b0'
        assert results['AuxCarryFlag'] == '0b0'
        assert results['ZeroFlag'] == '0b0'
        assert results['SignFlag'] == '0b0'
        assert results['ParityFlag'] == '0b0'
    
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")

def test_adc_woutcarry_mem_to_acc(setup_and_cleanup):
    commands = retrieve_commands('adc_m')
    commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b111, 0x42)", ":run", "write_mem(0x0002, 0x3D)", ":run", "write_reg16(0b10, 0x0002)", ":run", "update_c_flag(0b0)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)

        assert results['A'] == '0x7F'
        assert results['CarryFlag'] == '0b0'
        assert results['AuxCarryFlag'] == '0b0'
        assert results['ZeroFlag'] == '0b0'
        assert results['SignFlag'] == '0b0'
        assert results['ParityFlag'] == '0b0'
    
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")

""" SUB TESTS """
def test_sub_reg_to_acc(setup_and_cleanup):
    commands = retrieve_commands('sub_r')
    commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b111, 0x3E)", ":run", "write_reg8(0b010, 0x3E)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)

        assert results['A'] == '0x00'
        assert results['CarryFlag'] == '0b0'
        assert results['AuxCarryFlag'] == '0b1'
        assert results['ZeroFlag'] == '0b1'
        assert results['SignFlag'] == '0b0'
        assert results['ParityFlag'] == '0b1'
    
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")
    

def test_sub_mem_to_acc(setup_and_cleanup):
    commands = retrieve_commands('sub_m')
    commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_mem(0x0002, 0x3E)", ":run", "write_reg8(0b111, 0x3E)", ":run", "write_reg16(0b10, 0x0002)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

    with open(commands_file_path, 'w') as file:
        for command in commands:
            file.write(f"{command}\n")
    
    try:
        result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        output = result.stdout.split('\n')
        results = extract_results(output)

        assert results['A'] == '0x00'
        assert results['CarryFlag'] == '0b0'
        assert results['AuxCarryFlag'] == '0b1'
        assert results['ZeroFlag'] == '0b1'
        assert results['SignFlag'] == '0b0'
        assert results['ParityFlag'] == '0b1'
        
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Subprocess failed with error: {e}")

""" SBB TESTS """
def test_sbb_withcarry_reg_to_acc(setup_and_cleanup):
    pass
    
def test_sbb_withcarry_mem_to_acc(setup_and_cleanup):
    pass

def test_sbb_woutcarry_reg_to_acc(setup_and_cleanup):
    pass

def test_sbb_woutcarry_mem_to_acc(setup_and_cleanup):
    pass

""" ANA TESTS """

""" XRA TESTS """

""" ORA TESTS """

""" CMP TESTS """

