from rest_framework import viewsets
from rest_framework.decorators import action
from api.classes import Commit
from api.decorator import wrapper_response
from api.request import get_request
from api.serializers import CommitSerializer


class CommitViewSet(viewsets.ModelViewSet):
    serializer_class = CommitSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    @wrapper_response
    @action(detail=True, methods=['get'], name='Get info about commit')
    def commit(self, request, *args, **kwargs):
        commit = {}
        sha_commit = kwargs['pk']
        data = get_request('commits/{}'.format(sha_commit))
        files = {}
        number_files = len(data['files'])
        counter_files = 0
        while counter_files < number_files:
            files[counter_files] = data['files'][counter_files]['filename']
            counter_files += 1
        commit['commit'] = Commit(
            date=data['commit']['author']['date'], message=data['commit']['message'],
            author=data['commit']['author']['name'], email=data['commit']['author']['email'],
            number_files=number_files, files=files
        )
        serializer = CommitSerializer(instance=commit.values(), many=True)
        return serializer.data
