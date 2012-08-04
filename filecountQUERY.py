'''Counts each file type, by extension, in a given location.
N Waterman 23-06-12
'''

import os

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
            mylist.append(os.path.splitext(myfile)[1])
    a1=count_doc_type(direc, mylist)
#    s1=str(mycount)+" "+"file(s)"+"\n"
    s2=str(myfolders)+" "+"folder(s)"
    z = a1 + s2
    return z

def create_doc_type(direc):
    '''creates the list of doc types by file extension'''
    
    mylist=[]
    for root, dir, files in os.walk(direc):
        for x in range(len(files)):
            wibble = files[x-1]
            wibble1 = os.path.splitext(wibble)
            mylist.append(wibble1[1])
    y=count_doc_type(direc, mylist)
    return y
            
def count_doc_type(direc, mylist):
    '''sorts the list, counts each type, provides totals'''
    
    type_count=[]
    mylist.sort()
    myString=""
    a=str('There are: '+ str(len(mylist))+ ' files in '+ direc + '\n')
    for z in range(len(mylist)):
        if z+1==len(mylist):
            d=(mylist[z] + " " + str(mylist.count(mylist[z]))+ '\n')
            type_count.append(str(d))
        elif mylist[z]!=mylist[z+1]:
            f=(mylist[z] +" "+str(mylist.count(mylist[z]))+ '\n')
            type_count.append(str(f))
    myString += a
    for z1 in range(len(type_count)):
        myString+=str(type_count[z1])
    return myString
    
if __name__ == "__main__":
        print("You can only run this module by importing it")
