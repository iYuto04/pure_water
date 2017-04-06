from eta import eta
import numpy as np
from config import config
from scipy import fftpack

def calc_DCM_from_HNC(c_i):
    '''
    :DCM -> Direct Correlation Function
    :c_i 実空間での直接相関関数
    :c_j 波数空間での直接相関関数
    '''
    c_j = fftpack.fft(c_i)
    return c_j

def solve_OZ_equation(c_j):
    '''
    OZ方程式を解く
    :h_j 波数空間での全相関関数
    :h_i 実空間での全相関関数
    '''
    from solvent import solvent
    h_j = c_j / (1. - solvent['rho'] * c_j)
    h_i = fftpack.ifft(h_j)
    return h_i

def iteration(eta):
    '''
    イタレーション部分
    '''
    count = 0 #無限ループ阻止
    while True:
        count += 1
        c_i = np.exp(- config['beta'] * eta.potential + eta.value) - eta.value - 1.
        c_j = calc_DCM_from_HNC(c_i)
        h_i = solve_OZ_equation(c_j)
        check = eta.check_diff(h_i - c_i)
        if check != 1:
            return h_i
        if count > 10000:
            break


if __name__ == '__main__':
    from main import set_up
    import matplotlib.pyplot as plt
    set_up()
    eta = eta()
    h_i = iteration(eta)
    gr = h_i + 1.
    plt.plot(eta.r, gr)
    plt.show()
