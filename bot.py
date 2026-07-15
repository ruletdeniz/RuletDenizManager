import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers.panel import router as panel_router
from handlers.platform import router as platform_router
from handlers.announce import router as announce_router
from handlers.video import router as video_router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Routerlar
dp.include_router(panel_router)
dp.include_router(platform_router)
dp.include_router(announce_router)
dp.include_router(video_router)


async def main():
    print("🚀 Rulet Deniz Manager Başlatıldı...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())