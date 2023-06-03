# Typer - Roku Remote Control via Python

This Python program allows you to control a Roku device using a computer. It emulates a remote control by sending commands to the Roku device through HTTP requests. You can input a message, and the program will type it out on the Roku device using the virtual keyboard.

## Requirements

- Python 3.x
- `curl` command-line tool
- Access to a Roku device on the same network

## Installation

1. Clone the repository or download the `rokutyper.py` file to your local machine.
2. Make sure you have Python 3.x installed on your system.
3. Install the `curl` command-line tool if it is not already installed. You can download it from the official website or use a package manager specific to your operating system.
4. Ensure that your computer and the Roku device are connected to the same network.

## Usage

1. Open a terminal or command prompt and navigate to the directory where `typer.py` is located.
2. Run the program using the following command:

```shell
python rokutyper.py
```

3. The program will display a welcome message and prompt you to enter the Roku IP address. If you don't know the IP address of your Roku device, you can press enter to automate a quick nmap scan to find it.
4. Once the IP address is entered, the program will establish a connection with the Roku device and navigate to the search menu.
5. Enter the desired message you want to type on the Roku device. The message can contain lowercase letters, numbers, spaces, and special characters.
6. Press enter to initiate the typing process.
7. The program will simulate typing on the Roku device by sending appropriate HTTP requests to navigate the virtual keyboard and select each character.
8. Repeat steps 5-7 to type multiple messages.
9. To exit the program, press `Ctrl+C` in the terminal or command prompt.

## Notes

- The program uses the `curl` command-line tool to send HTTP requests. Make sure `curl` is installed and accessible from the command line.
- The program assumes the default port for Roku devices is `8060`. If your Roku device uses a different port, you may need to modify the URL in the program accordingly.
- The program uses a dictionary (`board`) to map each character to its corresponding position on the Roku keyboard. You can modify this dictionary if you want to change the mapping.
- The program sends HTTP requests to control the Roku device. Make sure your Roku device is powered on and connected to the network before running the program.
- This program is for educational purposes and assumes you have proper authorization to control the Roku device.

## Credits

- Author: Clempton
- Created: September 17, 2021
