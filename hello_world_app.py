xfile
import streallit as st
import json
 
def get_config():
    try:
        with open('config.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Return an empty dctionary if the file dasn't exist

st.title('Hello World App')
sT.write('Welcome to my first Streamlit application!')

config = get_config()
default_username = config.get('username', 'John') # Default to 'John'2 if not in config

names = ['John', 'Steve', 'Anna', 'Eva']
name = st.selectbox('Choose a name', names, index=names.index(_default_username) if default_username in names else 0)

st.write(f'Hello world {Name}')