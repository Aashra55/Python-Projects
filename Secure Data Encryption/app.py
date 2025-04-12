# 📌 Importing required libraries
import streamlit as st  # Streamlit for web app interface
import hashlib          # For hashing passkeys securely
from cryptography.fernet import Fernet  # For encryption and decryption
import base64          # For encoding and decoding data
import os            # For file operations
import json         # For JSON file operations

DATA_FILE = "data.json"  # File to store encrypted data
USERS_DATA = "users.json"  # File to store user data

# 📌 Function to load encrypted data from the JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {} 

# Function to save encrypted data to the JSON file
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(st.session_state.stored_data, f, indent=4)

# 📌 Function to load user data from the JSON file
def load_users_data():
    if os.path.exists(USERS_DATA):
        with open(USERS_DATA, "r") as f:
            return json.load(f)
    return {}

# 📌 Function to save user data to the JSON file
def save_user_data():
    with open(USERS_DATA, "w") as f:
        json.dump(st.session_state.users_data, f, indent=4)

# 📌 Function to hash passkey using SHA256
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# 📌 In-memory dictionary for storing encrypted data and hashed passkeys
if "stored_data" not in st.session_state:
    st.session_state.stored_data = load_data()

# 📌 Initialize session state for login and failed attempts
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 📌 Initialize session state for user data
if "users_data" not in st.session_state:
    st.session_state.users_data = load_users_data()

# 📌 Initialize session state for failed attempts   
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

# 📌 Initialize page state
if "page" not in st.session_state:
    st.session_state.page = "login"

# 📌 Authorization page function
def auth_page():
    st.title("🔑 Authorization Page")
    st.write("Please create your account to access the system.")
    username = st.text_input("Enter Username: ")
    password = st.text_input("Enter Password: ", type="password")
    
    if st.button("🔒 Create Account"):
        if username and password:
            if username in st.session_state.users_data:
                st.error("❌ Username already exists! Please choose another one.")
            else:
                hashed_password = hash_passkey(password)
                st.session_state.users_data[username] = hashed_password
                st.success("✅ Account created successfully!")
                save_user_data()
                st.session_state.logged_in = True
    st.info("🔑 If you alreadty have an account, please login!")
    if st.button("🔑 Log in"):
        st.session_state.page = "login"
        st.rerun()

# 📌 Login page function
def login_page():
    st.title("🔑 Login Page")
    username = st.text_input("Enter Username: ")
    password = st.text_input("Enter Master Password: ", type="password")
    hashed_password = hash_passkey(password)
    if st.button("🔐 Login"):
        if username in st.session_state.users_data:
            if hashed_password == st.session_state.users_data[username]:
                st.session_state.logged_in = True
                st.session_state.failed_attempts = 0
                st.success("✅ Login successful!")
                st.rerun() # Refresh the app and go to main page
            else:
                st.error("❌ Incorrect password!")
        else:
            st.error("❌ Username not found!")
    st.info("🔒 If you don't have an account, please create one!")
    if st.button("📝 Create Account"):
        st.session_state.page = "auth"
        st.rerun()

