# https://favtutor.com/blogs/red-black-tree-python


# Define Node
class Node():
    def __init__(self,val):
        self.val = val                                   # Value of Node
        self.parent = None                               # Parent of Node
        self.left = None                                 # Left Child of Node
        self.right = None                                # Right Child of Node
        self.color = 1                                   # Red Node as new node is always inserted as Red Node

# Define R-B Tree
class RBTree():
    def __init__(self):
        self.NULL = Node ( 0 )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL


    # Insert New Node
    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Set root colour as Red

        print("Ustawianie oryginalnego koloru na czerwony.")

        y = None
        x = self.root

        print("Poszukiwanie miejsca na drzewie dla elementu")

        while x != self.NULL :                           # Find position for new node
            y = x
            if node.val < x.val :
                x = x.left
                print("Wartosc elementu wstawianego mniejsza niz wartosc elementu sprawdzanego.")
                print("Idziemy w lewo drzewa.")
            else :
                x = x.right
                print("Wartosc elementu wstawianego wieksza lub rowna wartosci elementu sprawdzanego.")
                print("Idziemy w prawo drzewa.")

        node.parent = y                                  # Set parent of Node as y
        if y == None :                                   # If parent i.e, is none then it is root node
            self.root = node
        elif node.val < y.val :                          # Check if it is right Node or Left Node by checking the value
            y.left = node
        else :
            y.right = node

        if node.parent == None :                         # Root node is always Black
            node.color = 0
            print("Element jest korzeniem, wiec zmieniamy kolor na czarny i konczymy wstawianie.")
            return

        if node.parent.parent == None :                  # If parent of node is Root Node
            print("Rodzic jest korzeniem wiec konczymy wstawianie.")
            return

        self.fixInsert ( node )                          # Else call for Fix Up


    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node


    # Code for left rotate
    def LR ( self , x ) :
        y = x.right                                      # Y = Right child of x
        x.right = y.left                                 # Change right child of x to left child of y
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent                              # Change parent of y as parent of x
        if x.parent == None :                            # If parent of x == None ie. root node
            self.root = y                                # Set y as root
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y


    # Code for right rotate
    def RR ( self , x ) :
        y = x.left                                       # Y = Left child of x
        x.left = y.right                                 # Change left child of x to right child of y
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent                              # Change parent of y as parent of x
        if x.parent == None :                            # If x is root node
            self.root = y                                # Set y as root
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y


    # Fix Up Insertion
    def fixInsert(self, k):
        print("Wykonujemy algorytm naprawiajacy tak dlugo jak rodzic jest czerwony.")
        while k.parent.color == 1:                        # While parent is red
            if k.parent == k.parent.parent.right:         # if parent is right child of its parent
                print("Jesli rodzic jest prawym dzieckiem swojego rodzica,")
                u = k.parent.parent.left                  # Left child of grandparent
                if u.color == 1:                          # if color of left child of grandparent i.e, uncle node is red
                    print("i wujek jest czerwony, zamieniamy kolor wujka i rodzica na czarny,")
                    print("zamieniamy kolor dziadka na czerwony,")
                    print("i powtarzamy algorytm dla dziadka.")
                    u.color = 0                           # Set both children of grandparent node as black
                    k.parent.color = 0
                    k.parent.parent.color = 1             # Set grandparent node as Red
                    k = k.parent.parent                   # Repeat the algo with Parent node to check conflicts
                else:
                    print("i wujek jest czarny,")
                    if k == k.parent.left:                # If k is left child of it's parent
                        print("a sprawdzany element jest lewym dzieckiem swojego rodzica,")
                        print("zamieniamy sprawdzany element na rodzica, wywolujemy na nim prawa rotacje")
                        k = k.parent
                        self.RR(k)                        # Call for right rotation
                    print("zamieniamy kolor rodzica na czarny i dziadka na czerwony,")
                    print("po czym wykonujemy lewa rotacje na dziadku.")
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:                                         # if parent is left child of its parent
                print("Jesli rodzic jest lewym dzieckiem swojego rodzica,")
                u = k.parent.parent.right                 # Right child of grandparent
                if u.color == 1:                          # if color of right child of grandparent i.e, uncle node is red
                    print("i wujek jest czerwony, zamieniamy kolor wujka i rodzica na czarny,")
                    print("zamieniamy kolor dziadka na czerwony,")
                    print("i powtarzamy algorytm dla dziadka.")
                    u.color = 0                           # Set color of childs as black
                    k.parent.color = 0
                    k.parent.parent.color = 1             # set color of grandparent as Red
                    k = k.parent.parent                   # Repeat algo on grandparent to remove conflicts
                else:
                    print("i wujek jest czarny,")
                    if k == k.parent.right:               # if k is right child of its parent
                        print("a sprawdzany element jest prawym dzieckiem swojego rodzica,")
                        print("zamieniamy sprawdzany element na rodzica, wywolujemy na nim lewa rotacje")
                        k = k.parent
                        self.LR(k)                        # Call left rotate on parent of k
                    print("zamieniamy kolor rodzica na czarny i dziadka na czerwony,")
                    print("po czym wykonujemy lewa rotacje na dziadku.")
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)              # Call right rotate on grandparent
            if k == self.root:                            # If k reaches root then break
                print("Jesli sprawdzajac elementy dojdziemy do korzenia, wychodzimy z algorytmu.")
                break
        print("Ustawiamy kolor korzenia na czarny i konczymy.")
        self.root.color = 0                               # Set color of root as black


    # Function to fix issues after deletion
    def fixDelete ( self , x ) :
        print("Algorytm naprawy powtarzamy dopóki nie dojdziemy do korzenia i korzen jest czarny.")
        while x != self.root and x.color == 0 :           # Repeat until x reaches nodes and color of x is black
            if x == x.parent.left :                       # If x is left child of its parent
                print("Jesli sprawdzany element jest lewym dzieckiem swojego rodzica")
                s = x.parent.right                        # Sibling of x
                if s.color == 1 :                         # if sibling is red
                    print("i ma czerwone rodzenstwo")
                    print("to zmieniamy kolor rodzenstwa na czarny a kolor rodzica na czerwony")
                    print("I wywolujemy lewa rotacje na rodzicu.")
                    s.color = 0                           # Set its color to black
                    x.parent.color = 1                    # Make its parent red
                    self.LR ( x.parent )                  # Call for left rotate on parent of x
                    s = x.parent.right
                # If both the child are black
                if s.left.color == 0 and s.right.color == 0 :
                    print("Jesli rodzenstwo ma czarne dzieci,")
                    print("to ustawiamy kolor rodzenstwa na czerwone")
                    print("i sprawdzamy wedlug algorytmu rodzica")
                    s.color = 1                           # Set color of s as red
                    x = x.parent
                else :
                    print("Jesli rodzenstwo nie ma obu dzieci czarnych")
                    if s.right.color == 0 :               # If right child of s is black
                        print("a prawe dziecko ma czarne, to ustawiamy kolor lewego dziecka na czarne")
                        print("a kolor rodzenstwa na czerwone, i wywolujemy prawa rotacje na rodzenstwie")
                        s.left.color = 0                  # set left child of s as black
                        s.color = 1                       # set color of s as red
                        self.RR ( s )                     # call right rotation on x
                        s = x.parent.right
                    print("ustawiamy kolor rodzenstwa na ten sam co kolor rodzica elementu sprawdzanego.")
                    print("Nastepnie kolor rodzica i prawego dziecka rodzenstwa ustawiamy na czarny")
                    print("po czym wywolujemy lewa rotacje na rodzicu")
                    print("i przeskakujemy z algorytmem do korzenia drzewa.")
                    s.color = x.parent.color
                    x.parent.color = 0                    # Set parent of x as black
                    s.right.color = 0
                    self.LR ( x.parent )                  # call left rotation on parent of x
                    x = self.root
            else :                                        # If x is right child of its parent
                print("Jesli sprawdzany element jest prawym dzieckiem swojego rodzica")
                s = x.parent.left                         # Sibling of x
                if s.color == 1 :                         # if sibling is red
                    print("a rodzenstwo sprawdzanego elementu jest czerwone,")
                    print("ustawiamy kolor rodzenstwa na czarny, a rodzica na czerwony,")
                    print("po czym wykonujemy prawa rotacje na rodzicu.")
                    s.color = 0                           # Set its color to black
                    x.parent.color = 1                    # Make its parent red
                    self.RR ( x.parent )                  # Call for right rotate on parent of x
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0 :
                    print("jesli dzieci rodzenstwa sprawdzanego elementu sa czarne,")
                    print("ustawiamy kolor rodzenstwa na czerwony i sprawdzanym elementem staje sie jego rodzic")
                    s.color = 1
                    x = x.parent
                else :
                    print("jesli oba dzieci rodzenstwa sprawdzanego elementu nie sa czarne")
                    if s.left.color == 0 :                # If left child of s is black
                        print("ale lewe dziecko jest, to ustawiamy kolor prawego na czarne")
                        print("kolor rodzenstwa na czerwony, i wywolujemy lewa rotacje na rodzenstwie")
                        s.right.color = 0                 # set right child of s as black
                        s.color = 1
                        self.LR ( s )                     # call left rotation on x
                        s = x.parent.left
                    print("ustawiamy kolor rodzenstwa na ten sam co kolor rodzica")
                    print("po czym ustawiamy kolor rodzica i lewego dziecka rodzenstwa na czarny")
                    print("i wywolujemy prawa rotacje na rodzicu.")
                    print("na koniec przeskakujemy z algorytmem do korzenia drzewa.")
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.RR ( x.parent )
                    x = self.root
        print("Zamieniamy kolor sprawdzanego elementu na czarny.")
        x.color = 0


    # Function to transplant nodes
    def __rb_transplant ( self , u , v ) :
        if u.parent == None :
            self.root = v
        elif u == u.parent.left :
            u.parent.left = v
        else :
            u.parent.right = v
        v.parent = u.parent


    # Function to handle deletion
    def delete_node_helper ( self , node , key ) :
        z = self.NULL
        print("Szukaj elementu do usuniecia.")
        while node != self.NULL :                          # Search for the node having that value/ key and store it in 'z'
            if node.val == key :
                z = node

            if node.val <= key :
                node = node.right
            else :
                node = node.left

        if z == self.NULL :                                # If Kwy is not present then deletion not possible so return
            print("Wartosci nie ma w drzewie.")
            print("Konczymy algorytm usuwania.")
            return

        y = z
        y_original_color = y.color                          # Store the color of z- node
        print("Zapisujemy kolor elementu ktory usuwamy.")
        if z.left == self.NULL :                            # If left child of z is NULL
            print("Jesli lewe dziecko usuwanego elementu jest null,")
            print("wstawiamy prawe dziecko na miejsce elementu usuwanego.")
            x = z.right                                     # Assign right child of z to x
            self.__rb_transplant ( z , z.right )            # Transplant Node to be deleted with x
        elif (z.right == self.NULL) :                       # If right child of z is NULL
            print("Jesli lewe dziecko usuwanego elementu nie jest null,")
            print("a prawe dziecko usuwanego elementu jest null")
            print("wstawiamy lewe dziecko na miejsce elementu usuwanego.")
            x = z.left                                      # Assign left child of z to x
            self.__rb_transplant ( z , z.left )             # Transplant Node to be deleted with x
        else :                                              # If z has both the child nodes
            print("Jesli usuwany element ma oboje dzieci,")
            print("znajdujemy najmniejszy element prawego poddrzewa usuwanego elementu")
            print("i nadpisujemy kolor elementu usuwanego, kolorem znalezionego elementu.")
            y = self.minimum ( z.right )                    # Find minimum of the right sub tree
            y_original_color = y.color                      # Store color of y
            x = y.right
            if y.parent == z :                              # If y is child of z
                print("Jesli znaleziony element to dziecko elementu do usuniecia,")
                print("Ustawiamy znaleziony element jako rodzic prawego dziecka najmniejszego")
                print("elementu prawego poddrzewa usuwanego elementu")
                x.parent = y                                # Set parent of x as y
            else :
                print("Jesli znaleziony element nie jest dzieckiem elementu do usuniecia,")
                print("transplantujemy znaleziony element z jego prawym dzieckiem.")
                self.__rb_transplant ( y , y.right )
                y.right = z.right
                y.right.parent = y

            print("Nastepnie transplantujemy element do usuniecia ze znalezionym elementem")
            self.__rb_transplant ( z , y )
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0 :                          # If color is black then fixing is needed
            print("Jesli zapisany kolor to czarny, to wywolujemy algorytm naprawy kolorow przy usuwaniu")
            print("na wspomnianym wczesniej najmniejszym elemencie prawego poddrzewa.")
            self.fixDelete ( x )


    # Deletion of node
    def delete_node ( self , val ) :
        self.delete_node_helper ( self.root , val )         # Call for deletion


    # Function to print
    def __printCall ( self , node , indent , last ) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.val ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )

    # Function to call print
    def print_tree ( self ) :
        self.__printCall ( self.root , "" , True ) 

if __name__ == "__main__":
    temp = 10
    my_tree = RBTree()
    while temp != 0:
        temp = int(input("1 - insert\n2 - delete\n3 - print\n0 - exit\n"))
        print(f"Your choice: {temp}")
        if temp == 1:
            my_tree.insertNode(int(input("1 = insert\n")))
        if temp == 2:
            my_tree.delete_node(int(input("2 = delete\n")))
        if temp == 3:
            my_tree.print_tree()
        
