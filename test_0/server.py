from bottle import get, run


def get_info(video_id):
    for x in xrange(999999):
        pass

    return video_id[::-1]


@get('/test/<video_id>')
def test(video_id):
    return {'video_id': get_info(video_id)}


if __name__ == "__main__":
    run(server="gunicorn", workers=8, port=2222,
        worker_class='egg:meinheld#gunicorn_worker')
