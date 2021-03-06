import pickle
from termcolor import colored
# original code taken from:
# https://github.com/YCAyca/Data-Structures-and-Algorithms-with-Python/tree/main/Huffman_Encoding

def print_green(string):
    print(colored(string, 'green'))


# A Huffman Tree Node
class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # symbol 
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

# A helper function to print the codes of symbols by traveling Huffman Tree
codes = dict()

def Calculate_Codes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.code)

    if(node.left):
        Calculate_Codes(node.left, newVal)
    if(node.right):
        Calculate_Codes(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal
         
    return codes        

# A helper function to calculate the probabilities of symbols in given data
def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else: 
            symbols[element] += 1     
    return symbols

# A helper function to obtain the encoded output
def Output_Encoded(data, coding):
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])
        
    string = ''.join([str(item) for item in encoding_output])    
    return string
        
# A helper function to calculate the space difference between compressed and non compressed data
def Total_Gain(data, coding):
    before_compression = len(data) * 8 # total bit space to stor the data before compression
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol]) #calculate how many bit is required for that symbol in total
    print("Space usage before compression (in bits):", before_compression)    
    print("Space usage after compression (in bits):",  after_compression) 
    print(colored("COMPRESSION RATIO: ", 'red'), round(after_compression/before_compression, 2), "%")         

def Huffman_Encoding(data):
    symbol_with_probs = Calculate_Probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("symbols: ", symbols)
    print("probabilities: ", probabilities)
    
    nodes = []
    
    # converting symbols and probabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.prob)
        # for node in nodes:  
        #      print(node.symbol, node.prob)
    
        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]
    
        left.code = 0
        right.code = 1
    
        # combine the 2 smallest nodes to create new node
        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
    
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
            
    huffman_encoding = Calculate_Codes(nodes[0])
    # print("symbols with codes", huffman_encoding)
    for key in huffman_encoding:
        print(f"{key} : {huffman_encoding[key]}")
    Total_Gain(data, huffman_encoding)
    encoded_output = Output_Encoded(data,huffman_encoding)
    return encoded_output, nodes[0]  
    
 
def Huffman_Decoding(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right   
        elif x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head
        
    string = ''.join([str(item) for item in decoded_output])
    return string        

print_green("Provide name of the file you want to load (without .txt extension)")
file_name = input()
with open(file_name + ".txt", 'r') as file:
    data = file.read()

print(colored("Loaded text: ", 'green'), data)

print(colored("Do you want to encode or decode the file? [encode/decode]", 'green'))
choice = input()

if choice == "encode":
    encoding, tree = Huffman_Encoding(data)
    dumped_file_name = file_name + "_tree"
    with open(dumped_file_name, "wb") as dumped_file:
        pickle.dump(tree, dumped_file)
        # print(f"key to decode the file has been dumped to {dumped_file_name}")
        print(colored("Key to decode the file has been dumpted to:", 'green'), dumped_file_name)
    print(colored("Encoded:", 'green'), encoding)
    encoded_file_name = file_name + "_encoded.txt"
    with open(encoded_file_name, "w") as encoded_file:
        encoded_file.write(encoding)
        print(colored("Encoding saved to:", 'green'), encoded_file_name)

if choice == "decode":
    print(colored('Provide name of the file containing key you want to use', 'green'))
    file_with_key_name = input()
    with open(file_with_key_name, "rb") as file_with_key:
        tree = pickle.load(file_with_key)
    print(colored("Decoded:", 'green'), Huffman_Decoding(data, tree))