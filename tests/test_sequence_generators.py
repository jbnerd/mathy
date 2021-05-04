from . import _init_paths
from lib.sequence_generators import FibonacciSequenceGenerator


class FibonacciSequenceGeneratorTestHelper:
    def __init__(self):
        with open('tests/data/first_100_prime_numbers.txt') as infile:
            data = infile.read().strip().split('\n')
        self.verification_data = [int(item) for item in data]

    def check_fib_seq_generator_with_num_terms(self):
        generator = FibonacciSequenceGenerator(0, 1)
        generated_data = generator.generate(num_terms=100)
        assert self.verification_data == generated_data

    def check_fib_seq_generator_with_upper_bound(self):
        generator = FibonacciSequenceGenerator(0, 1)
        generated_data = generator.generate(upper_bound=4000000)
        verification_data = [item for item in self.verification_data if item < 4000000]
        assert verification_data == generated_data


def test_fib_seq_generator():
    helper = FibonacciSequenceGeneratorTestHelper()
    helper.check_fib_seq_generator_with_num_terms()
    helper.check_fib_seq_generator_with_upper_bound()
