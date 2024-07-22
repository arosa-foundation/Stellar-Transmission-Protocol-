from encryption import AdvancedConstellationEncryption
from rate_adaptation import DynamicNebulaRateAdaptation
from error_correction import QuantumForwardErrorCorrection
import random

class AdvancedStellarTransmissionProtocol:
    def __init__(self):
        self.encryption = AdvancedConstellationEncryption()
        self.dnra = DynamicNebulaRateAdaptation()
        self.qfec = QuantumForwardErrorCorrection()

    def transmit(self, plaintext, signal_quality):
        rate = self.dnra.adjust_rate(signal_quality)
        print(f"Transmitting at {rate} bytes/second")

        encrypted_data = self.encryption.encrypt(plaintext.encode('utf-8'))
        encoded_data = self.qfec.encode(encrypted_data.encode('utf-8'))
        return encoded_data

    def receive(self, encoded_data):
        decoded_data = self.qfec.decode(encoded_data)
        decrypted_data = self.encryption.decrypt(decoded_data.decode('utf-8'))
        return decrypted_data.decode('utf-8')


if __name__ == "__main__":
    stp = AdvancedStellarTransmissionProtocol()

    signal_quality = random.randint(0, 100)
    print(f"Signal Quality: {signal_quality}")

    original_message = "Hello, this is a highly secure and efficient message."
    print("Original Message:", original_message)

    transmitted_data = stp.transmit(original_message, signal_quality)
    print("Transmitted Data:", transmitted_data)

    received_message = stp.receive(transmitted_data)
    print("Received Message:", received_message)
