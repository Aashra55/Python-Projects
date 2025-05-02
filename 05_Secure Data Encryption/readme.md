# 🔒 Secure Data Encryption System

A simple yet powerful **Streamlit-based web app** for securely encrypting, storing, and retrieving sensitive data with your personal passkey.  
This system uses **Fernet encryption** and **SHA256 hashing** for enhanced security, all handled locally with persistent JSON storage.

---

## 📜 Features

- 🔑 **User Authentication:**  
  - Create an account with a username and master password  
  - Login to access encrypted data securely  

- 🔐 **Data Encryption:**  
  - Enter your sensitive data and passkey  
  - Data is encrypted using **Fernet symmetric encryption**  
  - Encrypted data is saved locally and securely  

- 🔓 **Data Decryption:**  
  - Retrieve your encrypted data  
  - Decrypt it by providing the correct passkey  
  - Incorrect attempts are limited to **3 tries** before logout  

- 📃 **View Encrypted Data:**  
  - View a list of all your encrypted records safely

- 🔒 **Persistent Storage:**  
  - Data and user credentials are stored in JSON files (`data.json` & `users.json`)

- ✨ **Clean, Interactive UI:**  
  - Built using **Streamlit**  
  - Sidebar navigation  
  - User-friendly notifications  

---

## 📁 Project Structure

```bash
📦 secure-data-encryption-system/
 ├── 📄 data.json              # Encrypted data storage
 ├── 📄 users.json             # User credentials (hashed passwords)
 ├── 📄 app.py                 # Main Streamlit app code
 └── 📄 README.md              # This file
```

---

## 🛠️ How It Works

1. **Create an account**
2. **Login with your credentials**
3. **Store data** — type your message and set a passkey, encrypt and save it
4. **Retrieve data** — paste your encrypted message and enter the passkey to decrypt it
5. **View your encrypted records**
6. **Logout securely**

---

## 📦 Installation & Usage

### 🔽 Install Dependencies  
Ensure Python 3.8+ is installed, then install required packages:
```bash
pip install streamlit cryptography
```

### ▶️ Run the App
```bash
streamlit run app.py
```

---

## 🔒 Security Highlights

- **SHA256 Hashing:**  
  Used to securely hash passkeys before storing and verifying.

- **Fernet Encryption (Symmetric):**  
  - Passkey is hashed to generate an encryption key  
  - Data is encrypted with this key  
  - Decryption requires the same passkey  

- **Local Persistent Storage:**  
  No external servers or databases — everything remains on your machine in JSON files.

---

## 📌 To-Do / Ideas

- ⏳ Add **password recovery (security question / hint)**  
- 📝 Add **note titles** / categories  
- 🔒 Encrypt stored JSON files further  
- 📊 Analytics (number of records stored, last login, etc.)

---

## 📚 Tech Stack

- **Python 3**
- **Streamlit**
- **Cryptography**
- **Hashlib**
- **JSON / Local storage**

---

## 📑 License

This project is for educational and personal use only.  
Feel free to fork and improve!


