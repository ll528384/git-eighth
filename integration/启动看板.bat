@echo off
cd /d %~dp0
start "integration-server" cmd /k "py server.py"
timeout /t 3 >nul
start "" "http://127.0.0.1:8767/"
pause
