#!python

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Node({!r})'.format(self.data)

class LinkedList(object):
    def __init__(self, items=None):
        self.head = None
        self.tail = None

        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        items = []
        node = self.head
        while node is not None:
            items.append(node.data)
            node = node.next
        return items

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.head is None:
            total = 0
            return total
        else:
            current_node = self.head

            total = 1

            while current_node.next != None:
                total += 1
                current_node = current_node.next
            return total

    
    def append(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node

        if self.tail != None:
            self.tail.next = new_node
        self.tail = new_node

    def prepend(self, item):
        new_node = Node(item)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        elif self.head == self.tail:
            self.head = new_node
            self.head.next = self.tail
        else:
            new_node.next = self.head
            self.head = new_node
        

    def find(self, quality):
        current = self.head

        while current != None:
            if quality(current.data):
                return current.data
            current = current.next
        return None

    def delete(self, item):
        current_node = self.head
        previous_node = None

        # Loop until the end of the linked list
        while current_node is not None:
            # if the currentnode.data is equal to the item passed in
            if current_node.data == item:
                    # If current node is in the middle
                if current_node is not self.head and current_node is not self.tail:
                    previous_node.next = current_node.next
                # If current node is the head
                if current_node is self.head:
                    self.head = current_node.next
                # If current node is the tail
                if current_node is self.tail:
                    if previous_node is not None:
                        previous_node.next = None
                    self.tail = previous_node
                return 
            previous_node = current_node
            current_node = current_node.next
        raise ValueError("Node does not exist")
            

        # while current_node and current_node.data != item:
        #     previous_node = current_node
        #     current_node = current_node.next
        
        # if previous_node is None:
        #     self.head = current_node.next
        # elif current_node:
        #     previous_node.next = current_node.next
        #     current_node.next = None
        
        # print(self.length())
        # print(self.tail)

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print(ll.head)

    print('\nTesting append: ')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r}'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('lenght: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()
    