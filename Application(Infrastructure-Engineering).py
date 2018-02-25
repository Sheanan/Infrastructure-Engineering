import os,sys,platform,heapq
from os import listdir
from os.path import expanduser
import time
tuple1=[]
def HeapCreate(home):
        #home = expanduser("~")
        no_of_files=0
        global tuple1 #"/home/sheanan/Desktop"):
        #home=home+"/dev/sda1/"
        #print home
        for dirpath, dirs, files in os.walk(home):      
                for filename in files:
                        try:
                                fname = os.path.join(dirpath,filename)
                                #print fname
                                file_size = os.path.getsize(fname)
                                #file_size_in_mb=file_size/(1024*1024)
                                no_of_files+=1
                                heapq.heappush(tuple1, (file_size,fname))
                                #print tuple1
                        except:
                                pass
        print("*************************************************************************************");
def Largest(n):
        global tuple1
        AnsList=heapq.nlargest(n, tuple1)
        for i in AnsList:
                print "Name of file with its path=",i[1]
                print "File Size=",i[0]/(1024*1024),"MB"
        print("*************************************************************************************");
def Smallest(n):
        global tuple1
        AnsList=heapq.nsmallest(n, tuple1)
        for i in AnsList:
                print "Name of file with its path=",i[1]
                print "File Size=",i[0],"Bytes"
        print("*************************************************************************************");

def ensure_dir(file_path):
        if not os.path.exists(file_path):
                os.makedirs(file_path)

def Traverse(spath,dpath):
#spath='/home/sheanan/Desktop/'
#dpath="/home/sheanan/Documents/"
        try:
                directory=os.listdir(spath)
                try:
                        for i in directory:
                                extension = os.path.splitext(os.path.join(spath,i))[1]
                                if((os.path.isdir(os.path.join(dpath,(extension[1:]).lower()))==True) and ((extension[1:]).lower()!="")):
                                        os.rename(os.path.join(spath,i),os.path.join(os.path.join(dpath,(extension[1:]).lower()),i))
                                elif((extension[1:]).lower()!=""):
                                        ensure_dir(os.path.join(dpath,(extension[1:]).lower()))
                                        os.rename(os.path.join(spath,i),os.path.join(os.path.join(dpath,(extension[1:]).lower()),i))
                except:         
                        print "Error"
                        pass
        except:
                print "Invalid Path"
        if ((platform.system()!= "Windows") and (platform.system()!= "Linux")):
                print("Sorry, we don't currently have support for the " + platform.system() + "OS")
        print("*************************************************************************************");

def main():
        
        choice=1
        start=time.time()
        
        if platform.system() == "Windows":
                home = expanduser("~")
                HeapCreate(home)
        elif platform.system()== "Linux":
                home=os.sep
                HeapCreate(home)
        end=time.time()
        print "Prefetch Time==",(end-start),"Sec"
        print("*****************Welcome*****************")
        while(choice):
                print ("*******************************************************************************************")
                print "Choose from the following option"
                print "1:For moving the file from Desktop to Documents"
                print "2:For finding top 10 files which have the largest size on the system."
                print "3:For doing operation 1 and 2 together."
                print "****MORE SPECIFIC OPERATION*****"
                print "4:For finding the N Largest files in system."
                print "5:For finding the N Smallest file in system."
                print "6:For moving the file from specific location to other specific location. "
                print "7:For Exit."
                
                select=input()
                if(select==1):
                        start=time.time()
                        if (platform.system() == "Windows"):
                                spath=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                                dpath=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
                                Traverse(spath,dpath)
                                print "Desktop Cleaned"
                                
                        elif(platform.system() == "Linux"):
                                #print "Hello"
                                spath=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
                                dpath=os.path.join(os.path.join(os.path.expanduser('~')), 'Documents')
                                #print spath
                                #print dpath
                                Traverse(spath,dpath)
                                print "Desktop Cleaned"
                        end=time.time()
                        print "Operation Time==",(end-start),"Sec"
                elif(select==2):
                        print "********10 Largest files of System********"
                        start=time.time()
                        Largest(10)
                        end=time.time()
                        print "Operation Time==",(end-start),"Sec"
                elif(select==3):
                        spath=os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
                        dpath=os.path.join(os.path.join(os.path.expanduser('~')), 'Documents')
                        start=time.time()
                        Traverse(spath,dpath)
                        print "********10 Largest files of System********"
                        Largest(10)
                        end=time.time()
                        print "Desktop Cleaned"
                        print "Operation Time==",(end-start),"Sec"
                elif(select==4):
                        print "Enter number of files"
                        no=input()
                        print "********",no,"Largest files of System********"
                        start=time.time()
                        Largest(no)
                        end=time.time()
                        print "Operation Time==",(end-start),"Sec"
                elif(select==5):
                        print "Enter number of files"
                        no=input()
                        print "********",no,"Smallest files of System********"
                        start=time.time()
                        Smallest(no)
                        end=time.time()
                        print "Operation Time==",(end-start),"Sec"
                elif(select==6):
                        print "Enter Source Path"
                        spath=raw_input()
                        print "Enter Destination Path"
                        dpath=raw_input()
                        start=time.time()
                        Traverse(spath,dpath)
                        end=time.time()
                        print "Operation Time==",(end-start),"Sec"
                elif(select==7):
                        print "Thank you for using our Application"
                        sys.exit()

if __name__== "__main__":
        main()
