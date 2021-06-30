import os
import time

def only_try():
    try:
        f = open("try_file", "w")

        for i in range(3000000):
            f.write(str(i))

        f.close()
    except:
        print("open error")
    finally:
        os.remove("try_file")

def try_else():
    try:
        f = open("try_else_file", "w")
    except:
        print("open error")
    else:
        for i in range(3000000):
            f.write(str(i))

        f.close()
    finally:
        os.remove("try_else_file")

def check_runtime(func):
    accumulate_time = 0
    for i in range(10):
        start = time.time()
        func()
        accumulate_time += (time.time() - start)

    print("Runtime : {}".format(str(accumulate_time)))

if __name__ == "__main__":
    print("Only try performance")
    check_runtime(only_try)

    print("try else performance")
    check_runtime(try_else)
