import ast
import autopep8
import traceback

def fix_syntax_errors(code: str):
    """Attempts to fix syntax errors in the given Python code."""
    try:
        compile(code, '<string>', 'exec')
        return code, "No syntax errors detected."
    except SyntaxError as e:
        return autopep8.fix_code(code), f"Fixed syntax error: {e}"

def safe_execute(code: str):
    """Executes the given Python code safely and catches runtime errors."""
    try:
        exec(code, {})
        return "Execution successful."
    except Exception as e:
        return f"Runtime error detected: {e}\n{traceback.format_exc()}"

def analyze_and_repair_code(code: str):
    """Analyzes Python code for issues and attempts repairs."""
    repaired_code, fix_message = fix_syntax_errors(code)
    execution_result = safe_execute(repaired_code)
    return repaired_code, fix_message, execution_result

if __name__ == "__main__":
    sample_code = """
    def add_numbers(a, b):
        return a + b
    
    print(add_numbers(5, ))  # Intentional syntax error
    """
    repaired_code, fix_message, execution_result = analyze_and_repair_code(sample_code)
    print("Repaired Code:")
    print(repaired_code)
    print("Fix Message:", fix_message)
    print("Execution Result:", execution_result)
