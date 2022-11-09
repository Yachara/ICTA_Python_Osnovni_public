# Poiščite vsa praštevila med 2 in 30
# Praštevilo je število, ki je deljivo samo z 1 in s samim sabo.

# zanka --> i --> sprehodi se po številih ki jih preverjamo [2,3,4,5,...,30] --> range(2,31)
for i in range(2,31):
	# print(i)
	# zanka --> j --> se sprehodi in sešteje koliko ima deljiteljev --> range(1,j+1)
	counter = 0
	for j in range(1,i+1):
		# if --> preveri če je (j) deljitelj od (i)
		if i % j == 0.0:
			counter = counter + 1
	# if --> preveri če sta samo 2 deljitelja
	if counter == 2:
		print(f"Število {j} je preaštevilo.")
	else:
		print(f"Število {j} NI preaštevilo, saj ima {counter} deljiteljev.")









# 	CTRL + C
# i = 0
# while 1<2:
# 	print(i)
# 	i += 1