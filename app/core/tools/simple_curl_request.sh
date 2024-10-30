#!/bin/bash
code="195372322400003260665111"
response_file="server_response.json"

curl -s -d "tracking_code=$code" -X POST "http://127.0.0.1:8000/take_shot" >> "$response_file"
echo "" >> "$response_file"
grep -i "$code" "$response_file"
