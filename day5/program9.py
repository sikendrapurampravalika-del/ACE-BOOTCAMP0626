with open("/workspaces/ACE-BOOTCAMP0626/day5/tulip.jpg",'rb')as f:
    content=f.read()
    with open("/workspaces/ACE-BOOTCAMP0626/day5/tulip1.jpg","wb")as cf:
        cf.write(content)