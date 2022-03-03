import hashlib


class Helpers:
    def validation(self):
        hash_code = ''
        new_hash_code = hashlib.md5(self.encode('utf-8')).hexdigest()
        if new_hash_code != hash_code:
            hash_code = new_hash_code
            return 1
        else:
            return 0
