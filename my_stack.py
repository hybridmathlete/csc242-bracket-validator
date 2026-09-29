"""
Author: AU75ZB
Date: 9/10/2026

Purpose: Implements MyStack, a LIFO (last-in, first-out) stack built by
inheriting from MyLinkedList (Lab 3). The TOP of the stack is mapped to
the FRONT of the linked list, so push, pop, and get_top reuse the O(1)
front operations add_first / delete_at(0) / get_first -- no node or
pointer logic is reimplemented. Also provides is_empty_stack, get_count
(delegating to the inherited count), deep-copy support through the
inherited copy_list, and a __str__ that prints TOP to BOTTOM using only
the stack interface plus a temporary MyStack to restore order.

Input: No console input. The test driver (test_my_stack.py) constructs
MyStack objects and passes integer values to push; the other methods
take no arguments, except copy_list, which takes another MyStack (or
MyLinkedList) instance.

Output: Printed test results comparing expected vs. actual behavior for
every stack operation -- construction, push/get_top, pop (including pop
on an empty stack), deep copy with self-copy safety and object
independence, and __str__ -- verified line-by-line against
Lab_4_expected_output.txt.
"""

from my_linked_list import MyLinkedList


class MyStack(MyLinkedList):
    '''
    MyStack is a LIFO stack built by inheriting from MyLinkedList instead
    of managing its own nodes. Inheriting keeps every node and pointer
    operation in one place: the stack never touches _first, _last, or
    _count directly, so it cannot corrupt the list's invariants, and any
    fix or optimization made to MyLinkedList is picked up automatically.
    Each stack method is a thin rename over an inherited operation --
    push, pop, and get_top all map to the O(1) FRONT of the list
    (add_first / delete_at(0) / get_first).
    '''

    # -----------------------------------------------------------------
    # Required comment -- LIFO (stack) vs. FIFO (queue)
    #
    # A stack is LIFO: the last item pushed is the first one popped.
    # Every operation happens at ONE end, the TOP. This class maps TOP
    # to the FRONT of the inherited linked list, because a linked list
    # adds and removes at the front in O(1) -- so push, pop, and get_top
    # all act on index 0 (add_first / delete_at(0) / get_first).
    #
    # A queue is FIFO: the first item enqueued is the first one
    # dequeued, so a queue works at BOTH ends -- new items join the
    # back, old items leave from the front. If this were MyQueue instead
    # of MyStack, the front/back mapping would change to:
    #     enqueue -> add_last     (join at the BACK)
    #     dequeue -> delete_at(0)  (leave from the FRONT)
    #     peek    -> get_first     (look at the FRONT)
    # A linked list stays O(1) at both ends (delete_at(0) at the front,
    # and add_last is O(1) thanks to the _last pointer), so a linked
    # queue is efficient. An array-backed queue would not be -- removing
    # from the front shifts every element -- which is why MyArrayQueue
    # would need circular indexing.
    # -----------------------------------------------------------------

    def __init__(self):
        '''
        Precondition: none.
        Postcondition: Creates an empty MyStack by reusing MyLinkedList's
        constructor -- no additional state is needed.
        '''
        super().__init__()

    def is_empty_stack(self):
        '''
        Precondition: none.
        Postcondition: Returns True if the stack has no elements, False
        otherwise. Reuse the correct inherited method -- do not write
        new emptiness logic.
        '''
        return self.is_empty()

    def push(self, item):
        '''
        Precondition: item is the value to add.
        Postcondition: item becomes the new TOP of the stack. TOP =
        FRONT of the linked list. Do NOT use add_last.
        '''
        self.add_first(item)

    def pop(self):
        '''
        Precondition: none.
        Postcondition: If the stack is not empty, the TOP element is
        removed (does not return a value). If the stack is empty, it is
        left unchanged. TOP = FRONT of the linked list.
        '''
        self.delete_at(0)

    def get_top(self):
        '''
        Precondition: the stack is not empty.
        Postcondition: Returns the TOP element without modifying the
        stack. Reuse the correct inherited accessor.
        '''
        return self.get_first()

    def get_count(self):
        '''
        Precondition: none.
        Postcondition: Returns the number of elements currently in the
        stack. Reuse inherited count logic.
        '''
        return super().get_count()

    def __str__(self):
        '''
        Precondition: none.
        Postcondition: Returns "EMPTY STACK" if the stack has no
        elements. Otherwise returns each value from TOP to BOTTOM, one
        value per line. Do NOT access node references directly and do
        NOT call MyLinkedList's own __str__ -- build this using only
        push/pop/get_top/is_empty_stack (a temporary MyStack can hold
        items during the traversal so you can restore the original
        order afterward).
        '''
        if self.is_empty_stack():
            return "EMPTY STACK"

        temp = MyStack()
        result = ""

        # Drain self into temp, recording each value as it comes off the
        # top. Taking the top first gives TOP-to-BOTTOM order.
        while not self.is_empty_stack():
            value = self.get_top()
            if result == "":
                result = str(value)
            else:
                result = result + "\n" + str(value)
            temp.push(value)
            self.pop()

        # Pour temp back into self so the stack is left exactly as it was.
        while not temp.is_empty_stack():
            self.push(temp.get_top())
            temp.pop()

        return result

    # Creative Final Feature
    def peek_below(self, n):
        '''
        Precondition: n is an integer.
        Postcondition: Returns the value n positions below the TOP of
        the stack without modifying it -- n = 0 returns the TOP itself,
        n = 1 the element just beneath it, and so on. Returns None if n
        is out of range (negative, or n >= get_count()). Because the TOP
        of the stack is the FRONT of the linked list, "n below the top"
        is simply index n, so this reuses the inherited get_at.
        '''
        if n < 0 or n >= self.get_count():
            return None
        return self.get_at(n)
