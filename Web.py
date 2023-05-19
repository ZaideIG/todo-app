import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("->This app will increase your Productivity")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo: ", placeholder="Add new todo...")
