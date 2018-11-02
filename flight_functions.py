"""Starter code for CSC108 Assignment 3"""

from typing import List, Set, Tuple
from flight_reader import AirportDict, RouteDict, AIRPORT_DATA_INDEXES

def get_airport_info(airports: AirportDict, iata: str, info: str) -> str:
    """Return the airport information for airport with IATA code iata for
    column info from AIRPORT_DATA_INDEXES.

    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA1', 'Name')
    'Apt1'
    >>> get_airport_info(TEST_AIRPORTS_DICT, 'AA4', 'IATA')
    'AA4'
    """
    if airports.__contains__(iata):
        return airports[iata][AIRPORT_DATA_INDEXES[info]]
    return None


def is_direct_flight(iata_src: str, iata_dst: str, routes: RouteDict) -> bool:
    """Return whether there is a direct flight from the iata_src airport to
    the iata_dst airport in the routes dictionary. iata_src may not
    be a key in the routes dictionary.

    >>> is_direct_flight('AA1', 'AA2', TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_direct_flight('AA2', 'AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """
    if routes.__contains__(iata_src):
        return routes[iata_src].__contains__(iata_dst)
    return False


def is_valid_flight_sequence(iata_list: List[str], routes: RouteDict) -> bool:
    """Return whether there are flights from iata_list[i] to iata_list[i + 1]
    for all valid values of i. IATA entries may not appear anywhere in routes.

    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    True
    >>> is_valid_flight_sequence(['AA3', 'AA1', 'AA2', 'AA1', 'AA2'], TEST_ROUTES_DICT_FOUR_CITIES)
    False
    """
    for i in range(len(iata_list) - 1):
        if not (iata_list[i] in routes.keys()):
            return False
        if not routes[iata_list[i]].__contains__(iata_list[i + 1]):
            return False
    return True


def count_outgoing_flights(iata: str, routes: RouteDict) -> int:
    """
    Return the amount of outgoing flights for the airport given the IATA code
    based on route information. 
    iata refers to IATA code; 
    routes refers to route information.
    
    >>> count_outgoing_flights('AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    2
    >>> count_outgoing_flights('AA4', TEST_ROUTES_DICT_FOUR_CITIES)
    1
    """
    if routes.__contains__(iata):
        return len(routes[iata])
    else:
        return 0


def count_incoming_flights(iata: str, routes: RouteDict) -> int:
    """
    Return the amount of incoming flights for the airport given the IATA code
    based on route information. 
    iata refers to IATA code; 
    routes refers to route information.
    >>> count_incoming_flights('AA1', TEST_ROUTES_DICT_FOUR_CITIES)
    2
    >>> count_incoming_flights('AA4', TEST_ROUTES_DICT_FOUR_CITIES)
    2
    """
    result = 0
    for i in routes.keys():
        if routes[i].__contains__(iata):
            result += 1
    return result


def reachable_destinations(iata: str, m: int, r: RouteDict) -> List[Set[str]]:
    """
    Return a list of the sets of IATA codes reachable from 
    the first parameter in steps from 0 up to (and including) 
    the maximum number of hops.
    iata refers to IATA of an airport;
    m refers to maximum number of flights;
    r refers to route information
    
    
    >>> result = reachable_destinations('AA1',2,{'AA1': {'AA2', 'AA4'},\
    'AA2': {'AA3'}, 'AA3': {'AA4', 'AA1'}, 'AA4': {'AA1'}})
    >>> compare = [{'AA1'}, {'AA4', 'AA2'}, {'AA3'}]
    >>> result == compare
    True
    >>> result = reachable_destinations('AA3',1,{'AA1': {'AA2', 'AA4'},\
    'AA2': {'AA3'}, 'AA3': {'AA4', 'AA1'}, 'AA4': {'AA1'}})
    >>> compare = [{'AA3'}, {'AA1', 'AA4'}]
    >>> result == compare
    True
    """
    count_step, dict_1, index, l, result = 0, {}, 0, set(), [{iata}]
    dict_1[iata] = 0
    while (count_step <= m - 1):
        for i in result[index]:
            if r.__contains__(i):
                for j in r[i]:
                    if not dict_1.__contains__(j):
                        l.add(j)
                        dict_1[j] = 0
        if l == set():
            for k in range(m - len(result) + 1):
                result.append(set())
                ii = k
                ii += 1
            return result
        result.append(l)
        l = set()
        index += 1
        count_step += 1
    return result

    
def find_busiest_airports(routes: RouteDict, limit: int) -> List[Tuple[str, int]]:
    """
    Return a list of tuple of n busiest airports. If n + 1 airport equals to
    the value of nth airport, then all airports at that value are excluded from
    output list.
    routes refers to route information;
    limit refers to the amount of busiest airports
    
    >>> find_busiest_airports({'AA1': {'AA2', 'AA4'}, \
    'AA2': {'AA3'}, 'AA3': {'AA4', 'AA1'}, 'AA4': {'AA1'}},3)
    [('AA1', 4), ('AA3', 3), ('AA4', 3)]
    >>> find_busiest_airports({'AA1': {'AA2', 'AA4'}, \
    'AA2': {'AA3'}, 'AA3': {'AA4', 'AA1'}, 'AA4': {'AA1'}},2)
    [('AA1', 4)]
    """
    l = {}
    for i in routes.keys():
        v = count_outgoing_flights(i, routes) +\
            count_incoming_flights(i, routes)
        if l.__contains__(v) and not i in l[v]:
            l[v].append(i)
            l[v].sort()
        elif not l.__contains__(v):
            l[v] = [i]
        for j in routes[i]:
            v = count_outgoing_flights(j, routes) +\
                count_incoming_flights(j, routes)
            if l.__contains__(v) and not j in l[v]:
                l[v].append(j)
                l[v].sort()
            elif not l.__contains__(v):
                l[v] = [j]
    key, result = reversed(sorted(list(l.keys()))), []
    for i in key:
        for j in l[i]:
            result.append((j, i))
    if len(result) <= limit:
        return(result)
    elif result[limit - 1][1] != result[limit][1]:
        return(result[:limit])
    while (limit != 0 and result[limit - 1][1] == result[limit][1]):
        limit = limit - 1
    return(result[:limit])
    
# Write the rest of the data analysis functions + your helper functions here








if __name__ == '__main__':
    """Uncommment the following as needed to run your doctests"""
    #from flight_types_constants_and_test_data import TEST_AIRPORTS_DICT
    #from flight_types_constants_and_test_data import TEST_AIRPORTS_SRC
    #from flight_types_constants_and_test_data import TEST_ROUTES_DICT_FOUR_CITIES
    #from flight_types_constants_and_test_data import TEST_ROUTES_SRC

    #import doctest
    #doctest.testmod()
