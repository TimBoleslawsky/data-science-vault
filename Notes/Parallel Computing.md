Parallel computing is at the core of modern big data solutions. It enables us to tackle the challenges of the modern world. In this note I will discuss the basic theory behind parallel computing. 

We can think of parallel computing as the concept, and parallel programming as how to implement that concept. Tools like Pool(), MapReduce, and Spark are different ways to do parallel programming. More on this here [[Parallel Programming in Python]].
## Concurrency vs. Parallelism
Parallelism and concurrency are both important concepts in computing. Concurrency is when multiple tasks are in progress at the same time but not necessarily _executing_ at the same instant. We do this to improve responsiveness, like when using a browser and a text editor at the same time. Parallelism is when multiple tasks are executed _simultaneously_. We do this to improve performance. 
### Different Types of Parallelism
Parallelism can be done on different levels of hardware or software. These are the concepts used in computer architecture:
1. Bit-Level Parallelism: This just means using more bits to do more things at the same time (64bit operations). This is controlled by hardware.
2. ILP – Instruction-Level Parallelism: Executing multiple instructions via for example *pipelining.* Pipelining is the splitting of instructions into multiple stages and then running different stages of these instructions parallel. This is also controlled by hardware. 
3. DLP – Data-Level Parallelism: Happens when the same operation is applied to multiple data elements within a data set. 
4. TLP – Thread-Level Parallelism: Running different threads in parallel, essentially, independent CPUs that share the same main memory. This can be implemented by using multithreading or multiprocessing. 
5. RLP – Request-Level Parallelism: Handling independent external requests through asynchronous or multi-threaded request handling.

To implement the different levels of parallelism in code, we typically rely on two main programming models:
- [[Parallel Programming in Python#Data Parallelism|Data Parallelism]], meaning, same operation applied to different pieces of data, for DLP.
- [[Parallel Programming in Python#Task Parallelism|Task Parallelism]], meaning, different tasks or operations running in parallel, for TLP/RLP.
## Parallelism in Computer Architecture
Flynn’s Taxonomy is a classification system for computer architectures. It categorizes systems based on the number of concurrent **instruction streams** and **data streams** they support.
- SISD – Single Instruction, Single Data:
	- **Meaning**: One instruction stream processes one data stream.
	- **Type**: Traditional, sequential computers.
	- **Example**: A basic single-core CPU.
	- **Execution**: Only one operation at a time.
- SIMD – Single Instruction, Multiple Data
	- **Meaning**: One instruction operates on multiple data points simultaneously.
	- **Type**: Data-level parallelism.
	- **Example**: GPUs, vector processors.
	- **Use case**: Image processing, matrix operations, scientific simulations.
- MISD – Multiple Instruction, Single Data => Rare and mostly theoretical.
- MIMD – Multiple Instruction, Multiple Data
	- **Meaning**: Multiple instruction streams operate on multiple data streams.
	- **Type**: Task-level parallelism.
	- **Example**: Multi-core processors, distributed systems.
	- **Use case**: Modern CPUs, cloud computing, parallel applications.
### **Symmetric Multiprocessing (SMP) Systems**
Symmetric Multiprocessing (SMP) or shared-memory systems are an implementation of MIMD systems. SMP is a type of computer architecture where two or more processors/cores share the same memory and OS and are treated equally (symmetric). All processors have equal access to I/O devices and can perform any task. This system architecture is the standard for modern computing.

Having said that, there can occur problems in SMP systems. Most common are these two:
- Updating shared variables can create *race conditions*. This just means that some update is overwritten by a concurring thread.
	- Some ways to solve this include atomic read-write operations (each write operation is fully finished before the next can start), or mutual exclusion (mutex) locks of threads but this can lead to deadlocks.
- Another problem is *cache coherence*. Most cores have a local copy of the data. How can we make sure this is always the same for each core?
## Processes, Threads, and Pools
Processes, threads, and pools are the core components when talking about parallel computing. Processes are independent units of execution with their own memory space. They essentially correspond to "a program in execution".  Processes contain a number of threads. Threads are a sequence of instructions within an execution. Threads within a process share memory. 
=> **Multithreading**: Using multiple threads within the same process to perform tasks *concurrently*. (Can be done on multiple cores, then it is parallelism! But this is not possible in Python, see below!)
=> **Multiprocessing**: Using multiple processes, each with its own memory space, to perform tasks in *parallel.

Python specific note: Python uses a global interpreter lock or GIL. GIL is a mutex lock that enforces synchronization by allowing only one thread to modify the assets of the Python interpreter (such as reading or writing variables) at one time. The implication of this is that using multithreading in Python is essentially useless for speedup: since only one thread can execute at a time, multithreaded code is concurrent but not parallel, and no speedup is to be expected. In Python multithreading is only useful for I/O-bound code. Instead, multiprocessing must be used.

Pools are collections of resources that are kept in memory to be used on need. In general these resources could be memory, threads, or processes. In Python we can use pools to do multiprocessing. Here is a simple example:

``` python
if __name__ == '__main__':
    n = 1_000_000
    w = 4  # Number of processes

    with Pool(w) as p:
        ms = p.map(sample, [n // w] * w)  # Split the workload evenly

    total_in_circle = sum(ms)
    print(4 * total_in_circle / n)
```

Pool() creates a pool of $w$ worker processes (separate Python processes). Each process runs in parallel on its own CPU core (if available). The Pool() function automatically does a few things for us: 
- Manages a fixed number of worker processes. 
- Distributes tasks (like calling sample() function) across those workers. 
- Handles communication and results collection.

But we need to be careful that our function cannot create race conditions!
## Amdahl's Law
To understand Amdahl's law, we first need to introduce *speedup*. Speedup is how much faster a program runs, when we are using $N$ instead of $1$ processor. Speedup is defined as $S(n) = \frac{t_0}{t(n)}$, with $t_0$ being the runtime with $1$ processor and $t(n)$ being the runtime with $n$ processors. 

If we now divide the program into parts that make use of the additional processors and parts that do not, we get the following function for the speedup: $S(N) = \frac{1}{(1 - P) + \frac{P}{N}}$, with $P$ being the proportion of the program that can be parallelized. Important to note is, that we have an upper limit of the speedup: $S_{max} = \frac{1}{1-P}$.
## Job Schedulers
Parallel computing is commonly used in high-performance computing (HPC), data processing, and scientific simulations. Since HPC systems consist of many nodes and processors, a **job scheduler** is required to efficiently allocate resources and manage workloads. Job schedulers manage the execution of jobs (programs, scripts) on a cluster by:
- Allocating CPU/GPU resources.
- Managing job queues and priorities.
- Distributing workloads across multiple nodes.
- Handling dependencies and scheduling optimizations.

On popular job scheduler, especially in academia, is [[SLURM]].

