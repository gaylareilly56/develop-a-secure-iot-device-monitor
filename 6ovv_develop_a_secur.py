import os
import time
import hashlib
import socket
import ssl
import json

# IoT Device Information
device_id = "DEV001"
device_key = "1234567890ABCDEF"

# Secure Server Information
server_addr = "192.168.1.100"
server_port = 8080

# Initialize Socket
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
conn = socket.create_connection((server_addr, server_port))
sock = context.wrap_socket(conn, server_hostname=server_addr)

# Test Case: Device Monitoring and Data Encryption
while True:
    # Read Sensor Data
    sensor_data = {"temperature": 25.5, "humidity": 60}

    # Encrypt Data using Device Key
    encrypted_data = json.dumps(sensor_data).encode()
    encrypted_data = hashlib.sha256(device_key.encode() + encrypted_data).hexdigest()

    # Create and Send Request to Server
    request = {"device_id": device_id, "data": encrypted_data}
    sock.sendall(json.dumps(request).encode())

    # Receive and Process Response from Server
    response = sock.recv(1024).decode()
    print("Received Response:", response)

    # Wait for 5 seconds before sending next request
    time.sleep(5)