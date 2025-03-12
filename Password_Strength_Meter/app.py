import streamlit as st 
import re
import string
import secrets

def generate_strong_password(length=12):
    """Generates a strong random password containing at least one uppercase letter,
       one digit, and one special character."""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.isupper() for c in pwd) and 
            any(c.isdigit() for c in pwd) and 
            any(c in "!@#$%^&*()_+" for c in pwd)):
            return pwd

def check_password_strength(password):
    """Checks the strength of the password and returns a score and feedback."""
    
    strength = 0
    feedback = []
    
    # check the length of password
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    #check uppercase in the password
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")
        
    #check number in the password
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
        
    #check special characters in the password
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")
        
    # Determine Strength
    if strength == 4:
        return "Strong", "✅ Your password is strong!"
    elif strength == 3:
        return "Medium", "⚠️ Your password is okay, but could be stronger."
    else:
        return "Weak", "❌ Your password is weak. Consider improving it.", feedback
    
# Streamlit UI
st.set_page_config(
    page_title="🔐 Password Strength Meter", 
    layout="wide",
    page_icon="🔑"
)

if 'history' not in st.session_state:
    st.session_state.history=[]

if 'suggestion' not in st.session_state:
    st.session_state.suggestion = generate_strong_password()

st.title("🔐 Password Strength Meter")

st.info(f"Suggested strong password: **{st.session_state.suggestion}**")

if st.button("Generate New Strong Password"):
    st.session_state.suggestion = generate_strong_password()

name = st.text_input("Enter username")
password = st.text_input("Enter your password", type="password")
button = st.button('Save')
if password:
    strength, message, *extra_feedback = check_password_strength(password)
    if strength == "Weak":
        color = "#e74c3c"
    elif strength == "Medium":
        color = "#f1c40f"
    elif strength == "Strong":
        color = "#27ae60"
    else:
       color = "black"  
    st.markdown(f"**Strength:**<span style='color: {color}; font-weight: bold;'>{strength}</span>", unsafe_allow_html=True)
    st.info(message)
    if button:
        if any(pwd == password for _, pwd in st.session_state.history):
            st.warning("Please enter a password differ than previous one!") 
        else: 
            st.session_state.history.append((name, password))
    
    #improvement suggestions in case if password is weak
    if strength == "Weak":
        st.warning("💡 Suggestions to improve:")
        if extra_feedback and extra_feedback[0]:  
            for tip in extra_feedback[0]:  
                st.write(f"- {tip}") 
        st.success(f"Try a stronger password, e.g., **{st.session_state.suggestion}**")

                 
with st.sidebar:
    st.title("🔑 Password History")
    for name, password in st.session_state.history:
        st.markdown(f"{name}<br>🗝 {password}", unsafe_allow_html=True)


