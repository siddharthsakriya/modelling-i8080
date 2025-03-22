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

"""STA"""
def test_sta():
    program_commands = retrieve_commands('sta')
    program_commands.extend(["write_reg8(0b111, 0x22);"])
    main_commands = ['print_bits("res ", read_mem(0x05B3));']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('sta')
    res = res.split('\n')
    assert res[0] == 'res 0x22'


"""LDA"""
def test_lda():
    program_commands = retrieve_commands('lda')
    program_commands.extend(["write_mem(0x05B3, 0x22);"])
    main_commands = ['print_test();']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('lda')
    results = extract_results(res.split('\n'))
    assert results['A'] == '0x22'

"""SHLD"""
def test_shld():
    program_commands = retrieve_commands('shld')
    program_commands.extend(["write_reg16(0b10, 0x05B3);"])
    main_commands = ['print_bits("res ", read_mem(0x010A));', 'print_bits("res ", read_mem(0x010B));']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('shld')
    res = res.split('\n')
    assert res[0] == 'res 0xB3'
    assert res[1] == 'res 0x05'


"""LHLD"""
def test_lhld():
    program_commands = retrieve_commands('lhld')
    program_commands.extend(["write_mem(0x010A, 0xB3);", "write_mem(0x010B, 0x05);"])
    main_commands = ['print_test();']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('lhld')
    results = extract_results(res.split('\n'))
    assert results['H'] == '0x05'
    assert results['L'] == '0xB3'

