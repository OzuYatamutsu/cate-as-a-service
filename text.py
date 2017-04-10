monospace_base = 65248;

def cateify(input_text: str) -> str:
    """
    Returns a monospaced version of a normal string.
    """
    result = []

    for char in input_text:
        if not __is_special_char(char):
            result.append(chr(ord(char) + monospace_base))
        else:
            result.append(__special_cast_char(char)) 
    return ''.join(result)

def __is_special_char(char) -> bool:
    return char in [' ', '\n']

def __special_cast_char(char) -> str:
    return {' ': chr(12288), '\n': '\n'}[char]

