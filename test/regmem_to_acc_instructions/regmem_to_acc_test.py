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

""" ADD TESTS """
def test_add_reg_to_acc(setup_and_cleanup):
    program_commands = retrieve_commands('add_r')
    program_commands.extend([ "write_reg8(0b111, 0x6C);", "write_reg8(0b010, 0x2E);"])
    main_commands = ["print_test();"]
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('add_r')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x9A'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b1'
    assert results['ParityFlag'] == '0b1'

def test_add_mem_to_acc(setup_and_cleanup):
    program_commands = retrieve_commands('add_m')
    program_commands.extend(["write_mem(0x0002, 0x2E);", "write_reg8(0b111, 0x6C);", "write_reg16(0b10, 0x0002);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('add_m')
    results = extract_results(res.split('\n'))
    
    assert results['A'] == '0x9A'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b1'
    assert results['ParityFlag'] == '0b1'
    
""" ADC TESTS """
def test_adc_withcarry_reg_to_acc(setup_and_cleanup):
    program_commands = retrieve_commands('adc_m')
    program_commands.extend(["write_reg8(0b111, 0x42);", "write_mem(0x0002, 0x3D);", "write_reg16(0b10, 0x0002);", "update_c_flag(0b1);"])
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
    
def test_adc_withcarry_mem_to_acc(setup_and_cleanup):
    program_commands = retrieve_commands('adc_r')
    program_commands.extend(["write_reg8(0b111, 0x42);", "write_reg8(0b010, 0x3D);", "update_c_flag(0b1);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('adc_r')
    results = extract_results(res.split('\n'))
    
    assert results['A'] == '0x80'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b1'
    assert results['ParityFlag'] == '0b0'

def test_adc_woutcarry_reg_to_acc(setup_and_cleanup):
    program_commands = retrieve_commands('adc_r')
    program_commands.extend(["write_reg8(0b111, 0x42);", "write_reg8(0b010, 0x3D);", "update_c_flag(0b0);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('adc_r')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x7F'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b0'
    
def test_adc_woutcarry_mem_to_acc(setup_and_cleanup):
    program_commands = retrieve_commands('adc_m')
    program_commands.extend(["write_reg8(0b111, 0x42);", "write_mem(0x0002, 0x3D);", "write_reg16(0b10, 0x0002);", "update_c_flag(0b0);"])
    main_commands = ["print_test();"]
    
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('adc_m')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x7F'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b0'

""" SUB TESTS """
def test_sub_reg_to_acc(setup_and_cleanup):
    program_commands = retrieve_commands('sub_r')
    program_commands.extend(["write_reg8(0b111, 0x3E);", "write_reg8(0b010, 0x3E);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('sub_r')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x00'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b1'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'
    
def test_sub_mem_to_acc(setup_and_cleanup):
    program_commands = retrieve_commands('sub_m')
    program_commands.extend(["write_mem(0x0002, 0x3E);", "write_reg8(0b111, 0x3E);", "write_reg16(0b10, 0x0002);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('sub_m')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x00'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b1'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'
        
""" SBB TESTS """
def test_sbb_withcarry_reg_to_acc(setup_and_cleanup):
    program_commands = retrieve_commands('sbb_r')
    program_commands.extend(["write_reg8(0b111, 0x04);", "write_reg8(0b010, 0x02);", "update_c_flag(0b1);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('sbb_r')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x01'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b0'

def test_sbb_withcarry_mem_to_acc(setup_and_cleanup):
    program_commands = retrieve_commands('sbb_m')
    program_commands.extend(["write_reg8(0b111, 0x04);", "write_mem(0x0002, 0x02);", "write_reg16(0b10, 0x0002);", "update_c_flag(0b1);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()    
    res = run_sail()
    save_coverage_info('sbb_m')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x01'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b0'

""" ANA TESTS """
def test_ana(setup_and_cleanup):
    commands = retrieve_commands('ana')
    commands.extend(["write_reg8(0b111, 0xFC);", "write_reg8(0b010, 0x0F);" ])
    main_commands = ["print_test();"]

    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('ana')
    results = extract_results(res.split('\n'))    
        
    assert results['A'] == '0x0C'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'

def test_ana_mem(setup_and_cleanup):
    commands = retrieve_commands('ana_m')
    commands.extend(["write_mem(0x0002, 0x0F);", "write_reg8(0b111, 0xFC);", "write_reg16(0b10, 0x0002);"])
    main_commands = ["print_test();"]

    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('ana_m')
    results = extract_results(res.split('\n'))
    
    assert results['A'] == '0x0C'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b1'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'
    
""" XRA TESTS """
def test_xra(setup_and_cleanup):
    program_commands = retrieve_commands('xra')
    program_commands.extend(["write_reg8(0b111, 0x5C);", "write_reg8(0b010, 0x78);"])
    main_commands = ["print_test();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('xra')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x24'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'


def test_xra_mem(setup_and_cleanup):
    program_commands = retrieve_commands('xra_m')
    program_commands.extend(["write_mem(0x0002, 0x78);", "write_reg8(0b111, 0x5C);",  "write_reg16(0b10, 0x0002);"])
    main_commands = ["print_test();"]
    
    create_program_and_main(program_commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('xra_m')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x24'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'
    
""" ORA TESTS """
def test_ora(setup_and_cleanup):
    commands = retrieve_commands('ora')
    commands.extend(["write_reg8(0b111, 0x33);", "write_reg8(0b010, 0x0F);"])
    main_commands = ["print_test();"]

    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('ora')
    results = extract_results(res.split('\n'))
    
    assert results['A'] == '0x3F'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'

def test_ora_mem(setup_and_cleanup):
    commands = retrieve_commands('ora_m')
    commands.extend(["write_mem(0x0002, 0x0F);", "write_reg8(0b111, 0x33);", "write_reg16(0b10, 0x0002);"])
    main_commands = ["print_test();"]
    
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('ora_m')
    results = extract_results(res.split('\n'))

    assert results['A'] == '0x3F'
    assert results['CarryFlag'] == '0b0'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b0'
    assert results['ParityFlag'] == '0b1'
    
""" CMP TESTS """
def test_cmp_acc_gt(setup_and_cleanup):
    commands = retrieve_commands('cmp')
    commands.extend(["write_reg8(0b111, 0x0A);", "write_reg8(0b010, 0x05);"])
    main_commands = ["print_test();"]

    create_program_and_main(commands, main_commands)
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

def test_cmp_acc_lt(setup_and_cleanup):
    commands = retrieve_commands('cmp')
    commands.extend(["write_reg8(0b111, 0x02);", "write_reg8(0b010, 0x05);"])
    main_commands = ["print_test();"]

    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('cmp2')
    results = extract_results(res.split('\n'))
    
    assert results['A'] == '0x02'
    assert results['CarryFlag'] == '0b1'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b1' 
    assert results['ParityFlag'] == '0b0'


def test_cmp_mem_lt(setup_and_cleanup):
    commands = retrieve_commands('cmp_m')
    commands.extend(["write_reg8(0b111, 0x02);", "write_reg16(0b10, 0x1111);", "write_mem(0x1111, 0x05);"])
    main_commands = ["print_test();"]

    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('cmp2mem')
    results = extract_results(res.split('\n'))
    
    assert results['A'] == '0x02'
    assert results['CarryFlag'] == '0b1'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b1' 
    assert results['ParityFlag'] == '0b0'

    assert results['A'] == '0x02'
    assert results['CarryFlag'] == '0b1'
    assert results['AuxCarryFlag'] == '0b0'
    assert results['ZeroFlag'] == '0b0'
    assert results['SignFlag'] == '0b1' 
    assert results['ParityFlag'] == '0b0'