# Node class represents a single element of the linked list
class Node:
    def __init__(self, data):
        self.data = data      # Store data
        self.next = None      # Pointer to next node


# LinkedList class contains all operations on the linked list
class LinkedList:
    def __init__(self):
        self.head = None      # Initialize head as None


    # Insert a node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        temp = self.head
        self.head = new_node
        new_node.next = temp


    # Insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    # Insert a node (general insertion at end)
    def insertion(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node


    # Delete node from the beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            print(f'deleting the only one {self.head.data}')
            self.head = None
            return
        self.head = self.head.next


    # Find and delete the middle node using slow & fast pointers
    def find_middle(self):
        slow = self.head
        fast = self.head
        check = None   # Keeps track of node before slow

        while fast and fast.next:
            fast = fast.next.next
            check = slow
            slow = slow.next

        print(f'middle node is {slow.data}')
        print(f'deleting the middle {slow.data}')
        check.next = slow.next


    # Delete node from the end
    def delete_at_end(self):
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


    # Check whether the linked list is a palindrome
    def palindrome(self):
        val = []
        temp = self.head

        while temp:
            val.append(temp.data)
            temp = temp.next

        return val == val[::-1]


    # Remove duplicate elements from the linked list
    def duplicate_delete(self):
        temp = self.head
        lis = []

        while temp.next:
            lis.append(temp.data)
            if temp.next.data in lis:
                temp.next = temp.next.next
            else:
                temp = temp.next


    # Reverse the linked list
    def reverse(self):
        temp = self.head
        prev = None

        while temp:
            save = temp.next
            temp.next = prev
            prev = temp
            temp = save

        self.head = prev


    # Sort the linked list using extra space
    def sorting(self):
        val = []
        temp = self.head

        while temp:
            val.append(temp.data)
            temp = temp.next

        val.sort()

        temp = self.head
        for i in val:
            temp.data = i
            temp = temp.next


    # Insert a node at a specific position (0-based index)
    def insert_at_position(self, index, data):
        new_node = Node(data)

        if index == 0:
            new = self.head
            self.head = new_node
            new_node.next = new
            return

        count = 0
        temp = self.head

        while temp and count < index - 1:
            temp = temp.next
            count += 1

        new_node.next = temp.next
        temp.next = new_node


    # Delete a node at a specific position
    def delete_at_position(self, index):
        if index == 0:
            self.head = self.head.next
            return

        temp = self.head
        count = 0

        while temp and count < index - 1:
            temp = temp.next
            count += 1

        temp.next = temp.next.next


    # Delete the first occurrence of a given value
    def delete_value(self, val):
        if self.head.data == val:
            self.head = self.head.next
            return

        temp = self.head
        while temp and temp.next.data != val:
            temp = temp.next

        temp.next = temp.next.next


    # Display the linked list
    def display_list(self):
        temp = self.head
        while temp:
            print(temp.data, end='->')
            temp = temp.next
        print()


# Driver code / Testing
ll = LinkedList()
ll.insertion(10)
ll.insertion(20)
ll.insertion(30)
ll.insertion(40)
ll.insertion(100)
ll.insertion(40)
ll.insert_at_beginning(100)
ll.insert_at_end(200)

ll.delete_at_beginning()
ll.delete_at_end()
ll.find_middle()

if ll.palindrome():
    print("palindrome")
else:
    print("not palindrome")

ll.duplicate_delete()
ll.reverse()
ll.sorting()
ll.insert_at_position(1, 99)
ll.delete_at_position(0)
# ll.delete_value(10)

ll.display_list()
