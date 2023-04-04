# Python3 code to demonstrate working of
# Replace words from Dictionary
# Using list comprehension + join()

# initializing string
test_str = 'geekforgeeks best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# lookup Dictionary
lookp_dict = {"best": "good and better", "geeks": "all CS aspirants"}

# one-liner to solve problem
res = " ".join(lookp_dict.get(ele, ele) for ele in test_str.split())

# printing result
print("Replaced Strings : " + str(res))


# https://www.geeksforgeeks.org/python-replace-words-from-dictionary/