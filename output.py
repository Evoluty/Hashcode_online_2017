from consts import *


# Export global variables into output file
def export_output(file_name):
    with open(file_name, 'w') as f:
        # Write first line
        number_used_servers = len(list(filter(lambda x: len(x) > 0, V.server_videos_stored)))
        f.write("{}\n".format(number_used_servers))

        # Write other lines
        for i, s in enumerate(V.server_videos_stored):
            videos = " ".join(map(str, s))
            f.write("{} {}\n".format(i, videos))
