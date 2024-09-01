
from faker import Faker 
import numpy as np
def generate_random_data(keys,rows):
    if len(keys) == 0:
        keys =np.array(['first name','last name','email','id','company'])
    faker =Faker()
    data = []
    for _ in range(rows):
        dic={}
        if 'first name' in  keys:
            dic['first name']=faker.first_name()
        if 'last name' in  keys:
            dic['last name']=faker.last_name()
        if 'email' in  keys:
            dic['email']=faker.free_email()
        if 'id' in  keys:
            dic['id']=faker.credit_card_security_code()
        if 'company' in  keys:
            dic['company']=faker.company()
        if 'phone' in  keys:
            dic['phone']=faker.phone_number()
        data.append(dic)
    return data    










