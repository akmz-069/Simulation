class MixedCongruentialGenerator:
    def __init__(self, seed, multiplier, increment, modulus):
    
        self.current = seed
        self.a = multiplier
        self.c = increment
        self.m = modulus

    def next(self):
        self.current = (self.a * self.current + self.c) % self.m
        return self.current

    def generate_sequence(self, n):
        return [self.next() for _ in range(n)]


if __name__ == "__main__":
    seed = 1
    multiplier = 5
    increment = 3
    modulus = 16

    rng = MixedCongruentialGenerator(seed, multiplier, increment, modulus)
    sequence = rng.generate_sequence(10)
    print("Generated Random Numbers:", sequence)
