from consts import *


# Export global variables into output file
def export_output(file_name):
    with open(file_name, 'w') as f:
        used_servers = filter(lambda x: len(x) > 0, V.cache_servers)

        for i, s in enumerate(used_servers):
            videos = " ".join(s)
            f.write("{} {}\n".format(i, videos))
