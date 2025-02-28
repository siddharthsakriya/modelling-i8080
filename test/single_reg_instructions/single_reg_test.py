# import sys
# import os
# import subprocess
# import re
# import pytest

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
# from asmfiles.assemble import retrieve_commands

# three_dirs_back = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
# commands_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../commands.txt'))

# @pytest.fixture
# def setup_and_cleanup():
#     """Fixture to ensure cleanup is called after the test."""
#     yield  # This is where the test function runs
#     cleanup()  # Cleanup is executed after the test finishes


# def cleanup():
#     """Function to perform cleanup tasks."""
#     subprocess.run(['make', 'clean'], cwd=three_dirs_back)
#     if os.path.exists(commands_file_path):
#         os.remove(commands_file_path)


# def extract_results(output):
#     res = []
#     for i in range(len(output) - 3, len(output) - 15, -1):
#         res.append(output[i])
#     res.reverse()
#     register_dict = {item.split(': ')[0].replace(' Reg', ''): item.split(': ')[1] for item in res}
#     return register_dict

# """INR tests"""

# #basic test
# def test_inr_basic():
#     commands = retrieve_commands('inr')
#     commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b000, 0b00000001)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)
#         assert results['B'] == '0x02'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")

# #parity test
# def test_inr_parity():
#     commands = retrieve_commands('inr')
#     commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b000, 0b00000010)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)
#         assert results['B'] == '0x03'
#         assert results['ParityFlag'] == '0b1'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")

# #auxiliary carry test
# def test_inr_ac():
#     commands = retrieve_commands('inr')
#     commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b000, 0b00001111)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)
#         assert results['B'] == '0x10'
#         assert results['AuxCarryFlag'] == '0b1'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")

# #zero flag test
# def test_inr_zero():
#     commands = retrieve_commands('inr')
#     commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b000, 0b11111111)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)
#         assert results['B'] == '0x00'
#         assert results['ZeroFlag'] == '0b1'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")

# def test_inr_sign():
#     commands = retrieve_commands('inr')
#     commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b000, 0b01111111)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)
#         assert results['B'] == '0x80'
#         assert results['SignFlag'] == '0b1'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")    

# """DCR tests"""

# #basic test
# def test_dcr_basic():
#     commands = retrieve_commands('dcr')
#     commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b000, 0b00000010)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)
#         assert results['B'] == '0x01'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")

# #parity test
# def test_dcr_parity():
#     commands = retrieve_commands('dcr')
#     commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b000, 0b00000100)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)
#         assert results['B'] == '0x03'
#         assert results['ParityFlag'] == '0b1'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")
    
# #AC TO-DO

# #sign test
# def test_dcr_sign():
#     commands = retrieve_commands('dcr')
#     commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b000, 0b00000000)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)
#         assert results['B'] == '0xFF'
#         assert results['SignFlag'] == '0b1'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")
    

# #zero flag test
# def test_dcr_zero():
#     commands = retrieve_commands('dcr')
#     commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b000, 0b00000001)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)
#         assert results['B'] == '0x00'
#         assert results['ZeroFlag'] == '0b1'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")

# """CMA tests"""
# #basic test 1
# def test_cma_1():
#     commands = retrieve_commands('cma')
#     commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b111, 0b10101010)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)
#         assert results['A'] == '0x55'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")

# #basic test 2
# def test_cma_2():
#     commands = retrieve_commands('cma')
#     commands.extend(["write_mem(0x0001, 0x76)", ":run", "write_reg8(0b111, 0b00000000)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)
#         assert results['A'] == '0xFF'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")

# """DAA tests"""

# #TO-DO

# """NOP tests"""
# #basic test
# def test_nop():
#     commands = retrieve_commands('nop')
#     commands.extend(["write_mem(0x0007, 0x76)", ":run", "startup_test()", ":run", "main()", ":run", "print_test()", ":run", ":quit"])

#     with open(commands_file_path, 'w') as file:
#         for command in commands:
#             file.write(f"{command}\n")    
    
#     try:
#         result = subprocess.run(['sail', '-is', 'commands.txt', 'main.sail'], cwd=three_dirs_back, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
#         output = result.stdout.split('\n')
#         results = extract_results(output)

#         assert results['B'] == '0x00'
#         assert results['C'] == '0x00'
#         assert results['D'] == '0x00'
#         assert results['E'] == '0x00'
#         assert results['H'] == '0x00'
#         assert results['L'] == '0x00'
#         assert results['A'] == '0x00'

#     except subprocess.CalledProcessError as e:
#         pytest.fail(f"Subprocess failed with error: {e}")