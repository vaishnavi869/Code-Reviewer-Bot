# Python Code Reviewer
A simple Python code reviewer that analyzes Python scripts for common issues, including function naming convention checks (strict camelCase), use of print() statements in production code, and syntax/runtime errors. The tool provides a colorful terminal report using [Rich](https://github.com/Textualize/rich) and saves feedback to a file.

## Features
- Function Naming Convention: Warns if function names do not follow strict camelCase (e.g., `myFunction` ✅, `my_function` ❌).
- Print Statement Detection: Flags the use of `print()` statements as warnings.
- Runtime & Syntax Checks: Detects syntax and runtime errors.
- Rich Console Output: Displays warnings, errors, and summary table in terminal.
- Save Feedback: Saves code review results to a text file.

## Installation
pip install rich
Usage
Set the Python file to review in the script:

python
Copy code
file_path = "C:/path/to/your/script.py"
Run the reviewer:

bash
Copy code
python code_reviewer.py
The script will display the review in the terminal and save feedback in file_path.txt.

Example Output
pgsql
Copy code
[WARN] Line 10: Avoid using print() in production code
[Error] Line 15: Function 'my_function' should be in camelCase format
[CLEAN] Code looks well-formatted!
Summary Table:

Warnings	Errors
2	1

Notes
Ensure the Python file is compatible with Python 3.x.
Use this tool as a preliminary code quality check, not a replacement for full linting tools.
