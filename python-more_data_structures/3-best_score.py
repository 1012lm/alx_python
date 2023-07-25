def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
