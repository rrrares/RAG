import streamlit as st
import query_data

st.image("data/NordicRPA logo.png")
st.title("The Nordic RPA Question Answerer")

# Prompt user for input
input_text = st.text_input("Ask your questions here")

# Button to submit the query
if st.button('Search'):
    if input_text:  # Check if input_text is not empty
        # Process the input text
        response = query_data.return_response(input_text)
        if response is not None:
            answer, references = response
        else:
            answer = 'Cannot find answer'
            references = 'Cannot find answer'

        # Display the answer and references
        st.header('Here is the answer to your question:')
        st.write(answer)  # Assuming answer is a string or can be displayed by st.write
        st.subheader('References:')
        st.write(references)  # Assuming references can be displayed by st.write
    else:
        st.error("Please input a non-empty text")
