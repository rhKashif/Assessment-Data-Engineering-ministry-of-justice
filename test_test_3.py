"""tests for functions defined in test_3.py"""
# pylint: skip-file
import pytest
from unittest.mock import patch, MagicMock
import test_3
import unittest


def test_invalid_argument_type():
    mock_invalid_argument = ['mock_invalid_time']
    with pytest.raises(TypeError):
        test_3.sum_current_time(mock_invalid_argument)


def test_invalid_argument_data():
    mock_invalid_argument = "invalid argument"
    with pytest.raises(ValueError):
        test_3.sum_current_time(mock_invalid_argument)


def test_valid_time_format():
    mock_time = '12:34:56'
    assert test_3.sum_current_time(mock_time) == 12 + 34 + 56


def test_invalid_time_format():
    mock_time = '12:34'
    with pytest.raises(ValueError):
        test_3.sum_current_time(mock_time)


def test_negative_numbers_in_data():

    with pytest.raises(ValueError):
        mock_time = '-12:34:56'
        test_3.sum_current_time(mock_time)

    with pytest.raises(ValueError):
        mock_time = '12:-34:56'
        test_3.sum_current_time(mock_time)

    with pytest.raises(ValueError):
        mock_time = '12:34:-56'
        test_3.sum_current_time(mock_time)


def test_exceeding_time_range():
    mock_time = '25:34:56'
    with pytest.raises(ValueError):
        test_3.sum_current_time(mock_time)

    mock_time = '12:61:56'
    with pytest.raises(ValueError):
        test_3.sum_current_time(mock_time)

    mock_time = '12:34:61'
    with pytest.raises(ValueError):
        test_3.sum_current_time(mock_time)
