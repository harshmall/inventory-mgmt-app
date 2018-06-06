#from products_app.app import *
from products_app.app import enlarge


def test_enlarge():
    result = enlarge(40)
    assert result == 4000
