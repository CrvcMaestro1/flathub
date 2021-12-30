class Branch(object):
    def __init__(self, **kwargs):
        for field in ('name', 'commits'):
            setattr(self, field, kwargs.get(field, None))


class BranchDetail(object):
    def __init__(self, **kwargs):
        for field in ('date', 'message', 'author', 'email', 'commit'):
            setattr(self, field, kwargs.get(field, None))


class Commit(object):
    def __init__(self, **kwargs):
        for field in ('date', 'message', 'author', 'email', 'number_files', 'files'):
            setattr(self, field, kwargs.get(field, None))


class PullRequest(object):
    def __init__(self, **kwargs):
        for field in ('number', 'author', 'title', 'description', 'head', 'base', 'state', 'close_pull'):
            setattr(self, field, kwargs.get(field, None))
