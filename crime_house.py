import sys


class CrimeTime(Exception):
    pass


class CrimeHouseBeliefState:
    def __init__(self):
        self.criminals_inside = []
        self.criminals_outside = []
        self.masked_entries = 0
        self.masked_exits = 0
        self.total_inside = 0

    def process_entry(self, criminal):
        self.total_inside += 1
        if criminal == 0:
            self.masked_entries += 1

        else:
            if criminal in self.criminals_inside:
                # we just saw somebody enter who we thought was already inside!
                if self.masked_exits == 0:
                    # and there are no unaccounted for masked exits
                    # it's CRIME TIME
                    raise CrimeTime()

                else:
                    # it's possible that it was a masked guy who we saw leave
                    self.masked_exits -= 1

            elif criminal in self.criminals_outside:
                # ok, now we believe he's inside
                self.criminals_outside.remove(criminal)
                self.criminals_inside.append(criminal)

            else:
                if self.masked_exits > 0:
                    # this could be a masked guy coming back in
                    self.masked_exits -= 1

                self.criminals_inside.append(criminal)

    def process_exit(self, criminal):
        # the running total is never allowed to go negative
        if self.total_inside > 0:
            self.total_inside -= 1
        if criminal == 0:
            self.masked_exits += 1

        else:
            if criminal in self.criminals_outside:
                # we just saw somebody leave who we thought was already
                # outside!
                if self.masked_entries == 0:
                    # and there are no unaccounted for masked entries
                    # it's CRIME TIME
                    raise CrimeTime()

                else:
                    # it's possible that it was a masked guy who we saw leave
                    self.masked_entries -= 1

            elif criminal in self.criminals_inside:
                # ok, now we believe he's outside
                self.criminals_inside.remove(criminal)
                self.criminals_outside.append(criminal)

            else:
                if self.masked_entries > 0:
                    # this could be a masked person leaving
                    self.masked_entries -= 1

                self.criminals_outside.append(criminal)

    def count_criminals(self):
        num_criminals = (
            self.total_inside
        )
        return max((num_criminals, 0))


def parse_line(l):
    num_events, events_s = l.split(';')
    events_s = events_s.strip()
    event_strings = events_s.split('|')
    events = []
    for event_string in event_strings:
        event_type, criminal = event_string.split(" ")
        criminal = int(criminal)
        events.append((event_type, criminal))

    return events


def process_line(l):
    events = parse_line(l)

    try:
        c = CrimeHouseBeliefState()
        for event in events:
            event_type, criminal = event
            if event_type == 'E':
                c.process_entry(criminal)
            elif event_type == 'L':
                c.process_exit(criminal)
        print(c.count_criminals())

    except CrimeTime:
        print("CRIME TIME")

if __name__ == '__main__':
    with open(sys.argv[1]) as lines:
        for line in lines:
            if not line.strip():
                continue
            process_line(line)
