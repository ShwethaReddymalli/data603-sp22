from mrjob.job import MRJob

class Count(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        if fields[1] != 'date':
            yield fields[1][:7], 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    Count.run()