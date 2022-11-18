import asyncio
import csv
from art import tprint

async def get_data():
    num = input("Введите число:")
    print(f"get_data - {num}")
    return num

async def processing_1():
    a = await get_data()
    print(f"pgs_1 - {a}")
    return a

async def processing_2():
    pass

async def processing_3():
    pass

async def save_result():
    a = await processing_1

    with open("result.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(
            ("Try_num", "result")
        )

    b = await processing_1
    c = await processing_1

async def main():
    main_loop.create_task(save_result())
    await processing_1()


if __name__ == '__main__':
    tprint("asyncio")
    main_loop = asyncio.get_event_loop() #2
    main_loop.run_until_complete(main()) #1
    main_loop.run_forever()