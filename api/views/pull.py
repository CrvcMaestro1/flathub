from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from api.classes import PullRequest
from api.request import get_request, get_user, patch_request, post_request, put_request
from api.serializers import PullRequestListSerializer, PullRequestCreateSerializer, PullRequestCloseSerializer
from flathub.settings import BASE_URL


class PullViewSet(viewsets.ModelViewSet):
    serializer_class = PullRequestCreateSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    def list(self, request, *args, **kwargs):
        result = {'status': True, 'message': ''}
        try:
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
            result['data'] = serializer.data
            return Response(result)
        except APIException as apiex:
            result['status'] = False
            result['message'] = str(apiex)
        except Exception as ex:
            result['status'] = False
            result['message'] = str(ex)
        return Response(result)

    def create(self, request, *args, **kwargs):
        result = {'status': True, 'message': ''}
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                pull_request = dict(serializer.validated_data)
                data = post_request('pulls', pull_request)
                if data['code'] == 201:
                    pull_created_number = data['text']['number']
                    del data['text']
                    if pull_request['state'] == 'merge':
                        merge = put_request('pulls/{}/merge'.format(pull_created_number), {})
                        data['code'] = merge['code']
                        if merge['code'] == 200:
                            result['message'] = 'Pull Request successfully created and merged'
                        else:
                            result['text'] = merge['text']
                    else:
                        result['message'] = 'Pull Request successfully created'
                else:
                    data['extra'] = "Most of the time this happens because the repository's owner restricted " \
                                    "or blocked you rights on editing. Contact the repository owner and ask him " \
                                    "to fix the permissions."
                result['data'] = data
            else:
                result['status'] = False
                result['message'] = 'There are errors in the data'
            return Response(result)
        except APIException as apiex:
            result['status'] = False
            result['message'] = str(apiex)
        except Exception as ex:
            result['status'] = False
            result['message'] = str(ex)
        return Response(result)


class PullCloseViewSet(viewsets.ModelViewSet):
    serializer_class = PullRequestCloseSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    def update(self, request, *args, **kwargs):
        result = {'status': True, 'message': ''}
        try:
            pull_number = self.request.POST['number']
            data = patch_request('pulls/{}'.format(pull_number), {"state": "closed"})
            if data['code'] == 200:
                del data['text']
                result['message'] = 'Status successfully changed'
            else:
                data['extra'] = "Most of the time this happens because the repository's owner restricted " \
                                "or blocked you rights on editing. Contact the repository owner and ask him " \
                                "to fix the permissions."
            result['data'] = data
            return Response(result)
        except APIException as apiex:
            result['status'] = False
            result['message'] = str(apiex)
        except Exception as ex:
            result['status'] = False
            result['message'] = str(ex)
        return Response(result)
