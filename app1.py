#div

import streamlit as st

st.title(' You can divide two numbers here')
a= st.number_input('ENTER FIRST NUMBER')


b =st.number_input('ENTER SECOND NUMBER')
if b == 0:
  a1=st.write(f'A/B = Undefined')
else:
  a1=st.write(f'A/B = {a/b}')
print(a1)
