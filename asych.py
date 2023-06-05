import asyncio
import time
import aiohttp
import os

api_key_one = os.environ.get('API_KEY_ONE')
api_key_two = os.environ.get('API_KEY_TWO')
api_key_three = os.environ.get('API_KEY_THREE')


async def count1(session):
    print('temp1')
    resp = await session.get(f'https://api.weatherbit.io/v2.0/current?lat=45.34&lon=28.84&key={api_key_one}&include=minutely')
    json_data = await resp.json()
    return json_data["data"][0]["temp"]


async def count2(session):
    print('temp2')
    resp = await session.get(f'https://api.weatherapi.com/v1/current.json?key={api_key_two}&q=45.34,28.84')
    json_data = await resp.json()
    temperature = json_data["current"]["temp_c"]
    return float(temperature)


async def count3(session):
    print('temp3')
    resp = await session.get(f'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={api_key_three}')
    json_data = await resp.json()
    temperature_kelvin = json_data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15
    return temperature_celsius


async def main():
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(count1(session), count2(session), count3(session))
        avg_temp = sum(result)/3
        print(result)
        print(f'Average temperature of Izmail {avg_temp}')


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f'{__file__} executed in {elapsed:0.2f} seconds.')
