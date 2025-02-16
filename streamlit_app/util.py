import streamlit as st
import os
import time

def save_uploaded_file(uploaded_file, directory="uploads"):
    """Saves an uploaded file to the specified directory."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def display_status(message, duration=2):
    """Displays a temporary status message."""
    with st.spinner(message):
        time.sleep(duration)
    st.success("Done!")

def format_code_snippet(code):
    """Formats and highlights code snippets for display."""
    return f"```python\n{code}\n```"

if __name__ == "__main__":
    st.write("Utility functions module.")
