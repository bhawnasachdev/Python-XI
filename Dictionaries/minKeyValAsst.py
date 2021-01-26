dict1 = eval(input("Enter dictionary 1: "))
dict2 = eval(input("Enter dictionary 2: "))

# printing original dictionaries 
print("The original dictionary 1 is : ", dict1) 
print("The original dictionary 2 is : ", dict2) 
  
# using min() to assign min values 
res = {}
for key, val in dict1.items():
    res[key] = min(val, dict2[key])
    
# printing result 
print("The minimum value keys : ", res)