class Memory:
    def __init__(self):
        self.value = 0.0

    def madd(self, number):
        """M+ — прибавить число к памяти."""
        self.value += number

    def msubtract(self, number):
        """M- — вычесть число из памяти."""
        self.value -= number

    def mrecall(self):
        """MR — вернуть текущее значение памяти."""
        return self.value

    def mclear(self):
        """MC — очистить память."""
        self.value = 0.0

    def mstore(self, number):
        """MS — записать число в память (перезаписать)."""
        self.value = number
