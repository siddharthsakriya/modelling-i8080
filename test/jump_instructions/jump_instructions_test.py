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


"""PCHL"""
def test_pchl(setup_and_cleanup):
    program_commands = retrieve_commands('pchl')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'write_reg16(0b10, 0x0152)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("pchl")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

"""JMP"""
def test_jmp(setup_and_cleanup):
    program_commands = retrieve_commands('jmp')
    program_commands.extend(['write_mem(0x0152, 0x76);'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("jmp")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

"""JC"""
def test_jc(setup_and_cleanup):
    program_commands = retrieve_commands('jc')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'update_c_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("jc")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

"""JNC"""
def test_jnc(setup_and_cleanup):
    program_commands = retrieve_commands('jnc')
    program_commands.extend(['write_mem(0x0152, 0x76);'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("jnc")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

"""JZ"""
def test_jz(setup_and_cleanup):
    program_commands = retrieve_commands('jz')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'update_z_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("jz")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

"""JNZ"""
def test_jnz(setup_and_cleanup):
    program_commands = retrieve_commands('jnz')
    program_commands.extend(['write_mem(0x0152, 0x76);'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("jnz")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

"""JM"""
def test_jm(setup_and_cleanup):
    program_commands = retrieve_commands('jm')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'update_s_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("jm")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

"""JP"""
def test_jp(setup_and_cleanup):
    program_commands = retrieve_commands('jp')
    program_commands.extend(['write_mem(0x0152, 0x76);'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("jp")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

"""JPE"""
def test_jpe(setup_and_cleanup):
    program_commands = retrieve_commands('jpe')
    program_commands.extend(['write_mem(0x0152, 0x76);', 'update_p_flag(0b1)'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("jpe")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

"""JPO"""
def test_jpo(setup_and_cleanup):
    program_commands = retrieve_commands('jpo')
    program_commands.extend(['write_mem(0x0152, 0x76);'])
    main_commands = ['print_bits("res ", PC_reg[full])']
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info("jpo")
    res = res.split('\n')
    assert res[0] == 'res 0x0153'

