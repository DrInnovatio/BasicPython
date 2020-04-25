#!/usr/bin/env python
# coding: utf-8

# In[25]:


from sklearn.datasets import load_iris
iris = load_iris()
print(iris)


# In[26]:


print(iris.data)


# In[27]:


print(iris.target)


# In[28]:


print(iris.target_names)


# In[29]:


print(type(iris.target))


# In[30]:


print(iris.data.shape)


# In[31]:


print(iris.target.shape)


# #Importing KNN

# In[32]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)


# In[33]:


x = iris.data
y = iris.target


# In[34]:


knn.fit(x,y)


# In[35]:


print(knn.predict([[5.1, 3.5, 1.4, 0.2]]))


# In[36]:


print(knn.predict([[5.9, 3. , 5.1, 1.8]]))


# # Separate data into train and test groups 

# In[51]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.40, random_state = 42)


# In[52]:


print(X_train)


# In[53]:


print(X_train.shape)


# In[42]:


print(X_test.shape)


# In[44]:


knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print(predictions)


# In[50]:


from sklearn import metrics
performance = metrics.accuracy_score(y_test, predictions)
print(performance)


# # Exercise - Finding the best value of K

# In[54]:


k_value = {}
k = 1

while k <= 25:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    performance = metrics.accuracy_score(y_test, predictions)
    k_value[k] = round(performance, 4)
    k += 1
print(k_value)


# In[56]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.plot(list(k_value.keys()), list(k_value.values()) )
plt.xlabel("Value of K")
plt.ylabel = ("Value of K")
plt.show()


# In[ ]:




