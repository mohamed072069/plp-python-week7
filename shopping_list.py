shopping_list = []

while True:
    choice = input("Choose: add / remove / show / done: ")

    if choice == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print("Item added.")

    elif choice == "remove":
        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print("Item removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        print("Shopping list:")
        for item in shopping_list:
            print(item)

    elif choice == "done":
        print("Goodbye!")
        break