Doing parallel programming in Python can have many different forms. Here the two main programming models we have for parallel programming.
## Data Parallelism
Data parallelism means that the same operation is applied to different pieces of data in parallel. These are usually synchronous computations, where parallelization is proportional to input  
data size and load balancing is easy.
### SIMD Programming
The concept of SIMD is introduced [[Parallel Computing#Parallelism in Computer Architecture|here]]. SIMD programming is the implementation of this concept. It is a practical programming model enabled through vector extensions. 

Vector extensions means that instead of single scalars, we can save elements in vector registers, so that one instruction can operate on all elements in parallel. We can, for example, store eight 8-bit elements in one register and perform element-wise addition with another register in a single instruction. The main improvement over the years was the length of the vector registers, which keeps increasing.

A lane in the context of SIMD programming is another name for the slot the elements get saved in within a vector register. We execute the instructions on each line over many registers.

The fundamental datatypes of Python are very much incompatible with vector extensions (int, list, dictionary, ...). This contributes to the inefficiency of Python code. However libraries like NumPy are usually optimized to enable vector extensions.
### CUDA Programming
SIMD programming leverages the advantages of vector extensions in CPUs. CUDA programming on the other hand leverages the massively parallel architecture of GPUs.

One example how this is enabled, is that instead of a loop (like we would do in "normal programming", we spawn a horde of threads, one thread per each element. Unfortunately these threads are not the same as I discussed here: [[Parallel Computing]], but are more like lanes in SIMD programming. These threads then execute in an unspecified order. If the code is properly parallelizable, this is super efficient. 

One way to make use of GPUs through Python is to use *CuPy*. CuPy is essentially a GPU version of NumPy  In most ordinary cases, one just needs to replace numpy.ndarray classes with cupy.ndarray classes; there is an analog of almost all functions in CuPy.

**BLAS**
BLAS is a standard API for low-level linear algebra routines (e.g., vector/matrix operations) that is Implemented in CPU-optimized libraries like Intel MKL, OpenBLAS, AOCL. The equivalent for GPU-optimized routines is called cuBLAS.
=> Just like CuPy delegates linear algebra to cuBLAS on GPUs, NumPy delegates to BLAS libraries on CPUs.
## Task Parallelism
Task parallelism means that different tasks or operations are run in parallel. Here we have asynchronous computation, where parallelization is proportional to the number of tasks and load balancing may be difficult, because tasks may to very different things. 
### Multithreading/Multiprocessing
Parallel computing in Python in the easiest sense can be done with the *Pool* module from the *multiprocessing* library. An example of this can be found here: [[Easy Parallelization in Python.py]]. The Pool module spawns a process for each defined worker and has an easy, but restrictive predefined interface. 

If we want more flexibility, we can work with queues. With queues we can define the different processes of the parallel computing architecture more freely. An example of how this could look can be found here: [[Advanced Parallelization in Python.py]].
### MapReduce Programming
When doing parallel programming it is important to follow certain principles so that parallelization can be done correctly and without faults. Just like in object-oriented programming, we want to use inheritance, in parallel computing, we want to use MapReduce Programming. More on that here: [[MapReduce Programming]].
### Spark
Apache Spark is a general-purpose engine for large-scale data processing. Unlike MapReduce it is not a programming paradigm but Spark also includes the MapReduce idea. More on Spark here [[Spark]].