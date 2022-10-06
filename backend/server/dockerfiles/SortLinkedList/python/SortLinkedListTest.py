import unittest
from SortLinkedList import sort_linked_list, Node
import random


class TestSortLinkedList(unittest.TestCase):

    def is_sorted(self, head: Node) -> bool:
        while(head.next != None):
            if(head.val > head.next.val):
                return False
            head = head.next
        return True

    def test_1(self):
        head = self.gen_linked_list()
        head = sort_linked_list(head)
        assert self.is_sorted(head)

    def gen_linked_list(self) -> Node:
        mainHead = Node(random.randint(0, 500))
        head = mainHead
        for i in range(500):
            head.next = Node(random.randint(0, 500))
            head = head.next
        return mainHead


if __name__ == '__main__':
    unittest.main()
