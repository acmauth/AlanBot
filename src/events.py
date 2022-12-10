import configuration
import discord
import traceback
import asyncio
import time
import util
from datetime import datetime

async def scheduled_events(client: discord.Client) -> None:
    '''
    Gets a list of all the scheduled events and activate each one automatically
    when the system clock hits the event's starting time.
    ''' 
    while True:
        try:
            event_list = await client.get_guild(configuration.GUILD_ID).fetch_scheduled_events()
            now = datetime.now().strftime("%D %H:%M").split(" ")
            for event in event_list:
                start = util.datetime_from_utc_to_local(event.start_time).strftime("%D %H:%M").split(" ")
                if start == now and event.status != discord.ScheduledEventStatus.active:
                    await event.start()
            await asyncio.sleep(configuration.EVENT_SLEEP)
        except Exception as e:
            traceback.print_exc()
            await asyncio.sleep(configuration.EVENT_SLEEP)

