import streamlit as st 
import os
import json

# File to store book data
LIBRARY = "books_data.json"

# Function to load books from the JSON file
def load_books():
    if not os.path.exists(LIBRARY):
        # Create an empty JSON file if it doesn't exist
        with open (LIBRARY, "w") as file:
            json.dump([], file)
        return []
    else:
        try:
            with open(LIBRARY, "r") as file:
                return json.load(file) # Load and return book data
        except(FileNotFoundError, json.JSONDecodeError):
            return [] # Return an empty list if there's an error

# Function to save book data to the JSON file
def save_books(book):
    with open(LIBRARY, "w") as file:
        json.dump(book, file, indent=4) # Save book list with indentation

# Function to add a new book
def add_book(name, content, author):
    books = load_books()
    books.append({
        "name": name,
        "content": content,
        "author": author
    })
    save_books(books) # Save updated book list

# Function to remove a book by name
def remove_book(name):
    books = load_books()
     # Ignore case and trim spaces for comparison
    updated_books = [book for book in books if book["name"].strip().lower() != name.strip().lower()]
    if len(updated_books) == len(books):
        st.warning(f"Book **{name}** not found!")  # Show warning if book isn't found
    else: 
        save_books(updated_books) # Save the updated book list
        st.success(f"Book **{name}** removed successfully!")

# Function to update book details        
def update_book(input_name,name, content, author):
    books = load_books()
    for book in books:
        if book["name"] == input_name:
            # Update book details only if a new value is provided
            if name:
                book["name"] = name
            if content:
                book["content"] = content
            if author:
                book["author"] = author
            save_books(books)
            st.success(f"Book **{input_name}** updated successfully!")
        
# Streamlit UI
 
# UI Configuration
st.set_page_config(
    page_title="Personal Library Manager",
    page_icon="📚", 
    layout="wide"
)

st.title("📚 Personal Library Manager")

# Sidebar Navigation Menu
option = st.sidebar.radio(
    "🔍 **What would you like to do?**",
    ["➕ Add a Book", "📖 View Books", "❌ Delete a Book", "✏️ Update a Book", "🔎 Search for a Book"]
)    

# Add a New Book Section
if option == "➕ Add a Book":
    st.subheader("➕ Add a Book")
    name = st.text_input("Book Name")
    content = st.text_area("Book Content")
    author = st.text_input("Author")
    
    if st.button("📒 Add Book"):
        if not name or not content or not author:
            st.warning("Please fill in all fields before adding a book.")
        else:
            add_book(name, content, author)
            st.success(f"Book **{name}** added successfully!")

# View Books Section        
elif option == "📖 View Books":
    st.subheader("📔 **My Library**")
    st.markdown("<br>", unsafe_allow_html=True)
    books = load_books()
    if books:
        for book in books:
            st.markdown(f"##### 📖 {book['name']}")
            st.markdown(f"**Author:** ***{book['author']}***")
            st.markdown(f"**Content:** {book['content']}")
            st.markdown("---")
    else:
        st.info("No books found in your library.")
    
# Delete a Book Section
elif option == "❌ Delete a Book":
    books = load_books()
    books_name = [book["name"] for book in books]
    st.subheader("❌ Delete a Book")
    name = st.selectbox("Select Book", books_name)
    if st.button("🧹 Remove Book"):
        remove_book(name)
        
# Update a Book Section       
elif option == "✏️ Update a Book":
    books = load_books()
    book_name = [book["name"] for book in books]
    st.subheader("✏️ Update a Book")
    st.warning("Please enter the name of the book you want to update.")
    input_name = st.selectbox("Select Book Name", book_name)
    st.markdown("<br>", unsafe_allow_html=True)
    st.warning("Please fill in the fields you want to update.")
    name = st.text_input("Book Name")
    content = st.text_area("Book Content")
    author = st.text_input("Author")
    
    if st.button("📝 Update book"):
        if not input_name and not name and not content and not author:
            st.error("Please fill out the required fields!")
        elif input_name and not name and not content and not author:
            st.error("Nothing to update!")
        elif input_name and (name or content or author):
            update_book(input_name, name, content, author)

# Search for a Book Section         
elif option == "🔎 Search for a Book":
    st.subheader("🔎 Search for a Book")
    books = load_books()
    book = [book for book in books]
    name = st.text_input("Seacrh here")
    if st.button("🚀 Search"):
        for book in books:
            if name.lower() == book['name'].lower():
                st.markdown(f"##### 📖 {book['name']}")
                st.markdown(f"**Author:** ***{book['author']}***")
                st.markdown(f"**Content:** {book['content']}")
            else:
                st.warning(f"Book **{name}** not found!")    
    
    