from Arithmetic import Arithmetic
from Huffman import Huffman 

freq_dict = dict()
print('Hello! How are you today?\n---------------------------------')

while(True):
    al = input('What algorithm you wanna try?\nH -> Huffman\nAH -> Adaptive Huffman\nA -> Arithmetic\nE -> Exit\n')
    match al:
        case 'H': # Huffman coding
            freq = input('Enter your frequency table:\n').split(' ') 
            for e in freq: 
                e = e.split(':') 
                freq_dict[e[0]] = int(e[1])
            p = Huffman(freq_dict)
            print('Here\'s your Huffman codewords:')
            p.print_codewords()
            while True:
                msg = input('Enter your message:\n')
                print(f"The encoded message: {p.huffman_encode(msg)}") 
                choice = input('Wanna encode another message?') 
                if choice in ('No', 'no', 'n', 'N'): break
        case 'AH': # Adaptive Huffman coding
            pass
        case 'A': # Arithmetic coding
            freq = input('Enter your probability table:\n').split(' ')
            for e in freq: 
                e = e.split(':') 
                freq_dict[e[0]] = float(e[1])
            p = Arithmetic(freq_dict)
            while True:
                msg = input('Enter your message:\n')
                en_msg = p.arithmetic_encode(msg)
                de_msg = p.arithmetic_decode(en_msg, len(msg))
                print(f"The encoded message: {en_msg}") 
                print(f"The decoded message: {de_msg}")
                choice = input('Wanna encode another message?') 
                if choice in ('No', 'no', 'n', 'N'): break
        case 'E': # Exit
            print('Bye!---------------------------------')
            break
        case other:
            print('No match found! try again')
    
    print('---------------------------------')   
    freq_dict.clear()   
        