lista  =  [1,20,31,45,50,61]
lista[1] = 200
print(lista)


soma  =  lista[2] + lista[-1]
print(soma)


isso_e_uma_lista = list(range(1,251,2))
print(isso_e_uma_lista)


l = list(range(1,11))
print(l)


# funções:


# funções para adicionar um dado
l = []
print(l)
l.append(10)
print(l)
l.extend([10,1,2,0])
l +=(5,332,65)
l.insert(0,250)
l[0] = 250
print(l)


# deleta o último valor
l.pop(1)
l.remove(250)
del l[3]
print(l)


# print(dir(l))

# funlções que nã i impactam s estrutura da lista. 
print(len(l))
print(max(l))
l.sort(reverse=True)
print(l)