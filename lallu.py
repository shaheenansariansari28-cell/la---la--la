"""for i in range (1,10):
    for j in range(1,i+1):
        print(j,end="")
print()"""



#simple login system
correct_username="faaahhh"
correct_password ="67"
username=input("enter correct_username:")
password=input("enter correct_password:")
if username==correct_username and password==correct_password:
    print("login successful ! welcome")
else:
    print("invalid username or password, access denied!")