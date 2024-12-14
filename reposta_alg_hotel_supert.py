"""Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)"""

#RESOLUÇÃO COM FOR IN

print()   
print() 

print ("resolução com laço for in\n")
qtd_andares = 20

for i in range(1, qtd_andares + 1):
    if i ==13:
        continue
    print("Andar", i)
    
print()   
print()   
    
    
#RESOLUÇÃO COM FOR WHILE

print ("resolução com laço for while\n")
andares = 20    
i = 1  

while i < andares:
    if i == 13:
        i += 1
        continue
    print("Andar", i)
    i += 1
    
print()   
print() 


#RESOLUÇÃO COM FOR IN DESCRESCENTE

print ("resolução com laço for in Decrescente\n")
qtd_andares = 20

for i in range(qtd_andares, 0, -1):
    if i == 13:
        continue
    print("Andar", i) 