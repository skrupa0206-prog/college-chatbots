import streamlit as st

# Page title
st.set_page_config(page_title="College Enquiry Chatbot")

# Heading
st.title("College Enquiry Chatbot")

st.write("Ask your college-related questions below.")

# Responses
responses = {
    "name": "Shanthinikethan College.",
    "courses": "B.Tech (Computer Science), B.Tech (Electronics & Communication), MBA, B.Sc (Physics).",
    "fees": "Average yearly fees is around ₹50,000.",
    "admission": "Admissions are accepted online via the college portal. Entrance exam scores like EAMCET, JEE, CAT are required.",
    "contact_email": "admissions@shanthinikethan.edu",
    "contact": "+91-xxxx-xxxxxx",
    "location": "Our college is located in Ramanagar, India.",
    "library": "Our library contains more than 20,000 books.",
    "placement": "Top companies visit our campus every year.",
    "sports": "The college has cricket, football, basketball and indoor sports facilities."
}

# Session state
if "question" not in st.session_state:
    st.session_state.question = ""

if "reply" not in st.session_state:
    st.session_state.reply = ""

# Input box
user_input = st.text_input("Ask Your Question", key="question")

# Buttons
col1, col2 = st.columns(2)

# Send button
with col1:

    if st.button("Send"):

        reply = "Sorry, I don't understand."

        for key in responses:

            if key in user_input.lower():

                reply = responses[key]
                break

        st.session_state.reply = reply

# Clear button
with col2:

    if st.button("Clear"):

        st.session_state["question"]
        st.session_state.reply = ""
        st.rerun()

# Show response
if st.session_state.reply:
    st.success(st.session_state.reply)