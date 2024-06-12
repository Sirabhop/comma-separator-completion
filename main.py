import streamlit as st
import re

st.title('For those who need help 😜')
st.text('This website will separate, convert string to number, and add commas/single quotes.')

st.subheader("Paste your text here")
string_input = st.text_input('Input')
options = st.multiselect('Select options', ['Add single quotes', 'Convert to number']) 

if string_input and options:
    result = string_input  # Start with the original input

    # Apply options (order matters!)
    for option in options:

        if option == 'Add single quotes' and isinstance(result, str):
            # Split the string and add quotes to each part
            result = ", ".join([f"'{part}'" for part in result.split()])
        elif option == 'Convert to number':
            try:
                if isinstance(result, str):
                    result = [int(x) for x in re.findall(r'\d+', result)]
            except ValueError:
                st.error("Conversion to number failed. Input contains non-numeric characters.")
                break  # Stop processing if conversion fails

    st.subheader("Result:")
    
    # Display the result appropriately
    if isinstance(result, list):
        st.write(", ".join(map(str, result)))  # For lists of numbers
    else:
        st.write(result)  # For single strings
