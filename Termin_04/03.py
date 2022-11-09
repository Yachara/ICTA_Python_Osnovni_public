# FOR/WHILE zanke


# BREAK

# a = ["mojca","nejc","anže","gregor","lon"]
# for ime in a:
# 	print(ime)
# 	if ime=="nejc":
# 		break


# CONTINUE

# a = ["mojca","nejc","anže","gregor","lon"]
# for ime in a:
# 	if "n" in ime:
# 		continue
# 	print(ime)

a = [1,5,8,2]
b = [11,4,9,3]
# for <ime_spremenljivke> in <iterable object>:
for nekineki in a:
	for el_b in b:
		if nekineki < el_b:
			print(nekineki,el_b)


