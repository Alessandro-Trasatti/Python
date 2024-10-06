# Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar
# with these methods:

# __init__ should initialize a cookie jar with the given capacity,
# which represents the maximum number of cookies that can fit in the cookie jar.
# If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.
# __str__ should return a str with n 🍪, where n is the number of cookies in the cookie jar.
# For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
# deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though,
# deposit should instead raise a ValueError.
# withdraw should remove n cookies from the cookie jar.
# Nom nom nom. If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.
# capacity should return the cookie jar’s capacity.

class Jar:
    def __init__(self, capacity: int, nb_cookies: int = 0):
        if nb_cookies > capacity:
            raise ValueError("Initial number of cookies cannot exceed the jar's capacity.")
        self.capacity = capacity
        self.nb_cookies = nb_cookies
        
    def __str__(self) -> str:
        return "🍪" * self.nb_cookies
    
    def deposit(self, n: int):
        if isinstance(n, int) and n >= 0:
            if self.nb_cookies + n > self.capacity:
                raise ValueError(f"Adding {n} cookies would exceed the jar's capacity.")
            self.nb_cookies += n
        else:
            raise ValueError(f"A non-negative integer number of cookies should be deposited, but got {n}")
    
    def withdraw(self, n: int):
        if isinstance(n, int) and 0 <= n <= self.nb_cookies:
            self.nb_cookies -= n
        else:
            raise ValueError(f"Cannot withdraw {n} cookies. Only {self.nb_cookies} cookies are available.")
    
    @property
    def capacity(self) -> int:
        return self._capacity
    
    @property
    def nb_cookies(self) -> int:
        return self._nb_cookies
    
    @capacity.setter
    def capacity(self, capacity: int):
        if isinstance(capacity, int) and capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError(f"Capacity should be a non-negative integer, but got {capacity}")
    
    @nb_cookies.setter
    def nb_cookies(self, nb_cookies: int):
        if isinstance(nb_cookies, int) and 0 <= nb_cookies <= self.capacity:
            self._nb_cookies = nb_cookies
        else:
            raise ValueError(f"Number of cookies should be a non-negative integer and not bigger than the jar's capacity, but got {nb_cookies}")