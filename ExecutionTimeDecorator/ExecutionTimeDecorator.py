import time

def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

if __name__ == '__main__':

    #Tests:
    @time_execution
    def my_func1():
        time.sleep(2)
        return "Function 1 complete"

    @time_execution
    def my_func2():
        time.sleep(5)
        return "Function 2 complete"

    print(my_func1())
    print(my_func2())