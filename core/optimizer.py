import ast
import autopep8
import time
import psutil

def measure_execution_time(code: str):
    """Measures the execution time of a given Python code snippet."""
    start_time = time.time()
    exec(code, globals())
    return time.time() - start_time

def measure_memory_usage(code: str):
    """Measures memory usage of a given Python code snippet."""
    process = psutil.Process()
    before_memory = process.memory_info().rss
    exec(code, {})
    after_memory = process.memory_info().rss
    return (after_memory - before_memory) / (1024 * 1024)  # Convert to MB

def optimize_code_format(code: str):
    """Formats the code using autopep8 for better readability and efficiency."""
    return autopep8.fix_code(code)

def suggest_optimizations(code: str):
    """Analyzes the code and suggests potential optimizations."""
    tree = ast.parse(code)
    suggestions = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.For):
            if any(isinstance(child, ast.Call) and getattr(child.func, 'id', '') == 'range' for child in ast.iter_child_nodes(node)):
                suggestions.append("Consider using list comprehensions or map/filter instead of loops where possible.")
        if isinstance(node, ast.If):
            if isinstance(node.test, ast.Compare) and isinstance(node.test.ops[0], ast.Eq):
                suggestions.append("Use 'if variable' instead of 'if variable == True' where applicable.")
    
    return suggestions

if __name__ == "__main__":
    sample_code = """
    x = [i for i in range(10)]
    for i in range(len(x)):
        print(x[i])
    if x:
        print("List is not empty")
    """
    
    optimized_code = optimize_code_format(sample_code)
    execution_time = measure_execution_time(sample_code)
    memory_usage = measure_memory_usage(sample_code)
    optimizations = suggest_optimizations(sample_code)
    
    print("Optimized Code:")
    print(optimized_code)
    print("Execution Time:", execution_time, "seconds")
    print("Memory Usage:", memory_usage, "MB")
    print("Suggestions:", optimizations)
