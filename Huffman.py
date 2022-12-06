# Importing the important libraries
import heapq
 
# This is the class that implements the Huffman Compression Algorithm 
class Huffman: 
    
    class node:
        def __init__(self, freq, symbol, left=None, right=None):
            """ Constructor

            Args:
                freq (int): Frequency of the character
                symbol (char): Character we want to encode
                left (node, optional): _description_. Defaults to None.
                right (node, optional): _description_. Defaults to None.
            """
            self.freq = freq
            self.symbol = symbol
            self.left = left
            self.right = right
            self.huff = '' # Huffman value [0/1]
         
            
        def __lt__(self, nxt):
            """ Compare function
            Args:
                nxt (node): the next node

            Returns:
                boolean: true if freq is less than next node's freq
            """
            return self.freq < nxt.freq
  
        
    def __init__(self, freq_table):
        """ Constructor

        Args:
            freq_table (dict): Frequency dictionary 
        """
        self.freq_table = freq_table
        self.codeword_dict = dict()      # Codeword dictionary 
        self.__huffman_dict()            # To fill the codeword dictionary  
        
        
    def __construct_dict(self, node, val=''):
        """ Construct a dictionary from the huffman tree

        Args:
            node (node): Node from the tree that will be added
            val (str, optional): String to concatenate the huffman value
        """
        newVal = val + str(node.huff)
        if node.left:                                   
            self.__construct_dict(node.left, newVal)    # Recursive call for left leaves
        if node.right:
            self.__construct_dict(node.right, newVal)   # Recursive call for right leaves
        if not node.left and not node.right:            # If node is a leaf
            self.codeword_dict[node.symbol] =  newVal   # Add its codeword
    
        
    def __huffman_dict(self):
        """ The main function for huffman algorithm

        Returns:
            dict: codeword_dictionary
        """
        nodes = []                                                                                  # Heap
        for symbol in self.freq_table:
            heapq.heappush(nodes, self.node(self.freq_table[symbol], symbol))                       # Add all nodes to the heap
        
        while len(nodes) > 1:                                                                       # Construct the huffman tree
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            left.huff = 0
            right.huff = 1
            newNode = self.node(left.freq + right.freq, left.symbol + right.symbol, left, right)    # Construct internal node
            heapq.heappush(nodes, newNode)                                                          
        self.__construct_dict(nodes[0])
  
            
    def print_codewords(self):
        """ Print the codeword_dictionary
        """
        for symbol in self.codeword_dict:
            print(f"{symbol}: {self.codeword_dict[symbol]}")  

                           
    def huffman_encode(self, msg):
        """ Encode any message using codeword_dictionary

        Args:
            msg (string): Message 

        Returns:
            string: Encoded message
        """
        if not msg: return
        encoded_msg = ''
        for c in msg:
            encoded_msg += self.codeword_dict[c]+ ' '
        return encoded_msg
    
    
    def huffman_decode(self, msg):
        """ decode any message using rev_codeword_dictionary

        Args:
            msg (string): Message 

        Returns:
            string: Decoded message
        """
        if not msg: return
        msg = msg.split(' ')[:-1]
        decoded_msg = ''
        rev_dict = {v: k for k, v in self.codeword_dict.items()}
        for c in msg:
           decoded_msg += rev_dict[c]
        return decoded_msg
           
            
                       
         
