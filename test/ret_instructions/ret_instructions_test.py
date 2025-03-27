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

"""RET"""
def test_ret(setup_and_cleanup):
    program_commands = retrieve_commands('ret')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'push_stack(0x0152)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("ret")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

"""RC"""
def test_rc(setup_and_cleanup):
    program_commands = retrieve_commands('rc')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'push_stack(0x0152);', 'update_c_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rc")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

def test_rc_nt(setup_and_cleanup):
    program_commands = retrieve_commands('rc')
    program_commands.extend(['update_c_flag(0b0)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rc_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0002'

"""RNC"""
def test_rnc(setup_and_cleanup):
    program_commands = retrieve_commands('rnc')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'push_stack(0x0152)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rnc")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

def test_rnc_nt(setup_and_cleanup):
    program_commands = retrieve_commands('rnc')
    program_commands.extend(['update_c_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rnc_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0002'

"""RZ"""
def test_rz(setup_and_cleanup):
    program_commands = retrieve_commands('rz')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'push_stack(0x0152);', 'update_z_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rz")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

def test_rz_nt(setup_and_cleanup):
    program_commands = retrieve_commands('rz')
    program_commands.extend(['update_z_flag(0b0)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rz_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0002'

"""RNZ"""
def test_rnz(setup_and_cleanup):
    program_commands = retrieve_commands('rnz')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'push_stack(0x0152)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rnz")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

def test_rnz_nt(setup_and_cleanup):
    program_commands = retrieve_commands('rnz')
    program_commands.extend(['update_z_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rnz_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0002'

"""RM"""
def test_rm(setup_and_cleanup):
    program_commands = retrieve_commands('rm')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'push_stack(0x0152);', 'update_s_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rm")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

def test_rm_nt(setup_and_cleanup):
    program_commands = retrieve_commands('rm')
    program_commands.extend(['update_s_flag(0b0)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rm_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0002'

"""RP"""
def test_rp(setup_and_cleanup):
    program_commands = retrieve_commands('rp')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'push_stack(0x0152)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rp")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

def test_rp_nt(setup_and_cleanup):
    program_commands = retrieve_commands('rp')
    program_commands.extend(['update_s_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rp_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0002'

"""RPE"""
def test_rpe(setup_and_cleanup):
    program_commands = retrieve_commands('rpe')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'push_stack(0x0152);', 'update_p_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rpe")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

def test_rpe_nt(setup_and_cleanup):
    program_commands = retrieve_commands('rpe')
    program_commands.extend(['update_p_flag(0b0)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rpe_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0002'

"""RPO"""
def test_rpo(setup_and_cleanup):
    program_commands = retrieve_commands('rpo')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'push_stack(0x0152);', 'update_p_flag(0b0)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rpo")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

def test_rpo_nt(setup_and_cleanup):
    program_commands = retrieve_commands('rpo')
    program_commands.extend(['update_p_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("rpo_nt")
    res = res.split('\n')
    assert res[0] == 'res 0x0002'