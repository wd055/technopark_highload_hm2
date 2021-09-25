from utils import read_conf, consts
from prefork import server


if __name__ == '__main__':
    read_conf.save_config(consts.CONFIG_PATH)
    server = server.Server()
    server.run_socket()
    server.prefork()
