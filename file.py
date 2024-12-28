st="Good Morning Hyderabad!!"
f=open("sample.txt","w") #write mode
f.write(st)
f.close()


st="\nGood Morning Nirmal!!"
f=open("sample.txt","a") #append mode
f.write(st)
f.close()


f=open("sample.txt","r") # default also read mode
data=f.read()
print(data)
f.close()

#same thing can be done by with keyword
with open("sample.txt") as f:
  print(f.read())
#dont need to explicitly write f.close() it does itself