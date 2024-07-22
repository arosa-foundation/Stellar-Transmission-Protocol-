# Stellar Transmission Protocol (STP)

## Overview

The Stellar Transmission Protocol (STP) is a cutting-edge, secure, and adaptive messaging protocol designed for real-time communication across networks. It features a robust client-server architecture that facilitates the secure transmission of messages, leveraging advanced encryption, dynamic rate adaptation, and sophisticated error correction mechanisms.

## Features

- **Advanced Encryption**: Implements Fernet encryption from the `cryptography` library to ensure secure data transmission.
- **Dynamic Rate Adaptation**: Utilizes dynamic adjustment of transmission rates based on signal quality to optimize performance and reliability.
- **Sophisticated Error Correction**: Employs Reed-Solomon error correction for maintaining data integrity.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- Python libraries: `cryptography`, `reedsolo`, `numpy`

To install the necessary Python libraries, run the following command:

```bash
pip install cryptography reedsolo numpy
```



 ### Running the Server

1. Open a terminal and navigate to the project directory.
2. Start the server with:

```bash
python server.py
```


The server will start listening for incoming connections on port `65432` (you can change this port in the `server.py` file if needed).

### Running the Client

1. Open a terminal on the client machine or use a different terminal for multiple clients.
2. Navigate to the project directory.
3. Start the client with:

```bash
python client.py
```


Update the `server_ip` in `client.py` to the IP address of the machine running the server if testing across different devices.

### Testing Across Devices

- Ensure all devices are on the same network or have proper network configurations.
- Run the server on one device.
- Update the `server_ip` in `client.py` to match the server's IP address.
- Run the client on another device or terminal.

## Code Details

### Encryption

The protocol uses `AdvancedConstellationEncryption` for secure message transmission, leveraging the `cryptography` library's Fernet encryption.

### Rate Adaptation

`DynamicNebulaRateAdaptation` adjusts the transmission rate based on signal quality to maintain optimal performance.

### Error Correction

`QuantumForwardErrorCorrection` ensures data integrity by encoding and decoding messages with Reed-Solomon error correction.

## Customization

- Modify the parameters in `encryption.py`, `rate_adaptation.py`, and `error_correction.py` to suit your needs.
- Adjust IP addresses and ports in `client.py` and `server.py` as required.

