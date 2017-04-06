from config import config
from iteration import iteration
from eta import eta
import matplotlib.pyplot as plt

def set_up():
    import numpy as np
    config['delta_r'] = config['r_range'] / config['N']
    delta_k = np.pi/(config['N'] * config['delta_r'])
    beta = np.reciprocal(config['T'] * config['kb'])
    config['delta_k'] = delta_k
    config['beta'] = beta

if __name__ == '__main__':
    set_up()
    eta = eta()
    h_i = iteration(eta)
    gr = h_i + 1.
    plt.plot(eta.r, gr)
    plt.show()
