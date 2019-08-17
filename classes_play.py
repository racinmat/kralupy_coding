class MyNumber:

    def __init__(self, number) -> None:
        super().__init__()
        self.number = number

    def __str__(self) -> str:
        return str(self.number) + ' kundo'

    def __repr__(self) -> str:
        return repr(self.number) + ' pyčo'


if __name__ == '__main__':
    my_number = MyNumber(10)
    print('print', my_number)
    print('repr', repr(my_number))
    print('str', str(my_number))
    print(f'moje číslo je {my_number}')