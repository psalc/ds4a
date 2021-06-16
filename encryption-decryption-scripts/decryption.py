#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
import math
import ast

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


# In[8]:


def decrypt(encrypted_chars):
    """
    Takes encrypted_chars input as a list and decrypts, returning
    the original unencrypted message.
    
    Arguments: encrypted_chars, list
    
    Output: decrypted_string, string
    """
    detranslated_chars = [(char ** d) % n for char in encrypted_chars]
    
    decrypted_chars = []
    
    for each in detranslated_chars:
        for key, value in replacement_dict.items():
            if each == value:
                decrypted_chars.append(key)
    
    decrypted_string = ''.join(decrypted_chars)
    
    return decrypted_string


# In[9]:


cipher = ast.literal_eval(input('Please paste your encrypted message exactly.\n'))


# In[13]:


print(decrypt(cipher))

