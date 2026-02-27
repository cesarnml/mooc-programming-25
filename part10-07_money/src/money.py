# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

    def __eq__(self, other: "Money"):
        return self.__euros * 100 + self.__cents == other.__euros * 100 + other.__cents

    def __lt__(self, other: "Money"):
        return self.__euros * 100 + self.__cents < other.__euros * 100 + other.__cents

    def __gt__(self, other: "Money"):
        return self.__euros * 100 + self.__cents > other.__euros * 100 + other.__cents

    def __ne__(self, other: "Money"):
        return not self.__eq__(other)

    def __add__(self, other: "Money"):
        euros = self.__euros + other.__euros
        cents = self.__cents + other.__cents
        if cents >= 100:
            euros = euros + cents // 100
            cents = cents % 100
        return Money(euros, cents)

    def __sub__(self, other: "Money"):
        total = (self.__euros - other.__euros) * 100 + self.__cents - other.__cents

        if total < 0:
            raise ValueError("a negative result is not allowed")

        euros = total // 100
        cents = total % 100
        return Money(euros, cents)
