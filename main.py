from Arithmetic import Arithmetic
from Huffman import Huffman
from LZW import LZW
import time
import random 

# Alphabets: 
alphabet0 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', 
             '%', '&', '(', ')', '*', '+', ',', '-', '.', ':', ';', '<', '=', '>', 
             '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

alphabet1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
             ]
alphabet2 = alphabet0 + alphabet1
alphabets = [alphabet0, alphabet1, alphabet2]
# Message lengths
length = [500, 1000, 5000]

# Lists and dictionaries for frequency and probability tables
f_lists = []
p_lists = []
f_tables = []
p_tables = []

for alphabet in alphabets:
    temp_list = random.sample(range(1, 101), len(alphabet))
    f_lists.append(temp_list) 
    p_lists.append([i/sum(temp_list) for i in temp_list])

    f_tables.append(dict(zip(alphabet, temp_list)))
    p_tables.append(dict(zip(alphabet, p_lists[len(p_lists)-1])))

# Generating 3 random strings based on the alphabets and frequencies above
print('Generating 3 random strings to input.txt')
file = open('input.txt', 'w')
for i in range(3):
    chars = random.choices(alphabets[i], weights = f_lists[i], k = length[i])
    msg = ''.join(chars)
    file.write(msg + '\n')
file.close()
# Reading the file again
print('Reading input.txt')   
file = open('input.txt', 'r')

# Apply all algorithms for the 3 messages
j = 0
for msg in file:
    print('----------------------------------')
    msg = msg[:-1]
    start = time.time()
    p1 = LZW(alphabets[j]) 
    encoded = p1.LZW_encode(msg)
    end = time.time()
    en_time = round(end - start, 10)
    decoded = p1.LZW_decode(encoded)
    print(f"LZW encoding msg {j+1} in: {en_time} secs")
    print('correct!') if msg == decoded else print('wrong!')

    start = time.time()
    p2 = Huffman(f_tables[j])
    encoded = p2.huffman_encode(msg)
    end = time.time()
    en_time = round(end - start, 10)
    decoded = p2.huffman_decode(encoded)
    print(f"Huffman encoding msg {j+1} in: {en_time} secs")
    print('correct!') if msg == decoded else print('wrong!')
    
    start = time.time()
    p3 = Arithmetic(p_tables[j])
    encoded = p3.arithmetic_encode(msg)
    end = time.time()
    en_time = round(end - start, 10)
    decoded = p3.arithmetic_decode(encoded, len(msg))
    print(f"Arithmetic encoding msg {j+1} in: {en_time} secs")
    print('correct!') if msg == decoded else print('wrong!')
    j += 1
