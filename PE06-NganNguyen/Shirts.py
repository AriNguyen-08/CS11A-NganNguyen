def make_shirt(size, message):        # Define a function that accepts shirt size and message
    print(f"The shirt is size {size} and has the message '{message}' printed on it.")   # Print a sentence describing the shirt
make_shirt("Medium", "Stay Positive") # Call the function using positional arguments
make_shirt(size="Large", message="Dream Big") # Call the function using keyword arguments

def make_shirt(size="Large", message="I love Python"):    # Define a function with default size and message
    print(f"The shirt is size {size} and has the message '{message}' printed on it.")  # Print the shirt size and message
make_shirt()            # Make a large shirt with the default message
make_shirt(size="Medium")      # Make a medium shirt with the default message
make_shirt(size="Small", message="Stay Healthy")  # Make a small shirt with a different message
