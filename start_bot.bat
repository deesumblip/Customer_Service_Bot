@echo off
echo Starting Shell Customer Service Assistant...
echo.

REM Load environment variables
python autoload_env.py

REM Start action server in background
echo Starting action server...
start "Action Server" cmd /c "rasa run actions --actions actions.actions --port 5055"

REM Wait for action server to start
timeout /t 3 /nobreak >nul

REM Start Rasa Inspector with the latest model automatically
for /f "delims=" %%i in ('dir /b /o-d models\*.tar.gz') do (
    echo Starting web interface with model: %%i
    rasa inspect --model models\%%i
    goto :end
)
echo No models found!
:end

pause
