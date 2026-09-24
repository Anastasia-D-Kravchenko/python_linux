# Python practice: fundamentals, sockets, threading

Small, runnable exercises I wrote while working through Python fundamentals and basic network programming (university coursework plus self-study).

## What's inside

| Path | Topic |
|---|---|
| `RedTeam/HelloWorld.py`, `Variables.py`, `TypeCasting.py`, `Operators.py` | Basics: variables, type casting, operators |
| `RedTeam/IfElse.py`, `Loops.py` | Control flow |
| `RedTeam/Lists.py`, `Tuples.py`, `Dictionary.py` | Built-in collections |
| `RedTeam/Classes/`, `RedTeam/Inheritance/` | OOP: classes, inheritance (`Account` → `CheckingAccount`) |
| `RedTeam/ErrorHandling.py`, `Logging.py` | Exceptions and the `logging` module |
| `RedTeam/Configs/` | Reading settings from an `.ini` file with `configparser` |
| `RedTeam/Modules.py` | Modules and imports |
| `RedTeam/Threading.py`, `Threading 2.py`, `threading.py` | Threads and synchronisation |
| `RedTeam/Sockets/` | TCP client and server with the `socket` module |
| `dnsenum.py` | Small helper that resolves a list of subdomains with the system `host` command |

## Run

```bash
python3 RedTeam/HelloWorld.py

# sockets: start the server in one terminal, the client in another
python3 RedTeam/Sockets/SocketsServer.py
python3 RedTeam/Sockets/SocketsClient.py
```

Requires Python 3.8+ and the standard library only. `dnsenum.py` uses the `host` utility (macOS/Linux) and should only be pointed at domains you own or are allowed to query.

## License

MIT, see [LICENSE](LICENSE).
