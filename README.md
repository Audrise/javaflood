<h1 align="center">
    <strong>JAVAFLOOD</strong>
</h1>

<div align=center>
    <strong>DoS Attack Tool for Minecraft Java</strong>
</div>
<br>

<div align=center>
    <img src="https://img.shields.io/badge/Python-FFDD00?style=for-the-badge&logo=python&logoColor=blue"/>
    <img src="https://img.shields.io/badge/Version-1.2-blue?style=for-the-badge"/>
    <br>
    <img src="https://img.shields.io/github/stars/Audrise/javaflood?style=social">
</div>

## Description
**JAVAFLOOD** is a tool designed for launching **Denial of Service (DoS)** attacks on Minecraft Java Edition servers. This tool floods the server with multiple methods to overload the server’s resources, resulting in an unresponsive state.

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

## Command-Line Arguments

| Argument | Required | Description                                                              |
| -------- | -------- | ------------------------------------------------------------------------ |
| `-ip`    | Yes      | Target server IP address **(e.g., `127.0.0.1`)**.                        |
| `-port`  | Yes      | Target server port **(must be an integer between `1` and `65535`)**.     |
| `-s`     | Yes      | Packet size **(must be an integer)**.                                    |
| `-t`     | Yes      | Number of threads **(must be an integer)**.                              |
| `-p`     | Yes      | Protocol version **(choose an integer value or set to `0` for random)**. |
| `-d`     | Yes      | Duration of the attack in seconds **(must be an integer)**.              |
| `-load`  | Optional | Path to a `.json` configuration file **(loads all parameters)**.         |
| `-delay` | Optional | Delay the attack by X seconds after all **required arguments are set.**  |
| `-api`   | Optional | Call the `api` function with the provided domain/IP and exit.            |
| `-h`     | No       | Show help message and exit.                                              |

## How to use

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Audrise/javaflood.git
    cd javaflood
    ```
2. Install the necessary Python libraries:
    ```bash
    pip3 install -r requirements.txt
    ```
   or
    ```bash
    pip3 install pystyle requests
    ```

3. To run `javaflood.py`, open a terminal and use the following command:
    ```bash
    python3 javaflood.py -ip [ ip address ] -port [ port ] -s [ packet size ] -t [ threads ] -p [ protocol ] -d [ duration ]
    ```

    Example
    ```bash
    python3 javaflood.py -ip 120.0.0.1 -port 25565 -s 100 -t 100 -p 47 -d 60
    ```
4. or you can use
    ```bash
    python3 javaflood.py -load <config.json>
    ```
    and don't forget to configure the attack in `config.json`


<br>

<h1 align="center">DISCLAIMER!</h1>

**JAVAFLOOD** is developed strictly for **educational** and **research** purposes within a **controlled environment**. This tool must only be used with the **explicit permission** of the **server owner**.

Any **unauthorized use**, including attempting to **disrupt**, **overload**, or **damage** servers, is strictly **prohibited** and may be considered **illegal** under applicable laws. Such actions can lead to **severe consequences** for both the target systems and the individuals involved.

Please use this tool **responsibly** and **only** for legitimate **security testing** and **academic purposes**. **Misuse** of this tool is **unethical**, potentially **unlawful**, and strongly **discouraged**.


## Credits
- Thanks to **[FiePaw](https://github.com/FiePaw)** to enable me to strengthen and modify the initial version of `JAVAFLOOD` that **[FiePaw](https://github.com/FiePaw)** developed
- Thanks to **[BillyTheGoat356](https://github.com/billythegoat356)** which provides the **[PyStyle](https://github.com/billythegoat356/pystyle.git)** module for very nice terminal styling and **[Hyperion](https://github.com/billythegoat356/hyperion.git)** for nice obfuscation tool
- Thanks to **[mcstatus.io](https://mcstatus.io)** which provides API to check minecraft server easily and quickly.

## **Latest Update**

### **1.2 - Usage of -load Parameter** 📌
By using the `-load` parameter, you can directly run the tool with the configuration set inside a `.json` file, without the need to manually input all the parameters. This is particularly useful for speeding up the setup process and running the tool with pre-configured settings.

#### **Example usage**
For example, if you have a configuration file named config.json that contains the default settings for the tool, you can run the tool with the following command:

```bash
python3 javaflood.py -load config.json
```
This will load all parameters from config.json and run the tool.

#### **JSON File Structure**
Make sure the `.json` file you create is formatted correctly, with the parameters expected by the tool. Here's an example of a valid JSON structure for this tool:

```bash
{
    "ip": "127.0.0.1",
    "port": 25565,
    "packet_size": 100,
    "threads": 100,
    "protocol": 0,
    "duration": 0
}
```
<h1></h1>
<h4 align="center">©AUDRISE</h4>
