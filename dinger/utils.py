""" Tools collections for Dinger. """


def get_webhook(file_name):
    """ Read webhook from a file.

    Note:
        the file must only contain one line, which is the whole url of webhook.
    """
    with open(file_name) as f:
        return f.readlines()[0].strip()
