#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    # Setting up a data structure, that contains a hashtable of tickets, and a list that will contain our final route
    ticket_collection = {}
    route = []

    # populate our hashtable with all of the tickets - key = origin, value = destination
    for ticket in tickets:
        ticket_collection[ticket.source] = ticket.destination

    # start off with our "home" location (looking at the key)
    cur = ticket_collection['NONE']

    # now we run through the tickets, looking at the key, and
    # begin populating our route with the data we need (linking the value with the next key)
    while cur != 'NONE':
        route.append(cur)
        cur = ticket_collection[cur]

    route.append('NONE')
    return route

