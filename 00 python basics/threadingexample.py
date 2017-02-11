import threading


class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10000):
            print(threading.current_thread().getName() + str(_))


# Diese Klasse kann also gethreaded werden, d.h. mehrere Objekte davon
# können zur gleichen Zeit laufen!

x = BuckysMessenger(name='Sender')
y = BuckysMessenger(name='Reveive')

# Immer wenn man einen Thread kreiert, muss man die START - Funktion aufrufen:
# (start selbst such in der Klasse nach der run - Methode
x.start()
y.start()