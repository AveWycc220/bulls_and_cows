""" Module of class : BullsAndCows """
import random


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

    def __create_sequence(self):
        """ Generate __computer_sequence """ 
        self.__computers_sequence = str()
        while len(self.__computers_sequence) != 4:
            rand = random.randint(0, 9)
            if str(rand) not in self.__computers_sequence:
                self.__computers_sequence  += str(rand)

    def check_value(self, value):
        """ Check the value and output the number of cows and bulls """
        if self.__is_correct(value):    
            self.__users_tries += 1
            bulls = 0 
            cows = 0
            for i in range(0, 4):
                if value[i] == self.__computers_sequence[i]:
                    bulls += 1
            if bulls == 4:
                self.status = F"--You won. Game end.--\nCount of tries = {self.__users_tries}\n\
Start new game, if you want to continue."
                return bulls, cows
            else:
                for i in range(0, 4):
                    if (value[i] in self.__computers_sequence) and (value[i] != self.__computers_sequence[i]):
                        cows += 1
                self.status = F"Bulls = {bulls} | Cows = {cows}"
                return bulls, cows

    def __is_correct(self, input_sequence):
        """ Validation check """
        if input_sequence.isdigit() and len(input_sequence) == 4 and (len(set(input_sequence)) == 4):
            return True
        else:
            self.status = 'Wrong input. Value must contain 4 unique digits'
            return False