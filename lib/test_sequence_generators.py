import pytest

from lib.sequence_generators import FibonacciSequenceGenerator, PrimeNumberSequenceGenerator, CollatzSequenceGenerator


@pytest.mark.parametrize('first, second', [
    (-1, 1),
    (1, -1),
    (-1, -1)
])
def test_fib_seq_generator_given_negative_seeds(first, second):
    with pytest.raises(ValueError) as exc:
        _ = FibonacciSequenceGenerator(first, second)
    assert str(exc.value) == "Provide non-negative seeds."


@pytest.fixture
def first_100_fib_numbers():
    with open('lib/test_data/first_100_fib_numbers.txt') as infile:
        data = infile.read().strip().split('\n')
    return list(map(int, data))


@pytest.mark.parametrize('num_terms, correct_fib_terms', [
    (0, 'first_100_fib_numbers'),
    (25, 'first_100_fib_numbers'),
    (50, 'first_100_fib_numbers'),
    (75, 'first_100_fib_numbers'),
    (100, 'first_100_fib_numbers')
])
def test_fib_seq_generator_given_num_terms(num_terms, correct_fib_terms, request):
    correct_fib_terms = request.getfixturevalue(correct_fib_terms)[:num_terms]
    predicted_fib_terms = FibonacciSequenceGenerator(0, 1).generate(num_terms=num_terms)
    assert predicted_fib_terms == correct_fib_terms


def test_fib_seq_generator_given_negative_num_terms():
    with pytest.raises(ValueError) as exc:
        _ = FibonacciSequenceGenerator(0, 1).generate(num_terms=-1)
    assert str(exc.value) == "Provide non-negative num_terms."


@pytest.mark.parametrize('upper_bound, correct_fib_terms', [
    (0, 'first_100_fib_numbers'),
    (25, 'first_100_fib_numbers'),
    (1000, 'first_100_fib_numbers'),
    (200000, 'first_100_fib_numbers'),
    (4000000, 'first_100_fib_numbers')
])
def test_fib_seq_generator_given_upper_bound(upper_bound, correct_fib_terms, request):
    correct_fib_terms = request.getfixturevalue(correct_fib_terms)
    correct_fib_terms = [item for item in correct_fib_terms if item < upper_bound]
    predicted_fib_terms = FibonacciSequenceGenerator(0, 1).generate(upper_bound=upper_bound)
    assert predicted_fib_terms == correct_fib_terms


def test_fib_seq_generator_given_negative_upper_bound():
    with pytest.raises(ValueError) as exc:
        _ = FibonacciSequenceGenerator(0, 1).generate(upper_bound=-1)
    assert str(exc.value) == "Provide non-negative upper_bound."


@pytest.mark.parametrize('upper_bound, num_terms', [
    (None, None),
    (15, 15)
])
def test_fib_seq_generator_given_both_upper_bound_and_num_terms(upper_bound, num_terms):
    with pytest.raises(ValueError) as exc:
        _ = FibonacciSequenceGenerator(0, 1).generate(upper_bound=upper_bound, num_terms=num_terms)
    if upper_bound is None and num_terms is None:
        assert str(exc.value) == "Provide appropriate value for one of upper_bound or num_terms."
    else:
        assert str(exc.value) == "Provide appropriate value for only one of upper_bound or num_terms."


@pytest.fixture()
def first_two_hundred_thousand_primes():
    with open('lib/test_data/first_two_hundred_thousand_primes.txt') as infile:
        data = infile.read().strip().split('\n')
    return list(map(int, data))


@pytest.mark.parametrize('upper_bound, correct_primes', [
    (-1, 'first_two_hundred_thousand_primes'),
    (1, 'first_two_hundred_thousand_primes'),
    (2, 'first_two_hundred_thousand_primes'),
    (10, 'first_two_hundred_thousand_primes'),
    (100, 'first_two_hundred_thousand_primes'),
    (541, 'first_two_hundred_thousand_primes'),
    (2000000, 'first_two_hundred_thousand_primes')
])
def test_prime_seq_generator(upper_bound, correct_primes, request):
    correct_primes = request.getfixturevalue(correct_primes)
    correct_primes = [item for item in correct_primes if item <= upper_bound]
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
