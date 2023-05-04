# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds a new element to the bag
        """
        self._da.append(value)  # .append adds a new element
        return

    def remove(self, value: object) -> bool:
        """
        Removes one element from the bag
        """
        for i in range(self._da.length()):  # iterates through the array
            if self._da.get_at_index(i) == value:  # determines the index of the value
                self._da.remove_at_index(i)  # removes the value at the index
                return True  # returns true if passes
            else:
                return False  # returns false if fails

    def count(self, value: object) -> int:
        """
        Counts the values in an array
        """
        count = 0  # sets the count to 0
        for i in range(self._da.length()):  # iterates through the array
            if self._da.get_at_index(i) == value:
                count += 1  # adds one to the count for every value in the array
            return count

    def clear(self) -> None:
        """
        Clears the bag of values
        """
        for i in range(self._da.length() - 1, -1, -1):  # iterates through the array at last index to 0
            self._da.remove_at_index(i)  # removes values at each index in reverse order

    def equal(self, second_bag: "Bag") -> bool:
        """
        Compares the elements of two bags. Returns true if the bags contain the same number of elements and false if
        they do not.
        """
        if self._da.length() != second_bag._da.length():  # determines if the bag are equal or not, if not, return false
            return False
        for element in range(self._da.length()):  # loops through the elements
            if second_bag.count(element) != self.count(element):  # checks if the elements are the same and happen
                # the same amount of times
                return False
        return True

    def __iter__(self):
        """
        Enable the bag to iterate across itself
        """
        self._index = 0

        return self

    def __next__(self):
        """
        TODO: Write this implementation
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index = self._index + 1
        return value

bag = Bag([5, 4, -8, 7, 10])
print(bag)
for item in bag:
    print(item)
