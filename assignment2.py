import csv


class CDLLNode:
    # csv_tweet = csv.reader(csv_file, delimiter='|')
    def __init__(self, time="", tweet="", next_node=None, prev_node=None):
        csv_tweet = csv.reader(csv_file, delimiter='|')
        self.time: str = time
        self.tweet: str = tweet
        self.next_node: CDLLNode = next_node
        self.prev_node: CDLLNode = prev_node
 
 
    def get_tweet (self):
    		return self.tweet
  
    def get_next (self):
    		return self.next_node

 
class CDLL:
    def __init__(self, r = None):
        self.head: CDLLNode = None
        self.current: CDLLNode = None
        self.numnodes: int = 0
        self.root = r
    
    def get_size (self):
    		return self.numnodes
        
    def get_node(self, index):
        current = self.head
        for i in range(index):
            current = current.next
            if current == self.head:
                return None
        return current
    
    # makes an insertion based on the 'current' node
    def insert(self,time: str, tweet: str):
        
        
        if not isinstance(time, CDLLNode):
            time = CDLLNode(time)

        if self.head is None:
            self.head = time
        else:
            self.tail.next = time

        self.tail = time
        def add_list_tweet(self, tweet):
        
            if not isinstance(tweet, CDLLNode):
                tweet = CDLLNode(tweet)

            if self.head is None:
                self.head = tweet
            else:
                self.tail.next = tweet

            self.tail = tweet
                
            return
            
    # moves 'current' pointer to the next node (circularly)
    def go_next (self, next_node):
        self.next_node = next_node
        self.current = next_node
    
    # moves 'current' pointer to the previous node (circularly)
    def go_prev(self, prev_node):
        self.prev_node = prev_node
        self.current = prev_node
   
    # moves 'current' pointer to the head (the first node)    
    def go_first(self, r):
        self.root = r
        self.current = r
    # moves 'current' pointer to the last node
    def go_last(self): 
        pass
     # moves 'current' pointer n elements ahead (circularly)
    def skip(self,n:int):    
          pass
     # Search tweet 
    def search_tweet (self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == self.root:
                return false
            else:
                this_node = this_node.get_next()
           
    def print_current(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.time, end = ' ')
            current = current.next
            if current == self.head:
                break
            
            #Print list
            print ("Print List..........")
            if self.root is None:
                return
            this_node = self.root
            print (this_node.to_string())
            while this_node.get_next() != self.root:
                this_node = this_node.get_next()
                print (this_node.to_string())
 
a_cdllist = CDLL()
 
# print('Menu')
# print(' <time>  <index>')
# print('insert <time> before <index>')
# print('insert <time> at beg')
# print('insert <time> at end')
# print('remove <index>') 
# print('quit')
 
while True:
    a_cdllist.print_current()
    print()
    do = input().split()
 
    operation = do[0].strip().lower()
 
    if operation == 'n':
        time = int(do[1])
        position = do[3].strip().lower()
        new_node = CDLLNode(time)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            if position == 'beg':
                a_cdllist.insert_at_beg(new_node)
            elif position == 'end':
                a_cdllist.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = a_cdllist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_cdllist.insert(ref_node, new_node)
            elif suboperation == 'before':
                a_cdllist.insert_before(ref_node, new_node)
    elif operation == 'p':
        index = int(do[1])
        tweet = a_cdllist.get_node(index)
        a_cdllist.go_prev(tweet)
        
    elif operation == 'f':
        index = int(do[1])
        tweet = a_cdllist.get_node(index)
        a_cdllist.go_first(tweet)
        
    elif operation == 'l':
        index = int(do[1])
        tweet = a_cdllist.get_node(index)
        a_cdllist.go_last(tweet)
                
    elif operation == 'num':
        index = int(do[1])
        tweet = a_cdllist.get_node(index)
        a_cdllist.get_size(tweet)
    
    elif operation == 's':
        index = int(do[1])
        tweet = a_cdllist.get_node(index)
        a_cdllist.search_tweet(tweet)
 
    elif operation == 'q':
        break
    
if __name__ == "__main__":
    main()