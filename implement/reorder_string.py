##### 문자열 재정렬 #####
import re

strings = input()
string_list = []
sum = 0
for char in strings:
    if char.isalpha():
        string_list.append(char)
    else:
        sum += int(char)
        

string_list.sort()
if sum != 0:
    string_list.append(str(sum))
print(''.join(string_list))