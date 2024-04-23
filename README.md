# Concurrency in Python

A little refresher of modern concurrency in python with a set of examples.
Each of the following scripts will fetch the first 151 pokemon names by `id` from [PokeApi](https://pokeapi.co/) and print it as a list of strings.

* [Sequential](./src/multithreading_pokemon.py)
* [Multithreading](./src/multithreading_pokemon.py)
* [Multiprocessing](./src/multiprocessing_pokemon.py)
* [Coroutines with Asyncio](./src/asyncio_pokemon.py)

## Sources and relevant info
* [asyncio](https://docs.python.org/3/library/asyncio.html)
* [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
* [threading vs multiprocessing in python](https://www.youtube.com/watch?v=AZnGRKFUU0c)
