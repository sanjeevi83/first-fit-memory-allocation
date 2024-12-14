# First Fit Memory Allocation

This project demonstrates the First Fit Memory Allocation Algorithm using Python. The algorithm dynamically assigns memory blocks to processes based on their sizes, ensuring efficient use of resources.

## Features:
- Implements the **First Fit Memory Allocation Algorithm**.
- Dynamically allocates memory blocks to processes.
- Command-line interface (CLI) for user interaction.
- Displays detailed allocation results and the final memory state.

## How to Use:
1. Clone the repository:
   git clone https://github.com/sanjeevi83/first-fit-memory-allocation.git

2. Navigate to the project directory:
   cd first-fit-memory-allocation

3. Run the program
   python first_fit_allocation.py

4. Enter memory block sizes and process sizes as prompted in the terminal.

   Example Execution:
     # Input:
     Memory Blocks: 200 300 500 100 50
     Processes: 190,450,90

   
    # Output:
 
    Allocating Processes...
    Process A: Allocated 190 KB in Block 1.
    Process B: Allocated 450 KB in Block 3.
    Process C: Allocated 90 KB in Block 2.
    
    Final Memory State:
    Block 1: 10KB - Free
    Block 2: 210KB - Free
    Block 3: 50KB - Free
    Block 4: 100KB - Free
    Block 5: 50KB - Free


# Benefits:
    1. Easy to Understand: Simplifies the concept of memory allocation.
    2. Interactive: Allows users to input custom memory and process sizes.
    3. Educational Tool: Ideal for students learning dynamic memory management.

# Project Structure:
first_fit_allocation.py: The main Python script implementing the algorithm.

       
