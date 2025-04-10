import difflib

def suggest_commands(user_input, command_map):
    input_clean = user_input.lower()
    possible_commands = list(command_map.keys())

    # Частковий збіг
    partial_matches = [cmd for cmd in possible_commands if input_clean in cmd]

    # Найближчі за схожістю (тільки якщо часткових мало)
    if not partial_matches:
        partial_matches = difflib.get_close_matches(input_clean, possible_commands, n=5, cutoff=0.4)

    return partial_matches
