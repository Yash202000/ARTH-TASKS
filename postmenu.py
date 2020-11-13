import os
import getpass


def core_site_conf():

    def file(name,ip):
        
        with open('/etc/hadoop/core-site.xml',"w") as f:
            f.write("""<?xml version="1.0"?>\n""")
            f.write("""<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n""")

            f.write("<!-- Put site-specific property overrides in this file. -->\n")

            f.write("<configuration>\n")
            f.write("<property>\n")
            f.write("<name>fs.default.{}</name>\n".format(name))
            f.write("<value>hdfs://{}:9001</value>\n".format(ip))
            f.write("</property>\n")
            f.write("</configuration>")
            f.close()
    print()
    print('Welcome to core-site.xml file configuration\n')
    ip = input("plz specify ip: ")
    file("name",ip)
    print('Your core-site.xml file is configured..\n')


def hdfs_site_conf():
    

    def hdfs_site(val,di):
        with open("/etc/hadoop/hdfs-site.xml","w") as f:
            f.write("""<?xml version="1.0"?>\n""")
            f.write("""<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n""")
            f.write("<!-- Put site-specific property overrides in this file. -->\n\n")
            f.write("<configuration>\n")
            f.write("<property>\n")
            f.write("<name>dfs.{}.dir</name>\n".format(val))
            f.write("<value>{}</value>\n".format(di))
            f.write("</property>\n")
            f.write("</configuration>\n")
            f.close()

    print()
    print("welcome in  hdfs-file.xml configuration !!\n")
    val=input("configure your system as namenode/datanode : ")
    di=input("give full path of your working directory : ")

    if val == "namenode":
        hdfs_site("name",di)
        print("your hdfs-site.xml file is configured!!")
    elif val == "datanode":
        hdfs_site("data",di)
        print("your hdfs-site.xml file is configured!!")
    else:
        print("choose correct option for configuration.")


def cluster_service():
    cluwill = True
    
    while cluwill:
        os.system('tput setaf 14')        
        print()
        print("\t\t\t\tWelcome to Menu")
        print("\t\t\t\t-----------------\n")

        print("1. Software name and version\n2. Configure hadoop cluster \n3. Format Namenode\n4. Start service\n5. Check status \n6. Check report\n0. For return previous menu\n")
        t=int(input("Enter Your choice : "))
        print()
        if t==0:
            cluwill=False
        elif t==1:
            os.system('tput setaf 10')
            os.system("hadoop version")
        elif t==2:
            hdfs_site_conf()
            core_site_conf()
        elif t==3:
            os.system('tput setaf 10')
            os.system('hadoop namenode -format')
        elif t==4:
            os.system('tput setaf 10')
            sys=input("which system you want to start (namenode/datanode): ")
            if sys=='namenode':
                os.system('hadoop-daemon.sh start namenode')
            elif sys=='datanode':
                os.system('hadoop-daemon.sh start datanode')
            else:
                print("give valid choice!\n")
        elif t==5:
            os.system('tput setaf 10')
            os.system('jps')
        elif t==6:
            os.system('tput setaf 10')
            os.system('hadoop dfsadmin -report')
        else:
            os.system('tput setaf 10')
            print("Enter valid choice\n")

