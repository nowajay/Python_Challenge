#!/usr/bin/env python
# coding: utf-8

# In[79]:


import os
import csv


# In[80]:


pybank_csv = os.path.join('Resources', 'budget_data.csv')
pybank_csv


# In[100]:


#Set variables to 0 
month_counter = 0
total_budget = 0
open_value = 0
total = 0
#Create lists for values
change_list = []
months_list = []
#Creat variables for greatest profit and greratest loss of profit and set to 0
greatest_profit = 0
loss_profit = 0
#Read csv file
with open(pybank_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')
#Skip header    
    next(csv_reader)

    for row in csv_reader:
#Create a formula for month and total    
        month_counter +=1
        total_budget += int(row[1])
#Create if statement to skip header and append lists            
        if open_value != 0:
            change = int(row[1]) - open_value
            m_change = str(row[0])
            change_list.append(change)
            months_list.append(m_change)
        
        open_value = int(row[1])
#Formulas for change lists, greatest profit, and loss profit 
    for i in change_list:
        total = total + i
        
        if i > greatest_profit:
            greatest_profit = i
            
        if i < loss_profit:
            loss_profit = i
#Formula for average change  
    average_change = total/len(change_list)
#Assigning lists to variables for analysis
    greatest_month = months_list[change_list.index(greatest_profit)]
    loss_month = months_list[change_list.index(loss_profit)]

bank_results = f"""
    "Financial Analysis"
    "------------------------------"
    "Total Months: {month_counter}"
    "Total: ${total_budget}"
    "Average  Change: ${average_change}"
    "Greatest Increase in Profits: {greatest_month} ($ {greatest_profit})"
    "Greatest Decrease in Profits: {loss_month} ($ {loss_profit})"
    -------------------------------"""

print(bank_results)

file = open("Bank Results.txt" , "w")
file.write(bank_results)
file.close()


# In[ ]:





# In[ ]:





# In[ ]:



    
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




