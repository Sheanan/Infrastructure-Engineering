This Application is build in Python 2.7.
By Sheanan Verma(IIIT H ,M tech CSE)

Infrastructure Engineering Assignment.

This Application software is designed to accomplish task of cleaning up cluttered dictortoies and finding out Top 10 largest file.
Here.
We have used a Efficient way for finiding Top n Largest and Smallest files by creating heap.
We do PreComputation and Build a Heap of a tuple(File name and Path , Size).The Complexiity to build heap is O(n).
This is a Scalable Solution.
  
Apart From Regular Feature Like 
For moving the file from Desktop to Documents(by creating extension name folder)
Finding top 10 files which have the largest size on the system.

There and many Other feature added in This Application (For Bonus Points :D) These are as follows:

Finding the N Largest files in system.

(The Computation time for This feature is Less than < 2 Sec(In ubuntu and Windows  when no of files< 1 million) )

Finding the N Smallest file in system.

(The Computation time for This feature is Less than < 1 Sec(In ubuntu and Windows when no of files< 1 million) ) 

Moving files(Extension file) from Specific location like Document,Downloads,Picture folder to Some other specific folder like Desktop,Movie,Project Folder .
We have created a menu Driven Application for same.

Time to perform all operation are in Sec(Added in Code).

The Code is thoroughly Tested on Linux(Ubuntu 16.04 version) and Windows 10.

In Ubuntu apart from given problem statment i.e. Scan in /home/* and disk media,We also Consider Everything from the ROOT(/) i.e. /dev ,/Core Files ,Page Files etc

In Windows as there are more then >10 million of files Present hence we keep our search within HOME(i.e. Excluded Disk)
 
After Running--> python Application(Infrastructure-Engineering).py
The Application Take For Prefetch(<2 min) time when it Start.
After That all Operations are(<2 Sec)
