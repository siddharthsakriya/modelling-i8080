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
    # subprocess.run(['make', 'clean'], cwd=three_dirs_back)

def test_stc(setup_and_cleanup):
    program_commands = retrieve_commands('stc')
    main_commands = [
        "   print_carry_bit();"
    ]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    results = run_sail()
    save_coverage_info('stc')
    carry_bit = re.search(r'b(\d+)$', results.split('\n')[-2]).group(1)
    assert carry_bit == '1'

def test_cmc_1to0 (setup_and_cleanup):
    program_commands = retrieve_commands('cmc')
    main_commands = [
        "   print_carry_bit();"
    ]
    
    create_program_and_main(program_commands, main_commands)
    build_sail()
    results = run_sail()
    save_coverage_info('cmc')
    carry_bit = re.search(r'b(\d+)$', results.split('\n')[-2]).group(1)
    assert carry_bit == '1'  
    
def test_cmc_0to1 (setup_and_cleanup):
    program_commands = retrieve_commands('cmc')
    program_commands.extend([
        "update_c_flag(0b1);"])
    main_commands = ["print_carry_bit();"]

    create_program_and_main(program_commands, main_commands)
    build_sail()
    results = run_sail()
    save_coverage_info('cmc2')
    carry_bit = re.search(r'b(\d+)$', results.split('\n')[-2]).group(1)
    assert carry_bit == '0'

