from typing import List


class LinkedList:
    head = None

    def __init__(self):
        pass

    def get(self, index: int) -> int:
        c = self.head
        for _ in range(index):
            if c is None:
                return -1
            c = c.next_node
        r = -1 if c is None else c.val
        return r

    def insertHead(self, val: int) -> None:
        current_head = self.head
        self.head = Node(val)
        self.head.add_link(current_head)

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
        else:
            c = self.head
            while c.next_node is not None:
                c = c.next_node
            c.add_link(Node(val))

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        elif index == 0:
            self.head = self.head.next_node
            return True
        else:
            next_node = self.head.next_node
            c = self.head
            prev = self.head
            for _ in range(index):
                if c is None:
                    return False
                else:
                    try:
                        prev = c
                        c = c.next_node
                        next_node = c.next_node
                    except:
                        return False

            if c is None:
                return False
            else:
                prev.add_link(next_node)
                return True

    def getValues(self) -> List[int]:
        values = []
        c = self.head
        while c is not None:
            values.append(c.val)
            c = c.next_node
        return values


class Node:
    val = None
    next_node = None

    def __init__(self, val):
        self.val = val

    def add_link(self, node):
        self.next_node = node
