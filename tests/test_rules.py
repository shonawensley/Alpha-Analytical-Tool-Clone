import alpha_analytical.stable as stab

def test_is_3value():
    assert stab.is_3value("5599")
    assert stab.is_3value("661155")
    assert not stab.is_3value("55983")

def test_single_left():
    assert stab._eval_single_left(rowcov=3, span=1, straight=True)
    assert not stab._eval_single_left(rowcov=4, span=1, straight=True)

def test_hotzone():
    cfg = stab.CFG
    assert stab._hot_bonus(col="1", hot=2) == 2 * cfg["hot_level_2_bonus"]
    assert stab._hot_bonus(col="4", hot=2) == cfg["hot_level_2_bonus"] 