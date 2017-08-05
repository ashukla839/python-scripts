"""
Stopwatch is used to capture elapsed time for a code blocks
"""
class StopWatch:
    def __init__(self):
        self.start = datetime.now()
        
    def reset(self):
        self.start = datetime.now()
    
    def lap(self, reset = True):
        elapsed = (datetime.now() - self.start).microseconds / 1000.0
        if(reset):
            self.reset()
        return elapsed

"""
Batch class is used to create batch of a large set of data. 
Often used to create mini batch for gradient descent algorith.
"""
class Batch():    
    def __init__(self, total, batch_size):
        self.total = total
        self.batch_size = batch_size
        self.current = 0

    def next(self):
        max_index = self.current + self.batch_size
        indices = [i if i < self.total else i - self.total 
                       for i in range(self.current, max_index)]
        self.current = max_index % self.total
        return indices 
