
# coding: utf-8

# In[1]:

import tkinter as tk


# In[2]:

from msvcrt import getch


# In[3]:

src = open("Source.txt","a" )


# In[4]:

root = tk.Tk()


# In[5]:

root.withdraw()


# In[6]:

if root.clipboard_get() == "":
    root.clipboard_append("Moin Moin")
else:
    clipboard = root.clipboard_get()
    
print(clipboard)


# In[ ]:


key = ord(getch())
if key == key: #Wwww
    print(root.clipboard_get)


# In[ ]:

print("HI")


# In[ ]:



