# Importing the important libraries
from io import StringIO

# This is the class that implements the Huffman Compression Algorithm 
class LZW:
    
    def LZW_encode(self, msg):
        """ Encode any message using dictionary

        Args:
            msg (string): Message 

        Returns:
            string: Encoded message
        """
        if not msg: return
        w = ""
        i = 256
        dictionary = {chr(i): i for i in range(i)} # Initial dictionary for the alphabet(All ASCII codes)
        result = ''
        for c in msg:
            wc = w + c
            if wc in dictionary:                                    # If c in dictionary, continue reading
                w = wc
            else:
                result += str(dictionary[w]) + ' '                  # Add it to the result string
                dictionary[wc] = i                                  # Add it to dictionary
                i += 1
                w = c
        if w:
            result += str(dictionary[w]) 
        return result


    def LZW_decode(self, msg):
        """ Decode any message using reverse dictionary

        Args:
            msg (string): Message 

        Returns:
            string: Decoded message
        """
        if not msg: return
        i = 256
        dictionary = {i: chr(i) for i in range(i)} # Initial reverse dictionary for the alphabet
        msg = list(map(int, msg.split(' ')))                         # Convert msg to int list
        result = StringIO()                                          # Instead of string to decrease running time
        w = dictionary[msg.pop(0)]
        result.write(w)
        for k in msg:
            if k in dictionary:
                entry = dictionary[k]                               # Add it to the result string
            elif k == i:
                entry = w + w[0]                                    # If it's not in dictionary, it must be equals to dictionary length
            else:
                raise ValueError('Bad msg k: %s' % k)
            result.write(entry)
            dictionary[i] = w + entry[0]                           # Add it to dictionary
            i += 1
            w = entry
            
        return result.getvalue()


