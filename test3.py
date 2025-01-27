import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")  # Привязываемся к порту 5555

    print("Сервер запущен и ожидает запросы...")

    while True:
        # Получаем запрос от клиента
        message = socket.recv_pyobj()
        print(f"Получен запрос: {message}")

        # Обрабатываем запрос (например, удваиваем каждый элемент списка)
        response = [x * 2 for x in message]

        # Отправляем ответ клиенту
        socket.send_pyobj(response)

if __name__ == "__main__":
    main()
