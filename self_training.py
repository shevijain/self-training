#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import division
"""
Created on Tue Apr 30 22:37:26 2019

@author: shevijain
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 18:55:13 2019

@author: shevijain
"""

import math 
import copy
final=[]
final1=[]
final2,height,weight,age1=[],[],[],[]
super_class=[]
test_class=[]
true_probability=[]
classes={}
#class1=[]
unique=set()
with open('supervised.txt','r') as t1:
    
    for line in t1:
        line=line.lstrip('(')
        line=line.lstrip(',')
        line=line.rstrip(')')
        line=line.rstrip(')')
        line=line.rstrip('\n')
        #print(line)
        
        words=line.split(',')
        # type(words)
        #words.rstrip('\n')
        ht=float(words[0])
        height.append(ht)
        wt=float(words[1])
        weight.append(wt)
        age=(words[2])
        age=age.rstrip(')')
        age=float(age)
        age1.append(age)
        #class1 = words[3]
        unique.add(words[3])
        #print("ll",unique)
        class1=list(unique)
        if(words[3]==' W )'):
            classes[0]=words[3]
            true_probability.append(int(0))
        else:
            classes[1]=words[3]
            true_probability.append(int(1))
            
        #super_class.append(class1)
        #classes.add(class1)
        final.append((ht,wt,age))
        
        
                                                                                        
                                           
        #l.append(i)
t1.close()

height_u,weight_u,age1_u,class_u=[],[],[],[]
with open('unsupervised.txt','r') as t2:
    for line in t2:
        line=line.lstrip('(')
        line=line.lstrip(',')
        line=line.rstrip(')')
        line=line.rstrip('\n')
        #print(line)
        
        words=line.split(',')
        # type(words)
        #words.rstrip('\n')
        ht=float(words[0])
        height_u.append(ht)
        wt=float(words[1])
        weight_u.append(wt)
        age=(words[2])
        age=age.rstrip(')')
        age=float(age)
        age1_u.append(age)
        #classes.add(class1)
        final1.append((ht,wt,age))
        #l.append(i)
t2.close()

height_t,weight_t,age1_t,class_t=[],[],[],[]
unique_t=set()
class1_t=[]
classes_t={}
test_probability=[]
with open('test.txt','r') as t3:
    for line in t3:
        line=line.lstrip('(')
        line=line.lstrip(',')
        line=line.rstrip(')')
        line=line.rstrip(')')
        line=line.rstrip('\n')
        #print(line)
        
        words=line.split(',')
        # type(words)
        #words.rstrip('\n')
        ht=float(words[0])
        height_t.append(ht)
        wt=float(words[1])
        weight_t.append(wt)
        age=(words[2])
        age=age.rstrip(')')
        age=float(age)
        age1_t.append(age)
        class1 = words[3]
        #test_class.append(class1)
        unique_t.add(words[3])
        #print("ll",unique)
        class1_t=list(unique_t)
        if(words[3]==' W)'):
            classes_t[0]=words[3]
            test_probability.append(int(0))
        else:
            classes_t[1]=words[3]
            test_probability.append(int(1))
            
        #super_class.append(class1)
        #classes.add(class1)
        #final.append((ht,wt,age))
        #classes.add(class1)
        final2.append((ht,wt,age))
        #l.append(i)
t3.close()


                                                                                                                
                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                            
                                                                  
                                                                                                                                 
theta=[float(1)]*4                                                                                                               
#print "Initial Theta values",theta                                                                                                                                                                                                                                  
                                                                                                                                  
def dot_product(full,theta):                                                                                                      
    multiply1=[]                                                                                                                  
    for i in range(len(full)):                                                                                                    
        add=0.0                                                                                                                   
        for j in range(len(theta)):                                                                                               
            add+=full[i][j]*theta[j]                                                                                              
        multiply1.append(round(add,4))                                                                                         
    return multiply1                                                                                                              
                                                                                                                                  
                                                                                                                                  
def sigmoid_cal(multiply1):                                                                                                       
    sigmoid=[] 
    without_round=[]                                                                                                                    
    temp=0.0                                                                                                                      
    for i in range(len(multiply1)):                                                                                               
        temp=1.0/(math.exp(-multiply1[i])+1.0) 
        without_round.append(temp)                                                                                   
        sigmoid.append(round(temp,4))                                                                                         
    return sigmoid,without_round                                                                                                                
                                                                                                                                  
                                                                                                                                  
