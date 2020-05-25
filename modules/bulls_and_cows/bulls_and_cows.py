""" Module of class : BullsAndCows """
import random

SIZE = 4


class BullsAndCows():
    """ Class for playing in Bulls and Cows """
    __computers_sequence = None
    __users_tries = None
    status = "Game is not initialized"

    def __init__(self):
        """ Init game-session """
        self.__create_sequence()
        self.__users_tries = 0
        self.status = 'Game started'

    @property
    def sequence(self):
        return self.__computers_sequence

    def __create_sequence(self):
        """ Generate __computer_sequence """
        self.__computers_sequence = str()
        while len(self.__computers_sequence) != SIZE:
            rand = random.randint(0, 9)
            if str(rand) not in self.__computers_sequence:
                self.__computers_sequence += str(rand)

    def check_value(self, value):
        """ Check the value and output the number of cows and bulls. Value must be type == str """
        if self.__is_correct(value) and self.__computers_sequence is not None:
            self.__users_tries += 1
            bulls = 0
            cows = 0
            for i in range(0, SIZE):
                if value[i] == self.__computers_sequence[i]:
                    bulls += 1
            if bulls == SIZE:
                self.status = F"--You won. Game end.--\nCount of tries = {self.__users_tries}\n\
Start new game, if you want to continue."
                self.__computers_sequence = None
                return bulls, cows
            else:
                for i in range(0, SIZE):
                    if (value[i] in self.__computers_sequence) and (value[i] != self.__computers_sequence[i]):
                        cows += 1
                self.status = F"Bulls = {bulls} | Cows = {cows} | Nubmer of Tries = {self.__users_tries}"
                return bulls, cows
        else:
            return None, None

    @staticmethod
    def check_value_static(value, sequence):
        """ Static method. Check the value and output the number of cows and bulls. """
        bulls = 0
        cows = 0
        for i in range(0, SIZE):
            if value[i] == sequence[i]:
                bulls += 1
        if bulls == SIZE:
            return bulls, cows
        else:
            for i in range(0, SIZE):
                if (value[i] in sequence) and (value[i] != sequence[i]):
                    cows += 1
            return bulls, cows

    def __is_correct(self, input_sequence):
        """ Validation check. """
        if isinstance(input_sequence, str) and input_sequence.isdigit() \
                and len(input_sequence) == SIZE and (len(set(input_sequence)) == SIZE):
            return True
        else:
            if self.__computers_sequence is None:
                self.status = F'--You won. Game end.--\nCount of tries = {self.__users_tries}\n\
Start new game, if you want to continue.'
            else:
                self.status = F'Wrong input. Value must contain {SIZE} unique digits'
            return False
