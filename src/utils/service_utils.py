"""Utility functions for the project"""
import socket

def get_available_port():
    """Get an available port on the local machine"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port
