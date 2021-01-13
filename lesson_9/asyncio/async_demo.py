import asyncio
from loguru import logger


async def foo():
    logger.info('foo стартанула')
    await asyncio.sleep(.3)
    logger.info('foo завершилась')


async def bar():
    logger.info('bar стартанула')
    await asyncio.sleep(.2)
    logger.info('bar завершилась')


async def spam():
    logger.info('spam стартанула')
    await asyncio.sleep(.1)
    logger.info('spam завершилась')


def run_main():
    logger.info('STARTING MAIN')
    queue = [foo(), bar(), spam()]
    task = asyncio.wait(queue)
    asyncio.run(task)
    logger.info('FINISHING MAIN')


if __name__ == '__main__':
    run_main()
