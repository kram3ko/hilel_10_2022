class frange:
    def __init__(self, start, end=None, step=None):
        self._start = start
        self._end = end
        self._step = step if step else 1

        if self._end is None:
            self._end = 0
            self._start, self._end = self._end, self._start

    def __next__(self):
        if self._start >= self._end:
            if self._step > 0:
                raise StopIteration("stop")
            if self._start + self._step < self._end:
                raise StopIteration("stop")
        if self._start < self._end and self._step < 0:
            raise StopIteration("stop")

        result = self._start
        self._start += self._step
        return result

    def __iter__(self):
        return self


assert list(frange(5)) == [0, 1, 2, 3, 4]
assert list(frange(2, 5)) == [2, 3, 4]
assert list(frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(frange(1, 5)) == [1, 2, 3, 4]
assert list(frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(frange(0, 0)) == []
assert list(frange(100, 0)) == []

print("SUCCESS!")
