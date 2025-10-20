#!/usr/bin/env python3
"""
Script de test pour le TP - Utilise un port alternatif pour éviter AirPlay
"""
import os
import sys
from app import app

if __name__ == "__main__":
    # Utiliser le port 5000 comme spécifié dans le TP
    # Si occupé par AirPlay, utiliser 5001
    import socket
    
    def is_port_in_use(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
    
    if is_port_in_use(5000):
        print("⚠️  Port 5000 occupé par AirPlay, utilisation du port 5001")
        app.run(host="0.0.0.0", port=5001, debug=False)
    else:
        app.run(host="0.0.0.0", port=5000, debug=False)
