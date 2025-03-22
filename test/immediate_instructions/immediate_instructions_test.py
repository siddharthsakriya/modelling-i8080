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
    yield
    cleanup()


def cleanup():
    """Function to perform cleanup tasks."""
    subprocess.run(['make', 'clean'], cwd=three_dirs_back)

def extract_results(output):
    res = []
    for i in range(len(output) - 2, len(output) - 16, -1):
        res.append(output[i])

    res.reverse()
    print(res)
    register_dict = {item.split(': ')[0].replace(' Reg', ''): item.split(': ')[1] for item in res if item}
    return register_dict

"""MVI"""
def test_mvi_basic():
    program_commands = retrieve_commands('mvi')
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('mvi')

    results = extract_results(res.split('\n'))
    assert results['B'] == '0x22'
    assert results['C'] == '0x22'
    assert results['D'] == '0x22'
    assert results['E'] == '0x22'
    assert results['H'] == '0x22'
    assert results['L'] == '0x22'
    assert results['A'] == '0x22'  


"""ADI"""
def test_adi():
    program_commands = retrieve_commands('adi')
    program_commands.extend(["write_reg8(0b111, 0x6C);"])
    main_commands = ["print_test();"]
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('adi')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x9A'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b1'
    assert results['ParityFlag'] == '0b1'

"""ACI"""
def test_aci():
    program_commands = retrieve_commands('aci')
    program_commands.extend(["write_reg8(0b111, 0x42);", "update_c_flag(0b1);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('adc_m')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x80'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b1'
    assert results['ParityFlag'] == '0b0'

"""SUI"""
def test_sui():
    program_commands = retrieve_commands('sui')
    program_commands.extend(["write_reg8(0b111, 0x3E);"])
    main_commands = ["print_test();"]
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('sui')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x00'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b1'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'

"""SBI"""
def test_sbi():
    program_commands = retrieve_commands('sbi')
    program_commands.extend(["write_reg8(0b111, 0x04);", "update_c_flag(0b1);"])
    main_commands = ["print_test();"]
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('sbi')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x01'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b0'

"""ANI"""
def test_ani():
    program_commands = retrieve_commands('ani')
    program_commands.extend(["write_reg8(0b111, 0xFC);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('ani')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x0C'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'

"""XRI"""
def test_xri():
    program_commands = retrieve_commands('xri')
    program_commands.extend(["write_reg8(0b111, 0x5C);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('xri')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x24'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'
    
"""ORI"""
def test_ori():
    program_commands = retrieve_commands('ori')
    program_commands.extend(["write_reg8(0b111, 0x33);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('ori')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x3F'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'

"""CPI"""
def test_cpi_lt():
    program_commands = retrieve_commands('cpi')
    program_commands.extend(["write_reg8(0b111, 0x02);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('cpi_lt')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x02'
    assert results['CarryFlag'] == '0b1'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b1' 
    assert results['ParityFlag'] == '0b0'


def test_cpi_gt():
    program_commands = retrieve_commands('cpi')
    program_commands.extend(["write_reg8(0b111, 0x0A);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('cmp')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x0A'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0' 
    assert results['ParityFlag'] == '0b1'