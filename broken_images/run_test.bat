@echo off
echo Starting Selenium test for broken images...

:: Set Python path
set PYTHON_PATH=C:\Users\lukas\AppData\Local\Programs\Python\Python311\python.exe
set PIP_PATH=C:\Users\lukas\AppData\Local\Programs\Python\Python311\Scripts\pip.exe

:: Install dependencies
echo Installing dependencies...
%PIP_PATH% install selenium==4.29.0 requests==2.31.0

:: Run the test
echo Running the test...
%PYTHON_PATH% broken_images.py

:: Pause to see the results
pause 