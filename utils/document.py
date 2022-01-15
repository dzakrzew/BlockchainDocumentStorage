import json

class Document():
    def __init__(self, side_a, side_b, checksum, description):
        self.side_a = side_a
        self.side_b = side_b
        self.checksum = checksum
        self.description = description
    
    def serialize(self):
        data = {
            'a': self.side_a,
            'b': self.side_b,
            'c': self.checksum,
            'd': self.description
        }

        return data