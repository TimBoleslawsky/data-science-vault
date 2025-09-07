from mrjob.job import MRJob
from mrjob.step import MRStep

class MRJobTwitterFollowers(MRJob):

    def mapper(self, _, line):
        line = line.strip()
        if not line or ':' not in line:
            return
        name_part, follower_part = line.split(':', 1)
        name = name_part.strip()
        followers = [f.strip() for f in follower_part.strip().split(' ') if f.strip()]

        yield (name, 0)
        for follower in followers:
            yield (follower, 1)

    def combiner(self, follower, counts):
        yield (follower, sum(counts))

    def reducer(self, follower, counts):
        yield (None, (follower, sum(counts)))

    def reducer2(self, _, follow_counts):
        max_followers = (None, 0)
        total = 0
        no_followers = 0
        users = 0

        for (user_id, count) in follow_counts:
            users += 1
            total += count
            if count == 0:
                no_followers += 1
            if count > max_followers[1]:
                max_followers = (user_id, count)

        yield ("Most follows", max_followers)
        yield ("Average follows per account", total / users)
        yield ("Accounts with no follows", no_followers)

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   combiner=self.combiner,
                   reducer=self.reducer),
            MRStep(reducer=self.reducer2)
        ]

if __name__ == '__main__':
    MRJobTwitterFollowers.run()