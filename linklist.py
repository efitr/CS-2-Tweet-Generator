
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self, head_data=None):
        self.head = head_data

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    

    def get_index(self, index):
        if self.head:
            current = self.head
            for _ in range(index-2):
                current = current.next
                print(current.data)
                if current.next == None:
                    return -1
            return current.data
        else:
            return -1
    

    def __str__(self):
        data = ""
        current = self.head
        while current != None:
            data += str(current.data)+" "
            current = current.next
        return data

if __name__ == '__main__':
    