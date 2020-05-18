""" Module of class : BullsAndCows """
import random

class BullsAndCows(): 
    """ Class for playing in Bulls and Cows """ 
    __players_sequence = None
    __computers_sequence = None
    status = "Game is not initialized"
    def __init__(self, input_sequence):
        """ Init game-session """ 
        if input_sequence.isdigit() and len(input_sequence) == 4:
            self.__players_sequence = input_sequence
            self.__computers_sequence = 0  #self.__create_sequence()
            self.status = 'Game started'
        else: 
            self.status = 'Wrong input. Value must contain 4 digits'
    