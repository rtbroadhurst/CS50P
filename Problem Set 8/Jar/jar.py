# Implements a CookieJar class that manages depositing and withdrawing cookies with a fixed capacity

class CookieJar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return "🍪" * self._cookies

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Amount must be a non-negative integer")
        if self._cookies + n > self._capacity:
            raise ValueError("Amount of cookies cannot exceed capacity")
        self._cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Amount must be a non-negative integer")
        if self._cookies - n < 0:
            raise ValueError("Amount of cookies cannot be negative")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
    

def main():
    jar = CookieJar(10)

    jar.deposit(3)
    print(jar)

    jar.withdraw(1)
    print(jar)

    print(jar.size)
    print(jar.capacity)



if __name__ == "__main__":
    main()