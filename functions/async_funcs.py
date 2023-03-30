import asyncio


async def greeting(name):
    return f"Hello {name}"


async def main():
    """
    it is never possible to write code that calls 
    an async function from a non-async function
    """
    # NOTE: await to run an async func within an async func
    r = await greeting('Vik')
    print(r)


# NOTE: a manager to run an async func outside async func
r = asyncio.run(greeting('Vik'))
print(r)

asyncio.run(main())
