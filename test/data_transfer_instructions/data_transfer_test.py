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

"""MOV tests"""

def test_mov_basic():
    program_commands = retrieve_commands('mov')
    program_commands.extend(["write_reg8(0b111, 0x22)"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('mov')
    results = extract_results(res.split('\n'))
    assert results['B'] == '0x22'
    assert results['C'] == '0x22'
    assert results['D'] == '0x22'
    assert results['E'] == '0x22'
    assert results['H'] == '0x22'
    assert results['L'] == '0x22'
    assert results['A'] == '0x22'
    

def test_mov_mem():
    program_commands = retrieve_commands('mov_m')
    program_commands.extend(["write_reg16(0b10, 0x1111);", "write_reg8(0b111, 0x22);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('mov_m')
    results = extract_results(res.split('\n'))
    assert results['M'] == '0x22'
    assert results['A'] == '0x22'
    assert results['B'] == '0x22'
    

""" STAX tests """

def test_stax_b():
    program_commands = retrieve_commands('stax_b')
    program_commands.extend(["write_reg16(0b00, 0x1111);" "write_reg8(0b111, 0x22);"])
    main_commands = ['print_bits("output: ", read_mem(read_reg16(0b00)));']

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('stax_b')
    assert "0x22" in res.split('\n')[-2]
    
def test_stax_d():
    program_commands = retrieve_commands('stax_d')
    program_commands.extend(["write_reg16(0b01, 0x1111);", "write_reg8(0b111, 0x22);"])
    main_commands = ['print_bits("output: ", read_mem(read_reg16(0b01)));']

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('stax_d')
    assert "0x22" in res.split('\n')[-2]


"""LDAX tests"""
def test_ldax_b():
    program_commands = retrieve_commands('ldax_b')
    program_commands.extend(["write_mem(0x1111, 0x22);", "write_reg16(0b00, 0x1111);"])
    main_commands = ['print_test();']

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('ldax_b')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x22'
    
def test_ldax_d():
    program_commands = retrieve_commands('ldax_d')
    program_commands.extend(["write_mem(0x1111, 0x22);", "write_reg16(0b01, 0x1111);"])
    main_commands = ['print_test();']

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('ldax_d')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x22'
    