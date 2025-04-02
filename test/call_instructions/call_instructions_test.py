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

def test_cc_nt(setup_and_cleanup):
    program_commands = retrieve_commands('cc')
    program_commands.extend(['update_c_flag(0b0)'])
    main_commands = ['print_bits("res ", PC_reg[full]);']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cc_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0004'

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

def test_cnc_nt(setup_and_cleanup):
    program_commands = retrieve_commands('cnc')
    program_commands.extend(['update_c_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full]);']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cnc_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0004'

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

def test_cz_nt(setup_and_cleanup):
    program_commands = retrieve_commands('cz')
    program_commands.extend(['update_z_flag(0b0)'])
    main_commands = ['print_bits("res ", PC_reg[full]);']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cz_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0004'

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

def test_cnz_nt(setup_and_cleanup):
    program_commands = retrieve_commands('cnz')
    program_commands.extend(['update_z_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full]);']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cnz_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0004'
    
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

def test_cm_nt(setup_and_cleanup):
    program_commands = retrieve_commands('cm')
    program_commands.extend(['update_s_flag(0b0)'])
    main_commands = ['print_bits("res ", PC_reg[full]);']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cm_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0004'

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

def test_cp_nt(setup_and_cleanup):
    program_commands = retrieve_commands('cp')
    program_commands.extend(['update_s_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full]);']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cp_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0004'

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

def test_cpe_nt(setup_and_cleanup):
    program_commands = retrieve_commands('cpe')
    program_commands.extend(['update_p_flag(0b0)'])
    main_commands = ['print_bits("res ", PC_reg[full]);']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cpe_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0004'
    
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

def test_cpo_nt(setup_and_cleanup):
    program_commands = retrieve_commands('cpo')
    program_commands.extend(['update_p_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full]);']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("cpo_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0004'

