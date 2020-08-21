def get_range_times(count, gap):
    times, remainder = divmod(count, gap)
    if remainder > 0 and times:
        times += 2
    else:
        times = 1
    return times
    