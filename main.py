# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import re

filepath = os.path.join('C:\\', 'Users', 'OlaOlumuyiwa', 'Documents', 'BridgeviewERAs')
arr = os.listdir(filepath)
pattern = re.compile("S5100")
mylist = list()

for filename in arr:
    FullFileName = filepath + '\\' + filename
    print(FullFileName)
    #print(os.path.exists(FullFileName))
    with open(FullFileName, 'r') as f:
        for line in f:
            if pattern.search(line):
                mylist.append(line.rstrip()[-3:-1])
                print(line.rstrip()[-3:-1])

print("End of line")
#results = list(map(int, mylist))
#print(results)
# filepath2 = filepath + '\\' + arr[1]
# print(filepath2)
# with open(filepath2, 'r') as f:
#     for line in f:
#         print (line)
# cwd = os.getcwd()
# print(cwd)

# print('\n Hi, Test')  # Press Ctrl+F8 to toggle the breakpoint.
