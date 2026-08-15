# 同步 IO
# import time
#
# def boil_water():
#     print("开始烧水...")
#     time.sleep(5)  # 模拟烧水 5s，cpu 完全空闲
#     print("烧水完成...")
#
#
# def send_message():
#     print("开始发消息...")
#     time.sleep(2)  # 模拟烧水2s
#     print("发消息完成...")
#
#
# def main():
#     # 1、烧水
#     boil_water()
#     # 2、发消息
#     send_message()
#
#
# main()
# 开始烧水...
# 烧水完成...
# 开始发消息...
# 发消息完成...


# 异步 IO
import asyncio


# 协程
async def boil_water_async():
    print("开始烧水...")
    await asyncio.sleep(5)  # 模拟烧水 5s，【关键】：异步操作，await 表示等待这个操作完成，但是期间可以做别的事情
    print("烧水完成...")


# 协程
async def send_message_asynx():
    print("开始发消息...")
    await asyncio.sleep(2)  # 模拟烧水2s
    print("发消息完成...")


async def main():
    # 1、烧水
    task1 = asyncio.create_task(boil_water_async())
    # 2、发消息
    task2 = asyncio.create_task(send_message_asynx())
    await task1
    await task2


asyncio.run(main())
# 开始烧水...
# 开始发消息...
# 发消息完成...
# 烧水完成...
