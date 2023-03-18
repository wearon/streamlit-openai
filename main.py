# Importing required packages
import streamlit as st
import openai
import os
from dotenv import load_dotenv
from streamlit_pills import pills

load_dotenv()

# Get the OpenAI API key from the environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.subheader("AI Assistant : Streamlit + OpenAI: `stream` *argument*")

# You can also use radio buttons instead
selected = pills("", ["NO Streaming", "Streaming"], ["🎈", "🌈"])


st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to interact with
       the OpenAI API's implementation of the ChatGPT model.
       Enter a **query** in the **text box** and **press enter** to receive
       a **response** from the ChatGPT
       '''
    )


user_input = st.text_input("You: ",placeholder = "Ask me anything ...", key="input")

if st.button("Submit", type="primary"):
    st.markdown("----")
    res_box = st.empty()
    
    if selected == "Streaming":
        report = []
        # Looping over the response
        for resp in openai.Completion.create(model='text-davinci-003',
                                            prompt=user_input,
                                            max_tokens=120, 
                                            temperature = 0.5,
                                            stream = True):
            # join method to concatenate the elements of the list 
            # into a single string, 
            # then strip out any empty strings
            report.append(resp.choices[0].text)
            result = "".join(report).strip()
            result = result.replace("\n", "")        
            res_box.markdown(f'*{result}*') 
            
    else:
        completions = openai.Completion.create(model='text-davinci-003',
                                            prompt=user_input,
                                            max_tokens=120, 
                                            temperature = 0.5,
                                            stream = False)
        result = completions.choices[0].text
        
        res_box.write(result)
st.markdown("----")