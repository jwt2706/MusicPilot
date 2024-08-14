.PHONY: dev build clean

dev:
	@echo "Dev mode..."
	PYTHONPATH=src python3 -m src.main

build:
	@echo "Building..."
	@pyinstaller --onefile src/main.py --name MusicPilot

clean:
	@echo "Cleaning..."
	@rm -rf build/ dist/ __pycache__/ *.spec