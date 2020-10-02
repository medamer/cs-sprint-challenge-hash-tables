#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.next = None


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    for i in range(length):
        if tickets[i].source is None:
            cache[tickets[i].source] = tickets[i].destination
        elif tickets[i].source:
            
            
    route = []
    for t in cache:
        for k, v in cache.items():
            if k is None:
                route.append(v)
            elif k in t.destination:

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))