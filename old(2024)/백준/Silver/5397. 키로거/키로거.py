import sys
input = sys.stdin.readline


class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.tail

    def insert(self, data):
        new_node = Node(data)
        new_node.prev = self.cursor.prev
        new_node.next = self.cursor
        self.cursor.prev.next = new_node
        self.cursor.prev = new_node

    def delete(self):
        if self.cursor.prev != self.head:
            self.cursor.prev = self.cursor.prev.prev
            self.cursor.prev.next = self.cursor

    def move_left(self):
        if self.cursor.prev != self.head:
            self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor != self.tail:
            self.cursor = self.cursor.next

    def result(self):
        temp = ''
        now_node = self.head.next
        while now_node != self.tail:
            temp += now_node.data
            now_node = now_node.next
        return temp


t = int(input())
for tc in range(t):
    pw = input().rstrip()
    lst = DLList()
    for i in pw:
        if i == '<':
            lst.move_left()
        elif i == '>':
            lst.move_right()
        elif i == '-':
            lst.delete()
        else:
            lst.insert(i)
    print(lst.result())


