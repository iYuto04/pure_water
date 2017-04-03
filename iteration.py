from eta import eta
import numpy as np
from config import config

def calc_DCM_from_HNC(eta):
    '''
    :DCM -> Direct Correlation Function
    :c_i 実空間での直接相関関数
    :c_j 波数空間での直接相関関数
    '''
    c_i = np.exp(- config['beta'] * eta.potential + eta.value) - eta.value - 1
    return c_i
if __name__ == '__main__':
    from main import set_up
    set_up()
    eta = eta()
    print(calc_DCM_from_HNC(eta))
