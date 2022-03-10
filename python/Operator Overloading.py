class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02} eur"

    def __eq__(self, another) -> bool:
        return self._euros == another._euros and self._cents == another._cents

    def __gt__(self, another) -> bool:
        if self._euros > another._euros: return True
        elif self._euros == another._euros and self._cents > another._cents: return True
        else: return False
    
    def __lt__(self, another) -> bool:
        if self._euros < another._euros: return True
        elif self._euros == another._euros and self._cents < another._cents: return True
        else: return False

    def __ne__(self, another) -> bool:
        if self._euros != another._euros or self._cents != another._cents: return True
        else: return False
    
    def __add__(self, another) -> "Money":
        cents = self._cents + another._cents
        euros = self._euros + another._euros
        if cents >= 100:
            cents -= 100
            euros += 1
        return Money(euros, cents)

    def __sub__(self, another) -> "Money":
        euros = self._euros - another._euros
        cents = self._cents - another._cents
        if cents < 0:
            cents = 100 + cents
            euros -= 1
        if euros < 0: raise ValueError("a negative result is not allowed")
        return Money(euros, cents)
