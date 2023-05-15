
"""
#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e 
#optou por não ter um 13º andar.
#Escreva um código que imprima todos os números exceto o número 13
"""

andar= list(range(1, 21))
andar.remove(13)
    
print(f"Andar - {andar}")

"""
Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição 
aprendidos.
"""

#FOR 

print("===========FOR===========")
i=1

for i in range(1,21):
    if(i==13):
        continue
    print(f"Andar - {i}")



#WHILE

print("==========WHILE==========")
i = 1
while i <= 20:
    if i == 13:
        i += 1
        continue
    print(f"Andar - {i}")
    i += 1
print("=========================")

"""
Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
"""
i=1

for i in range(20,0,-1):
    if(i==13):
        continue
    print(f"Andar - {i}")
    
    