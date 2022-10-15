class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def sort_linked_list(list: Node):
    newHead = list
    while newHead is not None:
        max = newHead
        secondHead = newHead
        while(secondHead is not None):
            if(max.val > secondHead.val):
                max = secondHead
            secondHead = secondHead.next

        tmp = max.val
        max.val = newHead.val
        newHead.val = tmp
        # newHead = newHead.next
    return list
