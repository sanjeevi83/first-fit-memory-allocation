def first_fit(memory_blocks, process_sizes):

    allocation = [-1] * len(process_sizes)  # Initialize allocation array
    for i, process in enumerate(process_sizes):  # Iterate through each process
        for j, block in enumerate(memory_blocks):  # Check each memory block
            if block >= process:  # If the block can accommodate the process
                allocation[i] = j  # Allocate the block to the process
                memory_blocks[j] -= process  # Update the block size
                break  # Move to the next process
    return allocation

def get_input():

    memory_blocks = list(map(int, input("Enter memory block sizes (space-separated): ").split()))
    process_sizes = list(map(int, input("Enter process sizes (comma-separated): ").split(',')))
    return memory_blocks, process_sizes

def print_allocation_results(allocation, process_sizes):

    print("\nAllocating Processes...")
    for i, process in enumerate(process_sizes):
        if allocation[i] != -1:
            print(f"Process {chr(65 + i)}: Allocated {process} KB in Block {allocation[i] + 1}.")
        else:
            print(f"Process {chr(65 + i)}: Not Allocated.")

def print_memory_state(memory_blocks):
 
    print("\nFinal Memory State:")
    for i, block in enumerate(memory_blocks):
        status = "Free" if block > 0 else "Allocated"
        print(f"Block {i + 1}: {block}KB - {status}")


 # Main Execution
if __name__ == "__main__":
    memory_blocks, process_sizes = get_input()  # Get user input for memory and processes
    allocation = first_fit(memory_blocks, process_sizes)  # Perform First Fit allocation
    print_allocation_results(allocation, process_sizes)  # Output allocation results
    print_memory_state(memory_blocks)  # Display final memory state





    