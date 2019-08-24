from typing import Dict, List

from fuzzywuzzy import process


def closest_match(txt: str, choices: List[str]) -> Dict:
    """
	Returns the string which is the closest match

	Args:
		txt (str): [description]
		choices (List[str]): [description]
	
	Returns:
		choice_dict (Dict): Keys are txt and score with the closest_match and percent_match info
	"""
    closest_match, percent_match = process.extractOne(query=txt, choices=choices)
    choice_dict = {"txt": closest_match, "score": percent_match}
    return choice_dict
