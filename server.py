import socket
import pickle
from encryption import AdvancedConstellationEncryption
from rate_adaptation import DynamicNebulaRateAdaptation
from error_correction import QuantumForwardErrorCorrection

PORT = 65432

def main():
    # Set up encryption, rate adaptation, and error correction
    encryption = AdvancedConstellationEncryption()
    rate_adaptation = DynamicNebulaRateAdaptation()
    error_correction = QuantumForwardErrorCorrection()

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', PORT))
    server_socket.listen()

    print("Server listening for connections...")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        # Receive and decode the message
        data = conn.recv(1024)
        if not data:
            break

        rate_adjusted_message = pickle.loads(data)
        decoded_message = error_correction.decode(rate_adjusted_message)
        decrypted_message = encryption.decrypt(decoded_message)
        print(f"Received message: {decrypted_message}")

        # Process the message and send a response
        response_message = f"Server received: {decrypted_message}"
        encrypted_response = encryption.encrypt(response_message)
        encoded_response = error_correction.encode(encrypted_response)
        rate_adjusted_response = rate_adaptation.adjust_rate(encoded_response)
        conn.sendall(pickle.dumps(rate_adjusted_response))

    conn.close()
    server_socket.close()

if __name__ == '__main__':
    main()
