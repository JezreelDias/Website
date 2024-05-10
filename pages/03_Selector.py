import streamlit as st
st.number_input("Age in years :date:",min_value = 0, max_value = 100)
a,b = st.columns([0.5,0.56])
a.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/230818094951-jetzero-design-coastline.jpg")
b.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/istockphoto-136578178-612x612.jpg")
engines = st.selectbox("Engine",("Turboprop/Propeller","Turbofan/Jet","Scram/Ramjet/Rocket"))
if engines == "Turboprop/Propeller":
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/pilatus-2382567_1280.jpg")
if engines == "Turbofan/Jet":
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/turbojet_jet_engine_image.jpeg")
if engines == "Scram/Ramjet/Rocket":
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/mach_10_scram_xn4tf7u.webp")

size = st.number_input("Size",min_value = 0, max_value = 5)
if size == 0:
    st.title("Tiny")
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/airbus a3.jpeg")
if size == 1:
    st.title("Small")
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/16-1000_0200.jpg")
if size == 2:
    st.title("Medium")
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/a320.jpg")
if size == 3:
    st.title("Big")
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/A6-EDY_A380_Emirates_31_jan_2013_jfk_(8442269364)_(cropped).jpg")
if size == 4:
    st.title("Giant")
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/200429-F-GD886-9005.jpeg")
if size == 5:
    st.title("Humongous")
    st.image("/Users/grideldias/Desktop/Moonpreneur/Python/Website.py/Images/istockphoto-1351026716-612x612.jpg")
st.button("Submit:white_check_mark:")