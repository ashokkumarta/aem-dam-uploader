import os

path = '.'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for dir in d:
        files.append(os.path.join(r, dir))

for f in files:
    print(f)

    