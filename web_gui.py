import streamlit as st
import time

import functions as fn

now = time.strftime("%a %d.%m.%Y, %H:%M")
task_list = fn.get_tasks()

def add_task():
    new_task = st.session_state['task_entry']
    if new_task:
        msg = fn.addtask(new_task)
        st.toast(msg, icon="➕")

st.title("My Tasks")
st.subheader(now)

st.write("All my tasks:")

for i, task in enumerate(task_list):
    task_key = f'task_{i}'
    checkbox = st.checkbox(label=task, key=task_key)
    if checkbox:
        msg = fn.completetask(i)
        st.toast(msg, icon="❌")
        del st.session_state[task_key]
        time.sleep(0.4)
        st.rerun()

st.chat_input(placeholder="Add new task...", key='task_entry', on_submit=add_task)