# Bar Chart Race UI

## Instructions

### To run locally
- create a virtual environment
- install required dependencies using <code>requirements.txt</code>
- run <code>load_ui.py</code>

### To create singleton application

<pre>pyinstaller --add-data 'fonts:fonts' load_ui.py --onefile --windowed --hidden-import cmath </pre>