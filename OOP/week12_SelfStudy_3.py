import threading

class SumCalculator:
    def __init__(self, n):
        self.n = n
        self.total = 0

    def sum(self):
        self.total = sum(range(1, self.n + 1))
        print(f"1+2+3+...+ {self.n} = {self.total}")

calc1 = SumCalculator(1000)
calc2 = SumCalculator(100000)
calc3 = SumCalculator(10000000)

th1 = threading.Thread(target=calc1.sum)
th2 = threading.Thread(target=calc2.sum)
th3 = threading.Thread(target=calc3.sum)

th1.start()
th2.start()
th3.start()