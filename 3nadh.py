import tkinter as tk
from tkinter import messagebox
import csv
import os

CSV_FILE = 'library.csv'

def load_books():
    books = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, newline='') as f:
            reader = csv.DictReader(f)
            books = list(reader)
    return books

def save_books(books):
    with open(CSV_FILE, 'w', newline='') as f:
        fieldnames = ['Title', 'Author', 'Year', 'ISBN']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    isbn = entry_isbn.get()

    if not title or not author:
        messagebox.showwarning("Input error", "Title and Author are required.")
        return

    books = load_books()
    books.append({'Title': title, 'Author': author, 'Year': year, 'ISBN': isbn})
    save_books(books)
    messagebox.showinfo("Success", "Book added successfully!")
    listbox_books.insert(tk.END, f"{title} by {author}")

    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    entry_isbn.delete(0, tk.END)

def load_books_to_listbox():
    listbox_books.delete(0, tk.END)
    books = load_books()
    for book in books:
        listbox_books.insert(tk.END, f"{book['Title']} by {book['Author']}")

root = tk.Tk()
root.title("Library Management System")

tk.Label(root, text="Title").grid(row=0, column=0)
tk.Label(root, text="Author").grid(row=1, column=0)
tk.Label(root, text="Year").grid(row=2, column=0)
tk.Label(root, text="ISBN").grid(row=3, column=0)

entry_title = tk.Entry(root)
entry_author = tk.Entry(root)
entry_year = tk.Entry(root)
entry_isbn = tk.Entry(root)

entry_title.grid(row=0, column=1)
entry_author.grid(row=1, column=1)
entry_year.grid(row=2, column=1)
entry_isbn.grid(row=3, column=1)

btn_add = tk.Button(root, text="Add Book", command=add_book)
btn_add.grid(row=4, column=1)

listbox_books = tk.Listbox(root, width=50)
listbox_books.grid(row=5, column=0, columnspan=2)

load_books_to_listbox()

root.mainloop()
