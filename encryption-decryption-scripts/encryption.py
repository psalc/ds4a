#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
import math

# Setting up replacement dictionary constant
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
values = list(range(1, 54))
replacement_dict = {}
for letter, value in zip(letters, values):
    replacement_dict[letter] = value
    
# Setting values for constants
p = 101
q = 139
n = p * q
phi = (p - 1) * (q - 1)
e = 7
d = int((2 * phi + 1) / e)


# In[6]:


def encrypt(input_string):
    """
    Argument: input_string, a string variable based on user-prompted input.
    
    Output: encrypted_char_list, list of encrypted values for each character in input string
    """    
    characters = list(input_string)
    
    translated_string = [replacement_dict[char] for char in characters]
    
    encrypted_char_list = [(char ** e) % n for char in translated_string]

    return encrypted_char_list


# In[7]:


msg = input("Please type the message you would like to encrypt.\n")


# In[9]:


print(encrypt(msg))

