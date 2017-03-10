from consts import *
from input import next_line, import_input
from solution import add_video


def server_contains_video(server, video):
    return video in V.server_videos_stored[server]


def min_latency(ep, video):
    mini = V.endpoints[ep]["data_center"]

    servers_available = []
    for i, v in enumerate(V.endpoints[ep]["caches"]):
        if server_contains_video(i, video):
            servers_available.append(v)
    servers = list(filter(lambda x: x > 0, servers_available))
    for i, v in enumerate(servers):
        if v < mini:
            mini = v
    return mini


def earned_time(ep, video):
    return V.endpoints[ep]["data_center"] - min_latency(ep, video)


def rank(input_file, output_file):
    score = 0
    total_requests = 0
    # Resets global var
    import_input(input_file)

    # We check if input is valid and import it in variables
    with open(output_file, 'r') as f:
        # First line
        number_line = list(map(int, next_line(f)))[0]
        # Other lines
        for _ in range(number_line):
            line = next_line(f)
            if not line:
                break

            line = list(map(int, line))
            server = line.pop(0)
            videos = line

            for i, v in enumerate(videos):
                if not add_video(server, v):
                    print("Cannot add video {} in server {}".format(v, server))
                    exit(1)

    # We go through requests and get score each time
    for i, p in enumerate(V.requests):
        ep, video, nb_rq = p["ep"], p["video"], p["number"]
        time_saved = earned_time(ep, video) * nb_rq
        total_requests += nb_rq
        score += time_saved

    score = int(score*1000/total_requests)

    return score
