class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next # points to the next node in the list

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

# append / add ---> add_to_tail
    def add_to_tail(self, value):
        # check if theres a tail
        # if theres no tail (empty list)
        if not self.tail: # could also check length, check if tail = None 
        #   create new node
            new_tail = Node(value, None)
        #   set self.head and self.tail to the new node
            self.head = new_tail
            self.tail = new_tail

        # if there is a tail(general case):
        else:
        #   create a new node with the value we want to add , next = None
            new_tail = Node(value, None)
        #   set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
        #   set self.tail to the new node 
            self.tail = new_tail
        self.length += 1


    #remove 
    def remove_head(self):
        # Check if head 
        # If not head(empty list):
        if not self.head:
            return None
        #   Return None

        # List with one element:
        if self.head == self.tail:
        #   Set self.head to current_head.next (which is also none)
            current_head = self.head
        #   set self.tail to None
            self.tail = None
        #   Decrement length by 1
            self.length -= 1 
            return current_head.value

        # If head (General case):
        else:
        #   Set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            self.length -= 1

        #   Return current_head.value
            return current_head.value



    def remove_tail(self):
    # check if its there
        if not self.tail:
            return None

    #List of only one element
    # save the current_tail_value
    # set self.tail to None
    # set self.head to None
        if self.head == self.tail:
            current_tail = self.tail.value
            self.tail = None
            self.head = None
            return current_tail

    # general case:
        else:
        # dtart at head and iterate to the next -to-last node
            current_node = self.head
        # stop when the current_node.next == self.tail
            while(current_node.next != self.tail):
                current_node = current_node.next
        # save the current_tail value
            # current_tail = current_node.value

            # set self.tail to cuurent_node
            self.tail = current_node

            # set current_node.next to None
            current_node.next = None
            

