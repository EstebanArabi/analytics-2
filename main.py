
# Q3. sport  Prize money-M prize money-F 

  # |-------------------------------------------|
  # |      |  Average    |    Men    |   Women  |
  # |------|             |           |          |
  # | ISFJ |    14%      |    8%     |    19%   |
  # |------|             |           |          |
  # | ESFJ |    12%      |    8%     |    17%   | 
  # |------|             |           |          | 
  # | ISTJ |    12%      |   16%     |     7%   |
  # |------|             |           |          |
  # | ISFP |     9%      |    8%     |    10%   |
  # |------|             |           |          |
  # | ESTJ |     9%      |   11%     |     6%   |
  # |-------------------------------------------|

# Make 3 lists: name of sport, average prize for men & women, difference in prize money between men & women. 

# X-label - name of mbti type 

# Y-axis - % for average, men & women

# Use a legend - use ply.plot 

import matplotlib.pyplot as ply
import numpy as np

# average = [14, 12, 12, 9, 9] 
# mbti = ["ISFJ", "ESFJ", "ISTJ", "ISFP", "ESTJ"] 
# men = [8, 8, 16, 8, 11]
# women = [19, 17, 7, 10, 6]

file = open("list.csv","r")
dataIn = file.read() 
file.close()

arrays = dataIn.split('\n')

average = [eval(i) for i in arrays[0].split(' ')]
mbti = arrays[1].split(' ')
men = [eval(i) for i in arrays[2].split(' ')]
women = [eval(i) for i in arrays[3].split(' ')]
  

# Create a line graph with names on x-axis and numbers on  y-axis 

X = np.arange(5)
ply.bar(X - 0.25, list(men), width=0.2) 
ply.bar(list(mbti), list(average), width=0.2) 
ply.bar(X + 0.25, list(women), width=0.2)

ply.xlabel("MBTI") 
ply.ylabel("Total") 
ply.legend(["Men %", "Average %", "Women %"]) 
ply.show()