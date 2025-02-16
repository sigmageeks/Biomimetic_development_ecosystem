import streamlit as st

def render_sidebar():
    st.sidebar.header("Navigation")
    option = st.sidebar.radio("Choose a feature:", [
        "Code Analysis", 
        "Genetic Optimization", 
        "Self-Healing Code", 
        "Performance Dashboard"
    ])
    
    st.sidebar.write("---")
    st.sidebar.subheader("Settings")
    enable_logs = st.sidebar.checkbox("Enable Debug Logs")
    auto_fix = st.sidebar.checkbox("Auto-Fix Detected Issues")
    optimization_level = st.sidebar.selectbox("Optimization Level", ["Basic", "Advanced", "Aggressive"])
    
    st.sidebar.write("---")
    st.sidebar.write("**Project Info**")
    st.sidebar.write("Biomimetic Dev Ecosystem v1.0")
    st.sidebar.write("Developed by Uday")
    
    return option, enable_logs, auto_fix, optimization_level

if __name__ == "__main__":
    render_sidebar()
