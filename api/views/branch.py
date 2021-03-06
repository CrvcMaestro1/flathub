from rest_framework import viewsets
from rest_framework.decorators import action
from api.classes import Branch, BranchDetail
from api.decorator import wrapper_response
from api.request import get_request
from api.serializers import BranchSerializer, BranchDetailSerializer
from flathub.settings import BASE_URL


class BranchViewSet(viewsets.ModelViewSet):
    serializer_class = BranchSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    @wrapper_response
    def list(self, request, *args, **kwargs):
        branches = {}
        data = get_request('branches')
        for xid, datum in enumerate(data):
            commits = '{}/branch/{}/commits'.format(BASE_URL, datum['commit']['sha'])
            branches[xid] = Branch(name=datum['name'], commits=commits)
        serializer = BranchSerializer(instance=branches.values(), many=True)
        return serializer.data

    @wrapper_response
    @action(detail=True, methods=['get'], name='Get all commits by branch')
    def commits(self, request, *args, **kwargs):
        counter = 0
        commits = {}
        branch_name = kwargs['pk']
        data = get_request('commits/{}'.format(branch_name))
        while len(data['parents']) > 0:
            commits = self.append_commit(commits, data, counter)
            counter += 1
            data = get_request('commits/{}'.format(data['parents'][0]['sha']))
            if len(data['parents']) == 0:  # check last commit
                commits = self.append_commit(commits, data, counter)
                counter += 1
        serializer = BranchDetailSerializer(instance=commits.values(), many=True)
        return serializer.data

    def append_commit(self, commits, data, counter):
        commit = '{}/commits/{}/commit'.format(BASE_URL, data['sha'])
        commits[counter] = BranchDetail(
            date=data['commit']['author']['date'], message=data['commit']['message'],
            author=data['commit']['author']['name'], email=data['commit']['author']['email'],
            commit=commit
        )
        return commits
