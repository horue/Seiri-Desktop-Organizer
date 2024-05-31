import configparser

def read_ini(section, config_file=r'GUI\config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    extensions = config.get(section, 'extensions').split()
    extensions = [ext.strip() for ext in extensions]
    return extensions

print(read_ini('image'))

