from modules.bulls_and_cows.bulls_and_cows import BullsAndCows

A = BullsAndCows()
print(A.status)
A._BullsAndCows__computers_sequence = '1579'
A.check_value('1579')
print(A.status)