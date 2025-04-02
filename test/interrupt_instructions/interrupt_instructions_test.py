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

def test_rst(setup_and_cleanup):
    program_commands = retrieve_commands('rst')
    program_commands.extend(['write_mem(0x0038, 0x76);'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rst")
    res = res.split('\n')
    assert res[0] == 'res 0x0039'

def test_ei(setup_and_cleanup):
    program_commands = retrieve_commands('ei')
    main_commands = ['print_bits("res ", INTE)']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("ei")
    res = res.split('\n')
    assert res[0] == 'res 0b1'

def test_di(setup_and_cleanup):
    program_commands = retrieve_commands('di')
    main_commands = ['print_bits("res ", INTE)']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("di")
    res = res.split('\n')
    assert res[0] == 'res 0b0'

def test_in(setup_and_cleanup):
    program_commands = retrieve_commands('in')
    program_commands.extend(['write_reg8(0b111, 0x69);', 'write_devacc(0x24);', 'write_reg8(0b111, 0x00);'])
    main_commands = ['print_test()']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("in")
    result = extract_results(res.split('\n'))
    assert result['A'] == '0x69'

def test_out(setup_and_cleanup):
    program_commands = retrieve_commands('out')
    program_commands.extend(['write_reg8(0b111, 0x69);'])
    main_commands = ['write_reg8(0b111, 0x00);', 'read_devacc(0x24);', 'print_test()']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("out")
    result = extract_results(res.split('\n'))
    assert result['A'] == '0x69'
