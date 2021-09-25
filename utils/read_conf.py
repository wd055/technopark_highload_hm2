from utils import config


def save_config(path: str):
    conf = {}
    file = open(path)
    for line in file:
        key, value = map(lambda x: x.strip(), line.split(" ", 1))
        conf[key] = value
    file.close()

    try:
        config.CPU_LIMIT = int(conf['cpu_limit'])
        config.DOCUMENT_ROOT = conf['document_root']
    except Exception as e:
        print('Fail parse config', str(e))
    print(f'Config {path} parsed')
