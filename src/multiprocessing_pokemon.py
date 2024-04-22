from utils import get_pokemon_data, pokemon_ids, timer
import concurrent.futures

@timer
def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        responses = executor.map(get_pokemon_data, pokemon_ids)
    pokemon_names = [r["name"] for r in responses]
    print(pokemon_names)

if __name__ == "__main__":
    print('Fetching pokemon data with multiprocessing...')
    main()
