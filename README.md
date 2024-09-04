# Robot Communication System (RCS)

**RCS** is a tool that allows you to connect controls, transfer data, and send commands from your computer to any Single Board Computer (SBC), such as a Raspberry Pi, using WebSockets. This system facilitates real-time interaction between your computer and your robot or SBC device, enabling remote control of the hardware efficiently and reliably.

## Project Structure

The project is organized into two levels:

1. **Basic files (./):**
   - `client.py`
   - `server.py`

   These two files provide a simple example of how the library works using WebSockets and the `pynput` library to capture keyboard inputs. They are useful for quickly understanding the communication system, but they are not recommended for more advanced projects.

2. **RCS folder (./RCS/):**
   - Contains a complete implementation of the library using Object-Oriented Programming (OOP), making it more robust, scalable, and maintainable.

## Recommendation

While the files in the root directory (`client.py` and `server.py`) are useful as an introductory example, **we strongly recommend using the complete OOP implementation found in the `./RCS/` folder** for your projects. This implementation is much more flexible and allows for better code organization, making it easier to extend and maintain the system in the long run.

## How Does RCS Work?

**RCS** is based on WebSockets to establish a bidirectional connection between your computer and the SBC device. Through this connection, you can:

- **Send commands** from your computer that will be executed on the SBC device.
- **Receive real-time data** from the SBC to your computer.
- **Control hardware** connected to the SBC using keyboard inputs or any other input device, such as joysticks.

### Key Features:

- **WebSockets**: Enable real-time, fast, and efficient communication between your computer and the SBC.
- **Pynput**: Facilitates capturing keyboard input events on the computer to be sent to the SBC.
- **Scalable**: The OOP implementation makes it easy to extend the system to adapt to different types of devices and communications.

## How to Use RCS

1. **Install dependencies:**
   Make sure to install the necessary libraries before running the files:

   ```bash
   pip install pynput
   ```

2. **Basic Example (./client.py and ./server.py):**

   If you just want to quickly test how the system works on a basic level, you can run the `client.py` and `server.py` files directly from the root folder:

   - Run `server.py` on the SBC device.
   - Run `client.py` on your computer to establish the connection and start sending commands.

3. **OOP Implementation (./RCS/):**

   For a more advanced and production-ready implementation, use the code within the `./RCS/` folder. This code is better structured and follows Object-Oriented Programming principles, allowing you to customize and scale the system more easily.

   - Follow the usage instructions within the code in the `./RCS/` folder to set up and run the system.

## Project Structure

```plaintext
.
├── client.py          # Basic client example connecting to the SBC
├── server.py          # Basic server example running on the SBC
└── RCS/               # Folder containing the full OOP implementation of the system
    ├── __init__.py    # Module initialization file
    ├── client.py      # Client code in OOP
    ├── server.py      # Server code in OOP
    └── ...            # Other files and classes supporting the implementation
```

## Contributions

If you have ideas for improvements, fixes, or new features, feel free to contribute to the project via pull requests or by creating issues. Your input is welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.