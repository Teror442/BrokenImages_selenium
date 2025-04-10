@echo off
echo Starting Selenium test for broken images...

echo Installing dependencies...
python -m pip install selenium==4.29.0 requests==2.31.0

echo Running the tests...
python -m unittest broken_images.py -v

pause 