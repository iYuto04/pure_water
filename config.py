'''
計算する上でのパラメータを辞書型で持っておく
:r_range [Å]
:delta_r [Å]
:T       [K]
:kb(ボルツマン定数)[kcal/K]
'''

config = {'r_range': 10, 'delta_r': 0.01,'T':300,'kb':3.47e-2}


if __name__ == '__main__':
    def show_config():
        print(config)
    print(config)
