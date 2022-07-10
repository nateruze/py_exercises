#!/usr/bin/env python
# coding: utf-8

# # Python Exercises (Beginner-Intermediate)

# In[3]:


import sys


# #### Let's start with printing out "Hello World!" as a rite of passage.

# In[4]:


print("Hello World!")


# #### IFs and LOOPS

# Ex 1. Write a function that takes in any integer i between 0 and 20, and outputs the square of all integers n where n <= i

# In[22]:


def num_sqr():
    try:
        n = int(input("Enter an integer between 0 and 20: "))
    except ValueError:
        print("Input must be an integer")
    
    if n >= 1 and n <= 20:
        for i in range(n):
            print(i*i)
    else:
        raise ValueError("Input out of range")
        
        


# In[23]:


num_sqr()


# Ex 2. Find the runner-up score

# In[30]:


def ru_score():
    arr = map(int, input("Enter scores separated by space: ").split())
   
    arr_sorted = sorted(arr, reverse=True)
    max_score = arr_sorted[0]
    
    
    for i in range(1, len(arr_sorted)):
        if arr_sorted[i] < max_score:
            ru_score = arr_sorted[i]
            break
    print("The runner up score is: " + str(ru_score))
    


# In[31]:


ru_score()


# #### Nested Lists and Bubble Sort

# Ex 3. Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade. If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# In[36]:


def second_lowest_score():
    
    main_lst = []
    
    for _ in range(int(input("Enter number of total students N: "))):
        temp_lst = []
        name = input("Enter name: ")
        temp_lst.append(name)
        score = float(input("Enter score: "))
        temp_lst.append(score)
        main_lst.append(temp_lst)
    
    main_lst.sort(key = lambda x: x[1])
    
    
    lowest_score = main_lst[0][1]
    i = 1
    while i < len(main_lst):
        if main_lst[i][1] > lowest_score:
            second_lowest = main_lst[i][1]
            break
        else:
            continue
    
    names_second_lowest = []
    for i in range(len(main_lst)):
        if main_lst[i][1] == second_lowest:
            names_second_lowest.append(main_lst[i][0])
    
    names_second_lowest.sort()
    for n in names_second_lowest:
        print(n)
        
   
        


# In[37]:


second_lowest_score()


# Ex 4. Repeat ex 3 using bubble sort

# In[ ]:




