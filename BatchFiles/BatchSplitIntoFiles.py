inputPath = input('Please enter your batch path location: ')

File = open(inputPath, 'r')

newListItems = []
for line in File:
    if line[-1] == '\n':
        newListItems.append(line[:-1])
    else:
        newListItems.append(line)


Countdocuments = len(newListItems)
print('----------------------------------------------------')
print('------- Total documents', [Countdocuments], '-------')
print('----------------------------------------------------')
AmountSplit = input('Please enter how much to divide the batch: ')

# how much to divide the file for example to 4
FilesAmount = int(AmountSplit)

# here we divide and we got the number for each file how much it should be 
forEachFile = Countdocuments // int(AmountSplit)

Path = input('Enter target file: ')

# N = 1 | 20 / 4 * N - 1 = 5 * N -1 | = 5 * 1 - 1 = 4 |
# N = 2 | 20 / 4 * N - 1 = 5 * N -1 | = 5 * 2 - 1 = 9 |
# N = 3 | 20 / 4 * N - 1 = 5 * N -1 | = 5 * 3 - 1 = 14|
# N = 4 | 20 / 4 * N - 1 = 5 * N -1 | = 5 * 3 - 1 = 19|

def defMain():
    tempcounter = 0
    N = 1
    for x in range(0, FilesAmount):
        newFileOpen = open(Path + 'Batch'+str(x+1)+'.bat', 'w')
        forEachDocument = forEachFile * N - 1
        N += 1
        while tempcounter < forEachDocument+1:
            newFileOpen.write(newListItems[tempcounter] +'\n')
            tempcounter += 1
        
    print('----------------------------------------------------')
    print(f'Created succssessfully {AmountSplit} files in the following location: {Path}')
    print('----------------------------------------------------')

if __name__ == '__main__':
    defMain()
    input()
