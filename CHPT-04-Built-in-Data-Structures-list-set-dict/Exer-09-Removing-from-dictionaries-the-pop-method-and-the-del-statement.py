# Exer-09-Removing-from-dictionaries-the-pop-method-and-the-del-statement

working_bets = {}
#working_bets[bet_name] = bet_amount
working_bets['pass'] = 1
del working_bets['come odds']
amount = working_bets.pop('come odds')
working_bets["come"] = 1
working_bets["come"] = None

for bet_name in working_bets:
    print(bet_name, working_bets[bet_name])


