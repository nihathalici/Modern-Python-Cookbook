# Exer-06-Designing-a-while-statement-which-terminates-properly

"""
# initialize something
while # not terminated:
    # do something
assert pword_text == confirming_pword_text
"""

"""
# initialize something
# assert the invariant new-input (pword_text)
# and new-input(confirming_pword_text)
while # not terminated:
    # do something
    # assert the invariant new-input (pword_text)
    # and new-input(confirming_pword_text)
assert pword_text == confirming_pword_text
"""

"""
# initialize something
# assert the invariant new-input (pword_text)
# and new-input(confirming_pword_text)
while pword_text != confirming_pword_text:
    # do something
    # assert the invariant new-input (pword_text)
    # and new-input(confirming_pword_text)
assert pword_text == confirming_pword_text
"""

"""
pword_text = getpass()
confirming_pword_text = getpass("Confirm: ")
# assert new-input (pword_text)
# and new-input(confirming_pword_text)
while pword_text != confirming_pword_text:
    # do something
    # assert new-input (pword_text)
    # and new-input(confirming_pword_text)
assert pword_text == confirming_pword_text
"""


"""
pword_text = getpass()
confirming_pword_text = getpass("Confirm: ")
# assert new-input (pword_text)
# and new-input(confirming_pword_text)
while pword_text != confirming_pword_text:
    pword_text = getpass()
    confirming_pword_text = getpass("Confirm: ")
    # assert new-input (pword_text)
    # and new-input(confirming_pword_text)
assert pword_text == confirming_pword_text
"""

"""
pword_text = getpass()
confirming_pword_text = getpass("Confirm: ")
while pword_text != confirming_pword_text:
    pword_text = getpass()
    confirming_pword_text = getpass("Confirm: ")
assert pword_text == confirming_pword_text
"""
