from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from members.models import Member, Group
from members.serializers import MemberSerializer, GroupSerializer, GroupMemberSerializer


class MemberList(APIView):
    """
    List all members, or create a new member.
    """

    def get(self, request, format=None):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupList(APIView):
    """
    List all group, or create a new group.
    """

    def get(self, request, format=None):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberDetail(APIView):
    """
    Retrieve, update or delete a Member.
    """

    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupDetail(APIView):
    """
    Retrieve, update or delete a Group.
    """

    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        group = self.get_object(pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupMember(APIView):
    """
    Retrieve, update or delete a Group Member.
    """

    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        groupmember = self.get_object(pk)
        serializer = GroupMemberSerializer(groupmember)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        groupmember = self.get_object(pk)
        serializer = GroupMemberSerializer(groupmember, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        groupmember = self.get_object(pk)
        groupmember.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    """
@api_view(['GET', 'POST'])
def member_list(request):
    """
    # List all members, or create a new member.
    """
    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def group_list(request):
    """
    #List all groups, or create a new group.
    """
    if request.method == 'GET':
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def member_detail(request, pk):
    """
    #Retrieve, update or delete a member.
    """
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(member, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def group_detail(request, pk):
    """
    #Retrieve, update or delete a member group.
    """
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GroupSerializer(group, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
"""