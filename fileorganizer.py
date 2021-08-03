import os
path = 'class99/b/file1.txt'
root_ext = os.path.splitext(path)
print('rootPart: ',root_ext[0])
print('extpart: ',root_ext[1])