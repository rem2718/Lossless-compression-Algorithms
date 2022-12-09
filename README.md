# LOSSLESS COMPRESSION ALGORITHMS

A program that implements 3 types of lossless compression algorithms: LZW, Huffman, Arithmetic coding.

## HOW TO RUN IT:

1.Download _Lossless-compression-Algorithms.zip_ file

2.Install all the requirements

```
 pip install -r requirements.txt
```

3.Open _Main.py_ file and run it, you can see a results of 3 encoded messages(stored in _input.txt_) and their running time.

4.Run _Manual.py_ if you wanna specify the alphabet and the message manually(it reads _input2.txt_).

5.If you wanna see some analysis of the 3 algorithms run _Running_time.py_ file

## CLASSES DESCRIPTION:

### LZW CLASS:

its constructor takes nothing.

| Method         | Params        | Return   | Description                                   |
| -------------- | ------------- | -------- | --------------------------------------------- |
| **LZW_encode** | _msg_(string) | (string) | The function that encode the original message |
| **LZW_decode** | _msg_(string) | (string) | The function that decode the encoded message  |

### HUFFMAN CLASS:

its constructor takes one parameter **freq_table** which is a dictionary contains the alphabet of the message and their frequencies.

| Method                 | Params                                | Return   | Description                                                                   |
| ---------------------- | ------------------------------------- | -------- | ----------------------------------------------------------------------------- |
| **\_\_construct_dict** | _node_(Node): root, _val_(string): '' | none     | Recursive function that construct the _codeword_dict_ out of the huffman tree |
| **\_\_huffman_dict**   | none                                  | none     | The function that construct the huffman tree                                  |
| **print_codewords**    | none                                  | none     | The function that print the _codeword_dict_                                   |
| **huffman_encode**     | _msg_(string)                         | (string) | The function that encode the original message                                 |
| **huffman_decode**     | _msg_(string)                         | (string) | The function that decode the encoded message                                  |

### ARITHMETIC CLASS:

its constructor takes one parameter **prob_table** which is a dictionary contains the alphabet of the message and their probabilities.

| Method                   | Params                                       | Return               | Description                                                    |
| ------------------------ | -------------------------------------------- | -------------------- | -------------------------------------------------------------- |
| **\_\_get_c_prob_table** | none                                         | _c_prob_table_(dict) | The function that construct _c_prob_table_ out of _prob_table_ |
| **arithmetic_encode**    | _msg_(string)                                | (string)             | The function that encode the original message                  |
| **arithmetic_decode**    | _msg_(string), _n_(int): original msg length | (string)             | The function that decode the encoded message                   |

## NOTES:

- Be careful when you specify the frequency table and message in _input2.txt_, otherwise you might end up with an encoded message longer than the original one! for that reason we used a random generator, check the _Main.py_ file(it safer).
- _input.txt_ is generated randomly from the file _Main.py_, it contains 3 strings each message has different alphabet and length.
- The implementation of Arithmetic encoding is very simple here and not efficient. It depends on the programming language, in python I used Decimal library to specify the precision of the decimal number, however there more efficient ways using different programming languages.
- Arithmetic is very slow, so try a message length not longer than 1000 characters.
- For more information about the algorithms, check _Report.pdf_.

## THANK YOU!

Hope you enjoy this simple implementation :)

If you face any problems please contact me

Made by:

Reem Hejazi 219410002

Raneem Balharith 219410305

Sara Al Shagawi 219410319

under _@rem2718_ account

For any suggestions/comments/questions email me at: rem.e2.718@gmail.com
