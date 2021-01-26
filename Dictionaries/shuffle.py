import random 
  
dictionary = eval(input("Enter a dictionary : "))
keys_list = list(dictionary.keys())
values_list = list(dictionary.values()) 

# shuffling values 
random.shuffle(values_list) 

# Forming the result
res = {}
for i in range(len(keys_list)):
    res[keys_list[i]] = values_list[i]

# printing result 
print("The shuffled dictionary : ", res) 