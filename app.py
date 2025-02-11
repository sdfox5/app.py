#fox
from flask import Flask, request, jsonify
import jwt
import requests
from protobuf_decoder.protobuf_decoder import Parser
from datetime import datetime
import json
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

def encrypt_api(plain_text):
    plain_text = bytes.fromhex(plain_text)
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher_text.hex()

def dec_to_hex(ask):
    ask_result = hex(ask)
    final_result = str(ask_result)[2:]
    if len(final_result) == 1:
        final_result = "0" + final_result
        return final_result
    else:
        return final_result

def convert_to_hex(PAYLOAD):
    hex_payload = ''.join([f'{byte:02x}' for byte in PAYLOAD])
    return hex_payload
