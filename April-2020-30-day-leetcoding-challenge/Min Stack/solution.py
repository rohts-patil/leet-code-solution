### https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3292/


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min:
            if x <= self.min[-1]:
                self.min.append(x)
        else:
            self.min.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


class MinStackOptimized(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_list = []
        self.min_no = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        if(self.min_no) is None:
            self.main_list.append(x)
            self.min_no = x
        else:
            if self.min_no < x:
                self.main_list.append(x)
            else:
                self.min_no = x
                self.main_list.append(2*x-self.min_no)

    def pop(self):
        """
        :rtype: None
        """
        y = self.main_list[-1]
        if y > self.min_no:
            self.main_list = self.main_list[:-1]
        else:
            self.min_no = 2 * self.min_no - y
            self.main_list = self.main_list[:-1]

    def top(self):
        """
        :rtype: int
        """
        return self.main_list[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_no
