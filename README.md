<h1 align="center">
    <strong>JAVAFLOOD</strong>
</h1>

<div align=center>
    <strong>DoS Attack Tool for Minecraft Java</strong>
</div>
<br>

<div align=center>
    <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Python 3-FFDD00?style=for-the-badge&logo=python&logoColor=blue"/>
    </a>
    <img src="https://img.shields.io/badge/JAVAFLOOD-1.2.1-blue?style=for-the-badge"/>
    <br>
    <img src="https://img.shields.io/github/stars/Audrise/javaflood?style=social"/>
    <img src="https://img.shields.io/github/forks/Audrise/javaflood?style=social"/>
    <br>
</div>
<br>

<h1 align="center">DISCLAIMER!</h1>

**JAVAFLOOD** is a tool designed for launching **Denial of Service (DoS)** attacks on Minecraft Java Edition servers. This tool floods the server with multiple methods to overload the server’s resources, resulting in an unresponsive state.

Any **unauthorized use**, including attempting to **disrupt**, **overload**, or **damage** servers, is strictly **prohibited** and may be considered **illegal** under applicable laws. Such actions can lead to **severe consequences** for both the target systems and the individuals involved.

Please use this tool **responsibly** and **only** for legitimate **security testing** and **academic purposes**. **Misuse** of this tool is **unethical**, potentially **unlawful**, and strongly **discouraged**.

**The developer of this tool only created it for educational and research purposes within a controlled environment and does not take any responsibility for any misuse, damage, or legal consequences resulting from intentional or unauthorized use by others.**

## Table of Contents
* **[Features](#features)**
* **[Usage](#usage)**
* **[Arguments](#arguments)**
* **[Credits](#credits)**
* **[Updates](#updates)**

## Features
- **TCP Handshake Flooding**:
   - Repeatedly initziates `TCP handshakes` to consume server socket resources.

- **Connection Reuse**:
    - Sends multiple forged packets over the same `TCP connection` to maximize impact.

- **Multithreading**:
    - Uses `ThreadPoolExecutor` to run multiple threads for parallel packet sending.

- **Thread Synchronization**:
    - The monitoring thread runs in the background as a `daemon threads`

- **Minecraft Protocol Abuse**:
    - Crafts and sends fake Minecraft handshake packets to simulate player connections.

- **Payload Padding**:
    - Adds random bytes to increase packet size and obfuscate attack patterns.

- **Rapid Connect-Disconnect Loops**:
    - Quickly opens and closes connections to exhaust server capacity.

- **Protocol Version Spoofing**:
    - Sends handshake packets using spoofed or invalid protocol versions to trigger unexpected server behavior.

- **Check Server Status**:
    - To check the server status directly with the api provided by **[mcstatus.io](https://mcstatus.io)**. Use the parameter `python3 javaflood.py -api < IP/Domain >`

## Arguments

| Argument | Required | Description                                                     |
| -------- | -------- | --------------------------------------------------------------- |
| -ip      | Yes      | Defines the destination server IP address (e.g., 127.0.0.1).    |
| -port    | Yes      | Specifies the target port (must integer between 1 and 65535).   |
| -s       | Yes      | Configures the size (in bytes) of each transmitted packet.      |
| -t       | Yes      | Determines the number of parallel execution threads.            |
| -p       | Yes      | Sets the protocol version to be used during execution.          |
| -d       | Yes      | Controls the total execution time (in seconds).                 |
| -api     | Optional | Call the API function from mcstatus with the domain.            |
| -load    | Optional | Loads external configuration from a specified JSON file path.   |
| -wait    | Optional | Delays execution by a specified number of seconds.              |
| -art     | Optional | Toggles visibility of the logo (1 = show, 0 = hide).            |
| -h       | No       | Show this help message and exit.                                |

## Usage

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Audrise/javaflood.git
    ```

    ```bash
    cd javaflood
    ```
2. Install the necessary Python libraries:
    ```bash
    pip3 install -r requirements.txt
    ```

3. Run javaflood using several methods as below:
    ```bash
    python3 javaflood.py -ip 120.0.0.1 -port 25565 -s 100 -t 100 -p 47 -d 60 -wait 10 -art 0
    ```
    or you can use -load parameter:
    ```bash
    python3 javaflood.py -load config.json
    ```

## Credits
- Thanks to **[FiePaw](https://github.com/FiePaw)** for allowing me to fortify and modify the initial version of **JAVAFLOOD** developed by FiePaw.
- Thanks to **[BillyTheGoat356](https://github.com/billythegoat356)** which provides the **[PyStyle](https://github.com/billythegoat356/pystyle.git)** module for very nice terminal styling and **[Hyperion](https://github.com/billythegoat356/hyperion.git)** for nice obfuscation tool
- Thanks to **[mcstatus.io](https://mcstatus.io)** which provides API to check minecraft server easily and quickly.

## Updates

### **1.2.1 - Usage of -load parameter** 📌
By using the `-load` parameter, you can directly run the tool with the configuration set inside a `.json` file, without the need to manually input all the parameters. This is particularly useful for speeding up the setup process and running the tool with pre-configured settings.

#### **Example usage**
For example, if you have a configuration file named config.json that contains the default settings for the tool, you can run the tool with the following command:

```bash
python3 javaflood.py -load config.json
```
This will load all parameters from `config.json` and run the tool.

#### **JSON File Structure**
Make sure the `.json` file you create is formatted correctly, with the parameters expected by the tool. Here's an example of a valid JSON structure for this tool:

```bash
{
    "ip": "127.0.0.1",
    "port": 25565,
    "packet_size": 0,
    "threads": 0,
    "protocol": 0,
    "duration": 0,
    "wait": 60,
    "art": 0
}
```
<h1></h1>
<h4 align="center">©AUDRISE</h4>
