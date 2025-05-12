# This Project
# Add contact
# Search contact
# View contacts list
# Delete contact using name
# Exit project

# Contact list
contacts = []

# Check if user input name and phone before adding contact
# The contadct is added as a dictionary inside a list
def addContact():
    print()
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    if name and phone:
        contacts.append({"name" : name, "phone" : phone})
        print(f"The contact named: {name} was added")
    else:
        print("Please enter a valid value")

# Check is if there is a contact inside the list
# Use for loop to loop through the list and print them numbered 
def viewContacts():
    if not contacts:
        print("The contact list is empty")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact["name"]}, Phone: {contact["phone"]}")

# Show the contacts list through the viewContact() function
# loop through the list then using remove function to delete the contact
def deleteContact():
    viewContacts()
    print()
    toDelete = input("Enter name to delete: ")
    for contact in contacts:
        if toDelete.lower() == contact["name"].lower():
            contacts.remove(contact)
            print(f"The contact {contact["name"]} was deleted")
        else:
            print("Please enter a valid name")

# Chech if contacts list have any contact
# Loop through the list and use a boolean value to check if the contact exist in the list
def searchContact():
    print()
    found = False
    if contacts:
        toFind = input("Enter name to search contact: ")
        for i in contacts:
            if i["name"].lower() == toFind.lower():
                print(f"Found The contact: Name: {i["name"]}, Phone: {i["phone"]}")
                found = True
                break
        if not found:
            print("Contact is not found")
    else:
        print("The contact list is empty")

# The main function have the infinity loop that loops till the user choose to exit the project
def main():
    while True:
        print()
        print("Welcome to simple Contact Book\n")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Delete contacts")
        print("4. Search contact")
        print("5. Exit")
        try:
            num = int(input("Please Choose a number: "))
            if num == 1:
                addContact()
            elif num == 2:
                viewContacts()
            elif num == 3:
                deleteContact()
            elif num == 4:
                searchContact()
            elif num == 5:
                print("Thanks for using Simple Contact Book")
                break
            else:
                print("Please enter a valid nuumber")
        except ValueError:
            print("PLease enter a valid number")

if __name__ == "__main__":
    main()