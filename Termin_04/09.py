# keyword arguments


# def fun(ime, priimek, naslavljanje="gospodična"):
# 	print(f"Pozdravljeni {naslavljanje} {ime} {priimek}.")

# fun("Miha","Novak")


# def fun(a,b,c=0):
# 	print(a+b+c)

# fun(1,2,3)
# fun(1,2)


# def seštevek(a,b,*args):
# 	print(a,b,args)

# seštevek(1,2)
# seštevek(1,2,3)
# seštevek(1,2,3,4)
# seštevek(1,2,8,3,6,[1,2,45],"alala")

def seštevek(a,b,*args,**kwargs):
	print(a,b,args,kwargs)

seštevek(1,2)
seštevek(1,2,55,c=3)
seštevek(1,2,55,88,c=3,d=4)
seštevek(1,2,c=8,d=3,e=6,f=[1,2,45],g="alala",nekaj="sad")