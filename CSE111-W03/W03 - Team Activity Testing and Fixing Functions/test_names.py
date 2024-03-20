from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Spencer", "Sedano") == "Sedano; Spencer"
    assert make_full_name("Joshua", "Cox") == "Cox; Joshua"
    assert make_full_name("", "") == "; "


def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Sedano; Spencer") == "Sedano"
    assert extract_family_name("Cox; Joshua") == "Cox"
    assert extract_family_name("Bailey-Sue; James") == "Bailey-Sue"
    assert extract_family_name("; ") == ""


def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Sedano; Spencer") == "Spencer"
    assert extract_given_name("Cox; Joshua") == "Joshua"
    assert extract_given_name("Bailey-Sue; James") == "James"
    assert extract_given_name("; ") == ""


pytest.main(["-v", "--tb=line", "-rN", __file__])
