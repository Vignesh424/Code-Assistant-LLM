import streamlit as st
import os, traceback
from dotenv import load_dotenv 
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#Define the Model Function
def google_gemini_response(question, prompt):
   model = genai.GenerativeModel('gemini-2.0-flash')
   response = model.generate_content([prompt[0],question])
   return response.text

#Define the Prompt

prompt = ["""

You are an expert in providing code in any programming language.
 You should be getting a question like below
 '1.Provide me a Python code for generation of Pascal Traingle'
 '2.Provide me a C++ Code for generation of Floyds Triangle'

 Your job is to give the complete code with comments wherever
required and also show example usecase
"""]

#Streamlit App
st.title('Coding Assistant in any Programming Language')
question = st.text_input("You give the question, I will give you the code", key='input')
submit = st.button("Submit")

if submit:
   try:     
      response = google_gemini_response(question,prompt)
      #print(f"Generated Reponse",{response})
      st.write(response)
    
   except Exception as e:
      print('Error. Please try again')
      traceback.print_exc()


    