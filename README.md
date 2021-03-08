# Bar Chart Race UI
A desktop application to create a bar chart race.

## Instructions to build the project

### To run locally
- create a virtual environment
- install required dependencies using <code>requirements.txt</code>
- run <code>load_ui.py</code>

### To create singleton application
This command will generate a desktop application for the operating system in which you are running this command. eg. .exe file if run on windows, .app file if run on mac.
<pre>pyinstaller load_ui.py --onefile --windowed --hidden-import cmath </pre>

If you need to include external files, use this command (adds folder <code>fonts</code> to the build).
<pre>pyinstaller --add-data 'fonts:fonts' load_ui.py --onefile --windowed --hidden-import cmath </pre>