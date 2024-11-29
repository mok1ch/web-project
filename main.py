import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

async def is_prime(n: float):
    if n % 1 == 0:
        return True
    else:
        return False

starting = time.perf_counter()
async def find_primes_singel_theard(start, end):
    try:
        lst = []
        for i in range(start,end):
            if is_prime(i):
                lst.sort()
                lst.append(i)
            await asyncio.sleep(0)
        return lst
    except TypeError:
        print('No type date')

ending = time.perf_counter()

async def main():
    start = 1
    end = 21
    lst = await find_primes_singel_theard(start, end)
    lst2 = await find_primes_multi_thread(start, end)
    print(f"Printing prime numbers {lst}")
    time.sleep(1)
    print(f"Printing prime numbers using 2 theard {lst2}")

start_time = time.perf_counter()
def hadnler_find_multi_thread(start, end):
    return asyncio.run(find_primes_singel_theard(start,end))

async def find_primes_multi_thread(start, end):
    mid = start + end / 2
    with ThreadPoolExecutor(max_workers=2) as executor:
        loop = asyncio.get_running_loop()

        theard1 = loop.run_in_executor(executor, hadnler_find_multi_thread, start, end)
        theard2 = loop.run_in_executor(executor, hadnler_find_multi_thread, mid, end)
        result1, result2 = await asyncio.gather(theard2,theard1)
        return result1,result2

end_time = time.perf_counter()
asyncio.run(main())
print(f"Time first func = {starting} - {ending}, and second func time = {start_time} - {end_time}")


# Щодо ефективности одного потоку від 2 у 1 потоці виконується швидше.
# Коли ми не вказуємо діпозон взагалі тоді викликається помилка!
