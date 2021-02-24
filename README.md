# Bar Chart Race UI
A desktop application to create a bar chart race.

## Instructions

### To run locally
- create a virtual environment
- install required dependencies using <code>requirements.txt</code>
- run <code>load_ui.py</code>

### To create singleton application
<pre>pyinstaller --add-data 'fonts:fonts' load_ui.py --onefile --windowed --hidden-import cmath </pre>
Note: This command will generate a desktop application for the operating system in which you are running this command. eg. .exe file if run on windows, .app file if run on mac