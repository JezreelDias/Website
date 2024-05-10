import streamlit as st
from streamlit_option_menu import option_menu
#with st.sidebar:
#    option_menu(menu_title = "Pages",options = ["Jezreel","Videos","Selector","Feedback"])
st.title("Jezreel's Website")
tab1,tab2,tab3 = st.tabs(["Jezreel","All about me!","Contact info"])
with tab1:
    st.subheader("Hi, My name is Jezreel! This is my webiste that I coded! I Hope you enjoy it!")
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/Screenshot 2024-04-25 at 5.42.06 PM.png")
with tab2:
    st.subheader("I love aviation and I know a lot about it. I also really like tech - phones, code, robots, A.I, etc... I know how to how to code in C++, Python, Java, HTML, and a few others. I like doing robotcs as a side hobby too.")
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/1000_F_294354542_pX8tXdAGZfmwwxRpcY6KLuIRHIicFy6v.jpg")
with tab3:
    st.subheader("You can call me at 650-772-1934 or email me at jezreeldias13@gmail.com")
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/phonemailatcall.jpg")