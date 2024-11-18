class User:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} получил сообщение: {message}")


class Chat:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def unsubscribe(self, user):
        self.subscribers.remove(user)

    def notify_subscribers(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

    def send_message(self, user, message):
        print(f"{user.name} отправил сообщение: {message}")
        self.notify_subscribers(message)


# Пример использования
if __name__ == "__main__":
    chat = Chat()

    user1 = User("Alice")
    user2 = User("Bob")
    user3 = User("Charlie")

    chat.subscribe(user1)
    chat.subscribe(user2)
    chat.subscribe(user3)

    chat.send_message(user1, "Привет всем!")
    # Alice отправил сообщение: Привет всем!
    # Alice получил сообщение: Привет всем!
    # Bob получил сообщение: Привет всем!
    # Charlie получил сообщение: Привет всем!

    chat.unsubscribe(user2)

    chat.send_message(user3, "Как дела?")
    # Charlie отправил сообщение: Как дела?
    # Alice получил сообщение: Как дела?
    # Charlie получил сообщение: Как дела?