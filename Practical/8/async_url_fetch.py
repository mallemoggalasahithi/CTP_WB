import asyncio
import aiohttp
import time

urls = [
    "https://example.com",
    "https://www.python.org",
    "https://www.google.com"
]

async def fetch(session, url):
    for attempt in range(3):
        try:
            async with session.get(url, timeout=10) as response:
                text = await response.text()
                return url, response.status, len(text)
        except Exception:
            if attempt == 2:
                return url, "Failed", 0
            await asyncio.sleep(1)

async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *(fetch(session, url) for url in urls)
        )

    end = time.time()

    for result in results:
        print(result)

    print("Time taken:", round(end - start, 2), "seconds")

asyncio.run(main())
