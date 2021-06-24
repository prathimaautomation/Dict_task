#1 - Define a dictionary call story1, it should have the following keys:
        # 'start', 'middle' and 'end'
story1 = {
    "start": "Villain destroying earth",
    "middle": "Hero fights with villain",
    "end": "Hero saves earth from the villain"
}

#2 - Print the entire dictionary
print(story1)

#3 - Print the type of your dictionary
print(type(story1))
#4 - Print only the keys
print(story1.keys())
#5 - print only the values
print(story1.values())
#6 - print the individual values using the keys (individually, lots of print commands)
print(story1.get("start"))
print(story1.get("middle"))
print(story1.get("end"))
#7 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero
story1.update({"hero": "yourSuperHero"})
print(story1.values())
