def destCity(paths: list) -> str:
    dc = {}
    for path in paths:
        dc[path[0]] = path[1]
    for path in paths:
        if dc.get(path[1]) is None:
            return path[1]