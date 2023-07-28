"""tests for functions defined in test_1.py"""
import pytest 
import test_1

def test_read_csv_file_invalid_input_type_raises_exception():
    mock_csv_file_name = ['invalid_file_type']
    with pytest.raises(TypeError):
        test_1.read_csv_file(mock_csv_file_name)
    
