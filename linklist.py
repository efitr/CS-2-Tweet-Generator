
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head_data=None):
        self.head = head_data

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return True
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

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

    def prepend(self, item):
        self.head = Node(data = item)
        self.next = self.head

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

    def __str__(self):
        data = ""
        current = self.head
        while current != None:
            data += str(current.data)+" "
            current = current.next
        return data

if __name__ == '__main__':
    import sys

    ll= LinkedList()
    ll.append("one")
    print(ll.__str__())
    ll.prepend('three')
    print(ll.__str__())
    print(ll.length())
    