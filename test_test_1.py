"""tests for functions defined in test_1.py"""
# pylint: skip-file
import pytest
from unittest.mock import patch

import test_1


def test_check_timestamp_invalid_argument_type():
    invalid_timestamp = ['invalid_timestamp_type']
    with pytest.raises(TypeError):
        test_1.check_timestamp(invalid_timestamp)


def test_check_timestamp_returns_True_for_valid_timestamp():
    mock_valid_timestamp = '03/11/21 08:51:01'
    res = test_1.check_timestamp(mock_valid_timestamp)
    assert res == True


def test_check_timestamp_returns_False_for_invalid_timestamp():
    mock_valid_timestamp = 'invalid_timestamp'
    res = test_1.check_timestamp(mock_valid_timestamp)
    assert res == False


def test_log_level_invalid_argument_type():
    invalid_log_level = ['invalid_log_level']
    with pytest.raises(TypeError):
        test_1.check_timestamp(invalid_log_level)


def test_log_level_returns_True_for_valid_log_level():
    mock_valid_log_level = 'INFO'
    res = test_1.check_log_level(mock_valid_log_level)
    assert res == True


def test_check_log_level_returns_False_for_invalid_log_level():
    mock_valid_log_level = 'invalid_log_level'
    res = test_1.check_log_level(mock_valid_log_level)
    assert res == False


def test_is_log_line_invalid_argument_type():
    invalid_is_log_line = ['invalid_is_log_line']
    with pytest.raises(TypeError):
        test_1.is_log_line(invalid_is_log_line)


@patch("test_1.check_timestamp")
def test_is_log_line_calls_correct_functions(mock_check_timestamp):
    mock_line = 'mock line for testing'
    test_1.is_log_line(mock_line)
    assert mock_check_timestamp.call_count == 1


def test_is_log_line_returns_True_for_valid_log_level():
    mock_line = '03/11/21 08:51:01 log_level message'
    res = test_1.is_log_line(mock_line)
    assert res == True


def test_is_log_line_returns_False_for_invalid_log_level():
    mock_line = 'invalid log_level message'
    res = test_1.is_log_line(mock_line)
    assert res == False


def test_is_get_dict_invalid_argument_type():
    invalid_log_line = ['invalid_get_dict']
    with pytest.raises(TypeError):
        test_1.get_dict(invalid_log_line)


def test_is_get_dict_invalid_argument_data():
    invalid_log_line = 'invalid log_level message'
    with pytest.raises(IndexError):
        test_1.get_dict(invalid_log_line)


@patch("test_1.check_log_level")
@patch("test_1.check_timestamp")
def test_get_dict_calls_correct_functions(mock_check_timestamp, mock_check_log_level):
    mock_line = 'mock line for testing'
    test_1.get_dict(mock_line)
    assert mock_check_timestamp.call_count == 1
    assert mock_check_log_level.call_count == 1


def test_get_dict_returns_dict_for_valid_log_level():
    mock_line = '03/11/21 08:51:01 INFO mock_message'
    expected_result = {'log_level': 'INFO',
                       'message': 'mock_message', 'timestamp': '03/11/21 08:51:01'}
    res = test_1.get_dict(mock_line)
    assert res == expected_result


def test_get_dict_returns_None_for_invalid_log_level():
    mock_line = '03/11/21 08:51:01 invalid_log_level mock_message'
    res = test_1.get_dict(mock_line)
    assert res == None
