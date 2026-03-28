# ==============================
# 1. Dynamic Array
# ==============================
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [0] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.arr[self.size] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            return "Empty"
        value = self.arr[self.size - 1]
        self.size -= 1
        return value

    def resize(self, new_capacity):
        new_arr = [0] * new_capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def display(self):
        print("Dynamic Array:", end=" ")
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()


# ==============================
# Node (Common for SLL, Stack, Queue)
# ==============================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ==============================
# 2. Singly Linked List (SLL)
# ==============================
class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        print("SLL:", end=" ")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ==============================
# 3. Doubly Linked List (DLL)
# ==============================
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        print("DLL:", end=" ")
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# ==============================
# 4. Stack using SLL
# ==============================
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return "Empty"
        val = self.top.data
        self.top = self.top.next
        return val

    def display(self):
        print("Stack:", end=" ")
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# ==============================
# 5. Queue using SLL
# ==============================
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return "Empty"
        val = self.front.data
        self.front = self.front.next
        return val

    def display(self):
        print("Queue:", end=" ")
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# ==============================
# 6. Parentheses Checker
# ==============================
def isBalanced(expr):
    stack = []

    for char in expr:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if (char == ')' and top != '(') or \
               (char == '}' and top != '{') or \
               (char == ']' and top != '['):
                return False

    return len(stack) == 0


# ==============================
# MAIN (Testing All)
# ==============================
if __name__ == "__main__":

    print("\n--- Dynamic Array ---")
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.display()
    print("Pop:", arr.pop())
    arr.display()

    print("\n--- Singly Linked List ---")
    sll = SLL()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    sll.display()
    sll.delete(2)
    sll.display()

    print("\n--- Doubly Linked List ---")
    dll = DLL()
    dll.insert(5)
    dll.insert(10)
    dll.insert(15)
    dll.display_forward()

    print("\n--- Stack ---")
    st = Stack()
    st.push(100)
    st.push(200)
    st.push(300)
    st.display()
    print("Pop:", st.pop())
    st.display()

    print("\n--- Queue ---")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    print("Dequeue:", q.dequeue())
    q.display()

    print("\n--- Parentheses Checker ---")
    expr = "{[()]}"
    print(expr, "Balanced?" , isBalanced(expr))