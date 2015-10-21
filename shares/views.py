# Create your views here.
from django.http.response import Http404
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import Member
from members.permissions import IsOwnerOrAdmin
from shares.models import Shares, ShareType, SharePurchase, ShareTransfer
from shares.serializers import SharesSerializer,ShareTypeSerializer, SharePurchaseSerializer, ShareTransferSerializer, \
    SharesMinimalSerializer, ShareTransactionsSerializer, SharePurchasePostSerializer


class ShareList(APIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get(self, request, format=None):
        """
        Show a list of shares
        """
        shares = Shares.objects.all()
        serializer = SharesSerializer(shares,many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        """
        Add new share
        """
        serializer = SharesSerializer(data=request.DATA)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SharesView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)

    def get_member(self, pk):
        """
        Get a member.
        """
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self,  request, pk, format=None):
        """
        Show Member's shares
        """
        member = self.get_member(int(pk))
        self.check_object_permissions(request, member)
        shares = Shares.get_members_shares(member, )
        serializer = SharesMinimalSerializer(shares, many=True)
        return Response(serializer.data)


class ShareTypesView(APIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get(self, request, format=None):
        """
        List the share types
        """
        sharetype = ShareType.objects.all()
        serializer = ShareTypeSerializer(sharetype, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Add a share type
        """
        serializer = ShareTypeSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SharePurchasesView(APIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)

    def get_member(self, pk):
        """
        Get a member.
        """
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        List Share Purchase Transactions
        ---
        serializer: shares.serializers.SharePurchaseSerializer
        """
        if pk is not None:
            member = self.get_member(int(pk))
        else:
            member = None
        self.check_object_permissions(request, member)
        sharepurchase = SharePurchase.get_share_purchases(members=member)
        serializer = SharePurchaseSerializer(sharepurchase, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        """
        Purchase a share
        ---
        serializer: shares.serializers.SharePurchasePostSerializer
        """
        member = self.get_member(int(pk))
        self.check_object_permissions(request, member)
        serializer = SharePurchasePostSerializer(data=request.data)
        if serializer.is_valid():
            SharePurchase.issue_shares(member=member, shares=serializer.validated_data['number_of_shares'], share_type=serializer.validated_data['share_type'])
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShareTransfersView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrAdmin)

    def get_member(self, pk):
        """
        Get a member.
        """
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        List Share Transfer Transactions
        """
        if pk is not None:
            member = self.get_member(int(pk))
        else:
            member = None
        self.check_object_permissions(request, member)
        sharetransfer = ShareTransfer.get_share_transfers(members=member)
        serializer = ShareTransferSerializer(sharetransfer, many=True)
        return Response(serializer.data)


class ShareTransactionsView(APIView):
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrAdmin)

    def get_member(self, pk):
        """
        Get a member.
        """
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self,  request, pk, format=None):
        """
        List Member's savings Deposits
        """
        if pk is not None:
            member = self.get_member(int(pk))
        else:
            member = None
        self.check_object_permissions(request, member)
        transactions = Shares.get_share_transactions(member)
        serializer = ShareTransactionsSerializer(transactions, many=True)
        return Response(serializer.data)