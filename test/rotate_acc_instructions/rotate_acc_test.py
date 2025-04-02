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
    for i in range(len(output) - 2, len(output) - 15, -1):
        res.append(output[i])
    res.reverse()
    register_dict = {item.split(': ')[0].replace(' Reg', ''): item.split(': ')[1] for item in res}
    return register_dict

"""RLC"""
def test_rlc():
    commands = retrieve_commands('rlc')
    commands.extend(["write_reg8(0b111, 0b11110010)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('rlc')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0xE5'
    assert results['CarryFlag'] == '0b1'

"""RRC"""
def test_rrc():
    commands = retrieve_commands('rrc')
    commands.extend(["write_reg8(0b111, 0b11110010)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('rrc')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x79'
    assert results['CarryFlag'] == '0b0'

"""RAL"""
def test_ral():
    commands = retrieve_commands('ral')
    commands.extend(["write_reg8(0b111, 0b10110101)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('ral')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x6A'
    assert results['CarryFlag'] == '0b1'

"""RAR"""
def test_rar():
    commands = retrieve_commands('rar')
    commands.extend(["write_reg8(0b111, 0b01101010);", "update_c_flag(0b1)"])
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('rar')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0xB5'
    assert results['CarryFlag'] == '0b0'
