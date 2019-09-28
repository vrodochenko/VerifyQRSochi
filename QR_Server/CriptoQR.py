import rsa


class CriptoQR:
    def __init__(self, pubkey, privkey):
        self.pubkey = pubkey
        self.privkey = privkey
    def __init__(self):
         self.pubkey, self.privkey = self.create_keys()
    def cipher(self, message, pubkey):
        crypto = rsa.encrypt(message, pubkey)
        return crypto
    def spelling_out(self, crypto, privkey):
        message = rsa.decrypt(crypto, privkey)
        return message
    def create_keys(self):
        (pubkey, privkey) = rsa.newkeys(512)
        return pubkey, privkey



if __name__ == '__main__':
    print(a.spelling_out(a.cipher(b'hi', a.pubkey), a.privkey))
