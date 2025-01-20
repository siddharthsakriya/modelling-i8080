import sys
import os
import subprocess
import re
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from asmfiles.assemble import retrieve_commands

three_dirs_back = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
commands_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../commands.txt'))

@pytest.fixture
def setup_and_cleanup():
    """Fixture to ensure cleanup is called after the test."""
    yield  # This is where the test function runs
    cleanup()  # Cleanup is executed after the test finishes


def cleanup():
    """Function to perform cleanup tasks."""
    subprocess.run(['make', 'clean'], cwd=three_dirs_back)
    if os.path.exists(commands_file_path):
        os.remove(commands_file_path)


def extract_results(output):
    res = []
    for i in range(len(output) - 3, len(output) - 15, -1):
        res.append(output[i])
    res.reverse()
    register_dict = {item.split(': ')[0].replace(' Reg', ''): item.split(': ')[1] for item in res}
    return register_dict

""" ADD TESTS """
""" ADC TESTS """
""" SUB TESTS """
""" SBB TESTS """
""" ANA TESTS """
""" XRA TESTS """
""" ORA TESTS """
""" CMP TESTS """

