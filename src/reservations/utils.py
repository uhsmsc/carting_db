def get_answer_format(data):
    res = []
    for item in data:
        sampler = {}
        attrs = list(item.__dict__.keys())
        attrs.pop(0)
        for attr in attrs:
            value = getattr(item, attr)
            sampler[attr] = value

        res.append(
            sampler
        )
    return res