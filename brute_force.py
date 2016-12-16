def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    start = time.time()
    cowsCopy2 = cows.copy()
    cowsList2 = sorted(cowsCopy2.items(), key=lambda x: x[1], reverse=True)
    powerset = get_partitions(cowsCopy2)
    
    best_set = []
    max_trip_count = len(cowsList2)
    
    for Set in powerset:
        
        trip_sum = 0
        test = 0
        for trip in Set:
            
            trip_weight = 0
            for item in trip:
                trip_weight += cowsCopy2[item]
                trip_sum = trip_weight
                
            if trip_sum > 10:
                test += 0
            else:
                test += 1
            
        if len(Set) == test and test <= max_trip_count:
            max_trip_count = test
            best_set = Set
    end = time.time()
    print(end - start)
    return best_set
