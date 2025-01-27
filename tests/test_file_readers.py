import pytest
from unittest.mock import patch
import pandas as pd
from src.file_readers import read_csv_file, read_excel_file


@pytest.fixture
def mock_csv_data():
    return "id,amount,currency\n1,100,USD\n2,200,EUR\n"


@pytest.fixture
def mock_excel_data():
    return pd.DataFrame({
        "id": [1, 2],
        "amount": [100, 200],
        "currency": ["USD", "EUR"]
    })


@patch("os.path.exists", return_value=True)
@patch("pandas.read_csv")
def test_read_csv_file(mock_read_csv, mock_exists):
    """Тест успешного чтения CSV-файла."""
    mock_read_csv.return_value = pd.DataFrame([
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ])
    result = read_csv_file("transactions.csv")
    assert result == [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]


@patch("os.path.exists", return_value=False)
def test_read_csv_file_not_found(mock_exists):
    """Тест обработки ошибки, если CSV-файл не найден."""
    with pytest.raises(FileNotFoundError, match="Файл .* не найден."):
        read_csv_file("transactions.csv")


@patch("os.path.exists", return_value=True)
@patch("pandas.read_excel")
def test_read_excel_file(mock_read_excel, mock_exists):
    """Тест успешного чтения Excel-файла."""
    mock_read_excel.return_value = pd.DataFrame([
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ])
    result = read_excel_file("transactions_excel.xlsx")
    assert result == [
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ]


@patch("os.path.exists", return_value=False)
def test_read_excel_file_not_found(mock_exists):
    """Тест обработки ошибки, если Excel-файл не найден."""
    with pytest.raises(FileNotFoundError, match="Файл .* не найден."):
        read_excel_file("transactions_excel.xlsx")
