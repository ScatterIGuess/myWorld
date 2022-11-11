import time 


def run():
    a = int(input("Enter a Number: ")) 
    b = int(input("Enter a Number: ")) 
    print(f"Sum: {sum([a,b])}")
    
def sum(a):
    result = 0
    for v in a:
        result += v
    return result


if __name__ == "__main__":
    startTime = time.time()
    run()
    print(f"Time Taken: {int(time.time()-startTime)} ms")
