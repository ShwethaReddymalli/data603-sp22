from mrjob.job import MRJob

class Count(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        if fields[7] != 'cool':
            if fields[7] != '0':
                yield 'Averaging rating of cool reviews', int(fields[3])

    def reducer(self, word, counts):
        num = 0
        total = 0
        for count in counts:
            num += 1
            total += count
        yield word, total/num

if __name__ == '__main__':
    Count.run()