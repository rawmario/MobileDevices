#!/usr/bin/env python
# coding: utf-8

# In[61]:


def callTar(direction, dur):
    if direction == 'o':
        myVarOfTar = 2
    elif direction == 'i':
        myVarOfTar = 0
    else:
        print('I\'m gay')
    return float(myVarOfTar * dur)


# In[65]:


def messTar(number):
    myNumOfTar = 10
    myTar = 1
    if number <= myNumOfTar:
        return 0
    return myTar * (number-myNumOfTar)


# In[71]:


import csv

def biller(a):
    bill = 0.0
    for row in csvReader:
        if row['msisdn_origin'] == a:
            bill += callTar('o',float(row['call_duration']))
            bill += messTar(int(row['sms_number']))
        elif row['msisdn_dest'] == a:
            bill += callTar('i', float(row['call_duration']))
    return bill
client = str(915783624)
with open('/Users/romanbelov/Downloads/lab1.csv', 'r', newline='') as csvfile:
    csvReader = csv.DictReader(csvfile, delimiter=',')
    print('Для абонента', client,'плата составит', biller(client),'рублей', )
    csvfile.close()


# In[ ]:





# In[ ]:




