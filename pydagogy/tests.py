from .utils import text_format
from .asserts import *


class BaseTest:
    def __init__(self):
        self._hint = ""
        self._solution = ""
        self._success = ""

    @property
    def hint(self):
        message = text_format("Hint: ", "yellow", "bold") + self._hint
        print(message)

    @hint.setter
    def hint(self, value):
        self._hint = value

    @property
    def solution(self):
        message = text_format("Solution: ", "blue", "bold") + self._solution
        print(message)

    @solution.setter
    def solution(self, value):
        self._solution = value

    @property
    def success(self):
        message = text_format("Success: ", "green", "bold") + self._success
        print(message)

    @success.setter
    def success(self, value):
        self._success = value


class ValueTest(BaseTest):
    def __init__(self, expected, tolerance=None):
        self.expected = expected
        self.tolerance = tolerance

    def check(self, value):
        result = False
        message = f"Expected to get {self.expected}, you passed {value} instead."

        if self.tolerance:
            result = assert_close(value, self.expected, self.tolerance, message)
        else:
            result = assert_equal(value, self.expected, message)

        if result:
            self.success

        return result
