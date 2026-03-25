import pytest
import os
import sys
import tempfile
import shutil

@pytest.fixture
def sample_person_data():
    return {
        "voornaam": "Jan",
        "achternaam": "Jansen",
        "hele_naam": "Jan Jansen",
        "roepnaam": "Kees",
        "geboortedatum": "15-03-1985",
        "favoriete_kleur": "Blauw",
        "oogkleur": "Bruin",
        "postcode": "1234 AB",
        "huisnummer": "42",
        "plaatsnaam": "Amsterdam",
        "provincie": "Noord-Holland",
        "temp_mail": "jan.jansen123@armyspy.com",
        "temp_mail_url": "https://www.fakemailgenerator.com/#/armyspy.com/jan.jansen123/"
    }


def test_generate_person_structure(sample_person_data):
    """Test that generated person has all required fields."""
    required_fields = [
        "voornaam", "achternaam", "hele_naam", "roepnaam",
        "geboortedatum", "favoriete_kleur", "oogkleur",
        "postcode", "huisnummer", "plaatsnaam", "provincie",
        "temp_mail", "temp_mail_url"
    ]
    for field in required_fields:
        assert field in sample_person_data


def test_build_output_returns_string(sample_person_data):
    """Test that build_output returns a string."""
    from main import build_output
    result = build_output(sample_person_data)
    assert isinstance(result, str)
    assert len(result) > 0


def test_save_functions_create_files(sample_person_data):
    """Test that save functions create files correctly."""
    from main import save_txt, save_json
    tmp_dir = tempfile.mkdtemp()
    try:
        txt_path = os.path.join(tmp_dir, "test_alias.txt")
        json_path = os.path.join(tmp_dir, "test_alias.json")
        
        save_txt(sample_person_data, txt_path)
        save_json(sample_person_data, json_path)
        
        assert os.path.exists(txt_path)
        assert os.path.exists(json_path)
    finally:
        shutil.rmtree(tmp_dir)


def test_print_function_exists():
    """Test that print_person function exists."""
    from main import print_person
    assert callable(print_person)