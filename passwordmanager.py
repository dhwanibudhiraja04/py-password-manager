import pwinput
import time 
import storage

print("-----------------------------WELCOME TO PASSWORD MANAGER----------------------------------")
print("How do you want to proceed?")
login=input("Are you a new user? Y/N \n")




def loginpage():
    print("-----------------LOGIN PAGE---------------------")
    global username
    username=input("Enter username: ")
    password=pwinput.pwinput('Enter Password: ')
    if [username,password] in storage.accounts:
        print("---------------------------------------------")
        print(f"Logged in as {username}")
        print("---------------------------------------------")
        firstpage()
    else :
        ("Login failed. Try again.")
        time.sleep(3)
        loginpage()

def signup():
    print("-----------------SIGNUP PAGE---------------------")
    username=input("Enter username: ")
    password= pwinput.pwinput('Enter Password: ')
    confirmpassword= pwinput.pwinput('Enter Password again: ')
    if password==confirmpassword:   
        storage.accounts.append([username,password])
        print(f"{username}'s account created successfully")
        with open("storage.py", "a") as file:
            file.write(f"accounts = {storage.accounts}")
        time.sleep(3)
        loginpage()
        
    else:
        print("Passwords do not match.")
        time.sleep(3)
        signup()
    
    

    
    
    
def viewpage():
    for item in storage.masterpassword:
        if item[0]==username: 
            print("Website name is " + item[1])
            print("Website username is " + item[2])
            print("Website password is " + item[3])
            print("---------------------------------------------")
    time.sleep(3)
    firstpage()
        
    
    
    
    
def addpage():
    print("-----------------ADD NEW ACCOUNT---------------------")
    website_name=input(("Enter website's name: \n"))
    website_username=input(("Enter website's username: \n"))
    website_password=input(("Enter password: \n"))
    storage.masterpassword.append([username, website_name, website_username, website_password])
    print(f"Password for {website_name} for {website_username} is saved. ")
    print("Information added successfully. Safe with us.")
    with open("storage.py", "a") as file:
        file.write(f"masterpassword = {storage.masterpassword}")
    time.sleep(3)
    firstpage()
    
    
    
    
def editpage():
    print("-----------------EDIT ACCOUNT---------------------")
    editname=int(input("""What do you want to edit? 
                   1) Website Name
                   2) Website Username
                   3) Website Password
                   Press 1 or 2 or 3 to edit\n"""))
    for i in storage.masterpassword:
            if i[0]== username:
    
                if editname==1 :
                    editweb=input("What website do you want to edit?\n")
                    editwebname=input("What do you want to change your website name into?\n")
                    i[1] = i[1].replace(editweb, editwebname)
                    print("Editing done Successfully.")
                    with open("storage.py", "a") as file:
                        file.write(f"masterpassword = {storage.masterpassword}")

                    print("Website name is changed to " + i[1])
                    
                    
                elif editname==2 :
                    editweb_username=input("What website do you want to edit?")
                    webedit_username=input("What do you want to change your website username into?")
                    i[2] = i[2].replace(editweb_username, webedit_username)
                    with open("storage.py", "a") as file:
                        file.write(f"masterpassword = {storage.masterpassword}")
                    print("Editing done Successfully.")
                    print("Website username is changed to" + i[2])
                    
                elif editname==3 :
                    editpassword=input("What website do you want to edit?")
                    new_password=input("What do you want to change your website name into?")
                    i[3] = i[3].replace(editpassword, new_password)
                    with open("storage.py", "a") as file:
                        file.write(f"masterpassword = {storage.masterpassword}")
                    print("Editing done Successfully.")
                    print("Website password is changed to" + i[3])
                
                else: 
                    print("Invalid choice for editing. Enter again.")
                    editpage()
    time.sleep(3)
    firstpage()
            
    

def deletepage():
    for item in storage.masterpassword:
        if item[0]== username:
            deleting=input("What website information do you want to delete?\n")
            if item[1].upper()==deleting.upper(): 
                storage.masterpassword.remove(item)
                with open("storage.py", "a") as file:
                    file.write(f"masterpassword = {storage.masterpassword}")
                print(f"Deleting {deleting} entry.....")
                time.sleep(2)
                
                print("Deleted Successfully!")
                
    time.sleep(3)
    firstpage()
    
def getpassword():
    for item in storage.masterpassword:
        if item[0]== username:
            get=input("Which website's information do you want to get?")
            if get.upper()==item[1].upper():
                print("Website name is " + item[1])
                print("Website username is " + item[2])
                print("Website password is " + item[3])
                print("---------------------------------------------")
    time.sleep(3)
    firstpage()

    
    

def firstpage():
    print("---------------------------------------------")
    openpage=int(input("""How do you want to proceed?
              1) View all your passwords. 
              2) Add new password.
              3) Get password.
              4) Edit your passwords.
              5) Delete your passwords.
              6) Exit and return to login page. 
              """))
    if openpage==1:
        viewpage()
    elif openpage==2:
        addpage()
    elif openpage==3:
        getpassword()
    elif openpage==4:
        editpage()
    elif openpage==5:
        deletepage()
    elif openpage==6:
        loginpage()
    else:
        print("Option does not appear to be valid. Please try again.")
        openpage()
    time.sleep(3)
    firstpage()

def main():
    if login.upper()=='N':
        loginpage()
    else:
        signup()
main()

