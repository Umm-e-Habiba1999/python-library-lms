import os
import json

# File name for saving and loading
LIBRARY_FILE = "library.txt"

# Load library from file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file)

# Display menu
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").lower()
    read_status = True if read_input == 'yes' else False
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    original_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title.lower()]
    if len(library) < original_length:
        print("Book removed successfully!")
    else:
        print("Book not found.")

# Search for a book
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    if choice == '1':
        keyword = input("Enter the title: ").lower()
        results = [book for book in library if keyword in book['title'].lower()]
    elif choice == '2':
        keyword = input("Enter the author: ").lower()
        results = [book for book in library if keyword in book['author'].lower()]
    else:
        print("Invalid choice.")
        return

    if results:
        print("Matching Books:")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.")

# Display all books
def display_all_books(library):
    if not library:
        print("Your library is empty.")
        return
    print("Your Library:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# Display statistics
def display_stats(library):
    total = len(library)
    if total == 0:
        print("Total books: 0\nPercentage read: 0.0%")
        return
    read_count = sum(1 for book in library if book['read'])
    percentage = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%")

# Main program
def main():
    library = load_library()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_stats(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == '__main__':
    main()