def AWS_service():
    awill = True
    while awill:
        os.system('tput setaf 14')

        print("\t\t\t\tWelcome to Menu")
        print("\t\t\t\t-----------------\n")

        print('1. login into AWS CLI\n2. launch instance \n3. start a instance \n4. stop instance\n5. Describe all instances\n6. Create a volume\n7. Attach volume with instance\n8. Partitioning attached volume \n8. configure webserver \n9. Format partition \n10.Mount webserver to volume \n0.return previous menu.\n')
        t=int(input('Enter Your choice : '))
        if t==0:
            awill=False
        elif t==1:
            os.system('tput setaf 10')
            os.system('aws configure')
            print()
        elif t==2:
            os.system('tput setaf 10')
            print("\n1.AWS linux\n2.Redhat Linux \n")
            img=input('Enter your choice : ')
            if int(img)==1:
                print()
                key=input('Enter your key name : ')
                os.system('aws ec2 rum-instances --image-id ami-0e306788ff2473ccb --subnet-id subnet-c60309ae --instance-type  t2.micro --key-name key_for_aws20  --count 1')
                print()
            elif int(img)==2:
                key=input('Enter your key name : ')
                os.system('aws ec2 rum-instances --image-id ami-0a9d27a9f4f5c0efc  --subnet-id subnet-c60308ae  --instance-type  t2.micro --key-name key_for_aws20  --count 1')
                print()
            else:
                print("enter correct choice ")
            print()

        elif t==3:
            uid=input('Enter Instance Id : ')
            os.system("aws ec2 start-instances --instance-id {}".format(uid))
            print()
        elif t==4:
            uid=input('Enter Instance Id : ')
            os.system("aws ec2 stop-instances --instance-id {}".format(uid))
            print()
        elif t==5:
            os.system("aws ec2 describe-instances")
            print()
        elif t==6:
            size=input("Enter Size : ")
            zone=input('Enter availablity zone : ')
            vtype=input('Enter volume type : ')
            os.system(' aws ec2 create-volume --availablity-zone {} --size {} --volume-type {}'.format(zone,size,vtype))
            print()
        elif t==7:
            print('volume zone and Instance zone must be same   ')
            vid = input('Enter volume-id : ')
            iid=input('Enter instance-id : ')
            device=input('Enter device : /dev/')
            os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{}".format(vid,iid,device))
            print()
        elif t==8:
            ip=input("Enter ip : ")
            key=input('Enter key : ')
            device=input('Enter device : /dev/')
            os.system("ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/{} ".format(ip,key,device))
            print()
        elif t==9:
            print("HTTPD MUST BE INSTALLED")
            ip=input("Enter IP : ")
            key=input("Enter key : ")
            os.system("ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd".format(ip,key))
            print()
        elif t==10:
            ip=input("Enter IP : ")
            key=input("Enter key : ")
            device=input("Enter device : /dev/")
            os.system("ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{}".format(ip,key,device))
            print()
        elif t==11:
            ip=input("Enter IP : ")
            key=input("Enter key : ")
            device=input("Enter device : /dev/")
            os.system("ssh -l ec2-user {} -i {}.pem sudo mount  /dev/{}  /var/www/html/".format(ip,key,device))
            print()
        else:
            print("Enter correct choice ")
            print()


def docker_service():
    dwill=True
    while dwill:
        os.system('tput setaf 14')

        print("\t\t\t\tWelcome to Menu")
        print("\t\t\t\t-----------------\n")

        print("1. docker version \n2. List Images name of docker\n3. list all the containers \n4. List running containers \n5. download new Images \n6. Start container with its name or container ID \n7. Stop container with its name or container ID \n8. Attach the container with its name or container ID \n9. Docker information \n10.Remove container or Images \n11.Remove all containers \n12.Launch new container \n13.See the log of container\n14.Start docker service \n15.Stop docker service \n16.Take help of docker \n17.Enable docker service permenently\n18.check docker status \n0. return previous menu\n")

        t=int(input("Enter your choice : "))
        print()

        if t==0:
            os.system("tput setaf 10")
            dwill=False
            print()
        elif t==1:
            os.system("tput setaf 10")
            os.system("docker version")
            print()
        elif t==2:
            os.system("tput setaf 10")
            os.system('docker images -a')
            print()
        elif t==3:
            os.system("tput setaf 10")
            os.system('docker ps -a')
            print()
        elif t==4:
            os.system("tput setaf 10")
            os.system('docker ps')
            print()
        elif t==5:
            os.system("tput setaf 10")
            img=input("Enter which image you have to download(version) : ")
            os.system("docker pull {}".format(img))
            print()
        elif t==6:
            os.system("tput setaf 10")
            w=input("Enter  name/id : ")
            os.system("docker start {}".format(w))
            print()
        elif t==7:
            os.system("tput setaf 10")
            w=input('Enter name/id : ')
            os.system("docker stop {}".format(w))
            print()
        elif t==8:
            os.system("tput setaf 10")
            w=input("Enter name/id : ")
            os.system("docker attach {}".format(w))
            print()
        elif t==9:
            os.system("tput setaf 10")
            os.system("docker info")
            print()
        elif t==10:
            os.system("tput setaf 10")
            w=input("what you want to remove container/image : ")
            if w=="container":
                i=input("Enter name/id :")
                os.system("docker rm {}".format(i))
                print()
            elif w=="image":
                i=input("Enter image name(version) : ")
                os.system("docker rmi {}".format(i))
                print()

            else:
                print("Enter valid choice.")
                print()
        elif t==11:
            os.system("tput setaf 10")
            os.system("docker rm $(docker ps -a -q)")
            print()
        elif t==12:
            os.system("tput setaf 10")
            w=input("do you want to give container name y/n : ")
            if w=='y':
                name=input("Enter name : ")
                os.system("docker run -it --name {} centos")
                print()
            else:
                os.system("docker run -it centos")
                print()
        elif t==13:
            os.system("tput setaf 10")
            c=input("enter container name : ")
            os.system("docker logs -f {}".format(c))
            print()
        elif t==14:
            os.system("tput setaf 10")
            os.system("systemctl start docker")
            print()
        elif t==15:
            os.system("tput setaf 10")
            os.system("systemctl stop docker ")
            print()
        elif t==16:
            os.system("tput setaf 10")
            os.system("docker --help")
            print()
        elif t==17:
            os.system("tput setaf 10")
            os.system("systemctl enable docker")
            print()
        elif t==18:
            os.system("tput setaf 10")
            print("Press ctrl+c to kill running command")
            os.system("systemctl status docker ")
            print()
        else:
            print("Enter valid choice")
            print()


        
