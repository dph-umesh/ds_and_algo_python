import ctypes

# What is expected?
# 1) An array that grows dynamically (i.e it resizes)  --> O(n)
# 2) Ability to append to the array --> O(1)
# 3) Ability to insert at a given position --> O(n)
# 4) Ability to delete from the end of the array --> O(1)
# 5) Ability to delete an element at a given position --> O(n)
# 6) Ability to get the length of the array --> O(1)
# 7) Ability to fetch an item at a given position --> O(1)


class DynamicArray:
    def __init__(self):
        self.n = 0  # Number of elements in array
        self.size = 1  # Initial size of array
        self.array = self.__create_array(self.size)

    def __del__(self):
        self.n = 0
        self.size = 0
        del self.array

    @property
    def n(self):
        return self.__number_of_elements

    @n.setter
    def n(self, n):
        self.__number_of_elements = n

    @property
    def size(self):
        return self.__array_size

    @size.setter
    def size(self, size):
        self.__array_size = size

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        return self.array[index]

    def __str__(self):
        array_items = ""
        for i in range(self.n - 1):
            array_items += f"{self.array[i]}, "

        array_items += str(self.array[self.n - 1])
        return array_items

    def append(self, value):
        if self.n == self.size:
            self.__resize_array(2 * self.size)

        self.array[self.n] = value
        self.n += 1

    def insert_at(self, index, value):
        if not 0 <= index < self.n:
            raise IndexError(f"Index out of range (0, {self.n})")

        if self.n == self.size:
            self.__resize_array(2 * self.size)

        for i in range(self.n, index - 1, -1):
            self.array[i] = self.array[i - 1]

        self.array[index] = value
        self.n += 1

    def pop(self):
        popped_value = self.array[self.n - 1]
        self.array[self.n - 1] = 0  # use del instead ?
        self.n -= 1

        return popped_value

    def remove_at(self, index):
        if not 0 <= index <= self.n:
            raise IndexError(f"Index out of range (0, {self.n})")

        for i in range(index + 1, self.n, 1):
            self.array[i - 1] = self.array[i]

        self.array[self.n] = 0  # use del instead ?
        self.n -= 1

    def __resize_array(self, new_size):
        new_array = self.__create_array(new_size)

        for i in range(self.n):
            new_array[i] = self.array[i]

        self.array = new_array
        self.size = new_size

    @staticmethod
    def __create_array(size):
        return (size * ctypes.py_object)()
