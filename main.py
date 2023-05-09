import asyncio
from aiohttp_ip_rotator import RotatingClientSession



async def main():
    f = open('sites.txt', "r")
    sites = f.read().split()

    
    async with RotatingClientSession(
        "http://web.archive.org",
        "AKIAZ77KOHU3FBNF2XT7",
        "aG7HwcOTdKV3mOAPC6oTMUvntBEgPCgntMC4SRpc"
    ) as session:
      
        for site in sites:
            response = await session.get('http://web.archive.org/cdx/search/cdx?url={}&matchType=prefix&filter=statuscode:200&filter=mimetype:text/html'.format(site))
            #print(f"Your ip: {await response.text()}")
            f = open(f"{site}.txt", "a")
            f.write(await response.text())
            f.close()

        

if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
