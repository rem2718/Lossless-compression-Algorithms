
from Arithmetic import Arithmetic
from Huffman import Huffman
from LZW import LZW

print('Reading input.txt')   
file = open('input2.txt', 'r')
string = file.readline().split(' ')

freq_table = dict()
for elem in string:
    elem = elem.split(':')
    freq_table[elem[0]] = int(elem[1])
    
p_sum = sum(freq_table.values())
prob_table = {k : v/p_sum for k, v in freq_table.items()}
    
msg = file.readline()
print(f"The message: {msg}")
p1 = LZW() 
encoded = p1.LZW_encode(msg)
decoded = p1.LZW_decode(encoded)
print(f"The LZW encoded message: {encoded}")
print(f"The LZW decoded message: {decoded}")
p2 = Huffman(freq_table)
encoded = p2.huffman_encode(msg)
decoded = p2.huffman_decode(encoded)
print(f"The Huffman encoded message: {encoded}")
print(f"The Huffman decoded message: {decoded}")
p3 = Arithmetic(prob_table)
encoded = p3.arithmetic_encode(msg)
decoded = p3.arithmetic_decode(encoded, len(msg))
print(f"The Arithmetic encoded message: {encoded}")
print(f"The Arithmetic decoded message: {decoded}")
