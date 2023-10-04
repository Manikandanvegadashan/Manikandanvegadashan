 Python3 code to demonstrate working of
# Cumulative List Split
# Using loop
 
# initializing list
test_list = ['gfg-is-all-best']
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing Split char
spl_char = "-"
 
# Cumulative List Split
# Using loop
res = []
for sub in test_list:
    for idx in range(len(sub)):
        if sub[idx] == spl_char:
            res.append([ sub[:idx] ])
    res.append([ sub ])
 
# printing result
print("The Cumulative List Splits : " + str(res))
