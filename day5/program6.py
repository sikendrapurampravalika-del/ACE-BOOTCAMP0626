f = open("/workspaces/ACE-BOOTCAMP0626/day5/program7.py","w+")
f.write("i liking working with codes")
print("file name is",f.name)
print(f.tell())
f.close()
print(f.closed)
with open("/workspaces/ACE-BOOTCAMP0626/day5/program7.py","r+") as f:
    print(f.read())
print(f.closed)