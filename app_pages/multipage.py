import streamlit as st

# Class to generate multiple Streamlit pages using an object oriented approach 
class MultiPage: 

    def __init__(self) -> None:
        self.pages = []

        st.set_page_config(
            page_title="Predictive Analytics - CI - Walkthrough Project 1",
            page_icon="🖥️")
        # check links below for additional icons reference
        # https://docs.streamlit.io/en/stable/api.html#streamlit.set_page_config
        # https://twemoji.maxcdn.com/2/test/preview.html
    
    def add_page(self, title, func) -> None: 
        self.pages.append({"title": title, "function": func })

    def run(self, app_name):
        st.title(app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']() # run a function related to a page 