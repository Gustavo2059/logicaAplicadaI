# aula
# funcao

# Imports
import numpy as np

X = np.random.rand(5)
W = np.random.rand(5)
b = 1

def juncaoAditiva():
    u = 0.0
    print("X:", X)
    print("W:", W)
    for i in range(len(X)):
        v = X[i] * W[i]
        u = u + v
        print("v =", v)
        print("u parcial =", u)
    u = u - b
    print("u final (z) =", u)
    return u  # <-- retorna z

def main():
    z = juncaoAditiva()   # <-- captura o retorno
    print("z =", z)
    if z >= 0:
        y = 1
        print(f"A rede neural foi ativada com valor igual a: {y}")
    else:
        y = 0
        print(f"A rede neural foi desativada com valor igual a: {y}")

if __name__ == "__main__":
    main()
