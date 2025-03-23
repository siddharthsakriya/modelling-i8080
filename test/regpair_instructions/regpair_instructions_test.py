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

"""PUSH"""
def test_pushde():
    commands = retrieve_commands('push_de')
    commands.extend(["write_reg16(0b01, 0x8F9D);", "write_reg16_sp(0b11, 0x3A2C)"])
    main_commands = ['print_bits("res ", read_mem(0x3A2A));', 'print_bits("res ", read_mem(0x3A2B));']
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    res = res.split('\n')
    save_coverage_info('pushde1')
    assert res[0] == "res 0x9D"
    assert res[1] == "res 0x8F"

"""POP"""
def test_popbc():
    commands = retrieve_commands('pop_bc')
    
    commands.extend(["write_mem(0x1239, 0x3D);", "write_mem(0x123A, 0x93);", "write_reg16_sp(0b11, 0x1239)"])
    main_commands = ['print_bits("res ", read_reg16(0b00));']
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    res = res.split('\n')
    save_coverage_info('popbc1')
    assert res[0] == "res 0x933D"

def test_pop_psw():
    commands = retrieve_commands('pop_psw')
    commands.extend(["write_mem(0x1239, 0xC3);", "write_mem(0x123A, 0xFF);", "write_reg16_sp(0b11, 0x1239)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('poppsw1')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0xFF'
    assert results['SignFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b1'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ParityFlag'] == '0b0'
    assert results['CarryFlag'] == '0b1'  

"""DAD"""
def test_dad():
    commands = retrieve_commands('dad')
    commands.extend(["write_reg16(0b00, 0x339F);", "write_reg16(0b10, 0xA17B);"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('dad1')
    results = extract_results(res.split('\n'))
    assert results['H'] == '0xD5'
    assert results['L'] == '0x1A'
    assert results['CarryFlag'] == '0b0'

"""INX"""
def test_inx():
    commands = retrieve_commands('inx')
    commands.extend(["write_reg16(0b00, 0x0011);"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('inx1')
    results = extract_results(res.split('\n'))
    assert results['B'] == '0x00'
    assert results['C'] == '0x12'


"""DCX"""
def test_dcx():
    commands = retrieve_commands('dcx')
    commands.extend(["write_reg16(0b00, 0x0011);"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('dcx1')
    results = extract_results(res.split('\n'))
    assert results['B'] == '0x00'
    assert results['C'] == '0x10'


"""XCHG"""
def test_xchg():
    commands = retrieve_commands('xchg')
    commands.extend(["write_reg16(0b01, 0x0011);", "write_reg16(0b10, 0x1122);"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('xchg1')
    results = extract_results(res.split('\n'))
    assert results['H'] == '0x00'
    assert results['L'] == '0x11'
    assert results['D'] == '0x11'
    assert results['E'] == '0x22'

"""XTHL"""
def test_xthl():
    commands = retrieve_commands('xthl')
    commands.extend(["write_reg16_sp(0b11, 0x10AD);", "write_reg16(0b10, 0x1122);", "write_mem(0x10AD, 0xF0);", "write_mem(0x10AE, 0x0D);"])
    main_commands = ['print_bits("res ", read_mem(0x10AD));', 'print_bits("res ", read_mem(0x10AE));', 'print_bits("res ", read_reg16(0b10));']
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    res = res.split('\n')
    save_coverage_info('xthl1')
    assert res[0] == "res 0x22"
    assert res[1] == "res 0x11"
    assert res[2] == "res 0x0DF0"

"""SPHL"""
def test_sphl():
    commands = retrieve_commands('sphl')
    commands.extend(["write_reg16(0b10, 0x1122);"])
    main_commands = ['print_bits("res ", read_reg16_sp(0b11));']
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    res = res.split('\n')
    save_coverage_info('sphl1')
    assert res[0] == "res 0x1122"