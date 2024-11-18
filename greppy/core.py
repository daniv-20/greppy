import re


def grep(pattern, text, values=False, ignore_case=False):
    """
    Search for a pattern in the text with optional flags.
    :param pattern: Regex pattern to search for.
    :param text: List of strings to search.
    :param values: Return matching lines if True, otherwise booleans.
    :param ignore_case: Perform case-insensitive search if True.
    :return: List of matching lines or booleans.
    """
    flags = re.IGNORECASE if ignore_case else 0
    regex = re.compile(pattern, flags)

    if values:
        # Return the matching lines
        return [line for line in text if regex.search(line)]
    else:
        # Return a list of booleans indicating matches
        return [bool(regex.search(line)) for line in text]
