#!/usr/bin/python
# The following config() function read the database.ini  file and returns connection parameters.
# The config() function is placed in the config.py file


from configparser import ConfigParser 

def config(filename = 'database.ini', section='postgresql'):
    # create a parser 
    parser = ConfigParser()

    # read config file 
    parser.read(filename)

    # get section, default to postgresql 
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception ('Section {0} not found in the {1} file'.format(section, filename))

    return db 

