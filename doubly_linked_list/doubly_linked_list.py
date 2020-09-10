"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # convert user val into node

        new_node = ListNode(value, None)
        #if its empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            new_node.next = old_head
            self.head.prev = new_node 

            self.head = new_node
        self.length += 1
        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None

        # if theres only one element
        if self.head == self.tail:
            current_head = self.head 
            self.head = current_head.next
            self.tail = None
            self.length -= 1
            return current_head.value
        
        # if head
        else:
            current_head = self.head
            self.head = current_head.next
            self.length -= 1
            return current_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):

        new_node = ListNode(value, None)

        #if its empty
        if not self.head and not self.tail:
            self.tail = new_node
            self.head = new_node
        #if there is a tail
        else:
            old_tail = self.tail
            new_node.prev = old_tail
            self.tail.next = new_node

            self.tail = new_node
        self.length += 1


            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None
        
        if self.head == self.tail:
            current_tail = self.tail
            self.tail = current_tail.next
            self.head = None
            self.length -= 1
            return current_tail.value
        
        else:
            current_tail = self.tail
            self.tail = current_tail.prev
            self.length -= 1
            return current_tail.value

        

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        
        #if they select the head
        if node is self.head:
            return
        
        value = node.value
        # if the select the tail
        self.delete(node)
        # add the node to the head using above meathod
        self.add_to_head(value)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):

        if node is self.tail:
            return

        value = node.value

        self.delete(node)

        self.add_to_tail(value)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        #check if its empty 
        self.length -= 1
        if not self.head and not self.tail:
            return
        
        #if theres only oone element
        if self.head is self.tail:
            self.head = None
            self.tail = None

        #if its the head
        elif node is self.head:
            self.head = node.next
            node.delete()

        # if its the tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()

        #general case
        else:
            node.delete()

            



    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        
        if not self.head:
            return None
        
        current = self.head
        max_val = current.value


        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next        

        return max_val

