import pytest

from tests import _init_paths
from lib.sequence_generators import FibonacciSequenceGenerator, PrimeNumberSequenceGenerator, CollatzSequenceGenerator


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


@pytest.mark.parametrize('upper_bound, correct_primes', [
    (10, [2, 3, 5, 7]),
    (100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]),
    (541, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
           107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
           229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
           359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
           491, 499, 503, 509, 521, 523, 541])  # First 100 primes
])
def test_prime_seq_generator(upper_bound, correct_primes):
    predicted_primes = PrimeNumberSequenceGenerator.generate(upper_bound)
    assert predicted_primes == correct_primes


@pytest.mark.parametrize('num, correct_sequence', [
    (13, [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
    (27, [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206,
          103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167,
          502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619,
          4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866,
          433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8,
          4, 2, 1])
])
def test_collatz_seq_generator(num, correct_sequence):
    predicted_sequence = CollatzSequenceGenerator.generate(num)
    assert predicted_sequence == correct_sequence
