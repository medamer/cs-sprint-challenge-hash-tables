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
    route = [None]* length
    for i in range(length):
        if tickets[i].source == 'NONE':
            route[0] = tickets[i].destination
        cache[tickets[i].source] = tickets[i].destination
                    
            
    for i in range(length):
        if route[i-1] is not None: 
            route[i] = cache[route[i-1]]
            

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))