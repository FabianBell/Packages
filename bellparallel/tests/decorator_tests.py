from bellparallel import parallel
import unittest

def inc(entry):
    return entry + 1

@parallel()
def inc_normal(entry):
    return inc(entry)

@parallel(tag='TEST', nproz=2)
def inc_tag_nproz(entry):
    return inc(entry)

def generator():
    for i in range(100):
        yield i

class Increment:
    
    def __init__(self, base):
        self.base = base

    @parallel(tag='INC')
    def inc(self, entry):
        return entry + self.base

class TestDecorator(unittest.TestCase):
    
    def check(self, func):
        data = list(range(100))
        p_out = func(data)
        out = [inc(elem) for elem in data]
        self.assertEqual(p_out, out)

    def test_normal(self):
        self.check(inc_normal)

    def test_tag_and_nproz(self):
        self.check(inc_tag_nproz)
    
    def test_generator(self):
        gen = generator()
        p_out = inc_normal(gen, length=100)
        out = [inc(elem) for elem in generator()]
        self.assertEqual(p_out, out)

    def test_context_parallel(self):
        base = 2
        increment = Increment(base)
        data = list(range(100))
        p_out = increment.inc(data)
        out = [entry + base for entry in data]
        self.assertEqual(p_out, out)

if __name__ == '__main__':
    unittest.main()
