#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 18:05:18 2020

@author: sanath
"""

#CSV to .txt file converter

import os




def csv_to_txt(csv_file_name="all_dataset.csv",skip_head=True,label_path=os.path.join(os.getcwd(),"labels")):
    f=open(csv_file_name)
    lines=f.read().split("\n")
    n=len(lines)
    start=0
    if skip_head is True:
        start=1
    for i in range(start,n-1):
        line=lines[i]
        fname,w,h,c,xmin,ymin,xmax,ymax=line.split(",")
        #print(fname,w,h,c,xmin,ymin,xmax,ymax)
        filename=os.path.basename(fname)
        filename,ext=os.path.splitext(filename)
        w=int(w)
        h=int(h)
        xmin=int(xmin)
        ymin=int(ymin)
        xmax=int(xmax)
        ymax=int(ymax)
        y1=(xmin+(xmax-xmin)/2)/w
        y2=(ymin+(ymax-ymin)/2)/h
        y3=(xmax-xmin)/w
        y4=(ymax-ymin)/h
        destination_file=os.path.join(label_path,filename+".txt")
        if not os.path.exists(destination_file):
            myfile=open(destination_file,"w+")
            myfile.write(str(c)+" "+str(y1)+" " +str(y2)+" " +str(y3)+" " +str(y4)+"\n")
            myfile.close()
        else:
            myfile=open(destination_file,"a")
            myfile.write(str(c)+" "+str(y1)+" " +str(y2)+" " +str(y3)+" " +str(y4)+"\n")
            myfile.close()
    f.close()


csv_to_txt()
