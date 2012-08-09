'''Counts each file type, by extension, in a given location.
N Waterman 23-06-12
'''

import os

mypath1='/home/nathan/testing1'

class File_type(object):
    mydict={}
    def __init__(self, mytype,  mysize):
        self.mytype=mytype
        self.mysize=mysize
    def create_dict(self):
        if self.mytype in self.mydict:
            n=self.mydict[self.mytype]+self.mysize
            self.mydict[self.mytype]=n
        else:
            self.mydict[self.mytype]=self.mysize
            n=self.mydict[self.mytype]+self.mysize
        return(self.mydict)

def ext_list_folder(direc):
    '''returns count of files & folders in direc'''
    mylist=[]
    mycount=0
    myfolders=0
    for myfile in os.listdir(direc):
        mypath=os.path.join(direc, myfile)
        if os.path.isdir(mypath)==True:
            myfolders+=1
        else:
            mycount+=1
            a=os.path.splitext(myfile)[1]
            b=os.stat(mypath).st_size
            h=File_type(a, b).create_dict()
            mylist.append(a)
    a1=count_doc_type(direc, mylist, h)
    s2=str(myfolders)+" "+"folder(s)"
    z = a1+s2
    return z

def create_doc_type(direc):
    '''creates the list of doc types by file extension'''
    
    mylist=[]
    for root, dir, files in os.walk(direc):
        for x in range(len(files)):
            mypath1=os.path.join(root, files[x-1])
            c1 = (os.path.splitext(mypath1)[1]).lower()
            c2=os.stat(mypath1).st_size
            h=File_type(c1, c2).create_dict()
            mylist.append(c1)
    y=count_doc_type(direc, mylist, h)
    return y
            
def count_doc_type(direc, mylist, h):
    '''sorts the list, counts each type, provides totals'''
    
    type_count=[]
    mylist.sort()
    myString=""
    a=str('There are: '+ str(len(mylist))+ ' files in '+ direc + '\n')
    for z in range(len(mylist)):
        if z+1==len(mylist):
            d=(str(mylist.count(mylist[z]))+" "+ mylist[z]+"\t totalling\t"+
                str(h[mylist[z]])+"\tbytes\n")
            type_count.append(str(d))
        elif mylist[z]!=mylist[z+1]:
            f=(str(mylist.count(mylist[z]))+" "+ mylist[z]+"\t totalling\t"+
                str(h[mylist[z]])+"\tbytes\n")
            type_count.append(str(f))
    myString += a
    for z1 in range(len(type_count)):
        myString+=str(type_count[z1])
    return myString
    
if __name__ == "__main__":
        print("You can only run this module by importing it")
