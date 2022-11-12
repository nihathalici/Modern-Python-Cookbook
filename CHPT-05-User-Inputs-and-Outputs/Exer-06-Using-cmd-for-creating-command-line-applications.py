# Exer-06-Using-cmd-for-creating-command-line-applications

red_bins = (1, 3, 5, 7, 9, 12, 14, 16, 18,
           21, 23, 25, 27, 28, 30, 32, 34, 36)

def roulette_bin(i):
    return str(i), {
        'even' if i % 2 == 0 else 'odd',
        'low' if 1 <= i < 19 else 'high',
        'red' if i in red_bins else 'black'
    }

def zero_bin():
    return '0', set()

def zerozero_bin():
    return '00', set()

def wheel():
    b0 = [zero_bin()]
    b00 = [zerozero_bin()]
    b1_36 = [
        roulette_bin(i) for i in range(1, 37)
    ]
    return b0+b00+b1_36