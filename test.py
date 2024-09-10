import asyncio
from fake_useragent import UserAgent

from twikit import Client

async def main():
    ua = UserAgent()
   
    client = Client(user_agent = str(ua.chrome), language ='en-US')

    # Log in to your Twitter account
    await client.login(
        auth_info_1='',
        auth_info_2='',
        password=''
    )
    client.save_cookies('cookies.json')
    
if __name__ == "__main__":
    asyncio.run(main())
