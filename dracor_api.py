import html
import json
import re
import requests
import os


def get_play_names(request_link):
    """Makes a request to RusDraCor API to get all play ids, generally constructed
    as "author-drama-name".

    :arg request_link - (str) an API link to send the request

    :returns play_ids - (list of str) ids for all the plays currently present in the
    corpus"""
    play_ids = []
    response = requests.get(request_link)
    if response:
        all_plays = response.json()["dramas"]
        for play in all_plays:
            play_ids.append(play["id"])
    return play_ids


def download_directions(play_id):
    """Downloads the stage directions for an indicated play, otherwise prints
    a fail message and returns an empty list.

    :arg play_id - (str) id of the play from RusDraCor (extracted from the API)
    to insert in the API request

    :returns directions - (list of str) all the direction from RusDraCor API 
    as they are in the play"""
    request_link = "https://dracor.org/api/corpora/rus/play/{}/stage-directions".format(play_id)
    response = requests.get(request_link)
    if response.status_code == 200:
        directions = response.text.split("\n")
    else:
        print("Couldn't retrieve the directions, status code: {} \
        \nReturning an empty list".format(response.status_code))
        directions = []
    return directions


def play_metadata_api(play_id):
    """Fetch play metadata from DraCor API, including:
        play title,
        playwriter's full name (important to distinguish between Leo Tolstoy and 
    Alexey Tolstoy),
        no. of characters in cast,
        no. of segments.
    In case the request returns with error code, returns an empty dict.

    :arg play_id - (str) id of the play from RusDraCor (extracted from the API)
    to insert in the API request

    :returns play_data - (dict) fetched data from API query results:
        title: str, 
        author: str, 
        characters: int, 
        segments: int
    """
    play_data = {"title": "",
    "author": "",
    "characters": 0,
    "segments": 0
    }
    request_link = "https://dracor.org/api/corpora/rus/play/{}".format(play_id)
    response = requests.get(request_link)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        play_data["title"] = response_json["title"]
        play_data["author"] = response_json["author"]["name"]
        play_data["segments"] = int(response_json["allInSegment"])
        play_data["characters"] = len(response_json["cast"])
    else:
        print("Couldn't retrieve metadata\n\t- play: {}\n\t- status code: {} \
        \n=> Returning an empty dict".format(play_id, response.status_code))
        play_data = {}
    return play_data
