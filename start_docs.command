#!/bin/bash
# Move to the script's directory
cd "$(dirname "$0")"

echo "--------------------------------------------------"
echo "Starting Phoenix Ecosystem Documentation Server..."
echo "Opening browser at http://127.0.0.1:8000"
echo "Press Ctrl+C in this terminal window to stop."
echo "--------------------------------------------------"

# Wait 1 second to let MkDocs initialize, then open the browser
(sleep 1 && open http://127.0.0.1:8000) &

# Activate the virtual environment and start MkDocs
source .venv/bin/activate
mkdocs serve
