from datetime import datetime
import os

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
class Batching():    
    def __init__(self, X, y, batch_size):
        self.X = X
        self.y = y
        self.total = X.shape[0]
        self.batch_size = batch_size
        self.current = 0

    def next(self):
        max_index = self.current + self.batch_size
        indices = [i if i < self.total else i - self.total 
                       for i in range(self.current, max_index)]
        self.current = max_index % self.total
        return self.X[indices, ], self.y[indices, ]
    
    
"""
Show files and their size
"""

def show_dir(path):
    for f in os.listdir(path):
        absolute_path = os.path.join(path, f)
        size = absolute_path, os.stat(absolute_path).st_size
        print("%d %s" % (size[1], absolute_path)) 
        
