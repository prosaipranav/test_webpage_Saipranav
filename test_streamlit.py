# pip install streamlit in the directory of the code
# melby !!! to run the code go to the directory of the code and type streamlit run [file_name] ... here the file_name is test_strealit.py
# streamlit run test_streamlit.py  <----- type this to your cmd 
import streamlit as st
import time as t 
#title
st.title("Welcome Saipranav :wave:") 
st.write("---")

#header
st.header("Machine learning ")

#subheader
st.subheader("linear regrssion")

#info
st.info("information about the user")

#Warning message
st.warning("Come on time or you will be marked absent")

#write
st.write("Student name")
st.write("range(50)") 
st.write(range(50)) # to get in coding format

#Error message 
st.error("Wrong password")

#Success message
st.success("Nice you got a Award !!!")

#Markdown 
st.markdown("# Saipranav")
st.markdown("## Saipranav")
st.markdown("### Saipranav")     # by adding hashtags you can reduce the size of the text 
st.markdown("#### Saipranav")
st.markdown("##### Saipranav")
st.markdown("###### Saipranav")
st.markdown(":moon:")   # to use emoji 

#Caption
st.caption("Caption is here")

#to display a mathematical equation using latex()
st.latex(r'''a+b^2+c''')

#to display image
st.image("brawlstarsloading1.jpg")
st.image("brawlstarsloading.jpg")

#----- WIDGETS -----
#checkbox
st.checkbox("login")
st.checkbox("password")
st.checkbox("email")

#button
st.button("click")

#radio
st.radio("pick your gender",["Male","Female","Other"])

#selectbox
st.selectbox("pick your course",["ML","NLP","Data Science"])

#multiselect
st.multiselect("choose your work space",["Home","Office","Park"])

#Selectsilder
st.select_slider("ratings",["Bad","Good","Best",])

#slider
st.slider("What is your age ?",1,100)\

#to input a number 
st.number_input("pick a number ",0,100)

#to input a text 
st.text_input("enter your text")

#time_input
st.time_input("enter your time of birth")

#date_input
st.date_input("enter your data of birth ")

#text area ..... to print text for more than one line 
st.text_area("write your thoughts !!")

#to upload a file
st.file_uploader("upload your birth certificate.")

#to pick a color
st.color_picker("pick your favorite color")

#to show the progress
st.progress(85)

#spinner to display a temporary waiting msg
with st.spinner("just wait"):
    t.sleep(2)
    

#to display balloons 
st.balloons()

#--- SIDE BAR ---
st.sidebar.title("Welcome Saipranav")
st.sidebar.text_input("enter your name")
st.sidebar.text_input("enter your username")
st.sidebar.text_input("enter your password")
st.sidebar.button("Submit")
st.sidebar.radio("Are you a ",["Student","Teacher","Web Developer"])