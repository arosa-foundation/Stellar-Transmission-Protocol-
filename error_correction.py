import reedsolo

class QuantumForwardErrorCorrection:
    def __init__(self):
        self.rs = reedsolo.RSCodec(10)  # 10 bytes of error correction

    def encode(self, message: bytes) -> bytes:
        return self.rs.encode(message)

    def decode(self, encoded_message: bytes) -> bytes:
        return self.rs.decode(encoded_message)
