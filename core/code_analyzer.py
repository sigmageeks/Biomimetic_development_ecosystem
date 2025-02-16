import ast
import re
import astor
import pylint.lint
from pylint.reporters.text import TextReporter
from io import StringIO

def analyze_code_syntax(code: str):
    """Analyzes Python code for syntax errors."""
    try:
        ast.parse(code)
        return []  # No syntax errors
    except SyntaxError as e:
        return [f"Syntax Error: {e.msg} at line {e.lineno}, column {e.offset}"]

def analyze_code_style(code: str):
    """Analyzes Python code for PEP8 style violations using pylint."""
    pylint_output = StringIO()
    reporter = TextReporter(pylint_output)
    pylint.lint.Run(['--from-stdin'], reporter=reporter, do_exit=False)
    return pylint_output.getvalue().strip().split('\n')

def analyze_code_efficiency(code: str):
    """Finds inefficient patterns in the code."""
    inefficiencies = []
    if re.search(r'for\s+\w+\s+in\s+range\(len\(', code):
        inefficiencies.append("Use enumerate() instead of range(len(...))")
    if re.search(r'if\s+\w+\s+==\s+True', code):
        inefficiencies.append("Use 'if variable' instead of 'if variable == True'")
    return inefficiencies

def provide_recommendations(code: str):
    """Provides recommendations based on analysis results."""
    recommendations = []
    syntax_issues = analyze_code_syntax(code)
    style_issues = analyze_code_style(code)
    efficiency_issues = analyze_code_efficiency(code)
    
    if syntax_issues:
        recommendations.extend(syntax_issues)
    if style_issues:
        recommendations.extend(style_issues)
    if efficiency_issues:
        recommendations.extend(efficiency_issues)
    
    return recommendations

if __name__ == "__main__":
    test_code = """
    def example():
        x = 5
        for i in range(len([1, 2, 3])):
            print(i)
    """
    
    results = provide_recommendations(test_code)
    for issue in results:
        print(issue)
