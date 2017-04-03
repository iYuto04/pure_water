'''
etaを管理するクラスの実装
'''
from config import config
import numpy as np
import sys
class eta:
    '''
    :value
    :pre_value
    :potential ポテンシャルの値は一度計算して持っておけばいいのでetaクラスに持たせる
    イタレーションによりetaの誤差を評価する際に前回の結果と今回の結果を比べるために持っておく
    :r 今回計算する実空間の距離.一度セットしておけば後で使えるためetaクラスで持っておく
    :tol 許容誤差
    :pre_diff 前回の計算のときの誤差
    '''
    value = []
    pre_value = []
    potential = []
    r = np.arange(0, config['r_range'], config['delta_r'])

    __tol = 0.001
    __pre_diff = 10000

    def __init__(self):
        from solvent import LJ_potential
        x = np.arange(0, config['r_range'], config['delta_r'])
        y = LJ_potential(x)
        self.potential = np.array(y)
        self.value = np.exp(-config['beta'] * y) - 1.

    def check_diff(new_value):
        '''
        etaの収束計算のための関数
        '''
        now_diff = np.max(np.absolute(self.value - new_value))
        if now_diff > pre_diff:
            print('誤差が収束していません')
            sys.exit()
        elif now_diff > self.__tol:
            self.pre_value = self.value
            self.value = new_value
            self.__pre_diff = now_diff

if __name__ == '__main__':
    '''
    このプログラムを実行すればetaの初期値がプロットされる
    '''
    import matplotlib.pyplot as plt
    from solvent import solvent
    from main import set_up
    set_up()
    def plot_eta(x,y):
        plt.plot(x,y)
        plt.plot(x,y)
        plt.show()
    eta = eta()
    x = np.arange(0, config['r_range'], config['delta_r'])
    plot_eta(eta.r,eta.value)
