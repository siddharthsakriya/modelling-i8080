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
    for i in range(len(output) - 2, len(output) - 16, -1):
        res.append(output[i])

    res.reverse()
    print(res)
    register_dict = {item.split(': ')[0].replace(' Reg', ''): item.split(': ')[1] for item in res if item}
    return register_dict


"""CALL"""
def test_call(setup_and_cleanup):
    program_commands = retrieve_commands('call')
    print(program_commands)
    program_commands.extend(['write_mem(0x0152, 0x76);'])
    main_commands = ['print_bits("res ", PC_reg[full]);', 'print_bits("res ", read_mem(SP_reg[full]));', 'print_bits("res ", read_mem(SP_reg[full] + 1))']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("call")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'
    assert res[1] == 'res 0x03'
    assert res[2] == 'res 0x00'

"""CC"""
def test_cc(setup_and_cleanup):
    program_commands = retrieve_commands('cc')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'update_c_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full]);', 'print_bits("res ", read_mem(SP_reg[full]));', 'print_bits("res ", read_mem(SP_reg[full] + 1))']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cc")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'
    assert res[1] == 'res 0x03'
    assert res[2] == 'res 0x00'

"""CNC"""
def test_cnc(setup_and_cleanup):
    program_commands = retrieve_commands('cnc')
    program_commands.extend(['write_mem(0x0152, 0x76);'])
    main_commands = ['print_bits("res ", PC_reg[full]);', 'print_bits("res ", read_mem(SP_reg[full]));', 'print_bits("res ", read_mem(SP_reg[full] + 1))']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cnc")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'
    assert res[1] == 'res 0x03'
    assert res[2] == 'res 0x00'

"""CZ"""
def test_cz(setup_and_cleanup):
    program_commands = retrieve_commands('cz')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'update_z_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full]);', 'print_bits("res ", read_mem(SP_reg[full]));', 'print_bits("res ", read_mem(SP_reg[full] + 1))']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cz")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'
    assert res[1] == 'res 0x03'
    assert res[2] == 'res 0x00'

"""CNZ"""
def test_cnz(setup_and_cleanup):
    program_commands = retrieve_commands('cnz')
    program_commands.extend(['write_mem(0x0152, 0x76);'])
    main_commands = ['print_bits("res ", PC_reg[full]);', 'print_bits("res ", read_mem(SP_reg[full]));', 'print_bits("res ", read_mem(SP_reg[full] + 1))']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cnz")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'
    assert res[1] == 'res 0x03'
    assert res[2] == 'res 0x00'
    
"""CM"""
def test_cm(setup_and_cleanup):
    program_commands = retrieve_commands('cm')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'update_s_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full]);', 'print_bits("res ", read_mem(SP_reg[full]));', 'print_bits("res ", read_mem(SP_reg[full] + 1))']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cm")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'
    assert res[1] == 'res 0x03'
    assert res[2] == 'res 0x00'

"""CP"""
def test_cp(setup_and_cleanup):
    program_commands = retrieve_commands('cp')
    program_commands.extend(['write_mem(0x0152, 0x76);'])
    main_commands = ['print_bits("res ", PC_reg[full]);', 'print_bits("res ", read_mem(SP_reg[full]));', 'print_bits("res ", read_mem(SP_reg[full] + 1))']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cp")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'
    assert res[1] == 'res 0x03'
    assert res[2] == 'res 0x00'

"""CPE"""
def test_cpe(setup_and_cleanup):
    program_commands = retrieve_commands('cpe')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'update_p_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full]);', 'print_bits("res ", read_mem(SP_reg[full]));', 'print_bits("res ", read_mem(SP_reg[full] + 1))']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cpe")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'
    assert res[1] == 'res 0x03'
    assert res[2] == 'res 0x00'

"""CPO"""
def test_cpo(setup_and_cleanup):
    program_commands = retrieve_commands('cpo')
    program_commands.extend(['write_mem(0x0152, 0x76);'])
    main_commands = ['print_bits("res ", PC_reg[full]);', 'print_bits("res ", read_mem(SP_reg[full]));', 'print_bits("res ", read_mem(SP_reg[full] + 1))']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cpo")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'
    assert res[1] == 'res 0x03'
    assert res[2] == 'res 0x00'

