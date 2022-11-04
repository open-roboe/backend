from app import db
from app.models import User,Image,get_images


def display_all_users ():
    users = User.query.all()
    print ("Current users: ",users)
    

def add_user():

    display_all_users()
    print ("-"*30)
    uname = input ("User name : ")
    passw = input ("Password  : ")

    print ("\nAdding ",uname, "with password ",passw)
    
    c = input("Confirm (Y/n) : ")
    
    if c == 'Y':        
        u = User(username=uname)
        u.set_password(passw)
        db.session.add(u)
        db.session.commit()

    print ("-"*30)
    display_all_users()
    
if __name__ == "__main__":
    add_user()

    
