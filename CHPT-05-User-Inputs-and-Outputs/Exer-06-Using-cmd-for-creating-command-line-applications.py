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

###
import cmd

class Roulette(cmd.Cmd):
    def preloop(self):
        self.bets = {}
        self.stake = 100
        self.wheel = wheel()
    def do_bet(self, arg_string):
        if arg_string not in BET_NAMES:
            print("{0} is not a valid bet".format(arg_string))
            return
        # Happy path: more goes here.
        self.bets[arg_string] = 1
    def do_spin(self, arg_string):
        if len(self.bets) == 0:
            print("No bets have been placed")
        return 
    # Happy path: more goes here.
    BET_NAMES = set(['even', 'odd', 'high', 'low', 'red', 'black'])

self.spin = random.choice(self.wheel)
print("Spin", self.spin)
label, winners = self.spin
for b in self.bets:
    if b in winners:
        self.stake += self.bets[b]
        print("Win", b)
    else:
        self.stake -= self.bets[b]
        print("Lose", b)
self.bets = {}

if __name__ == "__main__":
    r = Roulette()
    r.cmdloop()

###

class Roulette(cmd.Cmd):
    prompt="Roulette> "
