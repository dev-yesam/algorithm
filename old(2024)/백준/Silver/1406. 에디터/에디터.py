import sys
input = sys.stdin.readline

## 더미헤드 - 더미테일(커서)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None) # 더미 헤드
        self.tail = Node(None) # 더미 테일
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.tail

    def move_left(self):
        if self.cursor.prev != self.head:
            self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor != self.tail:
            self.cursor = self.cursor.next

    def delete(self):
        # 왼쪽에 글자가 없다면 왼쪽 노드 삭제.
        if self.cursor.prev != self.head:
            self.cursor.prev.prev.next = self.cursor
            self.cursor.prev = self.cursor.prev.prev

    def insert(self, data):
        new = Node(data)
        new.prev = self.cursor.prev
        new.next = self.cursor
        self.cursor.prev.next = new
        self.cursor.prev = new

    def result(self):
        temp = []
        current = self.head.next
        while current != self.tail:
            temp.append(current.data)
            current = current.next
        return ''.join(temp)


word = input().rstrip()
lst = DoublyLinkedList()
for char in word:
    lst.insert(char)


n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'L':
        lst.move_left()
    elif command[0] == 'D':
        lst.move_right()
    elif command[0] == 'B':
        lst.delete()
    elif command[0] == 'P':
        lst.insert(command[1])


print(lst.result())