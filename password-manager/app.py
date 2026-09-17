from manager import Manager



def main():
    manager = Manager()

    while True:
        print("\n1. Add")
        print("2. Get")
        print("3. List")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            site = input("Site: ")
            username = input("Username: ")
            password = input("Password: ")

            result = manager.add(site, username, password)

            if result:
                print(result)
            else:
                print("Added successfully")

        elif choice == "2":
            site = input("Site: ")

            result = manager.get(site)

            if result:
                print(f"Username: {result['username']}")
                print(f"Password: {result['password']}")
            else:
                print("Site not found")

        elif choice == "3":
            sites = manager.list_sites()

            if not sites:
                print("No saved sites")
            else:
                for site in sites:
                    print(site)

        elif choice == "4":
            site = input("Site: ")
            print("\nLeave blank to keep current username or password")
            username = input("New username: ")
            password = input("New password: ")

            print(manager.update(site, username, password))

        elif choice == "5":
            site = input("Site: ")
            print(manager.delete(site))

        elif choice == "6":
            break

        else:
            print("Invalid choice")