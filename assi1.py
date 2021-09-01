
# #List_remove_append
# #Description: Remove SPSS from input_list=['SAS', 'R', 'PYTHON', 'SPSS'] and add 'SPARK'
# #in its place.
#
# lis1 = ['sas', 'r', 'python', 'spss' ]
# print(lis1)
# lis1.remove('spss')
# print(lis1)
# lis1.append('spark')
# print(lis1)

# String to List Conversion
# Description: Convert a string input_str = 'I loveData Science & Python' to a list by
# splitting it on ‘&’. The sample output for this stringwill be:


# li = "I loveData Science & Python"
# print(li.split("&"))

# List to String Conversion
# Description: Convert a list ['Pythons syntax is easyto learn', 'Pythons syntax is very
# clear'] to a string using ‘&’. The sample output ofthis string will be:

# Conversion using Join
# inp_list = ['Pythons syntax is easy to learn', 'Pythons syntax is very clear']
# out_str = " & "
# print("Converting list to string using join() method:\n")
# print(out_str.join(inp_list))

# Nested List
# Description: Extract Python from a nested list
# input_list =  [['SAS','R'],['Tableau','SQL'],['Python','Java']]

# test_list = [['SAS','R'],['Tableau','SQL'],['Python','Java']]
# print(test_list[2][0])

# It’s the time to disco
# Description: t = ("disco", 12, 4.5)
# What is the output of: t[0][2]

# t = ("disco", 12, 4.5)
# print(t[0][2])
# #output - s

# String Palindrome
# Description: Write a program to check whether a stringis a palindrome or not. Print 1 if
# the string is a palindrome and 0 otherwise.
def isPalindrome(s):
    return s == s[::-1]

# s = "Avsr"
# ans = isPalindrome(s)
#
# if ans:
#     print("1")
# else:
#     print("0")

# MCQ
# S = 'I love Python'
# print(S[2:6])
#
# a = 3 * 3 ** 3
# print(a)
# Ans - C

# a= ((500//7) % 5) ** 3
# print(a)
# Ans - a

# T = (3, 5, 7, 11)
# Ans - c (3,5,7,11,9)

