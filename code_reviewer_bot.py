import re
from rich.console import Console
from rich.table import Table
import traceback

# Initialize Rich console
console = Console()

def review_code(file_path):
    feedback = []
    errors = 0
    warnings = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.readlines()
    except Exception as e:
        feedback.append(f"[bold red][ERROR][/bold red] Cannot read file: {e}")
        return feedback, 1, 0

    code_str = "".join(code)

    # -----------------------------
    # Function & print() Checks
    # -----------------------------
    for i, line in enumerate(code):
        stripped = line.strip()

        # Print statement warning
        if 'print(' in line:
            feedback.append(f"[yellow][WARN][/yellow] Line {i+1}: Avoid using print() in production code")
            warnings += 1

        # Function checks (strict camelCase)
        if stripped.startswith('def '):
            func_name_match = re.findall(r'def (\w+)\(', line)
            if func_name_match:
                func_name = func_name_match[0]

                # Strict camelCase: starts lowercase, has at least one uppercase, no underscores
                if not re.match(r'^[a-z]+[A-Z][a-zA-Z0-9]*$', func_name):
                    feedback.append(f"[red][Error][/red] Line {i+1}: Function '{func_name}' should be in camelCase format")
                    warnings += 1

    # -----------------------------
    # Runtime & Syntax Checks
    # -----------------------------
    try:
        exec(code_str, {})
    except Exception as e:  # Catch syntax or runtime errors
        lineno = None
        if isinstance(e, SyntaxError):
            lineno = e.lineno
            msg = e.msg
            feedback.append(f"[bold red][ERROR][/bold red] Line {lineno}: SyntaxError -> {msg}")
        else:
            tb = traceback.extract_tb(e.__traceback__)
            if tb:
                lineno = tb[-1].lineno
            feedback.append(f"[bold red][ERROR][/bold red] Line {lineno if lineno else '?'}: Runtime error -> {e}")
        errors += 1

    if not feedback:
        feedback.append("[green][CLEAN][/green] Code looks well-formatted!")

    return feedback, errors, warnings

# -----------------------------
# Run reviewer on external file
# -----------------------------
file_path = "C:/Users/RUTUJA/Desktop/AI Reviwer Code Bot/sample_code.py"
results, errors, warnings = review_code(file_path)

# -----------------------------
# Display report using Rich
# -----------------------------
console.rule("[bold blue]CODE REVIEWER REPORT[/bold blue]", style="blue")

for msg in results:
    console.print(msg)

# Summary table
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Warnings", justify="center", style="yellow")
table.add_column("Errors", justify="center", style="red")

table.add_row(str(warnings), str(errors))
console.print(table)

# Save results
output_path = "file_path.txt"
with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(results))

console.print(f"[bold green]Feedback saved to: {output_path}[/bold green]")
