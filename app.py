import streamlit as st
import base64

# Render the HTML
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()
st.components.v1.html(html, height=2000, scrolling=True)

# Add working download button
with open("MemeSense_Investor_OnePager.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    href = f'<a href="data:application/pdf;base64,{base64_pdf}" download="MemeSense_Investor_OnePager.pdf"><button style="margin-top:20px;padding:10px 20px;background-color:#e91e63;border:none;border-radius:6px;color:white;font-weight:bold;font-size:14px;cursor:pointer;">📄 Download Our One-Pager</button></a>'
    st.markdown(href, unsafe_allow_html=True)
