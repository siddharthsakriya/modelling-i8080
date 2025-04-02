import sys
import os
import subprocess
import re
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from asmfiles.assemble import *

three_dirs_back = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

def extract_results(output):
    res = []
    for i in range(len(output) - 2, len(output) - 15, -1):
        res.append(output[i])
    res.reverse()
    register_dict = {item.split(': ')[0].replace(' Reg', ''): item.split(': ')[1] for item in res}
    return register_dict


@pytest.fixture
def setup_and_cleanup():
    """Fixture to ensure cleanup is called after the test."""
    yield  
    cleanup()


def cleanup():
    """Function to perform cleanup tasks."""
    subprocess.run(['make', 'clean'], cwd=three_dirs_back)

def test_undoc():
    commands = ["write_mem(0x0000, 0x08)"]
    main_commands = ["print_test();"]
    create_program_and_main(commands, main_commands)
    build_sail()
    res = run_sail()
    save_coverage_info('undoc')
    results = extract_results(res.split('\n'))
    assert results['B'] == '0x00'
    assert results['C'] == '0x00'
    assert results['D'] == '0x00'
    assert results['E'] == '0x00'
    assert results['H'] == '0x00'
    assert results['L'] == '0x00'
    assert results['A'] == '0x00'