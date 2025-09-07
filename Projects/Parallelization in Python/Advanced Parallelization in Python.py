import os
import argparse
import sys
import time
import multiprocessing as mp
from collections import defaultdict

def get_filenames(path):
    """
    A generator function: Iterates through all .txt files in the path and
    returns the full names of the files

    Parameters:
    - path : string, path to walk through

    Yields:
    The full filenames of all files ending in .txt
    """
    for (root, dirs, files) in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                yield os.path.join(root, file)

def get_file(path):
    """
    Reads the content of the file and returns it as a string.

    Parameters:
    - path : string, path to a file

    Return value:
    The content of the file in a string.
    """
    with open(path,'r') as f:
        return f.read()

def count_words_in_file(filename_queue, wordcount_queue, batch_size):
    """
    Counts the number of occurrences of words in the file
    Performs counting until a None is encountered in the queue
    Counts are stored in wordcount_queue
    Whitespace is ignored

    Parameters:
    - filename_queue, multiprocessing queue :  will contain filenames and None as a sentinel to indicate end of input
    - wordcount_queue, multiprocessing queue : (word,count) dictionaries are put in the queue, and end of input is indicated with a None
    - batch_size, int : size of batches to process

    Returns: None
    """
    while True:
        size = 0
        counts = defaultdict(int)
        
        while size < batch_size:
            file = filename_queue.get()
            if file is None:
                if counts:
                    wordcount_queue.put(counts) 
                wordcount_queue.put(None)
                return

            content = get_file(file)
            for word in content.split():
                counts[word] += 1
            size += 1

        if counts:
            wordcount_queue.put(counts)


def get_top10(counts):
    """
    Determines the 10 words with the most occurrences.
    Ties can be solved arbitrarily.

    Parameters:
    - counts, dictionary : a mapping from words (str) to counts (int)
    
    Return value:
    A list of (count,word) pairs (int,str)
    """
    sorted_counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)
    top10 = []

    for i in range(min(len(sorted_counts), 10)):
        top10.append((sorted_counts[i][1],sorted_counts[i][0]))

    return top10

def merge_counts(out_queue, wordcount_queue, num_workers):
    """
    Merges the counts from the queue into the shared dict global_counts. 
    Quits when num_workers Nones have been encountered.

    Parameters:
    - out_queue: queue to put the final results (checksum and top10)
    - wordcount_queue, manager queue : queue that contains (word,count) pairs and Nones to signal end of input from a worker
    - num_workers, int : number of workers (i.e., how many Nones to expect)

    Return value: None
    """
    global_counts = defaultdict(int)
    none_count = 0
    
    while none_count < num_workers:
        item = wordcount_queue.get()
        if item is None:
            none_count += 1
        else:
            for word, count in item.items():
                global_counts[word] += count
    
    checksum = compute_checksum(global_counts)
    top10 = get_top10(global_counts)
    
    out_queue.put((checksum, top10))

def compute_checksum(counts):
    """
    Computes the checksum for the counts as follows:
    The checksum is the sum of products of the length of the word and its count

    Parameters:
    - counts, dictionary : word to count dictionary

    Return value:
    The checksum (int)
    """
    checksum = 0

    for (k,v) in counts.items():
        checksum = checksum + len(k) * v
    
    return checksum

if __name__ == '__main__':
    t1 = time.time()
    parser = argparse.ArgumentParser(description='Counts words of all the text files in the given directory')
    parser.add_argument('-w', '--num-workers', help='Number of workers', default=1, type=int)
    parser.add_argument('-b', '--batch-size', help='Batch size', default=1, type=int)
    parser.add_argument('path', help='Path that contains text files')
    args = parser.parse_args()

    path = args.path

    if not os.path.isdir(path):
        sys.stderr.write(f'{sys.argv[0]}: ERROR: `{path}\' is not a valid directory!\n')
        quit(1)

    num_workers = args.num_workers
    print("workers", num_workers)
    if num_workers < 1:
        sys.stderr.write(f'{sys.argv[0]}: ERROR: Number of workers must be positive (got {num_workers})!\n')
        quit(1)

    batch_size = args.batch_size
    print("batch size", batch_size)
    if batch_size < 1:
        sys.stderr.write(f'{sys.argv[0]}: ERROR: Batch size must be positive (got {batch_size})!\n')
        quit(1)

    # Create queues
    filename_queue = mp.Queue()
    wordcount_queue = mp.Queue()
    out_queue = mp.Queue()

    # Start workers
    workers = []
    for _ in range(num_workers):
        p = mp.Process(target=count_words_in_file, 
                       args=(filename_queue, wordcount_queue, batch_size))
        p.start()
        workers.append(p)

    # Put files into filename queue
    for file in get_filenames(path):
        filename_queue.put(file)

    # Signal end of input to workers
    for _ in range(num_workers):
        filename_queue.put(None)

    # Start merger process
    merger = mp.Process(target=merge_counts,
                        args=(out_queue, wordcount_queue, num_workers))
    merger.start()

    # Wait for results
    checksum, top10 = out_queue.get()

    # Print results
    print(f"Checksum: {checksum}")
    print("Top 10 words:")
    for count, word in top10:
        print(f"{word}: {count}")

    for worker in workers:
        worker.join()
    merger.join()
    t2 = time.time()

    print("Total runtime:", t2-t1)