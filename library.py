# Library Management System

library = []

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        book = input("Enter book name: ")
        library.append(book)
        print(book, "added successfully!")

    elif choice == '2':
        if len(library) == 0:
            print("Library is empty!")

        else:
            print("\nBooks in Library:")
            for book in library:
                print("-", book)

    elif choice == '3':
        search = input("Enter book name to search: ")

        if search in library:
            print(search, "is available.")

        else:
            print(search, "not found.")

    elif choice == '4':
        remove = input("Enter book name to remove: ")

        if remove in library:
            library.remove(remove)
            print(remove, "removed successfully!")

        else:
            print(remove, "not found.")

    elif choice == '5':
        print("Thank You")
        break

    else:
        print("Invalid Choice")
        