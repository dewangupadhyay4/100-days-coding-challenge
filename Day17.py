# file=open("hello.txt","r",encoding='UTF-8')
# print(file.read())
# file.close()

#-------------------------------------------------------------------------

# with open("hello.txt","r") as file:
#     for line in file:
#         print(line.strip())

#-------------------------------------------------------------------------

# file=open("hello.txt","w")
# file.write("I am adding new line by write command")
# file.close()

#-------------------------------------------------------------------------
file=open("hello.txt","a")
file.write("Here i am adding new line by appending the same")
file.close()