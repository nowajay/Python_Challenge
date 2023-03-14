#!/usr/bin/env python
# coding: utf-8

# In[57]:


#Import os, csv, and path
import os 
import csv


# In[58]:


pypoll_csv = os.path.join("Resources" , "election_data.csv")


# In[66]:


#Open file and read header
with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvfile)
#Set voter variables to 0    
    Stockham_votes = 0
    DeGette_votes = 0
    Doane_votes = 0
#Count candidate names for each row     
    for row in csv_reader:
        if row[2] =="Charles Casper Stockham":
            Stockham_votes += 1
        
        elif row[2] == "Diana DeGette":
            DeGette_votes += 1
        
        elif row[2] == "Raymon Anthony Doane":
            Doane_votes += 1 
            
    Results = {"Charles Casper Stockham" : Stockham_votes , "Diana DeGette" : DeGette_votes , "Raymon Anthony Doane" : Doane_votes}
            
    Winner = max(Results, key=Results.get)
#Find out the percentage by dividing the specific candidate votes by total votes    
    Stockham_percent = (Stockham_votes / vote_count) * 100
    DeGette_percent = (DeGette_votes / vote_count) * 100
    Doane_percent = (Doane_votes / vote_count) * 100
#Create text file and print to terminal the results    
    results_and_winner = f"""Election Results
    
    ----------------------------
    
    Total Votes: {vote_count}
    
    ----------------------------
    
    Charles Casper Stockham: {Stockham_percent}% ({Stockham_votes})
    Diana DeGette: {DeGette_percent}% ({DeGette_votes})
    Raymon Anthony Doane: {Doane_percent}% ({Doane_votes})
    
    ----------------------------
    
    Winner: {Winner}
    
    ----------------------------"""
    
    print(results_and_winner)
    
    file = open("Winners.txt" , "w")
    file.write(results_and_winner)
    file.close()


# In[ ]:





# In[20]:



    
    


# In[ ]:




