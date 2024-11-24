import time

def measure_time():
    start_time = time.time() 
    
    end_time = time.time() 
    
    elapsed_time = end_time - start_time
    
    print(f"Elapsed time: {elapsed_time:.6f} seconds")
