if False :
    a = 10
    b = 10
    c = 11

    if a == b :
        print('Egalité')
    elif a > c :
        print('A plus grand que c')
    else :
        print('A plus petit que c')

print('Boucles')
seuil = 20
m = 7
n = 10
# for i in range(n+1):
#     print(i)
#     p = m * i
#     if p < seuil :
#         print(i, ' x ', m , ' = ', p)
#     else :
#         print('Sup à ', seuil)
#         break

for i in range(n+1):
    # print(i)
    p = m * i
    
    couleur = 'Bleu'
    if i % 2 == 1 :
        couleur = 'Rouge'
        
    print(i, ' x ', m , ' = ', p, ' ', couleur)

    