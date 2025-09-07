#!/usr/bin/env python3
import time
import argparse
import findspark
findspark.init()
from pyspark import SparkContext

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compute Twitter followers.')
    parser.add_argument('-w', '--num-workers', default=1, type=int, help='Number of workers')
    parser.add_argument('filename', type=str, help='Input filename')

    args = parser.parse_args()
    start = time.time()

    sc = SparkContext(master=f'local[{args.num_workers}]')
    lines = sc.textFile(args.filename)

    # Parse (user, follows_count)
    follows = lines.map(lambda line: line.strip().split(":")) \
                   .map(lambda parts: (parts[0], [f for f in parts[1].split() if f.strip()]))

    # Parse (user, followers_count)
    followers = follows.flatMap(lambda x: [(f, 1) for f in x[1]])
    followers_count = followers.reduceByKey(lambda a, b: a + b)

    # Include users with no followers
    all_users = follows.map(lambda x: (x[0], 0)).distinct()
    combined = all_users.union(followers_count)
    combined_follower_counts = combined.reduceByKey(lambda a, b: a + b)

    # Now, calculate the results
    max_followers = combined_follower_counts.takeOrdered(1, key=lambda x: -x[1])[0]
    total_followers = combined_follower_counts.map(lambda x: x[1]).sum()
    total_users = combined_follower_counts.count()
    users_with_no_followers = combined_follower_counts.filter(lambda x: x[1] == 0).count()
    avg_followers = total_followers / total_users if total_users else 0

    end = time.time()

    print(f"user_with_most_followers: [{max_followers[0]}, {max_followers[1]}]")
    print(f"average_followers: {avg_followers:.2f}")
    print(f"users_with_no_followers: {users_with_no_followers}")
    print(f"num workers: {args.num_workers}")
    print(f"total time: {end - start:.2f}")