import time
import random
import matplotlib.pyplot as plt
from matplotlib import style
from Arithmetic import Arithmetic
from Huffman import Huffman
from LZW import LZW 

style.use('dark_background')

c1 = 0
c2 = 0
c3 = 0        
        
output1 = []
output2 = []
output3 = []  
n = []      
           
alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', 
             '%', '&', '(', ')', '*', '+', ',', '-', '.', ':', ';', '<', '=', '>', 
             '?', '@', '[', ']', '^', '_', '{', '|', '}', '~',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
             ]

input = range(3, len(alphabet), 3)
for t in  input:
    sub_alphabet = alphabet[:t]
    f_list = random.sample(range(1, 101), len(sub_alphabet)) 
    p_list = [i/sum(f_list) for i in f_list] 

    f_table = dict(zip(sub_alphabet, f_list))
    p_table = dict(zip(sub_alphabet, p_list))
    
    chars = random.choices(sub_alphabet, weights = f_list, k = 50 * t + 100)
    msg = ''.join(chars)
    n.append(50 * t + 100)

    start = time.time()
    p1 = LZW() 
    encoded = p1.LZW_encode(msg)
    end = time.time()
    total = round(end - start, 20)
    output1.append(total)
    decoded = p1.LZW_decode(encoded)
    if msg == decoded: c1 +=1 

    start = time.time()
    p2 = Huffman(f_table)
    encoded = p2.huffman_encode(msg)
    end = time.time()
    total = round(end - start, 20)
    output2.append(total)
    decoded = p2.huffman_decode(encoded)
    if msg == decoded: c2 +=1
    
    start = time.time()
    p3 = Arithmetic(p_table)
    encoded = p3.arithmetic_encode(msg)
    end = time.time()
    total = round(end - start, 20)
    output3.append(total)
    decoded = p3.arithmetic_decode(encoded, len(msg))
    if msg == decoded: c3 +=1
    
    
print(f"LZW accuracy: {(c1/len(input))*100}%")
print(f"Huffman accuracy: {(c2/len(input))*100}%")
print(f"Arithmetic accuracy: {(c3/len(input))*100}%")

plt.plot(n, output1)
plt.plot(n, output2)
plt.plot(n, output3)
plt.legend(['LZW', 'Huffman', 'Arithmetic'])
plt.title('Lossless Compression Algorithms\' Runtime')
plt.xlabel('Input Length')
plt.ylabel('Runtime')
plt.show()


