import time 


def run():
    print("Hello World")


print("Hello World")
print("Really?")


if __name__ == "__main__":
    startTime = time.time()
    run()
    print(f"Time Taken: {time.time()-startTime}")
