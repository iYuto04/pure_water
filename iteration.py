from eta import eta
import numpy as np
from config import config
from scipy import fftpack

def calc_DCM_from_HNC(eta):
    '''
    :DCM -> Direct Correlation Function
    :c_i 実空間での直接相関関数
    :c_j 波数空間での直接相関関数
    '''
    c_i = np.exp(- config['beta'] * eta.potential + eta.value) - eta.value - 1
    c_j = fftpack.fft(c_i)
    return c_j
if __name__ == '__main__':
    from main import set_up
    import matplotlib.pyplot as plt
    set_up()
    eta = eta()
    c_j = calc_DCM_from_HNC(eta)
    plt.plot(eta.k, c_j)
    plt.show()
    print(calc_DCM_from_HNC(eta))
