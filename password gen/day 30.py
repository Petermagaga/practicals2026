"""try:
    with open("killer.txt","r") as file:
        print(file.read())
except KeyError as error_message:
    print(f"the Key {error_message} d0es not exist")

except FileNotFoundError:
    with open("killer.txt","a") as file:
        file.write("look on his face\n Care free \n")


"""
#FileNotFound
"""with open("a_file.txt" ) as file:
    file.read()
    
"""

#indexerror
"""file=["m","n","s"]
print(file[7])"""

#KEYERROR
"""
dict={"KEY":"Value",
      "basic":"vamul"}
valument=dict["KEYs"]"""

#typeerror
"""text="abc"
print(text + 5)

"""

#catching Exceptions
"""try:
    file=open("A_file.txt")
    a_dictionary={"key":"value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file=open("A_file.txt","w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

else:
    print(file.read())

finally:
    raise TypeError("This is does")

"""
"""height=float(input("Height: "))
if height>3:
    raise ValueError("Human height should not be over 3 meters")

weight=int(input("weight: "))

txt=weight/height **2

print(txt)"""

fruits=["Apple","pear","Orange"]

"""def make_pie(index):
    try:
        fruit=fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit+ "pie")"""

facebook_posts=[
    {"likes":21,"comments":2},
    {"likes": 223, "comments": 32},
    {"comments":45,"shares":1},
    {"likes": 21, "comments": 52},
    {"comments":23,"shares":2},

    {"likes": 31, "comments": 32},

]
total_likes =0

for post in facebook_posts:
    try:
        total_likes=total_likes+post["likes"]
    except KeyError:
        pass

print(total_likes)
