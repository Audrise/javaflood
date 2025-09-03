import subprocess

ip = "127.0.0.1"
port = "25565"
s = 1
t = 1
p = 0
d = 0
# delay = 10

command = [
    "python3", "javaflood.py",
    "-ip", ip,
    "-port", port,
    "-s", str(s),
    "-t", str(t),
    "-p", str(p),
    "-d", str(d),
    # "-delay", str(delay)
]

try:
    subprocess.run(command)

except KeyboardInterrupt:
    exit()


