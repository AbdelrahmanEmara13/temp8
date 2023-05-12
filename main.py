import asyncio, os
from aiohttp_ip_rotator import RotatingClientSession

def read_dir(path):

    dir_list = os.listdir(path)
    clean=[]
    for i in dir_list:
        clean.append(i.split('.txt')[0])
    return clean

dir=read_dir('./sites') 

async def main():
    f = open('sites.txt', "r")
    sites = f.read().split()

    
    async with RotatingClientSession(
        "http://web.archive.org",
        "AKIAZ77KOHU3FBNF2XT7",
        "aG7HwcOTdKV3mOAPC6oTMUvntBEgPCgntMC4SRpc"
    ) as session:
      
        for site in sites:
            if site not in dir:
                    
                try:
                        
                    response = await session.get('http://web.archive.org/cdx/search/cdx?url={}&matchType=prefix&filter=statuscode:200&filter=mimetype:text/html'.format(site))
                    if response.status== 200:
                            
                        #print(f"Your ip: {await response.text()}")
                        f = open(f"./sites/{site}.txt", "a")
                        f.write(await response.text())
                        f.close()
                except Exception as e: print(e)

        

if __name__ == "__main__":
    asyncio.run(main())
