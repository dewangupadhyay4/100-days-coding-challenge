dict={"Maths":89,"Science":78,"History":76,"Hindi":67}
print(dict.keys())
print(dict.values())

for keys, values in dict.items():
    print(keys, values)

#-------------------------------------------------------------------------------------------------------------------------------------

contact_book={}
while(True):
    name=input("Enter the name: ")
    phone=input("Enter the phone: ")
    contact_book[name]=phone

    choice=input("Do you want to add another contact? Yes or No : ")
    if choice.lower() != 'yes':
        break

    print("your contact book is here")
    for name, phone in contact_book.items():
        print(name, phone)