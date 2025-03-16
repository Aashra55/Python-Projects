import streamlit as st 
import os
import json

LIBRARY = "books_data.json"

def load_books():
    if not os.path.exists(LIBRARY):
        with open (LIBRARY, "w") as file:
            json.dump([], file)
        return []
    else:
        try:
            with open(LIBRARY, "r") as file:
                return json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            return []

def save_books(book):
    with open(LIBRARY, "w") as file:
        json.dump(book, file, indent=4)

def add_book(name, content, author):
    books = load_books()
    books.append({
        "name": name,
        "content": content,
        "author": author
    })
    save_books(books)

def remove_book(name):
    books = load_books()
    updated_books = [book for book in books if book["name"].strip().lower() != name.strip().lower()]
    if len(updated_books) == len(books):
        st.warning(f"Book **{name}** not found!")
    else: 
        save_books(updated_books)
        st.success(f"Book **{name}** removed successfully!")
        
def update_book(input_name,name, content, author):
    books = load_books()
    for book in books:
        if book["name"].strip().lower() == input_name.strip().lower():
            if name:
                book["name"] = name
            if content:
                book["content"] = content
            if author:
                book["author"] = author
            save_books(books)
            st.success(f"Book **{input_name}** updated successfully!")
            break
        
# Streamlit UI

st.set_page_config(
    page_title="Personal Library Manager",
    page_icon="📚", 
    layout="wide"
)

st.title("📚 Personal Library Manager")

option = st.sidebar.radio(
    "🔍 **What would you like to do?**",
    ["➕ Add a Book", "📖 View Books", "❌ Delete a Book", "✏️ Update a Book", "🔎 Search for a Book"]
)    

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
    
elif option == "❌ Delete a Book":
    st.subheader("❌ Delete a Book")
    name = st.text_input("Name of book")
    if st.button("🧹 Remove Book"):
        remove_book(name)
        
elif option == "✏️ Update a Book":
    st.subheader("✏️ Update a Book")
    st.warning("Please enter the name of the book you want to update.")
    input_name = st.text_input("Name of book")
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
        else:
            update_book(input_name, name, content, author)
            
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
    