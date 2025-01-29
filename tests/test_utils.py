import pytest

from src.utils import read_json_file


@pytest.fixture
def json_file_path(tmp_path):
    file_path = tmp_path / "operations.json"
    file_path.write_text('[{"id": 1, "amount": 100, "currency": "USD"}]', encoding="utf-8")
    return str(file_path)

def test_read_json_file_valid(json_file_path):
    result = read_json_file(json_file_path)
    assert len(result) == 1
    assert result[0]["id"] == 1

def test_read_json_file_empty(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")
    result = read_json_file(str(file_path))
    assert result == []
