from hashlib import md5
from var import passwd

hashed = md5(passwd.encode('utf-8')).hexdigest()

with open("template.tbl", 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    first_place = f"{hashed}\n"
    f.writelines([first_place]+lines)
