from mrjob.job import MRJob
from numpy import mean

class Count(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        yield 'Average words per review', len(fields[4].split())

    def reducer(self, word, counts):
        num = 0
        total = 0
        for count in counts:
            num += 1
            total += count
        yield word, total/num

if __name__ == '__main__':
    Count.run()