"""test_2 - the second test as part of the ministry of justice take home code assessment"""

# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc

"""

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type




import os
import glob
import requests
import pandas as pd
class APIError(Exception):
    """Describes an error triggered by a failing API call."""

    def __init__(self, message: str, code: int = 500):
        """Creates a new APIError instance."""
        self.message = message
        self.code = code


def get_court_by_postcode(postcode: str) -> list[dict]:
    """
    Given a postcode, returns a list of the 10 nearest courts

    Argument:
        postcode (str): A string representing the postcode.

    Returns:
        list: a list of dicts containing information associated with the court

    Raises:
        TypeError: If the input argument is not of type str.

    """
    if not isinstance(postcode, str):
        raise TypeError("Input argument must be in str format!")
    url = f'https://courttribunalfinder.service.gov.uk/search/results.json?postcode={postcode}'
    response = requests.get(
        f'{url}', timeout=60)
    if response.status_code != 200:
        raise APIError(f'API Response:{response.status_code}')

    data = response.json()
    return data


def get_people_from_csv(csv_file_name: str) -> list[dict]:
    """
    Given the people csv file, returns a list of people data

    Argument:
        csv_file_name (str): A string representing the file name (not including file extension).

    Returns:
        list: a list of dicts containing information associated with a person

    Raises:
        TypeError: If the input argument is not of type str.

    """

    current_directory = os.getcwd()
    csv_file_path = os.path.join(current_directory, f'{csv_file_name}.csv')
    file = glob.glob(csv_file_path)[0]
    data = pd.read_csv(file).to_numpy()
    csv_data = []
    for entry in data:
        csv_data_entry = {}
        csv_data_entry["person_name"] = entry[0]
        csv_data_entry["home_postcode"] = entry[1]
        csv_data_entry["looking_for_court_type"] = entry[2]
        csv_data.append(csv_data_entry)
    return csv_data


def get_courts_for_person(people_data: list[dict]):
    """"""
    for person in people_data:
        name = person["person_name"]
        postcode = person["home_postcode"]
        desired_type = person["looking_for_court_type"]

        court_data = get_court_by_postcode(postcode)
        for court in court_data:
            try:
                court_type = court["types"][0]
            except:
                court_type = None
            # print(desired_type, court_type)
            if desired_type == court_type:
                print(court)
            break
        break


if __name__ == "__main__":
    postcode = 'E144PU'
    csv_file_name = 'people'
    people_data = get_people_from_csv(csv_file_name)
    res = get_courts_for_person(people_data)
