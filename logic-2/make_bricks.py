''' We want to make a row of bricks that is goal inches long. We have a number
of small bricks (1 inch each) and big bricks (5 inches each). Return True if it
is possible to make the goal by choosing from the given bricks. This is a
little harder than it looks and can be done without any loops. '''


def make_bricks(small, big, goal):
    if small + big * 5 >= goal:
        big_needed = goal // 5
        big_matched = big_needed if big_needed <= big else big
        if goal - big_matched * 5 <= small:
            return True
    return False
