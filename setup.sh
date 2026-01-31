#!/bin/bash

# Clone the official CrewAI Studio if not already present
if [ ! -d "CrewAI-Studio" ]; then
    echo "Cloning CrewAI Studio..."
    git clone https://github.com/strnad/CrewAI-Studio.git
    
    # Copy the main app files
    cp -r CrewAI-Studio/app/* ./ 2>/dev/null || true
    cp -r CrewAI-Studio/.streamlit/* .streamlit/ 2>/dev/null || true
fi

# Create streamlit config directory if it doesn't exist
mkdir -p ~/.streamlit/

# Create streamlit config
echo "[general]
email = \"\"

[server]
headless = true
enableCORS = false
port = $PORT
address = 0.0.0.0
" > ~/.streamlit/config.toml

# Make sure database directory exists
mkdir -p ./db

echo "Setup complete!"
