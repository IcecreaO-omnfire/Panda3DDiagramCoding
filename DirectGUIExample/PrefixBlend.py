a=open("Premodel.txt","w+")
b=["ChaliceRot"+str(index) for index in range(61)]
for e in b:
    a.write(e+".png ")
a.flush()
a.close() 
