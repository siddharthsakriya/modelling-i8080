import sys
import os
import subprocess
import re
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from asmfiles.assemble import *

three_dirs_back = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

@pytest.fixture
def setup_and_cleanup():
    """Fixture to ensure cleanup is called after the test."""
    yield  # This is where the test function runs
    cleanup()  # Cleanup is executed after the test finishes


def cleanup():
    """Function to perform cleanup tasks."""
    subprocess.run(['make', 'clean'], cwd=three_dirs_back)


def extract_results(output):
    res = []
    for i in range(len(output) - 2, len(output) - 15, -1):
        res.append(output[i])
    res.reverse()
    register_dict = {item.split(': ')[0].replace(' Reg', ''): item.split(': ')[1] for item in res}
    return register_dict

# """INR tests"""
#basic test
def test_inr_basic():
    commands = retrieve_commands('inr')
    commands.extend(["write_reg8(0b000, 0b00000001)"])
    main_commands = ["print_test();"]

    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('inr1')
    results = extract_results(res.split('\n'))
    assert results['B'] == '0x02'


#parity test
def test_inr_parity():

    commands = retrieve_commands('inr')
    commands.extend(["write_reg8(0b000, 0b00000010)"])
    main_commands = ["print_test();"]

    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('inr2')
    results = extract_results(res.split('\n'))
    assert results['B'] == '0x03'
    assert results['ParityFlag'] == '0b1'

    
#auxiliary carry test
def test_inr_ac():
    commands = retrieve_commands('inr')
    commands.extend(["write_reg8(0b000, 0b00001111)"])
    main_commands = ["print_test();"]

    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('inr3')
    results = extract_results(res.split('\n'))
    assert results['B'] == '0x10'
    assert results['AuxCarryFlag'] == '0b1'



#zero flag test
def test_inr_zero():
    commands = retrieve_commands('inr')
    commands.extend(["write_reg8(0b000, 0b11111111)"])
    main_commands = ["print_test();"]

    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('inr4')
    results = extract_results(res.split('\n'))

    assert results['B'] == '0x00'
    assert results['ZeroFlag'] == '0b1'

def test_inr_sign():
    commands = retrieve_commands('inr')
    commands.extend(["write_reg8(0b000, 0b01111111)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('inr5')
    print(res.split('\n'))
    results = extract_results(res.split('\n'))

    assert results['B'] == '0x80'
    assert results['SignFlag'] == '0b1'

"""DCR tests"""

#basic test
def test_dcr_basic():
    commands = retrieve_commands('dcr')
    commands.extend(["write_reg8(0b000, 0b00000010)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('dcr1')
    results = extract_results(res.split('\n'))
    assert results['B'] == '0x01'


#parity test
def test_dcr_parity():
    commands = retrieve_commands('dcr')
    commands.extend(["write_reg8(0b000, 0b00000100)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('dcr2')
    results = extract_results(res.split('\n'))
    assert results['B'] == '0x03'
    assert results['ParityFlag'] == '0b1'
    
# #AC TO-DO

#sign test
def test_dcr_sign():
    commands = retrieve_commands('dcr')
    commands.extend(["write_reg8(0b000, 0b00000000)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('dcr3')

    results = extract_results(res.split('\n'))
    assert results['B'] == '0xFF'
    assert results['SignFlag'] == '0b1'

#zero flag test
def test_dcr_zero():
    commands = retrieve_commands('dcr')
    commands.extend(["write_reg8(0b000, 0b00000001)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()    
    res = run_sail()
    save_coverage_info('dcr4')
    results = extract_results(res.split('\n'))
    assert results['B'] == '0x00'
    assert results['ZeroFlag'] == '0b1'
    

"""CMA tests"""
#basic test 1
def test_cma_1():
    commands = retrieve_commands('cma')
    commands.extend(["write_reg8(0b111, 0b10101010)"])    
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('cma1')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x55'

#basic test 2
def test_cma_2():
    commands = retrieve_commands('cma')
    commands.extend(["write_reg8(0b111, 0b00000000)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)

    build_sail()
    res = run_sail()
    save_coverage_info('cma2')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0xFF'
    

# """DAA tests"""
def test_daa():
    commands = retrieve_commands('daa')
    commands.extend(["write_reg8(0b111, 0b10011011)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('daa')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x01'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['CarryFlag'] == '0b1'

def test_daa2():
    commands = retrieve_commands('daa')
    commands.extend(["write_reg8(0b111, 0x6C)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('daa2')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x72'

def test_daa3():
    commands = retrieve_commands('daa')
    commands.extend(["write_reg8(0b111, 0x25)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('daa3')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x25'
    
"""NOP tests"""
#basic test
def test_nop():
    commands = retrieve_commands('nop')
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('nop')
    results = extract_results(res.split('\n'))
    assert results['B'] == '0x00'
    assert results['C'] == '0x00'
    assert results['D'] == '0x00'
    assert results['E'] == '0x00'
    assert results['H'] == '0x00'
    assert results['L'] == '0x00'
    assert results['A'] == '0x00'
