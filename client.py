import socket
import pickle
from encryption import AdvancedConstellationEncryption
from rate_adaptation import DynamicNebulaRateAdaptation
from error_correction import QuantumForwardErrorCorrection

SERVER_IP = '127.0.0.1'  # Replace with the server's IP address
PORT = 65432

def main():
    # Set up encryption, rate adaptation, and error correction
    encryption = AdvancedConstellationEncryption()
    rate_adaptation = DynamicNebulaRateAdaptation()
    error_correction = QuantumForwardErrorCorrection()

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))

    print("Connected to server.")

    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break

        # Encrypt, encode, and send the message
        encrypted_message = encryption.encrypt(message)
        encoded_message = error_correction.encode(encrypted_message)
        rate_adjusted_message = rate_adaptation.adjust_rate(encoded_message)
        client_socket.sendall(pickle.dumps(rate_adjusted_message))

        # Receive and decrypt the response
        response = client_socket.recv(1024)
        decoded_response = pickle.loads(response)
        corrected_response = error_correction.decode(decoded_response)
        decrypted_response = encryption.decrypt(corrected_response)
        print(f"Server response: {decrypted_response}")

    client_socket.close()

if __name__ == '__main__':
    main()
