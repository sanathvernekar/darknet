#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:51:06 2019

@author: sanath
"""
import os
#import numpy 
#import sys
import subprocess 
import shutil




def download_pre_requisites():
    if os.path.exists("darknet53.conv.74"):
        print("darknet53.conv.74 , exists ..... skipping download.:)")
    else :
        bashCommand = "wget https://pjreddie.com/media/files/darknet53.conv.74"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)
        
        
def test_train(totalcount, imgpath ,labelpath):
    test_percentage=30 # should be set based on your dataset size 
    train_count=0
    test_count=0
    #print("Number of Images considered for training are : ", train_count)
    #print("Number of Images considered for Testing are : ",test_count)
    if (os.path.exists("train.txt") == False) and  (os.path.exists("train.txt") == False):
        train=open("train.txt","w")
        test=open("test.txt","w")
        index_cmp=round(100 /test_percentage)
        counter =1
        x=open("Just_file_names.txt")
        lines = x.read().split("\n")
        for each in lines:
            if(each == ""):
                break
            jpgfile=os.path.join(imgpath,each)
            jpgfile=jpgfile+'.jpg'
            if counter == index_cmp:
                counter = 1
                test.write(str(jpgfile)+os.linesep)
                test_count+=1
            else :
                train.write(str(jpgfile)+os.linesep)
                train_count+=1
                counter+=1
        print(test_count," Test files ", train_count ," Train files created ")
        train.close()
        test.close()
    else :
        print("Train and Test File already exists......")
        
        
        
def copy_files(PathOfEachFile,DestinationDir):
    if not os.path.exists(PathOfEachFile):
        print("Input file is not present  in the current directory")
        exit()
    f=open(PathOfEachFile)
    if not os.path.exists(DestinationDir):
        os.mkdir(DestinationDir)
    cwd=os.getcwd()
    DestinationPath=os.path.join(cwd,DestinationDir)
    lines=f.read().split("\n")
    for line in lines:
        try:
            shutil.copy(line,DestinationPath)
        except:
            if line!="":
                print("Error copying ",line)
    f.close()
    
def classes(path):
    f=open(path)
    obj=open("objects.names","w")
    lines=f.read().split("\n")
    NumberOfClasses=0
    for line in lines:
        if line !="":
            NumberOfClasses+=1
            #print(line)
            obj.write(str(line)+"\n")
    f.close()
    obj.close()
    datafile=open("trainer.data","w")
    cwd=os.getcwd()
    datafile.write("classes = " + str(NumberOfClasses)+"\n")
    datafile.write("train = "+ str(os.path.join(cwd,"train.txt"))  +"\n")
    datafile.write("valid = "+ str(os.path.join(cwd,"test.txt"))  +"\n")
    datafile.write("names = "+ str(os.path.join(cwd,"objects.names"))  +"\n")
    datafile.write("backup = backup/"+"\n")
    datafile.close()
    return NumberOfClasses

        

        
        
    
    