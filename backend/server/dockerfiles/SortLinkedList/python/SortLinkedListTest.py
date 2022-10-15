import unittest
from SortLinkedList import sort_linked_list, Node
import random
import time

import signal
import sys
from functools import wraps


class TimedOut(BaseException):
    pass


def timeout(seconds):
    """Decorator that makes a function time out.
    Because test suites that hang are no fun.  Especially on buildbots.
    Currently only implemented for Unix.
    """
    def decorator(fn):
        if hasattr(signal, 'alarm'):
            # yay, unix!
            @wraps(fn)
            def wrapper(*args, **kw):
                this_frame = sys._getframe()

                def raiseTimeOut(signal, frame):
                    # the if statement here is meant to prevent an exception in the
                    # finally: clause before clean up can take place
                    if frame is not this_frame:
                        raise TimedOut('timed out after %s seconds' % seconds)
                prev_handler = signal.signal(signal.SIGALRM, raiseTimeOut)
                try:
                    signal.alarm(seconds)
                    return fn(*args, **kw)
                finally:
                    signal.alarm(0)
                    signal.signal(signal.SIGALRM, prev_handler)
            return wrapper
        else:
            # XXX um, could someone please implement this for Windows and other
            # strange platforms?
            return fn
    return decorator


class TestSortLinkedList(unittest.TestCase):

    def is_sorted(self, head: Node) -> bool:
        while(head.next != None):
            if(head.val > head.next.val):
                return False
            head = head.next
        return True

    @timeout(10)
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
