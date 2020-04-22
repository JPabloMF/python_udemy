# read ("path/name","r") - write ("path/name","w")
new_file = open(
    "E:\\Desarrollo\\PROGRAMMING COURSES\\PYTHON\\UDEMY\\additionalResources\\newfile.txt", "w+")

string = "This is the content that will be written to the text file"

new_file.write(string)
