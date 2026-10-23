@echo off
echo Starting local preview server for Wang's Geomechanics Lab website...
start http://localhost:8000
python -m http.server 8000
pause
