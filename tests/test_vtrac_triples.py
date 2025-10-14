from modules.vtrac_reference import get_vtrac_index


def test_doubles_with_class_triple_map() -> None:
    assert get_vtrac_index("277") == 26
    assert get_vtrac_index("227") == 26
    assert get_vtrac_index("010") == 2


def test_pure_triples_are_none() -> None:
    assert get_vtrac_index("000") is None
    assert get_vtrac_index("777") is None
