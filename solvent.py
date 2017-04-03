'''
溶媒のパラメータを指定するファイル.
辞書型のkeyに対して適切な単位の値を指定すること.
sigma[Å]
epsilon[kcal/mol]
'''

solvent = {'name':"Ar", 'sigma': 3.4, 'epsilon': 2.41e-1}

def LJ_potential(x):
    '''np.array型のxを受け取るとそれに対応するLJポテンシャルの値を返す
    グラフを書くときにarray型のyの値が必要になるためである.
    sigma_rはLJポテンシャル内のsigma/rを先に計算してしまう変数であり1e-15を分子に足しているのは0割りを防ぐためである.
    '''
    sigma_r = solvent['sigma']/(x + 1e-15)
    return 4*solvent['epsilon']*(sigma_r ** 12 - sigma_r ** 6)


if __name__ == '__main__':
    '''
    このプログラムを単体で動かすとsolventのLJポテンシャルの様子がプロットされる
    '''
    def plot_LJpotential():
        '''
        LJポテンシャルをプロットするプログラム
        x,yの範囲はsigma,epsilonの倍にとってある
        '''
        import matplotlib.pyplot as plt
        import numpy as np
        x = np.arange(0, 2 * solvent['sigma'], 0.1)
        y = LJ_potential(x)
        plt.plot(x,y)
        plt.xlim(0,2 * solvent['sigma'])
        plt.ylim(-2 * solvent['epsilon'], 2 * solvent['epsilon'])
        plt.show()
    plot_LJpotential()
