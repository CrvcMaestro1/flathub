from rest_framework import serializers

LIST_STATES = (
    ('open', 'open'),
    ('closed', 'closed'),
    ('merged', 'merged')
)

CREATE_STATES = (
    ('open', 'open'),
    ('merge', 'merge')
)


class BranchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    commits = serializers.CharField(max_length=256)


class BranchDetailSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    message = serializers.CharField(max_length=256)
    author = serializers.CharField(max_length=256)
    email = serializers.CharField(max_length=256)
    commit = serializers.CharField(max_length=256)


class CommitSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    message = serializers.CharField(max_length=256)
    author = serializers.CharField(max_length=256)
    email = serializers.CharField(max_length=256)
    number_files = serializers.IntegerField(default=0)
    files = serializers.JSONField()


class PullRequestListSerializer(serializers.Serializer):
    number = serializers.IntegerField(default=0)
    author = serializers.CharField(max_length=256)
    title = serializers.CharField(max_length=256)
    description = serializers.CharField(max_length=256)
    state = serializers.ChoiceField(choices=LIST_STATES)
    close_pull = serializers.CharField(max_length=256)


class PullRequestCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)
    body = serializers.CharField(max_length=256)
    head = serializers.CharField(max_length=256)
    base = serializers.CharField(max_length=256)
    state = serializers.ChoiceField(choices=CREATE_STATES)


class PullRequestCloseSerializer(serializers.Serializer):
    number = serializers.IntegerField(default=0)
