import json

import pytest

from euler.utils.sequence_generators import FibonacciSequenceGenerator, PrimeNumberSequenceGenerator, CollatzSequenceGenerator


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
    with open('euler/test_data/first_100_fib_numbers.txt') as infile:
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
    with open('euler/test_data/first_two_hundred_thousand_primes.txt') as infile:
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


@pytest.fixture()
def collatz_sequences():
    with open('euler/test_data/collatz_sequences.json') as infile:
        data = json.load(infile)
    return data


@pytest.mark.parametrize('num, correct_sequence', [
    (9, 'collatz_sequences'),
    (27, 'collatz_sequences'),
    (123, 'collatz_sequences')
])
def test_collatz_seq_generator(num, correct_sequence, request):
    correct_sequence = request.getfixturevalue(correct_sequence)[str(num)]
    predicted_sequence = CollatzSequenceGenerator.generate(num)
    assert predicted_sequence == correct_sequence


@pytest.mark.parametrize('upper_bound, correct_num', [
    (10, 9),
    (25, 25),
    (50, 27),
    (100, 97),
    (500, 327)
])
def test_longest_collatz_sequence_given_upper_bound(upper_bound, correct_num):
    predicted_num = CollatzSequenceGenerator.longest_sequence_seed(upper_bound)
    assert predicted_num == correct_num
