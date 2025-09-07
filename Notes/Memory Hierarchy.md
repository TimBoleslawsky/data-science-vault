Here are the main levels of the memory hierarchy: 
1. **Registers** (fastest, smallest); Latency is less than 1ns. 
2. **Cache Memory** (L1, L2, L3) stores frequently accessed data to reduce RAM access time; Latency is 1ns for L1 Cache, 3-10ns for L2 Cache, and 10-20ns for L3 Cache.
3. **RAM** (main memory) holds active program data but is slower than cache; Latency is 50-100ns. 
4. **Storage (SSD/HDD)** provides persistent data storage but is significantly slower; Latency is 100-200 μs for Flash disks (SSD) and 5-10 ms for hard disks (HDD). 
=> General rule of thumb is that the latency grows by an order of magnitude per level (even more so for disk storage).

A comment on virtual memory: Virtual memory is a memory management technique used by modern operating systems and CPUs to give each process its own isolated view of memory, even if they all share the same physical hardware. This means we have a virtual address (what the program sees) and a physical address (the actual location in RAM). Usually memory is divided into fixed-size blocks called pages and a page table maps the virtual pages to physical memory. 
## Latency vs. Bandwidth
When talking about computer memory, we usually have a trade-off between latency and bandwidth. Latency refers to the time between initiating a request for data and until the data has been retrieved. Bandwidth or throughput is the maximum rate of data transfer: how many units of data can we at most transfer over a unit of time on average.  

A technology with very high bandwidth can come with the expense of having very high latency, that is, it can take a very long time until the first piece of data is available even if the overall transfer rate can be high. Conversely, the latency can be very small, but the amount of bandwidth can be limited, e.g., because of having to initiate a lot of requests or the channel is simply too narrow to allow for high bandwidth. 
=> Note: This does not always apply, it depends on the context whether this is the case.
## Memory Management in Python
Traditional arrays are of fixed length and of fixed type, meaning all elements are of the same type. This is highly efficient, because we use contiguous memory and no type checking at runtime.

Python lists can contain arbitrary objects: numbers, strings, other lists, sets, dictionaries, modules, functions, ... These lists can shrink and grow dynamically making them NOT arrays! They store pointers to objects, which makes them very flexible, but also very inefficient for high-performance applications. 

One way to mitigate this are NumPy arrays. NumPy arrays have a fixed type (in this case, 64-bit floating-point numbers) and expose memory directly through the C interface. Another way to mitigate this is by using the multiprocessing module and allocate memory by creating an Array within this module. This not only creates a "real" array, but also lets us share memory between processes. 
## Registers
CPUs have a limited number of registers (register file). These registers are the fastest kind of memory available for a CPU and are used for individual computations. Registers have a fixed width, usually corresponding to the word length (usually 64bit). 

The registers available to a CPU are: A general-purpose registers (for arithmetic operations).
Depending on the architecture, there may be a number of special-purpose registers. Usually, there is a register **called instruction pointer (IP)** or **program counter (PC)** that holds the address of the next instruction to be executed.

