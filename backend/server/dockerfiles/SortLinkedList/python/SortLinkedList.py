class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def sort_linked_list(list: Node):
    """
    static <X> NodePair<X> sort(NodePair<X> pairs, Comparator<X> comp) {
        Node<X> head = pairs.head;
        while (head != null) {
            Node<X> max = head;
            Node<X> secondHead = head;
            while (secondHead != null) {
                if (comp.compare(max.data, secondHead.data) > 0) {
                    max = secondHead;
                }
                secondHead = secondHead.next;
            }
            X tmp = max.data;
            max.data = head.data;
            head.data = tmp;
            head = head.next;
        }
        return pairs;
    }
    """
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
        newHead = newHead.next
    return list
