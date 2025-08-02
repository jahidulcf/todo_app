
todos = []


def add_todo():
    text = input("Enter todo: ").strip()
    if text:
        todos.append({"text": text, "done": False})
        print("✅ Todo added!")
    else:
        print("⚠️ Empty todo not added")

def edit_todo():
    if not todos:
        print("📭 No todos to edit.")
        return

    list_todos()
    try:
        index = int(input("Enter todo number to edit: ")) - 1
        if 0 <= index < len(todos):
            new_text = input("Enter new text: ").strip()
            if new_text:
                todos[index]["text"] = new_text
                print("✏️ Todo updated.")
            else:
                print("⚠️ Empty text ignored.")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a number.")


def delete_todo():
    if not todos:
        print("📭 No todos to delete.")
        return

    list_todos()
    try:
        index = int(input("Enter todo number to delete: ")) - 1
        if 0 <= index < len(todos):
            removed = todos.pop(index)
            print(f"🗑 Removed: {removed['text']}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("⚠️ Please enter a number.")

def list_todos():
    if not todos:
        print("📭 No todos.")
        return
    for i, todo in enumerate(todos, 1):
        status = "✅" if todo["done"] else "❌"
        print(f"{i}. {todo['text']} {status}")

def main():
    while True:
        print("\n[1] Add [2] Edit [3] Delete [4] List [0] Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_todo()
        elif choice == "2":
            edit_todo()
        elif choice == "3":
            delete_todo()
        elif choice == "4":
            list_todos()
        elif choice == "0":
            break
        else:
            print("❓Invalid choice")

if __name__ == '__main__':
    main()