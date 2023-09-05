#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


chat1='Mytext: Hello, I am having an issue with my order # 42889912'

pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat1)
print(matches)


# In[3]:


chat2='Mytext: I have a problem with my order number 412889912'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat2)
matches


# In[4]:


chat3='Mytext: My order 412889912 is having an issue, I was charged 300$ when online it says 280$'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat3)
matches


# In[5]:


def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]


# In[6]:


get_pattern_match('order[^\d]*(\d*)', chat1)


# In[7]:


chat1 = 'Mytext: you ask lot of questions 😠  1235678912, abc@xyz.com'
chat2 = 'Mytext: here it is: (123)-567-8912, abc@xyz.com'
chat3 = 'Mytext: yes, phone: 1235678912 email: abc@xyz.com'


# In[8]:


get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)


# In[9]:


get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)


# In[10]:


get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)


# In[11]:


get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)


# In[12]:


get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat2)


# In[13]:


get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})', chat3)


# In[14]:


text='''
Born	Elon Reeve Musk
June 28, 1971 (age 50)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa (1971–present)
Canada (1971–present)
United States (2002–present)
Education	University of Pennsylvania (BS, BA)
Title	
Founder, CEO and Chief Engineer of SpaceX
CEO and product architect of Tesla, Inc.
Founder of The Boring Company and X.com (now part of PayPal)
Co-founder of Neuralink, OpenAI, and Zip2
Spouse(s)	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''


# In[15]:


get_pattern_match(r'age (\d+)', text)


# In[16]:


get_pattern_match(r'Born(.*)\n', text).strip()


# In[17]:


get_pattern_match(r'Born.*\n(.*)\(age', text).strip()


# In[18]:


get_pattern_match(r'\(age.*\n(.*)', text)


# In[19]:


def extract_personal_information(text):
    age = get_pattern_match('age (\d+)', text)
    full_name = get_pattern_match('Born(.*)\n', text)
    birth_date = get_pattern_match('Born.*\n(.*)\(age', text)
    birth_place = get_pattern_match('\(age.*\n(.*)', text)
    return {
        'age': int(age),
        'name': full_name.strip(),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()
    }


# In[20]:


extract_personal_information(text)


# In[21]:


text = '''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 64)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Stanford University (drop-out)
Occupation	Chairman and MD, Reliance Industries
Spouse(s)	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent(s)	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''


# In[22]:


extract_personal_information(text)


# In[ ]:




