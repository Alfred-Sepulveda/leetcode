# read file
f = open("demofile.txt", "r")
print(f.read())

#Write file
#w = open("demofile.txt", "w")
#w.write("whoops! I have deleted the content")

#close file
f.close()

#create a file called "myfile.txt"
f = open("myfile.txt", "x")

#create a new file if it doesn't exist
#f = open("myfile.txt", "w")


#very simple to learn but also very simple to forget.
#open file on a different location:
# f = open("D:\\myfiles\demofile.txt", "r")
# print(f.read())