def linux_service():
    lwill=True
    while lwill:
        os.system('tput setaf 14')

        print("\t\t\t\tWelcome to Menu")
        print("\t\t\t\t-----------------\n")

        print("1. Date\n2. Calender\n3. Present working directory \n4. Current user \n5. list files \n6. List all file with details \n7. See storage alocation to file system \n8. Attached volumes list \n9. open gedit editor \n10.Create new user and password\n11.See memory/RAM space of an system \n12.Print text output on screen \n13.get spoken output from system of typed statement \n14.see location of command\n15.See IP address of network card \n16.see network card details \n17.create directory \n18.move directory \n19.move file content to another file \n20.remove file \n21.remove directory \n22.Reboot system \n23.Change directory \n24.open file in vi editor \n25.open file in vim editor \n26.Create new password to user \n0. Return to previous menu \n")

        t=int(input("Enter Your choice : "))

        if t==0:
            lwill=False
            print()
        elif t==1:
            os.system("tput setaf 10")
            os.system("date")
            print()
        elif t==2:
            os.system("tput setaf 10")
            os.system("cal")
            print()
        elif t==3:
            os.system("tput setaf 10")
            os.system("pwd")
            print()
        elif t==4:
            os.system("tput setaf 10")
            os.system('whoami')
            print()
        elif t==5:
            os.system("tput setaf 10")
            os.system("ls")
            print()
        elif t==6:
            os.system("tput setaf 10")
            os.system('ls -l')
            print()
        elif t==7:
            os.system("tput setaf 10")
            os.system('df -h')
            print()
        elif t==8:
            os.system("tput setaf 10")
            os.system('fdisk -l')
            print()
        elif t==9:
            os.system("tput setaf 10")
            os.system('gedit')
            print()
        elif t==10:
            os.system("tput setaf 10")
            u=input("Enter name of user : {}")
            os.system("adduser {}".format(u))
            print()
        elif t==11:
            os.system("tput setaf 10")
            os.system("free -m")
            print()
        elif t==12:
            os.system("tput setaf 10")
            s=input("Enter statement to print : ")
            os.system("echo {}".format(s))
            print()
        elif t==13:
            os.system("tput setaf 10")
            s=input("Enter sentence to speak : ")
            print()
        elif t==14:
            os.system("tput setaf 10")
            s=input("Enter command : ")
            os.system("")
            print()
        elif t==15:
            os.system("tput setaf 10")
            os.system("ifconfig enp0s3")
            print()
        elif t==16:
            os.system("tput setaf 10")
            os.system("ifconfig")
            print()
        elif t==17:
            os.system("tput setaf 10")
            s=input("Enter directory location : ")
            os.system("mkdir {}".format(s))
            print()
        elif t==18:
            os.system("tput setaf 10")
            s=input("sorce directory location : ")
            d=input("destination for directory : ")
            os.system("mv {} {}".format(s,d))
            print()
        elif t==19:
            os.system("tput setaf 10")
            s=input("Enter sorce file location : ")
            d=input("Enter destination file location : ")
            os.system("mv {} {}".format(s,d))
            print()
        elif t==20:
            os.system("tput setaf 10")
            s=input("Enter name of file : ")
            os.system("rm {}".format(s))
            print()
        elif t==21:
            os.system("tput setaf 10")
            s=input("Enter location of directory : ")
            os.system("rmdir {}".format(s))
            print()
        elif t==22:
            os.system("tput setaf 10")
            os.system("init 0")
            print()
        elif t==23:
            os.system("tput setaf 10")
            s=input("Enter file location : ")
            os.system("cd {}".format(s))
            print()
        elif t==24:
            os.system("tput setaf 10")
            s=input("enter file location/name : ")
            os.system('vi {}'.format(s))
            print()
        elif t==25:
            os.system("tput setaf 10")
            s=input("Enter file location/name : ")
            os.system("vim  {}".format(s))
            print()
        
        elif t==26:
            os.system("tput setaf 10")
            s=input("Enter user name : ")
            os.system('passwd {}'.format(s))
            print()
        else:
            os.system("tput setaf 10")
            print('Enter valid choice')

