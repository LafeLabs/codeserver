file = open("sample.txt",'w+')


file2 = open("sketch.js",'r+')

foo = file2.read()
file2.close()

file.write("newefes" + foo)
file.close()
