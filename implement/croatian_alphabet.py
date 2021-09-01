##### 크로아티아 알파벳 #####
# URL : https://www.acmicpc.net/problem/2941
import re
str = input()
str = str.replace('c=','k')
str = str.replace('c-','k')
str = str.replace('dz=','k')
str = str.replace('d-','k')
str = str.replace('lj','k')
str = str.replace('nj','k')
str = str.replace('s=','k')
str = str.replace('z=','k')
print(len(str))
