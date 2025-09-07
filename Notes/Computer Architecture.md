Computer architecture defines how computers process and store data, execute instructions, and interact with memory and storage. While data scientists typically work at a higher level with programming languages and software, understanding the fundamentals of computer architecture can provide insight into performance bottlenecks and optimizations for computational tasks.
## **Computer Architecture Models**
Two key architectures define how computers manage instructions and data:

• **Von Neumann Architecture**: The dominant model in general-purpose computing, where instructions and data share the same memory and bus. This creates the **Von Neumann bottleneck**, where the CPU has to fetch instructions and data sequentially. Most modern computers mitigate this using caches and pipelines.

• **Harvard Architecture**: Uses separate memory for instructions and data, enabling parallel instruction and data access. This is widely used in specialized hardware like digital signal processors (DSPs) and microcontrollers but is less common in general-purpose computing.

• **Modern Adaptations**: Most modern CPUs use a **modified Von Neumann architecture** with cache hierarchies to improve performance by reducing memory access delays.
## **How Computers Execute Programs**
Computers transform high-level code into machine-executable instructions through multiple layers of processing:

1. **Compilation & Interpretation**: Programs are written in high-level humanly readable languages also called assembly languages. These programs are either: 
   - compiled, meaning the entire source code is turned into machine code (binary) before running the program
   - interpreted, meaning we execute the program line-by-line, translating each part on the fly during runtime.
	 Python executes the code by compiling the code into bytecode and using the Python Virtual Machine (PVM) to interpret the bytecode line by line as machine code. This is a hybrid between compilation and interpretation.

1. **Instruction Set Architecture (ISA)**: Defines the fundamental operations a CPU can perform, such as x86 (Intel, AMD) and ARM (mobile, embedded systems). ISAs determine for example instructions, data types, registers, how memory is accessed, and so on. We usually have three types of instructions in a ISA: Data transfer instructions (loading, copying storing data), Control flow instructions (comparisons, branches), Arithmetic and logical instructions. 

2. **Arithmetic Logic Unit (ALU)**: - The ALU performs the arithmetic and logical operations or the “math” of the instructions defined by the ISA and is located in the CPU. Here is how that works in the **datapath** of the CPU: 
   => Imagine executing ADD R1, R2, R3 (i.e., add contents of R2 and R3, store in R1):
   - **Control Unit** decodes the ADD instruction.
   - It signals:
	 - **Registers** R2 and R3 to send data to ALU
	 - ALU to perform ADD Result to be stored in R1

The CPU relies on **registers**, small but ultra-fast storage locations, to temporarily hold data for processing. The registers are part of a larger memory hierarchy which is further explained here: [[Memory Hierarchy]]. 
