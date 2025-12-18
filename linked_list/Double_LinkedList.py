# Doubly Linked List implementation in Python


# Node class represents each element in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store node value
        self.next = None      # Pointer to next node
        self.prev = None      # Pointer to previous node


# LinkedList class contains all DLL operations
class LinkedList:
    def __init__(self):
        self.head = None      # Initialize head as None


    # Insert a node at the end of the list
    def insertion(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp


    # Insert a node at the beginning of the list
    def insert_beginig(self, data):
        new_node = Node(data)

        temp = self.head
        self.head = new_node
        new_node.next = temp

        # Update previous pointer of old head
        temp.prev = new_node


    # Insert a node at the end of the list
    def insert_end(self, data):
        new_node = Node(data)
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp


    # Insert a node at a specific position (0-based index)
    def insert_position(self, data, index):
        new_node = Node(data)

        # Insert at head
        if index == 0:
            temp = self.head
            self.head = new_node
            new_node.next = temp
            temp.prev = new_node
            return

        temp = self.head
        count = 0

        # Traverse to the node before the given position
        while temp is not None and count < index - 1:
            temp = temp.next
            count += 1

        new_node.next = temp.next

        # Update previous pointer of next node
        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node
        new_node.prev = temp


    # Print the doubly linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print()


    # Check whether the doubly linked list is a palindrome
    def palindrome(self):
        # Single node is always a palindrome
        if self.head.next is None:
            return True

        left = self.head
        right = self.head

        # Move right pointer to the last node
        while right.next:
            right = right.next

        # Compare from both ends
        while left != right and left.prev != right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.prev

        return True


    # Delete the first node of the list
    def delete_first(self):
        self.head = self.head.next
        self.head.prev = None


    # Delete a node at a specific position
    def delete_po(self, po):
        # Delete head node
        if po == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        temp = self.head
        count = 0

        # Traverse to the given position
        while temp is not None and count < po:
            temp = temp.next
            count += 1

        # Update links
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next


    # Delete the first occurrence of a given value
    def delete_val(self, val):
        # If value is at head
        if self.head.data == val:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        temp = self.head

        while temp.next:
            if temp.next.data == val:
                temp.next = temp.next.next

                # Update previous pointer
                if temp.next:
                    temp.next.prev = temp
                return
            else:
                temp = temp.next


    # Reverse the doubly linked list
    def reverse(self):
        temp = self.head
        prev = None

        # Swap next and prev pointers for each node
        while temp:
            prev = temp.prev
            temp.prev = temp.next
            temp.next = prev
            temp = temp.prev

        # Update head after reversal
        if prev:
            self.head = prev.prev


    # Sort the doubly linked list
    def sorting(self):
        temp = self.head
        val = []

        # Store values in a list
        while temp:
            val.append(temp.data)
            temp = temp.next

        # Sort values
        val.sort()

        # Assign sorted values back to nodes
        temp = self.head
        for i in val:
            temp.data = i
            temp = temp.next


# Driver code
x = LinkedList()
x.insertion(10)
x.insertion(20)
x.insertion(30)

# Uncomment to test features
# if x.palindrome():
#     print('Palindrome')
# else:
#     print('Not Palindrome')
# x.insert_beginig(99)
# x.insert_position(100, 2)
# x.delete_first()
# x.reverse()
# x.sorting()
# x.delete_po(3)

x.print_list()
