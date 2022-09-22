import asyncio
from random import randint
import time

####################
# This class can be modified per asset to enable the asset specific connections and reading
#
####################


class EdgeNode:
    def __init__(self, asset, refreshrate) -> None:
        self.asset = asset  
        self.refreshrate = refreshrate
        self.value = -1
        self.connection = False
        self.stop_timer = 0
        self.start_timer = 0

    async def connect(self):
        print("Dummy Edge Node connected")
        self.connection = True

    def dicsonnect(self):
        print("Dummy Edge Node disconnected")
        self.connection = False

    async def read(self):
        self.value = randint(0,1000)
        print("Edge Node Value:" ,self.value)


    async def run(self):
        if not self.connection:
            await self.connect()
        while self.connection:
            await self.read()
            await asyncio.sleep(1/self.refreshrate)
            
            