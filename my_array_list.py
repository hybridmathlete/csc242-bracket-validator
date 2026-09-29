"""
Author: AU75ZB
Date: 8/24/2026

Purpose: Implements MyArrayList, an array-based list built from scratch
on top of a fixed-capacity backing Python list. Supports manual
capacity-doubling growth, insertion/deletion with element shifting,
deep copying (including a safe self-copy case), sequential search,
selection sort, and operator overloading for += and + and str().
Also includes binary_search, the Creative Final Feature, which
searches an already-sorted list in O(log n) time.

Input: An optional starting capacity (int) for the constructor; items,
indices, and values passed to the various methods (append, insert_at,
get, set_at, find, binary_search, etc.); and, for copy_list/from_array/
the operator overloads, either a Python list or another MyArrayList
instance.

Output: Printed test results comparing expected vs. actual behavior
for every method -- constructors, growth, insert/delete, search,
sort, deep copy, and the operator overloads -- verified line-by-line
against Lab_2_expected_output.txt.
"""

class MyArrayList:

    def __init__(self, capacity=4):
        '''
        Precondition: capacity, if given, is a positive integer.
        Postcondition: Creates an empty MyArrayList with a preallocated
        backing list of the given capacity (default 4) and a count of 0.
        '''
        self._capacity = capacity if capacity > 0 else 4
        self._array = [None] * self._capacity
        self._count = 0

    @classmethod
    def from_fill(cls, count, value):
        '''
        Precondition: count is an integer >= 0; value is the item to
        fill the list with.
        Postcondition: Returns a new MyArrayList containing count
        copies of value.
        '''
        newList = cls(count)
        for i in range(count):
            newList._array[i] = value
            newList._count += 1
        return newList

    @classmethod
    def from_array(cls, items):
        '''
        Precondition: items is a Python list (or other indexable
        sequence) of values.
        Postcondition: Returns a new MyArrayList containing a deep copy
        of items -- the new list does not share a reference with items.
        '''

        newList = cls(len(items))
        for i in range(len(items)):
            newList._array[i] = items[i]
            newList._count += 1
        return newList

    def copy_list(self, other):
        '''
        Precondition: other is a MyArrayList (may be the same object as
        self.
        Postcondition: self becomes a deep copy of other's contents.
        Correctly handles the self-copy case (copy_list(self)) without
        corrupting or losing data.
        '''
        count = other._count
        newArray = [None] * count
        for i in range(count):
            newArray[i] = deep_copy_value(other._array[i])
        self._array = newArray
        self._capacity = count
        self._count = count

    def append(self, item):
        '''
        Precondition: item is the value to add.
        Postcondition: item is added to the end of the list. If the
        backing list is full, capacity is doubled first.
        '''
        if self._count == self._capacity:
            newArray = [None] * (self._capacity * 2)
            # most calls are O(1) just a write and increment. Resizes are occasional
            # resizes cost O(n) and because capacity doubles as the list grows the resizes become rarer
            # that's what makes append amortized O(1) because not every call is fast, but the average call is

            for i in range(self._count):
                newArray[i] = self._array[i]
            self._array = newArray
            self._capacity = (self._capacity * 2)
        self._array[self._count] = item
        self._count += 1

    def insert_at(self, index, item):
        '''
        Precondition: index is an integer; item is the value to insert.
        Postcondition: If 0 <= index <= count, item is inserted at
        index, shifting later elements right by one (doubling capacity
        first if needed), and returns True. Otherwise, the list is left
        unchanged and returns False.
        '''
        if 0 <= index <= self._count:

            if self._count == self._capacity:
                newArray = [None] * (self._capacity * 2)
                # See append()'s comment for why this makes growth amortized O(1)
                for i in range(self._count):
                    newArray[i] = self._array[i]
                self._array = newArray
                self._capacity = (self._capacity * 2)

            for i in range(self._count,index, -1):
                self._array[i] = self._array[i-1]
            self._array[index] = item
            self._count += 1
            return True

        return False

    def delete_at(self, index):
        '''
        Precondition: index is an integer.
        Postcondition: If 0 <= index < count, removes the element at
        index, shifting later elements left by one, and returns True.
        Otherwise, the list is left unchanged and returns False.
        Capacity itself never shrinks.
        '''
        if 0 <= index < self._count:
            for i in range(index, self._count-1):
                self._array[i] = self._array[i+1]
            self._count -= 1
            return True
        return False

    def clear(self):
        '''
        Precondition: none.
        Postcondition: Removes all elements, resetting the list to an
        empty state. Capacity is left unchanged.
        '''
        self._count = 0

    def get_count(self):
        '''
        Precondition: none.
        Postcondition: Returns the number of elements currently stored
        in the list.
        '''
        return self._count

    def is_empty(self):
        '''
        Precondition: none.
        Postcondition: Returns True if the list contains no elements,
        False otherwise.
        '''
        return self._count == 0

    def get(self, index):
        '''
        Precondition: index is an integer.
        Postcondition: Returns the element at index if 0 <= index <
        count. Returns None if index is out of range.
        '''
        if 0 <= index < self._count:
            return self._array[index]
        return None

    def set_at(self, index, value):
        '''
        Precondition: 0 <= index < self.get_count().
        Postcondition: Overwrites the element at index with value.
        Does not shift any other elements or change count. Since
        MyArrayList is backed by a preallocated list, this is a
        one-line write to the underlying slot -- the indexed-write
        counterpart to get(). Required starting in Lab 8.
        '''
        self._array[index] = value

    def __str__(self):
        '''
        Precondition: none.
        Postcondition: Returns a string with each element separated by a
        single space, matching the format used by the C++ print()/
        operator<< equivalent.
        '''
        result = ""
        for i in range(0,self._count):
            if i == 0:
                result = result + str(self._array[i])
            else:
                result = result + " " + str(self._array[i])

        return result

    def contains(self, item):
        '''
        Precondition: item is the value to search for.
        Postcondition: Returns True if item appears in the list, False
        otherwise. Reuses find() so the search logic stays in one place
        '''
        # See find()'s comment for the sequential-vs-binary-search analysis
        return self.find(item) != -1

    def find(self, item):
        '''
        Precondition: item is the value to search for.
        Postcondition: Returns the index of the first occurrence of
        item, using sequential search. Returns -1 if not found.
        '''
        # Sequential search (this method) has a complexity of O(n) and worst case being it touching every element
        # Binary search complexity is O(log n) and each comparison removes half of the remaining outcomes
        # The gap is that this Class design doesn't keep elements sorted automatically,
        # so that precondition isn't guaranteed.
        for i in range(0, self._count):
            if self._array[i] == item:
                return i
        return -1

    def sort(self):
        '''
        Precondition: none.
        Postcondition: Rearranges the elements in ascending order, using
        selection sort.
        '''

        for start in range(self._count - 1):
            minIndex = start

            for i in range(start, self._count):
                if self._array[i] < self._array[minIndex]:
                    minIndex = i
            temp = self._array[start]
            self._array[start] = self._array[minIndex]
            self._array[minIndex] = temp

    def __iadd__(self, other):
        '''
        Precondition: other is either a single item or another MyArrayList.
        Postcondition: If other is a MyArrayList, appends every element
        from other to self (safely handling the self-append case using
        a temporary copy). Otherwise, appends other as a single item.
        Returns self to support chaining.
        '''
        if isinstance(other, MyArrayList):
            count = other.get_count()
            newArray = [None] * count
            for i in range(count):
                newArray[i] = other.get(i)
            for i in range(count):
                self.append(newArray[i])
        else:
            self.append(other)

        return self

    def __add__(self, other):
        '''
        Precondition: other is either a single item or another MyArrayList.
        Postcondition: Returns a NEW MyArrayList containing self's
        elements followed by other (single item or another list's
        elements). Neither self nor other is modified.
        '''
        newList = MyArrayList()
        newList.copy_list(self)
        newList += other
        return newList

    def binary_search(self, item):
        '''
        Precondition: self is already sorted in ascending order (this
        method does not check or enforce that -- see find()'s comment
        for why this class's design can't guarantee it automatically).
        Postcondition: Returns the index of item if found using binary
        search over self._array. Returns -1 if not found.
        '''
        low = 0
        high = (self._count - 1)
        while low <= high:
            mid = (low + high) // 2
            if self._array[mid] < item:
                low = mid + 1
            elif self._array[mid] > item:
                high = mid - 1
            else:
                return mid

        return -1


# helper function after AI conversation about deep copy(See conversation)
def deep_copy_value(value):
    '''
    Precondition: value is any Python value (an int, a string, a list).
    Postcondition: Returns an independent copy of value. If value is a
    list, returns a brand-new list with every element, recursively deep-copied.
    Otherwise, returns value directly, since immutable values can never leak a shared mutation.
    '''
    if isinstance(value, list):
        newInner = []
        for item in value:
            newInner.append(deep_copy_value(item))
        return newInner
    else:
        return value
