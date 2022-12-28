contacts = {
        "suman": 7903439433,
        "dipti prakash": 7205122544,
        "abhishek": 6306094611, 
        "aman": 8800787887,
        "tusar": 8218079544,
        "sourav": 6306028921,
        "gaurav": 9649549202,
        "amulya": 9766538968 
}


def display():
    """
    Prints out all contact names along their phone number."""
    print("-"*25)
    for name in contacts:
        number = contacts[name]
        print(f'{name.title()}: {number}')
    print("-"*25)
    

    
def search(name):
    """Search and return phone number of name from contacts.
    None is returned if name is not in contacts."""
    return contacts.get(name.lower())


def addName(name, number):
    """
    Adds name in contact list if name not in contacts."""
    if name.lower() in contacts:
        return f"{name} is already in contact list."
    else:
        contacts[name.lower()] = number
        return f"Successfully added {name} in contact list."


# printing out all contacts
display()

# getting name input from user to search contact
name = input('Enter name to search in contacts: ')
result = search(name)
if result is not None:
    print(f'{name} : {result}')
else:
    print(f'No contact exists with name {name}')