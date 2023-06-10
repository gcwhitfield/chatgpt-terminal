# Python terminal client for ChatGPT.

## How to use

Run `pipenv shell` in this directory to install the required dependencies.

`python main.py` to execute the program.

## Setup

To set the environment variable before running the script, you can follow these steps based on your operating system:

### On Windows:

1.  Open the Start menu and search for "Environment Variables".
2.  Click on "Edit the system environment variables" to open the System Properties dialog.
3.  In the System Properties dialog, click the "Environment Variables" button.
4.  In the "User variables" section, click "New" to create a new user-level environment variable.
5.  Enter "OPENAI_API_KEY" as the variable name and provide your API key as the variable value.
6.  Click "OK" to save the environment variable.

### On macOS and Linux:

1. Open a terminal.
2. Run the following command to open the shell configuration file in a text editor:
   - For macOS:
     - `nano ~/.bash_profile`
   - For Linux:
     - `nano ~/.bashrc`
3. Add the following line at the end of the file:
   - `export OPENAI_API_KEY="YOUR_API_KEY"`
   Replace "YOUR_API_KEY" with your actual API key.
   Save the file and exit the text editor.
4. Run the following command to apply the changes to the current terminal session:

- `source ~/.bash_profile` or `source ~/.bashrc`

  By setting the "OPENAI_API_KEY" environment variable before running the script, the Python code will be able to access the API key through os.environ.get("OPENAI_API_KEY").
