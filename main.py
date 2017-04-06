from config import config
def set_up():
    import numpy as np
    config['delta_r'] = config['r_range'] / config['N']
    delta_k = np.pi/(config['N'] * config['delta_r'])
    beta = np.reciprocal(config['T'] * config['kb'])
    config['delta_k'] = delta_k
    config['beta'] = beta

if __name__ == '__main__':
    set_up()
    print(config)
    print('hello')
