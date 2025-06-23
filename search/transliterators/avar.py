def avar_input_normal(field, text):
    """
    Prepare a string from one of the query fields for subsequent
    processing: replace common shortcuts with valid Avar characters.
    """
    if field not in ('wf', 'lex'):
        return text
    text = text.replace('1', 'ӏ')
    text = text.replace('I', 'ӏ')
    text = text.replace('l', 'ӏ')
    return text