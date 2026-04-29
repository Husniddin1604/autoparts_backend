import asyncio

from utils.http_client import get_http_client


async def decode_vin_api(vin):
    async with get_http_client() as client:
        url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValuesExtended/{vin}?format=json"
        response = await client.get(url)
        data = response.json()

        # Извлечение нужных параметров (например, Make, Model, ModelYear)
        results = data['Results']
        print(results)
        # for item in results:
        #     if item['Value'] and item['Variable'] in ['Make', 'Model', 'Model Year']:
        #         print(f"{item['Variable']}: {item['Value']}")


# Пример использования
asyncio.run(decode_vin_api("1FALP62W4WH128703"))

