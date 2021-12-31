from rest_framework import viewsets, status
from api.classes import PullRequest
from api.decorator import wrapper_response
from api.messages import PULL_MERGED, PULL_CREATED, PERMISSION_DENIED, INVALID_DATA, STATUS_CHANGED
from api.request import get_request, get_user, patch_request, post_request, put_request
from api.serializers import PullRequestListSerializer, PullRequestCreateSerializer, PullRequestCloseSerializer
from flathub.settings import BASE_URL


class PullViewSet(viewsets.ModelViewSet):
    serializer_class = PullRequestCreateSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    @wrapper_response
    def list(self, request, *args, **kwargs):
        pulls = {}
        data = get_request('pulls?state=all')
        for xid, datum in enumerate(data):
            close_pull = None
            state = 'closed'
            if not datum['merged_at'] is None:
                state = 'merged'
            elif datum['state'] == 'open':
                state = 'open'
                close_pull = '{}/pull/{}'.format(BASE_URL, datum['number'])
            author = get_user(datum['user']['login'])
            pulls[xid] = PullRequest(
                number=datum['number'], author=author['name'], title=datum['title'], description=datum['body'],
                state=state, close_pull=close_pull
            )
        serializer = PullRequestListSerializer(instance=pulls.values(), many=True)
        return serializer.data

    @wrapper_response
    def create(self, request, *args, **kwargs):
        data = {}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            pull_request = dict(serializer.validated_data)
            data = post_request('pulls', pull_request)
            if data['code'] == status.HTTP_201_CREATED:
                pull_created_number = data['text']['number']
                del data['text']
                if pull_request['state'] == 'merge':
                    merge = put_request('pulls/{}/merge'.format(pull_created_number), {})
                    data['code'] = merge['code']
                    if merge['code'] == status.HTTP_200_OK:
                        data['message'] = PULL_MERGED
                    else:
                        data['text'] = merge['text']
                else:
                    data['message'] = PULL_CREATED
            else:
                data['extra'] = PERMISSION_DENIED
            return data
        else:
            data['message'] = INVALID_DATA
        return data


class PullCloseViewSet(viewsets.ModelViewSet):
    serializer_class = PullRequestCloseSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    @wrapper_response
    def update(self, request, *args, **kwargs):
        pull_number = self.request.POST['number']
        data = patch_request('pulls/{}'.format(pull_number), {"state": "closed"})
        if data['code'] == status.HTTP_200_OK:
            del data['text']
            data['message'] = STATUS_CHANGED
        else:
            data['extra'] = PERMISSION_DENIED
        return data
