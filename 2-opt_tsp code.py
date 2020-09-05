from numpy import *
import numpy as np

def cout_g(cout, a, b, c, d):
    return cout[a][c] + cout[b][d] - cout[a][b] - cout[c][d]


def deux_opt_sol(route, cout):
    m_choix = route
    impr = True
    while impr:
        impr = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                if cout_g(cout, m_choix[i - 1], m_choix[i], m_choix[j - 1], m_choix[j]) < 0:
                    m_choix[i:j] = m_choix[j - 1:i - 1:-1]
                    impr = True
        route = m_choix
    return m_choix


if __name__ == '__main__':
    villes = 5
    init_route = list(range(villes))
    init_route.append(init_route[0])
    print("route initial \n",init_route)
    cout = np.random.randint(100, size=(villes, villes))
    print("distances aleatoires: \n",cout)
    cout += cout.T
    print("matrice diagonale \n",cout)
    np.fill_diagonal(cout, 0)
    print("matrice des distances \n",cout)
    cout = list(cout)
    k = 0
    for j in range(villes-1):
        k = k + cout[init_route[j]][init_route[j + 1]]
        print(k)
    print("le cout init =", k)
    m_route = deux_opt_sol(init_route, cout)
    print("solution \n",m_route)

    s=0
    for i in range(len(m_route)-1):
        s=s+cout[m_route[i]][m_route[i+1]]
        print(s)
    print("le cout =",s)





