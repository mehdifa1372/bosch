from app2 import allowed_file, app


def test_allowed_file_accepts_tabular_inputs():
    assert allowed_file("categorical.csv")
    assert allowed_file("numerical.txt")


def test_allowed_file_rejects_unexpected_inputs():
    assert not allowed_file("payload.py")
    assert not allowed_file("diagram.png")


def test_secret_is_not_the_original_placeholder():
    assert app.secret_key != "secret key"

