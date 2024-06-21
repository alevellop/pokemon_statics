import logging
from functools import lru_cache
import aiohttp

BASE_URL = "https://pokeapi.co/api/v2/"

@lru_cache(maxsize=100)
async def cached_request(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return data
        else:
            raise Exception(f'Error: {response.reason}, status: {response.status}')

async def get_pokemon_urls():
    url = f'{BASE_URL}pokemon?limit=100'
    async with aiohttp.ClientSession() as session:
        data = await cached_request(session, url)
        logging.info('Getting 100 urls of pokemons.')
        return [pokemon['url'] for pokemon in data['results']]

async def get_pokemon_data(pokemon_url):
    async with aiohttp.ClientSession() as session:
        data = await cached_request(session, pokemon_url)
        pokemon = {
            'id':   data['id'],
            'name': data['name'],
            'base_experience': data['base_experience'],
            'height': data['height'],
            'weight': data['weight']
        }
        species_url = data['species']['url']
        logging.info(f"Getting data of pokemon '{pokemon['name']}'.")
        return pokemon, species_url

async def get_egg_group_by_specie(species_url):
    async with aiohttp.ClientSession() as session:
        data = await cached_request(session, species_url)
        groups_list = [egg_group['name'] for egg_group in data['egg_groups']]
        logging.info(f"Getting egg_groups of specie '{species_url}'.")
        return groups_list

async def get_egg_groups_urls():
    url = f'{BASE_URL}egg-group/'
    async with aiohttp.ClientSession() as session:
        data = await cached_request(session, url)
        logging.info(f"Getting urls of egg_groups.")
        return [egg_group['url'] for egg_group in data['results']]