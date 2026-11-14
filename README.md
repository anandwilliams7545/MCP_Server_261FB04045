# Project README

**Name:** U ANAND WILLIAMS  
**Roll No:** 261FB04045

## Project Overview

This project is configured to launch a local Model Context Protocol (MCP) server named `helloMcp` from `server.py` using the Python interpreter in the project's `.venv` virtual environment.

## Project Files

- `.vscode/mcp.json` - VS Code MCP server configuration.
- `.venv/` - Python virtual environment.
- `server.py` - Expected MCP server entry point; add this file to run the configured server.


# Hello MCP Server – Function Explanations

## 1. Introduction

The Hello MCP Server is a simple Python-based Model Context Protocol (MCP) server. It demonstrates how to create and register tools using Python.

This server contains three tools:

1. `get_greeting()` – Generates a greeting message.
2. `add_numbers()` – Adds two integer numbers.
3. `is_prime()` – Checks whether a number is prime or not.

Each function is registered as an MCP tool using the `@mcp.tool()` decorator.

---

## 2. Importing MCP Server

```python
from mcp.server.mcpserver import MCPServer
```

### Explanation

- `mcp.server.mcpserver` provides the MCP server functionality.
- `MCPServer` is used to create an MCP server.
- It allows us to define and register tools that can be accessed by an MCP client.

---

## 3. Creating an MCP Server

```python
mcp = MCPServer("Hello MCP")
```

### Explanation

- This statement creates an MCP server instance.
- `"Hello MCP"` is the name of the server.
- The variable `mcp` is used to register tools and start the server.

---

## 4. Function 1: Get Greeting

### Code

```python
@mcp.tool()
def get_greeting(name: str) -> str:
    """Return a greeting for a student."""
    return f"Hello, {name}! Your first MCP tool works."
```

### Explanation

The `get_greeting()` function generates a personalized greeting message for a student.

- `@mcp.tool()` registers the function as an MCP tool.
- `name: str` accepts a student's name as a string.
- `-> str` indicates that the function returns a string.
- The `return` statement generates the greeting message.

### Example

**Input:**
```python
get_greeting("Anand")
```

**Output:**
```text
Hello, Anand! Your first MCP tool works.
```

### Applications

- Greeting students.
- Generating personalized messages.
- Testing basic MCP tool functionality.

---

## 5. Function 2: Add Numbers

### Code

```python
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
```

### Explanation

The `add_numbers()` function performs addition of two integer numbers.

- `@mcp.tool()` registers the function as an MCP tool.
- `a: int` represents the first integer.
- `b: int` represents the second integer.
- `-> int` indicates that the function returns an integer.
- `a + b` performs the addition operation.
55
## 6. Function 3: Prime Number Checker

### Code

```python
@mcp.tool()
def is_prime(n: int) -> str:
    """Check whether a number is prime or not."""

    if n <= 1:
        return f"{n} is not a prime number."

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f"{n} is not a prime number."

    return f"{n} is a prime number."
```

### Explanation

The `is_prime()` function checks whether a given integer is a prime number.

A prime number is a number greater than 1 that has exactly two factors: 1 and itself.3## 7. Starting the MCP Server

### Code

```python
if __name__ == "__main__":
    mcp.run()
```

### Explanation

- `if __name__ == "__main__":` checks whether the Python file is executed directly.
- `mcp.run()` starts the MCP server.
- After starting, the server can receive requests from a compatible MCP client.

---

## 8. Summary of MCP Tools

| Tool Name | Parameters | Purpose |
|---|---|---|
| get_greeting | name: str | Generates a greeting |
| add_numbers | a: int, b: int | Adds two numbers |
| is_prime | n: int | Checks prime numbers |

---

## 9. Conclusion

In this project, we developed a simple MCP server using Python.

We implemented three different tools: a greeting function, an addition function, and a prime number checker.

The `@mcp.tool()` decorator registers Python functions as tools that can be accessed through an MCP client.

This project demonstrates the basic working of MCP servers, tool registration, parameter handling, and function execution.

## Running in VS Code

Open this folder in VS Code with the MCP extension available. The server configuration runs:

```text
.venv/Scripts/python.exe server.py
```

Ensure `server.py` and any required Python dependencies are present in the project before starting the server.
