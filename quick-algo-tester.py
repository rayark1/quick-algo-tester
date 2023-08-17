import os
import subprocess
import argparse
from colorama import init, Fore

def test_solution(solution_folder, solution_file):
    testcases_path = os.path.join(solution_folder, "testcases")
    
    if not os.path.exists(testcases_path):
        print(Fore.RED + f"Error: '{testcases_path}' folder not found! Please ensure the folder exists and contains the testcases." + Fore.RESET)
        return

    input_files = sorted([f for f in os.listdir(testcases_path) if f.startswith('input')])
    output_files = sorted([f for f in os.listdir(testcases_path) if f.startswith('output')])

    if not input_files or not output_files:
        print(Fore.RED + "Error: Testcases files not found in the specified folder! Ensure files start with 'input' and 'output'." + Fore.RESET)
        return
    if len(input_files) != len(output_files):
        print(Fore.RED + "Error: Mismatched number of input and output test case files." + Fore.RESET)
        return

    passed_tests = 0

    for i, input_file_name in enumerate(input_files):
        input_file = os.path.join(testcases_path, input_file_name)
        output_file = os.path.join(testcases_path, output_files[i])

        with open(input_file, 'r') as file:
            input_data = file.read()

        with open(output_file, 'r') as file:
            expected_output = file.read()

        if not input_data.strip() or not expected_output.strip():
            print(Fore.YELLOW + f"Warning: Test case {i+1} has empty input or output. Skipping this test." + Fore.RESET)
            continue

        try:
            result = subprocess.run(['python', os.path.join(solution_folder, solution_file)], input=input_data, text=True, capture_output=True, check=True)
        except subprocess.CalledProcessError:
            print(Fore.RED + f"Error: Failed to run the solution file '{solution_file}'" + Fore.RESET)
            return

        if result.stdout.strip() == expected_output.strip():
            print(Fore.GREEN + f"Test case {i+1}: PASS" + Fore.RESET)
            passed_tests += 1
        else:
            print(Fore.RED + f"Test case {i+1}: FAIL" + Fore.RESET)
            print("Expected:")
            print(expected_output)
            print("Got:")
            print(result.stdout.strip())

    print(f"\nTotal: {len(input_files)} tests. Passed: {passed_tests}. Failed: {len(input_files) - passed_tests}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test a solution with provided test cases.")
    parser.add_argument("solution_folder", help="Path to the solution folder containing the solution file and testcases folder.")
    parser.add_argument("solution_file", help="Name of the solution file to test.")
    args = parser.parse_args()

    init(autoreset=True)  # Initialize colorama
    test_solution(args.solution_folder, args.solution_file)