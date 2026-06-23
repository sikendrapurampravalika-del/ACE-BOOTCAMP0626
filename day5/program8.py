fname=input("enter a file name you want to open")
f = open("/workspaces/ACE-BOOTCAMP0626/day5/program7.py","w")
if(f):
    f.write("i liking working with codes")
print("file name is",f.name)
print(f.tell())
f.close()
print(f.closed)
try:
    with open("/workspaces/ACE-BOOTCAMP0626/day5/program7.py","r") as f:
        print(f.read())
except Exception as e:
    print(e)
print(f.closed)