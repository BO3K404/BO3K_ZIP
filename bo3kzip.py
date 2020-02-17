#!/usr/bin/python

import zipfile 
import optparse 
from threading import Thread

print ("STARTING BO3KZIP") 
def extractFile(zfile,password):
    try:
       zfile.extractall(pwd=password) 
       print "[+] Found password: " + password+"\n" 
    except:
        pass

def main(): 
    parser=optparse.OptionParser("usage%prog -f <Zip File> -d <Dictionary.txt> ") 
    parser.add_option("-f",dest="zip_name",type="string",help="Specify zip file") 
    parser.add_option("-d",dest="dictionary_name",type="string",help="Specify dictionary.txt") 
    (options, args)=parser.parse_args()
    if(options.zip_name==None)|(options.dictionary_name==None):  
        print parser.usage
        exit(0)
    else: 
        zip_name=options.zip_name
        dictionary_name=options.dictionary_name

    zip_name=zipfile.ZipFile(zip_name)
    passFile=open(dictionary_name)

    for line in passFile.readlines():
        password=line.strip("\n")
        t=Thread(target=extractFile,args=(zip_name,password))
        t.start()
    print "password not found" 
main()

