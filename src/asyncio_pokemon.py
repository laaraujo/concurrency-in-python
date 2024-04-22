import asyncio
import aiohttp
from utils import pokemon_ids, get_pokemon_data_async, async_timer

@async_timer
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.ensure_future(get_pokemon_data_async(session, id)) for id in pokemon_ids]
        responses = await asyncio.gather(*tasks)
    pokemon_names = [r["name"] for r in responses]
    print(pokemon_names)

if __name__ == "__main__":
    print('Fetching pokemon data with corroutines(asyncio)...')
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
