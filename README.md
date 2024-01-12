# Website Blocker

## Description

Website Blocker is a simple Python script that blocks specified websites during working hours to increase productivity.

## Author

- Author: [Emycodes](https://github.com/emycodes)

## License

This project is licensed under the [MIT License](LICENSE).

## How to Run

### Linux

1. Open a terminal.

2. Clone this repo 
    ```bash
    git clone https://github.com/EmyCodes/web-blocker.git
    ```
3. Navigate to the project directory:

    ```bash
    cd ~/Desktop/web-blocker
    ```

4. Run the script:

    ```bash
    python3 blocker.py
    ```

### Windows

1. Open a command prompt.

2. Clone this repo 
    ```bash
    git clone https://github.com/EmyCodes/web-blocker.git
    ```
3. Navigate to the project directory:

    ```bash
    cd C:\Users\emycodes\Desktop\web-blocker
    ```

4. Run the script:

    ```bash
    python blocker.py
    ```

## Run at Startup

To run the script at system startup, follow these steps:

### Linux

1. Open a terminal.
2. Type the following command to open the crontab editor:

    ```bash
    crontab -e
    ```

3. Add the following line to run the script at startup:

    ```bash
    @reboot python3 /path/to/blocker.py
    ```

4. Save and exit the editor.

### Windows

1. Create a shortcut for `blocker.py`.
2. Press `Win + R` to open the Run dialog.
3. Type `shell:startup` and press Enter.
4. Move the shortcut to this folder.

Now, the script will run automatically at system startup.

## Configuration

Edit the `web_to_be_blocked.py` file to add or remove websites from the blocklist.

## Contributing

If you want to contribute to this project, feel free to open an issue or submit a pull request.

## Acknowledgments

Special thanks to [Emycodes](https://github.com/emycodes) for creating this project.
