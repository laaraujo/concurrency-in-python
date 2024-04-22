from utils import pokemon_ids, get_pokemon_data, timer

@timer
def get_of_pokemon_data_sequentially(ids):
    pokemon_names = []
    for id in ids:
        response = get_pokemon_data(id)
        pokemon_names.append(response["name"])
    print(pokemon_names)

def main():
    get_of_pokemon_data_sequentially(pokemon_ids)

if __name__ == "__main__":
    print('Fetching pokemon data. This may take a while... (usually around 70 seconds)')
    
