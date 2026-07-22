from ticket_system import *

initialize_database()

ticket = create_ticket(
    "VPN Authentication Failed"
)

print("Created Ticket:", ticket)

print()

tickets = get_all_tickets()

for t in tickets:
    print(t)