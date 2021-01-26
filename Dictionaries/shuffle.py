import random 
  
dictionary = eval(input("Enter a dictionary : "))
keys_list = list(dictionary.keys())
values_list = list(dictionary.values()) 

# shuffling values 
random.shuffle(values_list) 

# Forming the result
res = {keys_list[i]: values_list[i] for i in range(len(keys_list))}

# printing result 
print("The shuffled dictionary : " + str(res)) 