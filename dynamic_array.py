# Name: Justin Millet
# OSU Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Dynamic array and ADT implementation
# Due Date: 5/1/2023
# Description: Dynamic arrays and implementation


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        resize changes the capacity of the array
        """
        if new_capacity <= 0 or new_capacity < self._size:
            return
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._data[i]
        self._capacity = new_capacity
        self._data = new_array

    def append(self, value: object) -> None:
        """
        Doubles the size of the array, as needed, to add another value
        """
        if self._size == self._capacity:  # checks if the size is equal to the capacity
            self.resize(2 * self._capacity)  # if the size IS the same as capacity, it doubles the capacity
        self._data[self._size] = value  # assigns the next position as value
        self._size += 1  # adds one to the size of the array

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts a new value at a given index in an array
        """
        if index < 0 or index > self._size:  # checks if the index point is less than 0 and if the index is greater
            # than the size it wants to add to
            raise DynamicArrayException("Exception")  # raises the DynamicArrayException if either of the two
            # statements above are true
        if self._size == self._capacity:  # checks if the size is the same as the capacity of the given array
            self.resize(2 * self._capacity)  # doubles the capacity to accommodate the new size
        for i in range(self._size, index, -1):  # for loop that iterates through from self._size to the index
            self._data[i] = self._data[i - 1]  # makes a copy of the index point
        self._data[index] = value  # inserts the new value at the index once the for loop completes
        self._size += 1  # increase the size of the array

    def remove_at_index(self, index: int) -> None:
        """
        Removes a value at a specific index. Reduces the capacity by twice the number of current elements if the
        array is less than 1/4 of its capacity.
        """
        if index < 0 or index >= self._size:  # checks if the index point is less than 0 or greater than of equal to
            # the size of the array
            raise DynamicArrayException("Exception")  # raises the DynamicArrayException if either of the two
            # statements above are true
        if self._size - 1 < self._capacity // 4 and self._capacity > 10:  # determines if the size is less than 1/4
            # of the capacity and if the capacity is greater than index 10
            new_capacity = max(self._size * 2, 10)  # finds a new capacity by multiplying the size by 2 and index's 10
            self.resize(new_capacity)  # resizes the array to the new capacity found above
        for i in range(index, self._size - 1):  # loops through the array to find last element
            self._data[i] = self._data[i + 1]  # removes the last element
        self._data[self._size - 1] = None
        self._size -= 1  # decreases the size of the array by 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        Creates a new array based on the number of requested elements from an original array. Ensures there are
        enough elements in the original array to make the new array via a "slice"
        """
        if start_index < 0 or start_index >= self._size:  # checks if the starting index is in a valid position
            raise DynamicArrayException("Exception Occurred")
        if size < 0:  # checks if the size is 0
            raise DynamicArrayException("Exception Occurred")
        final_index = start_index + size - 1  # give us the final index minus 1
        if final_index >= self._size:  # checks if the final index is greater than or equal to the size of the array
            raise DynamicArrayException("Exception Occurred")
        new_array = DynamicArray()  # creates a new array in the dynamic class
        for i in range(start_index, final_index + 1):  # iterates through the new array from the starting index to
            # the final index minus 1
            new_array.append(self._data[i])  # adds the new array to the data
        return new_array

    def merge(self, second_da: "DynamicArray") -> None:
        """
        Merges two arrays by use of append. Elements stay in the same order as original, such as 1,2,3 and 6,7,
        8 becomes 1,2,3,6,7,8.
        """
        for i in range(second_da._size):  # iterates through the elements in second_da
            self.append(second_da[i])  # adds second_da to the dynamic array

    def map(self, map_func) -> "DynamicArray":
        """
        Create a new DA based on the function according to the value given.
        """
        new_array = DynamicArray()  # creates a new array for the function
        for i in range(self._size):  # iterates to apply the map function
            map_value = map_func(self._data[i])  # applies the map function based on the array and values
            new_array._data[new_array._size] = map_value
            new_array._size += 1  # adds the mapped value based on the code above at the given index
        return new_array

    def filter(self, filter_func) -> "DynamicArray":
        """
        Returns a new array based on the given function. Finds the values that the filter finds true.
        """
        new_array = DynamicArray()  # creates new array
        for i in range(self._size):  # iterates through and provides the filter function argument via next line
            if filter_func(self._data[i]):
                new_array.append(self._data[i])  # adds a true element to the new array
        return new_array

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Applies the reduce function to all elements in an array. Uses the function given to us when we test.
        """
        if self._size == 0:  # checks if the size is 0
            return initializer  # returns initializer, which is None
        if initializer is None:  # determines the initializer is none and sets the starting index to 1
            initializer = self._data[0]
            start_index = 1
        else:  # if initiazlier is not None, sets index to 0
            start_index = 0
        result = initializer  # sets the result as the initializer
        for i in range(start_index, self._size):  # iterates through the array
            result = reduce_func(result, self._data[i])  # applies the reduce fucntion based on the initializer and
            # the array
        return result


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    Receive a Dynamic Array that is sorted and return a tuple comprised of the mode, and the frequency of how many
    times they occur in the array
    """
    mode_val = arr[0]  # sets initial mode value to the first index in the array
    mode_freq = 1  # set initial frequency to 1
    current_val = arr[0]  # set current value in the array to the first element in the array
    current_freq = 1  # set the current frequency to 1
    mode_arr = DynamicArray()  # creates a new DA

    for i in range(1, len(arr)):  # iterates through the array starting at the SECOND element
        if arr[i] == current_val:  # determines if the current element is equal to the current value
            current_freq += 1  # if the above is true, adds 1 to the frequency
        else:
            if current_freq > mode_freq:  # updates both frequencies if the current is greater than the mode
                mode_val = current_val  # sets the mode value to the current value
                mode_freq = current_freq  # sets the mode frequency to the current frequency
            elif current_freq == mode_freq:  # determines if the current frequency is equal to the mode frequency
                mode_arr.append(current_val)  # adds the current value to the mode array
            current_val = arr[i]  # Updates current value
            current_freq = 1  # updates current frequency
    if current_freq > mode_freq:  # determines if the current frequency is greater than the mode frequency
        mode_val = current_val  # sets the mode value to the current value
        mode_freq = current_freq  # sets the mode frequency to the current frequency
        mode_arr = DynamicArray()  # updates the array
    elif current_freq == mode_freq:  # updates the current frequency if it is equal to the mode frequency
        mode_arr.append(current_val)  # adds on value to the array
    mode_arr.append(mode_val)  # adds one value to the mode array

    return mode_arr, mode_freq  # returns the tuple
