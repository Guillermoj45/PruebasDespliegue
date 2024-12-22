import asyncio

async def productor(queue):
    for i in range(1, 6):
        await queue.put(i)  # Añadir un elemento a la cola asincrónicamente
        print(f"Producido: {i}")

async def consumidor(queue):
    while True:
        item = await queue.get()  # Obtener un elemento de la cola asincrónicamente
        if item is None:  # Si encontramos None, significa que hemos terminado
            break
        print(f"Consumido: {item}")

async def main():
    queue = asyncio.Queue()  # Crear una cola asincrónica
    # Lanzamos el productor y el consumidor de forma concurrente
    await asyncio.gather(productor(queue), consumidor(queue))

# Ejecutar la función asincrónica
asyncio.run(main())
