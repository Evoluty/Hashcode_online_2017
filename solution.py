from consts import *


# Resolve the problem and put correct global variables
def solve():
    V.cache_servers = [[] for i in range(V.number_caches_servers)]

    print("number video: " + str(V.number_videos))
    print("number ep: " + str(V.number_endpoints))
    print("number rq: " + str(V.number_requests))
    print("number caches: " + str(V.number_caches_servers))
    print("size caches: " + str(V.size_caches_servers))
    print("Videos sizes: ")
    print(str(V.videos_sizes))
    print("endpoints: ")
    print(V.endpoints)
    print("requests: ")
    print(V.requests)
