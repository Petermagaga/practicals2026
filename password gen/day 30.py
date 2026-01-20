try:
    file=open("file.txt")
except:
    open("file.txt","w")
    print(f"there was an error")