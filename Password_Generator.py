from numpy import random 
import random 

abc='abcdefghijklmnopqrstuvwxyz'
num='0123456789'
spc='<>#&@{}'
lenght=int(input())
lrg=int(input())
sml=int(input())
nums=int(input())
if (lrg+sml+nums)>lenght:
  print('Error. Exit.')
  exit(False)
pasw=''
for i in range(lrg):
  if len(pasw)<=lenght:
      pasw += random.choice(abc.upper())
for i in range(sml):     
  if len(pasw)<=lenght:
    pasw += random.choice(abc)
for i in range(nums):    
  if len(pasw)<=(lenght):
    pasw += random.choice(num)
for i in range(lenght-lrg-sml-nums):
  if len(pasw)<=(lenght):
    pasw += random.choice(spc)
shuffled = random.sample(list(pasw),len(list(pasw)))
password=''
for i in range(len(shuffled)):
  password+=shuffled[i]
print(password)

