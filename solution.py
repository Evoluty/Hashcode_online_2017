from consts import *


def add_video(server, video):
    if V.server_size_left[server] - V.videos_sizes[video] < 0:
        return False

    V.server_videos_stored[server].append(video)
    V.server_size_left[server] -= V.videos_sizes[video]
    return True


# Resolve the problem and put correct global variables
def solve():
    for i in range(V.number_caches_servers):
        for j in range(V.number_videos):
            if V.server_size_left[i] - V.videos_sizes[j] >= 0:
                add_video(i, j)
