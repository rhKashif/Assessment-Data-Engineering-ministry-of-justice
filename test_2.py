"""test_2 - the second test as part of the ministry of justice take home code assessment"""

import os
import glob
import requests
import pandas as pd

from rich.console import Console
from rich.table import Table


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
    if not isinstance(csv_file_name, str):
        raise TypeError("Input argument must be in str format!")

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


def get_courts_for_person(person: dict) -> dict:
    """
    Given a dictionary containing details for a person, 
    return a dictionary containing data related to the nearest court

    Argument:
        person (dict): A dictionary containing a data related to a person: 
        name, court type, home postcode

    Returns:
        dictionary: a dictionary containing data associated with a person and the closest court: 
        name, postcode, court type, court name, court dx number, distance to court

    Raises:
        TypeError: If the input argument is not of type dict.

    """
    if not isinstance(person, dict):
        raise TypeError("Input argument must be in dict format!")

    name = person["person_name"]
    desired_type = person["looking_for_court_type"]
    postcode = person["home_postcode"]

    court_data = get_court_by_postcode(postcode)

    for court in court_data:
        try:
            court_type = court["types"][0]
        except:
            court_type = None

        if desired_type == court_type:
            desired_court_data_person = {
                "name": name, "postcode": postcode, "type": desired_type,
                "court_name": court["name"], "court_dx_number": court["dx_number"],
                "court_distance": court["distance"]}
            break

    return desired_court_data_person


def get_courts_for_people(people_data: list[dict]) -> list[dict]:
    """
    Given a list containing dictionaries,
    each dictionary contains details for a person, 
    return a list containing dictionaries,
    each dictionary contains details for a person and relevant court, 

    Argument:
        person (list[dict]): A list of dictionaries,
        with each dictionary containing data related to a person: 
        name, court type, home postcode

    Returns:
        list[dict]: a list of dictionaries,
        with each dictionary containing data associated with a person and their nearest court: 
        name, postcode, court type, court name, court dx number, distance to court

    Raises:
        TypeError: If the input argument is not of type dict.

    """
    if not isinstance(people_data, list):
        raise TypeError("Input argument must be in dict format!")

    desired_court_data_people = []
    for person in people_data:
        data = get_courts_for_person(person)
        desired_court_data_people.append(data)

    return desired_court_data_people


def render_data_output(people_court_data: list[dict]) -> Table:
    """
    Given a list of dictionaries, 
    render a list of people and their nearest court to the console using the Rich Library

    Argument:
        people_court_data (list[dict]): A list of dictionaries,
        with each dictionary containing data related to a person and their nearest court: 
        name, postcode, court type, court name, court dx number, distance to court

    Returns:
        Table: a rich table object

    Raises:
        TypeError: If the input argument is not of type dict.
    """

    if not isinstance(people_court_data, list):
        raise TypeError("Input argument must be in dict format!")

    table = Table(title="Court Information")

    table.add_column("Name:", justify="Left", style="cyan")
    table.add_column("Home Postcode:", style="cyan")
    table.add_column("Desired Court Type:", style="magenta")
    table.add_column("Court Name:", style="red")
    table.add_column("Court DX No.:", justify="left", style="red")
    table.add_column("Distance to Court:", justify="right", style="green")

    for person in people_court_data:
        name = person['name']
        court_type = person['type']
        postcode = person['postcode']
        court_name = person['court_name']
        court_dx_number = person['court_dx_number']
        court_distance = str(person['court_distance'])

        if court_dx_number is None:
            court_dx_number = 'N/A'

        table.add_row(name, postcode, court_type, court_name,
                      court_dx_number, court_distance)
    return table


if __name__ == "__main__":
    console = Console(record=True)
    CSV_FILE_NAME = 'people'
    people_data = get_people_from_csv(CSV_FILE_NAME)
    people_court_data = get_courts_for_people(people_data)
    rendered_data_table = render_data_output(people_court_data)
    console.print(rendered_data_table)
