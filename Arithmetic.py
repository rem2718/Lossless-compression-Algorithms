# Importing the important libraries
from decimal import Decimal
from decimal import getcontext
getcontext().prec = 2000 # Specifying the precision

# This is the class that implements the Arithmetic Compression Algorithm
class Arithmetic:
    
    def __init__(self, prob_table):
        """ Constructor to initialize the important properties
        Args:
            prob_table (Dict): the alphabet and their probabilities
        """
        self.prob_table = prob_table              
        self.c_prob_table = self.__get_c_prob_table()                         # Cumulative probability table 
 
    
    def __get_c_prob_table(self):
        """ Calculates the cumulative probability table
        Returns:
            c_prob_table (dict): the alphabet and their cumulative probabilities
        """
        c_prob_table = dict()
        cur = Decimal('0.0')
        for c in self.prob_table:
            c_prob_table[c] = cur
            cur += Decimal("%.10f" % self.prob_table[c])    
        return c_prob_table
   
    
    def arithmetic_encode(self, msg):
        """ This the function that encode the message into one decimal value
        Args:
            msg (string): The plain message
        Returns:
            ans (Decimal): The mean value of the message interval(encoded message)
        """
        if not msg: return
        min_lev = Decimal('0.0')
        max_lev = Decimal('1.0')
        r = max_lev - min_lev                                               # Whole number line between 0-1 
        for c in msg:                                                       # Looping over the entire message
            min_lev += self.c_prob_table[c] * r                             # Min value of the interval
            r *= Decimal("%.10f" % self.prob_table[c])                       # Current interval length 
            max_lev = min_lev + r                                           # Max value of the interval 
        ans = (min_lev + max_lev)/Decimal("%.1f" % 2.0)                     # Mean of the last interval
        return ans.normalize()                                              # Trimming the zeros


    def arithmetic_decode(self, msg, n):
        """ This the function that decode the decimal value into the plain message
        Args:
            msg (Decimal): Encoded decimal
            n (int): Length of the plain message
        Returns:
            ans (string): Decoded message
        """
        if not msg: return
        ans = ''
        min_lev = Decimal('0.0')
        max_lev = Decimal('1.0')
        r = max_lev - min_lev                                               # Whole number line between 0-1
        for i in range(n):                                                  # Looping till we get all the characters
            for c in self.prob_table:                                       # Looping on the number line till we find our interval
                cur_interval = Decimal("%.10f" % self.prob_table[c]) * r     # Try all the intervals     
                max_lev = min_lev + cur_interval 
                if msg < max_lev:                                          # If its within the interval:
                    r = cur_interval                                        # Expand the interval
                    ans += c                                                # Add the char
                    break  
                min_lev = max_lev                                           # Move to the next interval
        return ans


