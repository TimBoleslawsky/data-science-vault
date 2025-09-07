SLURM (Simple Linux Utility for Resource Management) is a widely used open-source job scheduler designed for HPC clusters. It enables [[Parallel Computing]] by allowing users to:
- Submit jobs to queues.
- Request resources (CPUs, GPUs, memory, time limits).
- Distribute parallel jobs efficiently.
- Monitor and manage running jobs.

SLURM is particularly efficient for large-scale parallel computing, as it can handle thousands of nodes and optimize resource allocation.
## SLURM Entities
Here are the most important entities that allow SLURM to execute parallel computing:
- Compute **nodes** are the physical computers that together constitute the compute **cluster**.  
- Each node has a finite amount of **resources** that can be used at a certain point in time (CPU cores, RAM, GPUs). 
- Nodes are divided into (possibly overlapping) **partitions** that are designed to accommodate different kinds of jobs. For example short/long partitions.  
- A job is a request by the user for a certain number of resources to be used for executing a **program** that they have written.
- The jobs are placed into a **queue** for the partition and are executed when a sufficient amount of resources are free for a sufficiently long time. => This is known as *batch processing*: a job can potentially include multiple computations that are executed in an unknown point in time in the future, and the user then gets results when they are finished.
## Sbatch Scripts
The files submitted through sbatch are shell scripts that contain special comments  
that begin with `#SBATCH`. These comments are ignored when executed, but they control resource allocation. Example:

``` sh
#! /bin/bash

#SBATCH -c 1 (Request only one CPU core)
#SBATCH ---mem=1G (Request 1 GB of RAM)

source ~/miniforge3/bin/activate

python3 myscript.py
```