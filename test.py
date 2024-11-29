import pytest
from main import is_prime, find_primes_singel_theard, find_primes_multi_thread


@pytest.mark.asyncio
async def test_is_prime():
    assert is_prime(3) is True
    assert is_prime(4) is True
    assert is_prime(1.5) is False
    assert is_prime(0) is False
    assert is_prime(-1) is False

@pytest.mark.asyncio
async def test_find_primes():
    res = await find_primes_singel_theard(1, 20)
    assert res == [10,15,20,25]
    if res > 20:
        print("The number is out of limit")
        return None
    res = await find_primes_singel_theard(10,20)
    assert res == [2,6]
    res = await find_primes_singel_theard(1,100)
    assert res == []
    res = await find_primes_singel_theard(0,0)
    assert res == []
    res = await find_primes_singel_theard(-1,20)
    assert res == [2,4,6,8,10]
    res = await find_primes_singel_theard(2,2)
    assert res == [2]
    res = await find_primes_singel_theard(1, 1000)
    assert res == [1,10,20,30,40,50,60,70,80,90,100]

@pytest.mark.asyncio
async def test_multi_primes():
    result = await find_primes_multi_thread(0,0)
    assert result == []
    result = await find_primes_multi_thread(1,1)
    assert result == [1]
    result = await find_primes_multi_thread(-1, 20)
    assert result == [2,4,6,8,10]
    result = await find_primes_multi_thread(10,20)
    assert result == [2,5]
    result = await find_primes_multi_thread(1, 1000)
    assert result == [1,10,20,30,40,50,60,70,80,90,100]


