#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[57]:


abc_co=pd.read_csv('myexcel - myexcel.csv.csv')
abc_co


# In[4]:


abc_co.info()


# In[5]:


abc_co.describe()


# ## Correct the data in the "height" column by replacing it with random numbers between 150 and 180.(Preprocessing)

# In[5]:


abc_co["Height"].value_counts()


# In[32]:


abc_co['Height'] = np.random.randint(150, 181, size=len(abc_co))
abc_co


# In[29]:


print(len(abc_co))


# ### Determine the distribution of employees across each team and calculate the percentage split relative to the total number of employees.

# In[88]:


teams=abc_co['Team'].value_counts()
teams # total teams and respective number of employees 


# In[89]:


team_perc=(teams/len(abc_co))*100
team_perc # Percentage split


# In[14]:


team_distribution = pd.DataFrame({
    'Team': teams.index,
    'Employee Count': teams.values,
    'Percentage': team_perc.values})
team_distribution


# In[91]:


plt.pie(team_perc)
plt.title("Distribution of Employees")
plt.show()


# ### The team New Orleans Pelicans has most number of employees with a percentage split of 4.148472%.

# ## Segregate employees based on their positions within the company.

# In[83]:


abc_co["Position"].value_counts()


# In[85]:


po=abc_co["Position"]
plt.hist(po)
plt.xlabel("Position")
plt.ylabel("Number of employees")
plt.show()


# ### The position SG has the most number of employees

# ## Identify the predominant age group among employees.

# In[13]:


a=abc_co["Age"].value_counts()
a


# In[19]:


a.max()


# In[18]:


a.idxmax()


# In[73]:


age=abc_co['Age']
plt.hist(age)
plt.show()


# ### The most employees of the age group are of 24 years followed by 25 years , 27 years.

# ## Discover which team and position have the highest salary expenditure.

# In[47]:


abc_co[["Salary","Position","Team"]].max()


# In[63]:


x=abc_co['Position']
y=abc_co['Salary']
plt.bar(x,y)
plt.title("Employee Position with Highest Salary")
plt.show()


# ### The Washington Wizards spend the most on salaries, with "SG" being the position with the greatest salary expenditure.
# 

# ###  Investigate if there's any correlation between age and salary, and represent it visually.

# In[59]:


sns.scatterplot(x='Age',y='Salary',data=abc_co)
sns.lineplot(x='Age',y='Salary',data=abc_co)
plt.title("Correlation Between Age & Salary")
plt.show()


# ### As per the graph , I think it is safe to say that there is no strong correlation between age and salary of employees

# In[ ]:




