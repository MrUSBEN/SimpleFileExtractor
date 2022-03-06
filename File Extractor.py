'''
This code is created by : USBEN

The function of this program is to extract files
of similar extension from any directory tree no
matter how complex or messy into one common folder
as specified by the user.

'''

import os
import shutil

#Storage
FileNamePathDict={} #stores file name and paths
FileNames=[] #stores file name
FileExtensions=[] #stores file extension
ValidDataLocation=[] #Stores required item location

#INPUTS
DirPath = input("Enter directory path :"+"  ")
OutputDir = input("Enter output directory path :"+"  ")
extensionType = input("What file extension you want to extract ?(example=.txt):"+" ")


#Directory parse loop
for roots,dir,files in os.walk(DirPath, topdown='false'):
    for name in files:
        # storing file name and path in dict
        FileNamePathDict[name]=os.path.join(roots, name)
#print(FileNamePathDict)

#Extracting key values from dict into list for processing
for items in FileNamePathDict.keys():
    FileNames.append(items)
#Extracting extension
for exts in FileNames:
    holder=os.path.splitext(exts)
    FileExtensions.append(holder[1])

#File extension Detection function
counter=-1
for text in FileExtensions:
    counter+=1
    if text == extensionType:
        ValidDataLocation.append(counter)
    else:
        pass

#Data check to check if required files exist
if(len(ValidDataLocation) == 0):
    print('No ('+extensionType+') file/s found , make sure the extension is correct.')
else:
    # Making output folder only if the files exist to be transferred to this folder
    if os.path.isdir(OutputDir) == True:
        print('Output Directory Exists.')
        pass
    else:
        os.mkdir(OutputDir)
        print('Output Directory created.')

#The copy algorithm which combies the similar files into one location
for values in ValidDataLocation:
    ActiveFilePath = FileNamePathDict[FileNames[values]]
    ActiveFileName = FileNames[values]
    shutil.copyfile(ActiveFilePath,os.path.join(OutputDir,ActiveFileName))
    print(ActiveFileName,' Copied successfully.')

print('Operation Completed .\n\n')
input("Press Any button to exit...")












