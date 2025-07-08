<h1 align="center">MCFLOOD</h1>

<div align=center>
    <strong>DoS Attack Tool for Minecraft Java</strong>
</div>
<br>

<div align=center>
    <img src="https://img.shields.io/badge/Python-FFDD00?style=for-the-badge&logo=python&logoColor=blue"/>
    <img src="https://img.shields.io/badge/Version-1.2 AF-blue?style=for-the-badge"/>
    <br>
    <img src="https://img.shields.io/github/stars/Audrise/mcflood?style=social">
</div>

## Description
**MCFLOOD** is a tool designed for launching **Denial of Service (DoS)** attacks on Minecraft Java Edition servers. This tool floods the server with multiple methods to overload the server’s resources, resulting in an unresponsive state.

## Features
- **Multithreading**:
    - Uses a lock mechanism to ensure that multiple operations

- **TCP Handshake Flooding**:
   - Repeatedly initiates TCP handshakes to consume server socket resources.

- **Minecraft Protocol Abuse**:
    - Crafts and sends fake Minecraft handshake packets to simulate player connections.

- **Multi-threaded Packet Spamming**:
    - Launches multiple threads to flood the server with packets in parallel.

- **Payload Padding**:
    - Adds random bytes to increase packet size and obfuscate attack patterns.

- **Connection Reuse**:
    - Sends multiple forged packets over the same TCP connection to maximize impact.

- **Rapid Connect-Disconnect Loops**:
    - Quickly opens and closes connections to exhaust server capacity.

- **Protocol Version Spoofing**:
    - Sends handshake packets using spoofed or invalid protocol versions to trigger unexpected server behavior.

- **Check Server Status**:
    - To check the server status directly with the api provided by **[mcstatus.io](https://mcstatus.io)**. Use the parameter **python3 bedflood.py -api < IP Address >**

## How to use
1. You must have **Python 3.xx**. If you don't have it you can download and install **Python** from [here](https://www.python.org/downloads/).<br>
    After that run this command in your terminal
    ```bash
    python3 --version
    ```
2. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/Audrise/mcflood.git
    cd mcflood
    ```
3. Install the necessary Python libraries:
    ```bash
    pip3 install -r requirements.txt
    ```
   Or
    ```bash
    pip3 install pystyle requests
    ```

4. To run MCFLOOD, open a terminal and use the following command:
    ```bash
    python3 mcflood.py -ip [ ip address ] -port [ port ] -s [ packet size ] -t [ threads ] -p [ protocol ] -d [ duration ]
    ```

    Addition
    ```bash
    -c [ Show Credit ] -input [ Switch to input mode ]
    ```

    Example
    ```bash
    python3 mcflood.py -ip 120.0.0.1 -port 25565 -s 100 -t 100 -p 47 -d 60
    ```
<br>

<h1 align="center">WARNING</h1>

**MCFLOOD** is developed strictly for **educational** and **research** purposes within a **controlled environment**. This tool must only be used with the **explicit permission** of the **server owner**.

Any **unauthorized use**, including attempting to **disrupt**, **overload**, or **damage** servers, is strictly **prohibited** and may be considered **illegal** under applicable laws. Such actions can lead to **severe consequences** for both the target systems and the individuals involved.

Please use this tool **responsibly** and **only** for legitimate **security testing** and **academic purposes**. **Misuse** of this tool is **unethical**, potentially **unlawful**, and strongly **discouraged**.

## Ethical Guidelines
- **Do not use this tool on any server without explicit permission.**
- **Only use this tool in a controlled environment, such as a local server.**
- **Educate others on the risks and consequences of launching DoS/DDoS attacks.**
- **Never attempt to attack a public or private server without authorization.**

## Credits
- Thanks to **[FiePaw](https://github.com/FiePaw)** to enable me to strengthen and modify the initial version of **[MCFLOOD](https://github.com/Audrise/mcflood.git)** that **[FiePaw](https://github.com/FiePaw)** developed
- Thanks to **[BillyTheGoat356](https://github.com/billythegoat356)** which provides the **[PyStyle](https://github.com/billythegoat356/pystyle.git)** module for very nice terminal styling and **[Hyperion](https://github.com/billythegoat356/hyperion.git)** for nice obfuscation tool
- Thanks to **[mcstatus.io](https://mcstatus.io)** which provides API to check server easily and quickly.
