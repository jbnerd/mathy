import _init_paths
from lib.sequence_generators import FibonacciSequenceGenerator

if __name__ == "__main__":
    generator = FibonacciSequenceGenerator(1, 2)
    fib_seq = generator.generate(4000000)
    print(sum([i for i in fib_seq if i % 2 == 0]))
