import asyncio
import random
from art import tprint

async def f():
    while True:       # while True - блокирующая функция т.ж. как input()
        print("f()")
        await asyncio.sleep(1)

async def g_helper():
    print("g_helper()")
    return random.randint(0, 100)

async def g():
    while True:
        a = await g_helper()
        print(a)
        await asyncio.sleep(1)


async def main():
    # await g()  -  такой вид не совсем верный т.к. если у нас в g() будет sleep(999), f() не будет выполнятся
    # await f()

    # main_loop.create_task(g())  -  это уже по-лучше т.к. g() никак не помешает f() , но тут прикол в том что мы создаём задачу
    # await f()                      """"create_task(g())"""", и поэтому выполняются сначала второстепенные (в нашем случае f())

    # ПРИ await ОЖИДАЕТСЯ ОКОНЧАНИЕ ФУНКЦИИ

    main_loop.create_task(g())
    main_loop.create_task(f())

if __name__ == '__main__':
    tprint("asyncio")
    main_loop = asyncio.get_event_loop() #2
    main_loop.run_until_complete(main()) #1
    main_loop.run_forever()


g_helper()
13
f()
g_helper()
34
f()
g_helper()
88
f()


