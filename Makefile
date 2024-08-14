.PHONY: dev build clean

dev:
	@echo "Dev mode..."
	@python3 -m engine.main

build:
	@echo "Building..."
	@pyinstaller --onefile engine/main.py --name MusicPilot

clean:
	@echo "Cleaning..."
	@rm -rf build/ dist/ __pycache__/ *.spec