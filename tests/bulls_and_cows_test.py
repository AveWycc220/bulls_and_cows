from modules.bulls_and_cows.bulls_and_cows import BullsAndCows, SIZE

# pylint: disable=W0212
# W0212 - Access to a protected member


def setup():
    """ Basic setup into module """


def test_init():
    """ Test for __init__ in BullsAndCows """
    A = BullsAndCows()
    assert A.status == "Game started"
    assert A._BullsAndCows__users_tries == 0


def test_create_sequence(): 
    """ Test for __create_sequence in BullsAndCows """ 
    A = BullsAndCows()
    assert len(set(A._BullsAndCows__computers_sequence)) == SIZE


def test_is_correct():
    """ Test for validation check """
    A = BullsAndCows()
    assert A._BullsAndCows__is_correct('1516') is False
    assert A._BullsAndCows__is_correct('15161616') is False
    assert A._BullsAndCows__is_correct(15) is False
    assert A._BullsAndCows__is_correct([15, 16]) is False
    assert A._BullsAndCows__is_correct('1623') is True


def test_check_value(): 
    A = BullsAndCows()
    A._BullsAndCows__computers_sequence = '1579'
    assert A.check_value('1579') == (4, 0)
    assert A.status == F"--You won. Game end.--\nCount of tries = {A._BullsAndCows__users_tries}\n\
Start new game, if you want to continue."
    assert A.check_value('2579') == (None, None)
    B = BullsAndCows()
    B._BullsAndCows__computers_sequence = '1579'
    assert B.check_value('2483') == (0, 0)
    assert B.check_value('7519') == (2, 2)


def teardown():
    """ Basic teardown into module """
