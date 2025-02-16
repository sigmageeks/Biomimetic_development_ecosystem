import sys
import os

# Add the project's root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import core.code_analyzer as code_analyzer
import core.genetic_algorithm as genetic_algorithm
import core.optimizer as optimizer
import core.self_healing as self_healing

def main():
    st.title("Biomimetic Dev Ecosystem")
    st.sidebar.header("Options")
    
    option = st.sidebar.selectbox("Choose a feature", [
        "Code Analysis", "Genetic Optimization", "Self-Healing Code"
    ])
    
    code_input = st.text_area("Enter your Python code here:")

    if st.button("Run Analysis"):
        if option == "Code Analysis":
            if not code_input.strip():
                st.warning("Please enter Python code before running the analysis.")
                return

            optimized_code = optimizer.optimize_code_format(code_input)
            execution_time = optimizer.measure_execution_time(code_input)
            memory_usage = optimizer.measure_memory_usage(code_input)
            suggestions = optimizer.suggest_optimizations(code_input)

            st.subheader("Optimized Code")
            st.code(optimized_code, language='python')
            st.write(f"Execution Time: {execution_time:.6f} seconds")
            st.write(f"Memory Usage: {memory_usage:.6f} MB")
            st.write("Suggestions:", suggestions)

        elif option == "Genetic Optimization":
            if not code_input.strip():
                st.warning("Please enter Python code before running optimization.")
                return

            # Define parameters
            pop_size = 10
            gene_length = len(code_input.split())  # Count words instead of characters
            generations = 20

            # Run genetic algorithm
            best_solution, best_fitness = genetic_algorithm.genetic_algorithm(pop_size, gene_length, generations)

            # Convert binary result to a valid Python code format
            optimized_code = "".join(chr(int("".join(map(str, best_solution[i:i+8])), 2)) for i in range(0, len(best_solution), 8))

            st.subheader("Optimized Code Using Genetic Algorithm")
            st.code(optimized_code, language='python')
            st.write(f"Best Fitness Score: {best_fitness}")


        elif option == "Self-Healing Code":
            if not code_input.strip():
                st.warning("Please enter Python code before running self-healing.")
                return

            repaired_code, fix_message, execution_result = self_healing.analyze_and_repair_code(code_input)
            st.subheader("Repaired Code")
            st.code(repaired_code, language='python')
            st.write("Fix Message:", fix_message)
            st.write("Execution Result:", execution_result)

if __name__ == "__main__":
    main()