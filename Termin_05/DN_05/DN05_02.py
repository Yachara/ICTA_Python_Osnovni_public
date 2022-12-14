"""
Naloga: 
Napiši generator moj_generator, ki igra igro BUM-BAM. Generator naj sprejme 1 argument, ki je številka s katero naj začne in igra do 21 (vključno 21). 
Nato naj vrača eno številko naenkrat.
Če je številka deljiva s 3 oziroma ima v sebi številko 3, naj vrne BUM. Če je številka deljiva s 7 oziroma ima v sebi številko 7, naj vrne BUM.

Ča sta izpolnjena oba pogoja, naj vrne BUM BAM.

Če ni izpolnjen noben pogoj, naj vrne številko.

Primeri:

Input:
for i in moj_generator(1):
    print(i)

Output:
1
2
BUM 
4
5
BUM 
BAM
8
BUM 
10
11
BUM 
BUM 
BAM
BUM 
16
BAM
BUM 
19
20
BUM BAM


Input:
for i in moj_generator(12):
    print(i)

Output:
BUM 
BUM 
BAM
BUM 
16
BAM
BUM 
19
20
BUM BAM
"""


def moj_generator(num):

    while num < 22:
        value = ""
        if "3" in str(num) or num % 3 == 0:
            value += "BUM "
        if "7" in str(num) or num % 7 == 0:
            value += "BAM"
        if not value:
            value = num
        yield value
        num += 1


for i in moj_generator(12):
    print(i)
