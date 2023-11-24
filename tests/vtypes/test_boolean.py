from pandaq.vtypes import Boolean


def test_to_str():
    assert Boolean("a", True).to_str() == "a==True"
    assert Boolean("a", False).to_str() == "a==False"
