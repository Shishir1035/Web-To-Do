import streamlit as st
import functions

def add_todo():
    txt = st.session_state['newtodo']   # shows information about an element using their key
    functions.write('todo.txt', txt+'\n', 'a')
    txt = ''
st.title("ToDo App")
st.subheader("Personal ToDo App")
st.write("Trying to learn something")

todos = functions.read('todo.txt')
for index, todo in enumerate(todos):
    todo.strip('\n')
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write('todo.txt', todos, 'w')
        del st.session_state[todo]
        st.experimental_rerun()

todo = None
todo = st.text_input(label="",placeholder="Enter a todo....",
                     on_change=add_todo, key='newtodo')

