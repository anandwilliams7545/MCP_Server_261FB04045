
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Hello MCP")


@mcp.tool()
def get_greeting(name: str) -> str:
    """Return a greeting for a student."""
    return f"Hello, {name}! Your first MCP tool works."


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def is_prime(n: int) -> str:
    """Check whether a number is prime or not."""

    if n <= 1:
        return f"{n} is not a prime number."

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f"{n} is not a prime number."

    return f"{n} is a prime number."


if __name__ == "__main__":
    mcp.run()
