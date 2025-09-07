Big data is a common buzz word used to describe data that has high volume, variety, velocity, veracity, and variability. Another way to think of big data is as inconveniently big. This is because this data leads to three major issues:

1. **Computational Complexity**
   When tackling big data, we need to use linear (or near-linear) algorithms because the scale of data make quadratic operations infeasible.
   
2. **Physical Constraints**
   One assumption could be that we could just wait out this computational complexity and let the natural evolution of hardware take care of it in a few years. This assumption is based on Moore's law which says that the performance, memory, ... of integrated circuits doubles every two years. But, Like all exponential laws, Moore's law cannot be sustained indefinitely. This (and Dennard Scaling) is the reason we see a lot multi core processors today. By using parallelism we can account for the slowing down in the improvement of CPUs. But this comes with new inherent struggles because these CPUs need to be properly managed and organized.
   
3. **Storage & I/O Bottlenecks**
   Handling and storing big amounts of data is very complicated. As discussed parallelism in GPUs and CPUs can help with handling computational complexity. But keeping these computational units occupied at all times and communicating is very difficult. This is because the throughput between units is much slower than the throughput within units:
   - Latency: time delay between the cause and effect  
   - Bandwidth: throughput, the rate of data transfer or processing  
	 => GPUs have very high throughput. However, communication between GPUs (NVLink) is slow, communication between the GPU and the host (NVLink) is slower, and communication between nodes is even slower (Infiniband) => Key problem: hiding communication latency  

