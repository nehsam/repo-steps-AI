import requests
import asyncio
import aiohttp

# Synchronous Function
def fetch_data_sync(url):
    print(f"Fetching (Sync) data from: {url}")
    response = requests.get(url)
    print(f"Response (Sync) from {url}: {response.status_code}")

# Asynchronous Function
async def fetch_data_async(url):
    print(f"Fetching (Async) data from: {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Response (Async) from {url}: {response.status}")

# Main Function
def main():
    # URLs for testing
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2"
    ]

    # Synchronous Execution
    print("\n--- Synchronous Execution ---")
    for url in urls:
        fetch_data_sync(url)

    # Asynchronous Execution
    print("\n--- Asynchronous Execution ---")
    asyncio.run(async_main(urls))

# Async Main for gathering tasks
async def async_main(urls):
    tasks = [fetch_data_async(url) for url in urls]
    await asyncio.gather(*tasks)

# Entry Point
if __name__ == "__main__":
    main()
