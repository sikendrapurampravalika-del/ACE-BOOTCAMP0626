with open("/workspaces/ACE-BOOTCAMP0626/day5/tulip.jpg", "rb") as f:
   content = f.read(2000)
with open("/workspaces/ACE-BOOTCAMP0626/day5/tulip.jpg", "wb") as cf:
      while content > 0:
       cf.write(content)
       content = f.read(2000)