def gradient_descent(full,sigmoid):                                                                                               
    diff=[]                                                                                                                       
    full_transpose = list(zip(*full))                                                                                             
    for i in range(len(sigmoid)):                                                                                                 
        diff.append(sigmoid[i]-true_probability[i])                                                                                        
    final_multiply=dot_product(full_transpose, diff)                                                                              
    for i in range(len(final_multiply)):                                                                                          
        final_multiply[i]=final_multiply[i]/len(sigmoid)                                                                            
    return final_multiply                                                                                                         
final_theta=[]                                                                                                                    
                                                                                                                                  
def update_weight(final,theta):                                                                                                       
    for i in range(len(theta)):                                                                                                      
        theta[i]=round(theta[i]-(0.01*final[i]),4)                                                                                        
    return theta                                                                                                                  
                                                                                                                                  
def mse(sigmoid):                                                                                                                 
    mse=[]                                                                                                                        
    diff=0                                                                                                                        
    for i in range(len(sigmoid)):                                                                                                 
        diff+=(sigmoid[i]-true_probability[i])**2                                                                                                             
    d=diff/2                                                                                                                      
    return d                                                                                                                      
                                                                                                                                  
def cross_entropy(sigmoid):                                                                                                       
    cost1=[]                                                                                                                    
    for i in range(len(sigmoid)):                                                                                                 
                                                                                                                                  
        cost2=(((-true_probability[i])*math.log(sigmoid[i]))-((1-true_probability[i])*math.log(1-sigmoid[i])))                                                                                                           
        cost1.append(cost2)                                                                                                       
    sum1=sum(cost1)/len(cost1)                                                                                                                                                                                                           
    return sum1                                                                                                                   
                                                                                                                                  
def cost(theta,full_without):                                                                                                                  
                                                                                                              
    for i in range(175):                                                                                                                                                                             
        sigmoid,without_round=sigmoid_cal(dot_product(full_without,theta))                                                                      
        gradient=gradient_descent(full_without,sigmoid)                                                                           
        theta=update_weight(gradient,theta)                                                                                       
        #if(i%10000==0):                                                                                                           
            #sigmoid=sigmoid_cal(dot_product(full_without,theta))                                                                  
    #print("Loss"),mse(sigmoid)                                                                                                         
    return theta   

print("1. Model only on labelled data\t2.Model on labelled and unlabelled")
ch=int(input("Enter choice: "))
if(ch==1):  
    print("When Logistic Regression model created on just labelled data")
    bias = [float(1)]*len(final) 
    full_without=[]                                                                                                                   
    for i in range(len(height)):                                                                                                                                                                            
        full_without.append((bias[i],height[i],weight[i],age1[i]))                                                                                                           
    theta=cost(theta,full_without)  
    #print(theta) 
    bias_t=[float(1)]*len(final2)
    #bias_test=[float(1)]*len(data2)                                                                                                   
    full_test=[]                                                                                                                      
    test_data=[]                                                                                                                      
                                                                                                                      
    for i in range(len(final2)):                                                                                                                                                                                                      
        full_test.append((bias_t[i],height_t[i],weight_t[i],age1_t[i]))                                                   
        #test_data.append((height_test[i],weight_test[i],age1_test[i]))                                                                                                                                                                                
    #print "\nTest Data",full_test                                                                                                     
                                                                                                                                      
                                                                                                                                      
    mul1 = dot_product(full_test,theta)                                                                                                          
    final_pred,without_round=sigmoid_cal(mul1)                                                                                                      
                                                                                                         
    print("Weights learned",theta    )                                                                                                 
    #print "Final prediction",final_pred                                                                                               
    for i in range(len(final_pred)):                                                                                                  
        final_pred[i]=round(final_pred[i])                                                                                            
    #print ("Actual classes",test_probability) 
                                                                                              
    
    for i in range(len(final_pred)):
        if(final_pred[i]==1):
            class_u.append('M')
        else:
            class_u.append('W')
    print ("Final prediction",class_u  )
    print(final_pred)
    count_t=0                                                                                               
    #print "Final prediction",final_pred                                                                                               
    for i in range(len(final_pred)):                                                                                                  
        final_pred[i]=round(final_pred[i])   
        if(final_pred[i]==test_probability[i]):
            count_t+=1   
    print("Accuracy",(count_t/len(final_pred))*100,"%")

