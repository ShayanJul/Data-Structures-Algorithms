"""linked lists under the hood
    we can imagine linked lists as nested dictionaries
    """

head = {
    'value': 11,
    'next': {
        'value': 3,
        'next': {
            'value': 23,
            'next': {
                'value': 7,
                'next': {
                    'value': 4,
                    'next': None
                }
            }
        }
    }
}

# for example if we want to access 23
print(head['next']['next']['value'])
