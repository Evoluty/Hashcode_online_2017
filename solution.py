from consts import *


def add_video(server, video):
    V.server_videos_stored[server].append(video)
    V.server_size_left[server] -= V.videos_sizes[video]


# Resolve the problem and put correct global variables
def solve():
    # Init the two variables needed to solve the problem
    V.server_videos_stored = [[] for _ in range(V.number_caches_servers)]
    V.server_size_left = [V.size_caches_servers for _ in range(V.number_caches_servers)]

    for i in range(V.number_caches_servers):
        for j in range(V.number_videos):
            if V.server_size_left[i] - V.videos_sizes[j] >= 0:
                add_video(i, j)
