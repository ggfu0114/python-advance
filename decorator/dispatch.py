from functools import singledispatch
from datetime import datetime



@singledispatch
def toString(item):
    """It's the default handler for the function."""

    print(f'Item type:any, after toString:{item}')


@toString.register
def _(item: int):
    """If the input type is int, then goes to this function."""

    print(f'Item type:int, after toString:{str(item)}')


@toString.register
def _(item: datetime):
    """Handle datetime type of the input, and transfer it to string."""

    print(f'Item type:datetime, after toString:{item.strftime("%m/%d/%Y, %H:%M:%S")}')



if __name__ == '__main__':
    toString('123')
    toString(123)
    toString(123.0)
    toString(datetime.now())