def parse_data_str_to_dict(text: str) -> dict:
    parts = [part.strip() for part in text.split(',')]
    data = {}
    for part in parts:
        if ':' in part:
            key, value = part.split(':', 1)
            data[key.strip()] = value.strip()
    return data

def parse_data_str_to_dict_notes(text: str) -> dict:
    parts = [part.strip() for part in text.split('|')]
    data = {}
    for part in parts:
        if ':' in part:
            key, value = part.split(':', 1)
            data[key.strip()] = value.strip()
    return data