import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def render_dashboard():
    st.title("Development Insights Dashboard")
    st.write("### Overview of Code Performance and Optimization")
    
    # Sample Data (Replace with real metrics later)
    data = {
        "Metric": ["Execution Time (ms)", "Memory Usage (MB)", "Lines of Code Optimized"],
        "Before Optimization": [250, 12.5, 120],
        "After Optimization": [180, 9.8, 90]
    }
    df = pd.DataFrame(data)
    
    st.write("#### Performance Metrics Comparison")
    st.dataframe(df)
    
    # Visualization
    fig, ax = plt.subplots(figsize=(8, 5))
    df_melted = df.melt(id_vars=["Metric"], var_name="Stage", value_name="Value")
    sns.barplot(data=df_melted, x="Metric", y="Value", hue="Stage", ax=ax)
    plt.xticks(rotation=15)
    plt.ylabel("Value")
    plt.xlabel("Metric")
    plt.title("Performance Improvement")
    st.pyplot(fig)
    
    st.write("### Code Optimization Insights")
    st.write("- Significant reduction in execution time and memory usage.")
    st.write("- Improved code efficiency through AI-powered optimization.")
    st.write("- Self-healing mechanisms successfully detected and resolved issues.")

if __name__ == "__main__":
    render_dashboard()
