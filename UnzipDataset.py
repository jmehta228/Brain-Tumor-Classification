# Unzipping Dataset.zip file

from zipfile import ZipFile as zf

with zf('Dataset.zip', 'r') as obj:
    obj.extractall(path='Dataset')