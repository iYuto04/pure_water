from config import config
def set_up():
    import numpy as np
    N = config['r_range'] / config['delta_r']
    delta_k = np.pi/(N * config['delta_r'])
    beta = np.reciprocal(config['T'] * config['kb'])
    config['N'] = int(N)
    config['delta_k'] = delta_k
    config['beta'] = beta

if __name__ == '__main__':
    set_up()
    print(config)
    print('hello')
