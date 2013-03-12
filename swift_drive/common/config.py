from ConfigParser import ConfigParser


def get_config(key, config_file='/etc/swift-drive/swift-drive.conf'):
    """
    Get the value for the specified key in the config file.

    :param key: The config parameter to get.
    :param config_file: The location of the config file to be parsed.
    :returns: The value for the requested key.
    """
    c = ConfigParser()
    try:
        if not c.read(config_file):
            raise Exception("Unable to read config file: %s" % config_file)
        return str(c.get('swift-drive', key))
    except:
        return False
