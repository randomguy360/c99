import os 
import shutil
source = input('source folder name: ')
destination = input('destination folder name: ')
source = source + '/'
destination = destination + '/'
list_of_files = os.listdir(source)
for i in list_of_files :
        shutil.move(source + i,destination )