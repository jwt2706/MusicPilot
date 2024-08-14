.PHONY: dev build

dev:
	@echo "Dev mode..."
	@python app.py

build:
	@echo "Building..."
	@pyinstaller --onefile app.py

clean:
	@echo "Cleaning..."
	@rm -rf build/ dist/ __pycache__/ *.spec