DB = {
    'users': {
        'tatchiwiggers@lewagon.com': {
            'name': 'Tatchi Wiggers',
            'password': 'Porcupine2406'
        }
    }
}


def query_user(user_id: str):
    """
    Get a user from the db
    :param user_id: E-Mail of the user
    :return: None or the user object
    """
    return DB['users'].get(user_id)