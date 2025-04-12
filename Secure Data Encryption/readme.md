# 🔒 Secure Data Encryption System

Welcome to **Secure Data Encryption System** — a secure web app built with **Streamlit** that allows users to:
- **Create accounts and log in securely**
- **Encrypt and store sensitive data**
- **Decrypt and retrieve their data using a secure passkey**

All data is safely stored in local JSON files, protected by encryption and hashed passkeys.

---

## 📑 Features

✅ User authentication system with:
- **Account creation**
- **Login with hashed passwords**
- **Multiple failed attempt handling**

✅ Secure data encryption using:
- **SHA256 for passkey hashing**
- **Fernet symmetric encryption with derived keys**

✅ Simple and intuitive Streamlit web interface:
- Store encrypted data with a passkey
- Retrieve decrypted data with the correct passkey
- Manage user accounts
- Logout functionality

---

## 📂 Project Structure

```
📁 your-project/
 ├── 📄 app.py               # Main Streamlit app
 ├── 📄 data.json            # Encrypted data storage (auto-generated)
 ├── 📄 users.json           # User credentials storage (auto-generated)
 ├── 📄 README.md            # Project documentation
```

---

## 💻 Installation & Setup

### 1️⃣ Install required libraries

```bash
pip install streamlit cryptography
```

### 2️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🔐 How It Works

### 📌 Create a New Account
- Go to **Create Account**
- Enter a **username** and **password**
- The password is hashed and stored securely

### 📌 Login
- Enter your **username** and **master password**
- Password is hashed and compared for authentication
- If failed 3 times → user is logged out automatically

### 📌 Store Data
- Enter data to encrypt
- Enter a passkey (used only for this data)
- Data is encrypted and saved locally with the hashed passkey

### 📌 Retrieve Data
- Enter the encrypted data string
- Enter the correct passkey used while storing
- The app decrypts and shows the original data

---

## 🔒 Security Notes

- **Passwords and passkeys are never stored in plain text**
- **Passwords are hashed with SHA256**
- **Data is encrypted using Fernet symmetric encryption with keys derived from the passkey**
- **Three-strike limit** on incorrect passkey attempts before logout

---

## 📌 Technologies Used

- [Streamlit](https://streamlit.io/)
- [Cryptography](https://cryptography.io/)
- [Python hashlib](https://docs.python.org/3/library/hashlib.html)
- JSON file handling


## 📝 Author

**Aashra Saleem**  
*Python + Streamlit developer, passionate about secure apps and clean UI.*

