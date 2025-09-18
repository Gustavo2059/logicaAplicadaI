'''#aulas funções

#declações
a = int(input('Digite de a: '))
b = int(input('Digite de b: '))
c = 0

def soma():
    c = a + b
    print(c)
    return c

def main():
    c = soma()
    d = int(c)+1
    print(d)

if __name__ == '__main__':
    main()'''


#Exercício lista 2b

#imports
import numpy as np

x = np.random.rand(5)
w = np.random.rand(5)
b = 1
v = 0
u = 0

def juncaoAditiva():
    print(w)
    print(x)
    for i in range(len(x)):
        v=x[i]*w[i]
        u = u+v
        print(v)
    u = u-b
    print(u)
def main():
    juncaoAditiva()

if __name__ == '__main__':
    main()