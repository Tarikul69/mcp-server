from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("LeaveManager")


# Tool: Submit a leave request
@mcp.tool()
def submit_leave(name: str, leave_type: str, start_date: str, end_date: str, reason: str) -> str:
    """Submit a leave request."""
    # In real apps, you'd store this in a DB
    return (f"Leave request submitted by {name} for {leave_type} leave from "
            f"{start_date} to {end_date}. Reason: {reason}")


# Tool: Get the status of a leave request (dummy logic)
@mcp.tool()
def get_leave_status(request_id: str) -> str:
    """Check the status of a leave request by request ID."""
    # Dummy status lookup
    return f"Request {request_id} is currently pending approval."


# Resource: List all leave requests (dummy data)
@mcp.resource("leave://all")
def list_all_leaves() -> list:
    """Return a list of all leave requests (mocked)."""
    return [
        {"id": "REQ123", "name": "Alice", "status": "Approved"},
        {"id": "REQ124", "name": "Bob", "status": "Pending"},
        {"id": "REQ125", "name": "Charlie", "status": "Rejected"},
    ]

f
# Prompt: Generate leave approval message
@mcp.prompt()
def approve_leave_prompt(name: str, days: int, leave_type: str) -> str:
    """Generate a message to approve a leave request."""
    return f"Dear {name}, your {leave_type} leave for {days} days has been approved. Please make sure your handover is complete."


# Prompt: Generate rejection message
@mcp.prompt()
def reject_leave_prompt(name: str, reason: str) -> str:
    """Generate a message to reject a leave request."""
    return f"Dear {name}, your leave request has been rejected due to the following reason: {reason}."

