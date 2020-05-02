# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:33:23 2020

@author: zxq
"""
#logistic map
import matplotlib.pyplot as plt
import numpy as np

def LogisticMap():
    x=0.9
    r=2.7
    plt.ion()   #开启interactive mode，关闭函数为 plt.ioff
    ix=[]
    iy=[]
    for n in range(50):
        x=r*x*(1-x)
        ix.append(n)  #保存历史数据
        iy.append(x)
        plt.plot(ix,iy)
        plt.xlabel('n')
        plt.ylabel('x_n')
        plt.pause(.01)
    print(iy)
    plt.ioff()
    #if iy[-1]==iy[-2]:
    #    print(ix[-1])
    #理想情况下才能看到
    return 

#LogisticMap()

#bifurcation
'''
Write a program to construct a bifurcation diagram for the logistic map
-An initial condition x0
-An rmin and an rmax that specify a range of r values for the x-axis of your bifurcation plot
-An rstep, which specifies how many "slices" your plot has
-A number n of total iterates to perform
-A number k of total iterates to discard without plotting (i.e., to remove the transient)
The output should be a plot of the logistic map bifurcation diagram for a range of r.
'''
def Bifurcation(x0,rmin,rmax,rstep,n,k):  #iters  不画图的迭代次数
  '''
    parameters:
    x0 -x
    rmin,rmax,rstep
    total iterates -n
    without plotting -k
  '''  
  x=x0
  r=np.arange(rmin,rmax,rstep)    #区间[2.4,4],每次增长0.01
  for i in range(n):
        x=r*x*(1-x)
        if i>=n-k:
            plt.plot(r,x,',k',alpha=.2)  #alpha 设置透明度
  plt.xlabel('r')
  plt.ylabel('x')
  return
Bifurcation(.2,2.8,3.6,.00001,1000,300)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



