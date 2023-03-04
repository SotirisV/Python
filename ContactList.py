contacts = {}

def add_contact(name, phone, email):
    contacts[name] = (phone, email)

def remove_contact(name):
    del contacts[name]

def search_contact(name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found"

def print_contacts():
    for name in contacts:
        print(name, ":", contacts[name][0], ",", contacts[name][1])

# Sample 
add_contact("Nick", "6984638485", "nick@email.com")
add_contact("John", "6934569876", "john@email.com")
print_contacts()


remove_contact("John")
print_contacts()


print(search_contact("John"))
print(search_contact("Nick"))

# Output:
# Contact not found
# (Nick)
