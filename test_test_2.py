"""tests for functions defined in test_2.py"""
# pylint: skip-file
import pytest
from unittest.mock import patch, MagicMock

from rich.table import Table

import test_2


def test_get_court_by_postcode_invalid_argument():
    mock_invalid_postcode = ['invalid post code']
    with pytest.raises(TypeError):
        test_2.get_court_by_postcode(mock_invalid_postcode)


def test_unsuccessful_api_response(requests_mock):
    postcode = 'invalid_postcode'
    with pytest.raises(test_2.APIError):
        requests_mock.get(
            f'https://courttribunalfinder.service.gov.uk/search/results.json?postcode={postcode}', status_code=400)
        test_2.get_court_by_postcode(postcode)


@patch("requests.get")
def test_get_court_by_postcode_calls_correct_functions(mock_requests_get):
    postcode = 'mock postcode'
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.return_value = {'court_name': 'Court A'}
    mock_requests_get.return_value = mock_response
    res = test_2.get_court_by_postcode(postcode)
    assert mock_requests_get.call_count == 1
    assert mock_response.json.call_count == 1


def test_get_people_from_csv_invalid_argument():
    mock_invalid_file_name = ['invalid file name']
    with pytest.raises(TypeError):
        test_2.get_people_from_csv(mock_invalid_file_name)


@patch('pandas.read_csv')
@patch('glob.glob')
@patch('os.path.join')
@patch('os.getcwd')
def test_get_people_from_csv_returns_list_and_calls_correct_functions(mock_getcwd, mock_os_path_join, mock_glob, mock_pd_read):
    mock_file_name = 'mock_file_name'
    mock_pd_read.return_value = MagicMock()
    res = test_2.get_people_from_csv(mock_file_name)
    assert mock_getcwd.call_count == 1
    assert mock_os_path_join.call_count == 1
    assert mock_glob.call_count == 1
    assert mock_pd_read.call_count == 1
    assert isinstance(res, list)


def test_get_courts_for_person_invalid_argument():
    mock_invalid_person = ['invalid person']
    with pytest.raises(TypeError):
        test_2.get_courts_for_person(mock_invalid_person)


@patch("test_2.get_court_by_postcode")
def test_get_courts_for_person_returns_dict_and_calls_correct_functions(mock_get_court_by_postcode):
    mock_person = {
        "person_name": "mock_name",
        "looking_for_court_type": "mock_type",
        "home_postcode": "mock_postcode"
    }
    mock_get_court_by_postcode.return_value = [
        {
            "name": "mock_name",
            "types": ["mock_type"],
            "dx_number": "mock_dx_number",
            "distance": "mock_distance"
        }
    ]
    expected_result = {
        "name": "mock_name",
        "postcode": "mock_postcode",
        "type": "mock_type",
        "court_name": "mock_name",
        "court_dx_number": "mock_dx_number",
        "court_distance": "mock_distance"
    }
    res = test_2.get_courts_for_person(mock_person)
    assert mock_get_court_by_postcode.call_count == 1
    assert res == expected_result
    assert isinstance(res, dict)


def test_get_courts_for_people_invalid_argument():
    mock_invalid_argument = 'invalid argument'
    with pytest.raises(TypeError):
        test_2.get_courts_for_people(mock_invalid_argument)


@patch("test_2.get_courts_for_person")
def test_get_courts_for_people_returns_list_and_calls_correct_functions(mock_get_courts_for_person):
    mock_people_data = ['mock_people_data']
    mock_get_courts_for_person.return_value = 'mock_person_data'
    res = test_2.get_courts_for_people(mock_people_data)
    assert mock_get_courts_for_person.call_count == 1
    assert isinstance(res, list)


def test_render_data_output_invalid_argument():
    mock_invalid_argument = 'invalid argument'
    with pytest.raises(TypeError):
        test_2.render_data_output(mock_invalid_argument)


@patch("test_2.Table")
def test_render_data_output_returns_table(mock_table_object):
    mock_people_court_data = [{
        "name": "mock_name",
        "postcode": "mock_postcode",
        "type": "mock_type",
        "court_name": "mock_name",
        "court_dx_number": "mock_dx_number",
        "court_distance": "mock_distance"
    }]
    mock_table_object.return_value = Table()

    res = test_2.render_data_output(mock_people_court_data)
    assert mock_table_object.call_count == 1
    assert isinstance(res, Table)