if(ch==2):
    print("When Logistic Regression model created on labelled and unlabelled data")
    bias = [float(1)]*len(final)
    full_without=[]                                                                                                                   
    for i in range(len(height)):                                                                                                                                                                            
        full_without.append((bias[i],height[i],weight[i],age1[i]))
    theta=cost(theta,full_without)  
    #print(theta) 
    bias_u=[float(1)]*len(final1)
    #bias_test=[float(1)]*len(data2)                                                                                                   
    full_test=[]                                                                                                                      
    test_data=[]                                                                                                                      
                                                                                                                      
    for i in range(len(final1)):                                                                                                                                                                                                      
        full_test.append((bias_u[i],height_u[i],weight_u[i],age1_u[i]))                                                   
        #test_data.append((height_test[i],weight_test[i],age1_test[i]))                                                                                                                                                                                
    #print "\nTest Data",full_test                                                                                                     
                                                                                                                                      
                                                                                                                                      
    mul1 = dot_product(full_test,theta)                                                                                                          
    final_pred,without_round=sigmoid_cal(mul1)                                                                                                      
    #print(without_round,len(without_round))
    male=[]
    female=[]
    combined=[]
    new=[]
    for i in range (len(without_round)):
        if without_round[i]>0.5:
            male.append((without_round[i],i))
            combined.append((without_round[i],i))
        else:
            female.append((1-without_round[i],i))
            combined.append((1-without_round[i],i))
    
    #print("male",male,"fem",female,"\n")
    #print(sorted(combined,reverse=True))
    new=sorted(combined,reverse=True).copy()
    updated=[]
    for i in range(5):
        updated.append(new[i])
    
    #combined=[]
    #combined=(male,female)
    #print(sorted(male,reverse=True))
    #print(sorted(female,reverse=True))
    #print(new[0][1])
    
    #full_without.append()
    print("Weights learned",theta    )                                                                                                 
    #print "Final prediction",final_pred                                                                                               
    for i in range(len(final_pred)):                                                                                                  
        final_pred[i]=round(final_pred[i])                                                                                            
    #print ("Actual classes",test_probability) 
                                                                                              
    
    for i in range(len(final_pred)):
        if(final_pred[i]==1):
            class_u.append('M')
        else:
            class_u.append('W')
    print ("Final prediction",class_u  )
    #print(final_pred)

    #print("Accuracy")
    for i in range(len(final1)):
        height.append(height_u[i])
        weight.append(weight_u[i])
        age1.append(age1_u[i])
        true_probability.append(final_pred[i])
    full_without=[]    
    bias=[float(1)]*len(height)                                                                                                               
    for i in range(len(height)):                                                                                                                                                                            
        full_without.append((bias[i],height[i],weight[i],age1[i]))
    theta=cost(theta,full_without)
    bias_t=[float(1)]*len(final2)
    #bias_test=[float(1)]*len(data2)                                                                                                   
    full_test=[]                                                                                                                      
    test_data=[]                                                                                                                      
                                                                                                                      
    for i in range(len(final2)):                                                                                                                                                                                                      
        full_test.append((bias_t[i],height_t[i],weight_t[i],age1_t[i]))                                                   
        #test_data.append((height_test[i],weight_test[i],age1_test[i]))                                                                                                                                                                                
    #print "\nTest Data",full_test                                                                                                     
                                                                                                                                      
                                                                                                                                      
    mul1 = dot_product(full_test,theta)                                                                                                          
    final_pred,without_round=sigmoid_cal(mul1)                                                                                                      
                                                                                                         
    print("Weights learned",theta    )  
    count_t=0     
    #print(final_pred)                                                                                          
    #print "Final prediction",final_pred                                                                                               
    for i in range(len(final_pred)):                                                                                                  
        final_pred[i]=round(final_pred[i])   
        if(final_pred[i]==test_probability[i]):
            count_t+=1   
    
    final_c=[]
    
    for i in range(len(final_pred)):
        if(final_pred[i]==1):
            final_c.append('M')
        else:
            final_c.append('W')
    print ("Final prediction",final_c  ) 
    print("Accuracy",(count_t/len(final_pred))*100,"%")                                                                                     
    #print ("Actual classes",test_probability) 
                                                                                              
    