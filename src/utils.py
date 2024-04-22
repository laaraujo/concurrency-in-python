import functools
import time
import requests

api_url = "https://pokeapi.co/api/v2"
og_pokemon_count = 151
pokemon_ids = [n for n in range(1, og_pokemon_count+1)]

async def get_pokemon_data_async(session, id):
    url = f"{api_url}/pokemon/{id}"
    async with session.get(url) as response:
        return await response.json()

def get_pokemon_data(id):
    response = requests.get(f"{api_url}/pokemon/{id}")
    return response.json()

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        stop = time.perf_counter()
        elapsed_time = stop - start
        print(f"Finished in: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer

def async_timer(func):
    @functools.wraps(func)
    async def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = await func(*args, **kwargs)
        stop = time.perf_counter()
        elapsed_time = stop - start
        print(f"Finished in: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer
