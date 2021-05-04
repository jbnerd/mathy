from typing import List, Iterable


class FibonacciSequenceGenerator:
    def __init__(self, first: int, second: int):
        self.first = first
        self.second = second

    def generate(self, upper_bound: int = 0, num_terms: int = 0) -> List[int]:
        """Generates the Fibonacci sequence starting from first and second.

        upper_bound is exclusive
        """
        sequence = []
        for i, next_term in enumerate(self._next_num()):
            if upper_bound == 0 and num_terms == 0:
                raise ValueError("Either provide a positive upper_bound for the sequence or the (positive) num_terms "
                                 "to be generated.")
            if 0 < upper_bound <= next_term:
                break
            elif 0 < num_terms <= i:
                break
            else:
                sequence.append(next_term)
        return sequence

    def _next_num(self) -> Iterable[int]:
        first, second, i = self.first, self.second, 1
        while True:
            if i == 1:
                yield first
            elif i == 2:
                yield second
            else:
                third = first + second
                first, second = second, third
                yield third
            i += 1
