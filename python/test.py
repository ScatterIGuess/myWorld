import time 


def run():
    nums=[]
    while True:
        a = input("Enter a Number: ")
        try:
            nums.append(int(a))
        except:
            break
    print(f"Sum: {sum(nums)}")
    
def sum(a):
    result = 0
    for v in a:
        result += v
    return result


if __name__ == "__main__":
    startTime = time.time()
    run()
    print(f"Time Taken: {int((time.time()-startTime)*1000)} ms")