def webserver_service():
    wwill=True
    while wwill:
        os.system('tput setaf 14')

        print("\t\t\t\tWelcome to Menu")
        print("\t\t\t\t-----------------\n")
        
        print("1. Download httpd software \n2. start httpd service \n3. Disable firewalld \n4. create website page \n5. See content of webpage \n6. create cgi-bin file \n7. Enable httpd permenently \n8.Stop httpd service \n9. status httpd   \n0.  return to Menu \n")

        t=int(input("Enter Your choice : "))

        if t==0:
            wwill = False
            print()
        elif t==1:
            os.system("tput setaf 10")
            os.system("yum install httpd -y")
            print()
        elif t==2:
            os.system("tput setaf 10")
            os.system("systemctl start httpd")
            print()
        elif t==3:
            os.system("tput setaf 10")
            os.system("systemctl disable firewalld")
            print()
        elif t==4:
            os.system("tput setaf 10")
            os.system("cd /var/www/html")
            n=input("Enter name of file : ")
            os.system("vim {}".format(n))
            print()
        elif t==5:
            os.system("tput setaf 10")
            s=input("Enter webpage location : ")
            os.system("curl {}".format(s))
            print()
        elif t==6:
            os.system("tput setaf 10")
            os.system('cd /var/www/cgi-bin')
            s=input("Enter file name : ")
            os.system('vim {}'.format(s))
            print()
        elif t==7:
            os.system("tput setaf 10")
            os.system("systemctl enable httpd")
            print()
        elif t==8:
            os.system("tput setaf 10")
            os.system("systemctl stop httpd")
            print()
        elif t==9:
            os.system("tput setaf 10")
            os.system("systemctl status httpd")
            print()
        else:
            print("Enter valid choice : ")
            print()
















def main():
    will = True
    while will:
        os.system("tput setaf 3")

        print("\t\t\t\tWelcome to Menu")
        print("\t\t\t\t-----------------\n")
        print("1. For Hadoop service\n2. For AWS service\n3. For docker service\n4. For Linux command service \n5. For Web server service\n0. For Quit\n")
        t=int(input("Enter Your choice : "))

        if t==0:
            will=False
        elif t==1:
            cluster_service()
        elif t==2:
            AWS_service()
        elif t==3:
            docker_service()
        elif t==4:
            linux_service()
        elif t==5:
            webserver_service()
        else:
            print("Enter correct choice.\n")
            


main()