# 📌 Main application function
def main_app():
    st.title("🔒 Secure Data Encryption System")
    
    # 📌 Sidebar navigation
    menu = ["🏠 Home", "🔐 Store Data", "🔓 Retrieve Data", "📝 New Account", "🔒 Logout"]
    choice = st.sidebar.selectbox("📑 Navigation", menu)

    # 📌 Home Section
    if choice == "🏠 Home":
        st.subheader("Welcome to Secure Data System")
        st.write("Use this app to **securely store and retrieve data**.")
        
    # 📌 Store Data Section
    elif choice == "🔐 Store Data":
        st.subheader("🔐 Store Your Data Securely")
        user_data = st.text_area("Enter data to encrypt:")
        passkey = st.text_input("Enter passkey:", type="password")
                
        # 📌 Generate a random encryption key (valid only during current session)
        def generate_key_from_passkey(passkey):
            hashed = hashlib.sha256(passkey.encode()).digest()
            return base64.urlsafe_b64encode(hashed)
        key = generate_key_from_passkey(passkey)
        
        # 📌 Create a cipher object for encryption and decryption using the generated key
        global cipher
        cipher = Fernet(key)
        
        # 📌 Function to encrypt plain text data
        def encrypt_data(data):
            return cipher.encrypt(data.encode()).decode()

        
        if st.button("🔒 Encrypt & Save"):
            if user_data and passkey:
                hashed_passkey = hash_passkey(passkey)
                encrypted_data = encrypt_data(user_data)
                st.session_state.stored_data[encrypted_data] = hashed_passkey
                save_data()  # Save encrypted data to JSON file
                st.success("✅ Data encrypted and stored successfully!")
                st.write("📋 Your Encrypted Data:")
                st.code(encrypted_data)
            else:
                st.error("⚠️ Please enter both data and passkey!")
                
    # 📌 Retrieve Data Section
    elif choice == "🔓 Retrieve Data":
        st.subheader("🔓 Retrieve Your Data")
        encrypted_input = st.text_area("🔐 Enter your Encrypted Data:")
        passkey_input = st.text_input("🔑 Enter your passkey:", type="password")
        
        # 📌 Function to generate encryption key from passkey
        def generate_key_from_passkey(passkey):
            hashed = hashlib.sha256(passkey.encode()).digest()
            return base64.urlsafe_b64encode(hashed)

        # 📌 Function to decrypt encrypted data
        def decrypt_data(encrypted_data):
            key = generate_key_from_passkey(passkey_input)  # Derive key from passkey again
            cipher = Fernet(key)  # Create cipher using this key
            return cipher.decrypt(encrypted_data.encode()).decode()

        if st.button("🔍 Decrypt & Retrieve"):
            if encrypted_input and passkey_input:
                hashed_passkey_input = hash_passkey(passkey_input)
                    
                # Check if the encrypted data exists and passkey matches
                if encrypted_input in st.session_state.stored_data:
                    if st.session_state.stored_data[encrypted_input] == hashed_passkey_input:
                        decrypted_data = decrypt_data(encrypted_input)
                        st.success("✅ Data Decrypted Successfully!")
                        st.write("📖 Your original data:")
                        st.code(decrypted_data)
                        st.session_state.failed_attempts = 0
                    else:
                        st.session_state.failed_attempts += 1
                        remaining_attempts = 3 - st.session_state.failed_attempts
                        
                        if remaining_attempts > 0:
                            st.error(f"❌ Incorrect passkey! ⚠️ Attempts remaining: {remaining_attempts}")
                        else:
                            st.error("❌ Too many failed attempts! Redirecting to login page.")
                            st.session_state.logged_in = False
                            st.rerun()
                else:
                    st.error("❌ Encrypted data not found!")
            else:
                st.error("⚠️ Please fill both fields!")
    
    # 📌 New Account Section 
    elif choice == "📝 New Account":
        st.subheader("🔑 Create New Account")
        username = st.text_input("Enter Username: ")
        password = st.text_input("Enter Password: ", type="password")
        
        if st.button("🔒 Create New Account"):
            if username and password:
                if username in st.session_state.users_data:
                    st.error("❌ Username already exists! Please choose another one.")
                else:
                    hashed_password = hash_passkey(password)
                    st.session_state.users_data[username] = hashed_password
                    st.success("✅ Account created Successfully!")
                    save_user_data()
    
    # 📌 Logout Section
    elif choice == "🔒 Logout":
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.session_state.stored_data = {}
        st.success("✅ Logged out successfully!")
        st.rerun()

# 📌 App control — show login or main app based on login status
if st.session_state.logged_in:
    main_app()
elif st.session_state.page == "auth":
    auth_page()
elif st.session_state.page == "login":
    login_page()
else:
    login_page()