There may be vector registers, such as the 128-bit SSE registers (XMM registers) on x86  
architectures to enable [[Parallel Programming in Python#Data Parallelism|data parallelism]].
## Cache
In the past, CPU and RAM operated at similar speeds but, since the 1980s, CPU speeds have increased dramatically, but RAM access latency has not kept up. Modern CPUs can execute many instructions in the time it takes to access one value from RAM. This is why we need Cache Memory. 

Cache is a **small, fast memory** (usually built from SRAM) located **close to or inside the CPU**. It stores **copies of frequently accessed data** from main memory (RAM). By accessing the cache instead of RAM, the CPU avoids long delays. Modern systems use **multiple levels of cache**:
- **L1** (smallest, fastest, closest to CPU core)
- **L2**
- **L3** (larger, slower, often shared between cores)

Cache is organized in a way that takes advantage of two things. First **temporal locality**, means that recently accessed data is likely to be accessed again soon. Second, **spatial locality**, means that nearby memory addresses are likely to be accessed soon. Cache is copied to and from at cache line length. Copying larger amounts of memory increases efficiency as it exploits spatial locality.

Another issue we have to deal with in multi-core systems is cache coherency. What if another core modifies the memory in its cache? How do we ensure that all CPUs see the same state  
of memory? => In practice, the writes need to **invalidate cache lines** in other CPUs’ cache or **force an update** of the content. 

Whenever a memory address is requested, it is first probed whether a copy is stored in the  
cache, and if so, it is retrieved from there (a **cache hit** occurs). If not, then a **cache miss** occurs, and the corresponding cache line is first copied from main memory to cache. We differentiate between different kinds of cache misses: 
- Compulsory miss occurs when an address is first read (it cannot reside in cache before)  
- Capacity miss occurs if the cache has become full and the line has had to be evicted from the cache  
- Conflict miss occurs if the cache placement policy has caused the line to be evicted from the cache  
- Coherence miss occurs if, to maintain cache coherence, a write in another core has invalidated the cache line  

Cache placement policies decide, where each line can go in the cache. We need these, because cache only contains space for a limited number of cache lines. We differentiate between:
- Fully-associative cache: the line can go anywhere in the cache  
- Direct-mapped cache: there is exactly one location where the line can go  
- Set associative cache: there is a set of possible locations where the line can go  
- n-way set associative cache: there is exactly n possible locations for each line that they can go to  

Since the cache has limited space, adding new lines into the cache means that some old line necessarily has to be evicted. Common simple policies:  
- Random: a random line is evicted  
- Least Recently Used (LRU): keep track of the reads of the lines and evict the one that has had the most cycles since it was last accessed.
- First-In, First-Out (FIFO): evict lines by the order they were added into the cache  
=> Modern CPUs tend to have complicated cache replacement policies, such as pseudo-LRU where an approximate information of accesses is maintained, and other more advanced adaptive strategies.

We also have different strategies when it comes to writing into memory with cache. They are divided into strategies on a cache hit and strategies on a cache miss:
On Cache Hit:
- Write-Through: Write to cache and RAM simultaneously, usually with *No-Write Allocate*.
- Write-Back: Write only to cache; update RAM later (on eviction), usually with *Write Allocate*.
On Cache Miss: 
- Write Allocate: Load data into cache on miss, then write. 
- No-Write Allocate: Write directly to RAM, skip cache.
## Random Access Memory
RAM is the volatile and smaller, but faster equivalent to mass storage like HDDs and SSDs. 
## Mass Storage
Mass storage is the storage of large amounts of data in a persistent fashion. Mass storage is often more cost effective than smaller memory but also often slower to access, by several orders of magnitude.
### Hard Disk Drives
HDDs are very large means of storing data at great GB/buck value. The main draw back for using HDDs, besides them being slow, is their unreliability. It is estimated, that HDDs have a 1.7–8.6% annualized failure rate. This emphasizes the need for replication and backups. 
=> Efficient accesses to hard disk are sequential, not random, and sufficiently large!
#### Redundant Array of Independent Disks
Redundant Array of Independent Disks (RAID) is a technology that can be used to improve speed and/or reliability of hard disks. That being said, RAID requires a lot of expensive hardware. Therefore, RAID is suited for expensive servers that need upmost reliability (or increased performance), but the disks still fail and need to be replaced. Important: RAID array does not constitute backup!

Here are some common RAID architectures: 
- RAID 0: Data is split (“striped”) across multiple disks => Good performance, bad fault tolerance. 
- RAID 1: Data is duplicated on two or more disks. => Good fault tolerance, bad read and memory efficiency. 
- RAID 01: Data is duplicated, and the mirrors are then striped. => Not common today. 
- RAID 5: Data and recovery information is striped across at least 3 disks. => Can survive one disk failure, compromise between RAID 0 and RAID 1. 
- RAID 6: Like RAID 5, but stores two parity blocks. => Can survive two disk failure, slower write than RAID 5. 
### Flash Memory
Flash memory is non-volatile semiconductor memory that is suitable for applications where memory is read often and written less often. A popular application for flash memory are Solid-Sate Drives or SSDs. 

SSDs are the main competitor to HDDs because they offer much smaller latency and can be plugged in like HDDs. Historically the advantage of HDDs was their size, but SSDs are catching up. 

Just like with HDDs reliability is an issue with SSDs. SSDs have an annualized failure rate of around 0.9%, which is better than HDDs but still not great. Also data on SDDs can only be erased a finite number of times, which is why data is often retained instead of erase, which could cause security concerns. 

=> SSDs have much more efficient random accesses than hard disks because they  
lack moving components. However, accessing lots of small blocks can be inefficient, so sequential accesses are still advised.

