# Personal Library Manager

## 📚 Overview
The **Personal Library Manager** is a simple book management app built using **Streamlit** and **Python**. It allows users to add, view, update, delete, and search for books in a personal digital library. The book data is stored in a JSON file for persistence.

## 🚀 Features
- **➕ Add a Book:** Store book details such as name, content, and author.
- **📖 View Books:** Display all books with their details.
- **✏️ Update a Book:** Modify book details.
- **❌ Delete a Book:** Remove a book from the library.
- **🔎 Search for a Book:** Find a book by its name.

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/personal-library-manager.git
cd personal-library-manager
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install streamlit
```

### 3️⃣ Run the Application
```bash
streamlit run app.py
```

## 📂 Project Structure
```
📁 personal-library-manager
│── 📄 app.py          # Main application file
│── 📄 books_data.json # JSON file storing book data
│── 📄 README.md       # Project documentation
```

## 🔄 How It Works
1. **Load & Store Books:** Data is managed using a JSON file (`books_data.json`).
2. **Streamlit UI:** The interface provides options for adding, updating, deleting, and searching books.
3. **Error Handling:** Ensures the app handles missing files and incorrect inputs gracefully.

## 🏗️ Future Enhancements
- 📌 Implement a rating and category system for books.
- 📌 Add a feature to export/import book data.
- 📌 Improve UI with better styling and interactivity.

## 💡 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## 📜 License
This project is licensed under the **MIT License**.

