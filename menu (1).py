import os
import getpass


def main():
    os.system("tput setaf 3")
    print("\n")
    print("\t\t\twelcome to my menu!!")
    print("\t\t----------------------------------")
    print("\n")
    print("which system do you want to work on?")
    print("1.Local\n2.Remote.")
    desk=int(input("Enter your choice : "))
    print("\n")
    if desk==1:
        os.system("tput setaf 14")
        os.system("python3 /root/postmenu.py")
    elif desk==2:
        os.system("tput setaf 14")
        ip=input("Enter IP Address of system : ")
        os.system("ssh {} python3 /root/postmenu.py".format(ip))

    else:
        print("choose 1/2 ")


     
if __name__=='__main__':
    main()

    
    
    
