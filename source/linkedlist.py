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
        self.head = Node(data = item)
        self.next = self.head

        if self.tail == None:
            self.tail = Node(data = item)

    def find(self, quality):
        current = self.head

        while current != None:
            if current.data == quality:
                return current.data
            else:
                current = current.next

    def delete(self, item):
        current_node = self.head
        previous_node = None
        while current_node and current_node.data != item:
            previous_node = current_node
            current_node = current_node.next
        
        if previous_node is None:
            self.head = current_node.next
        elif current_node:
            previous_node.next = current_node.next
            current_node.next = None
        
        print(self.length())
        print(self.tail)

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
        print('lenght: {}'.format(ll.lenght()))

if __name__ == '__main__':
    test_linked_list()
    