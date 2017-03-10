from consts import *


# Reads next line of a given file and returns an array of words
def next_line(file):
    res = file.readline()
    if res:
        res = res.replace('\n', "").split(" ")
    return res


# Import data from input files into global variables
def import_input(file_name):
    with open(file_name, 'r') as f:
        # Read first line
        first_line = next_line(f)
        V.number_videos, V.number_endpoints, V.number_requests, V.number_caches_servers, V.size_caches_servers = map(int, first_line)

        # Read second line
        second_line = next_line(f)
        V.videos_sizes = list(map(int, second_line))

        # Read endpoints
        for i in range(V.number_endpoints):
            ep = next_line(f)
            latency, connected_caches = map(int, ep)

            cache_latency = [[0] for _ in range(V.number_caches_servers)]
            for j in range(connected_caches):
                c = next_line(f)
                index, value = map(int, c)
                cache_latency[index] = value

            V.endpoints.append({
                "data_center": latency,
                "caches": cache_latency
            })

        # Rest of inputs
        line = next_line(f)
        while line:
            video, ep, number = map(int, line)
            r = {
                "video": video,
                "ep": ep,
                "number": number
            }
            V.requests.append(r)
            line = next_line(f)
