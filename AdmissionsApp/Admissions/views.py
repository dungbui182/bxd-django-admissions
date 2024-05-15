from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions,generics
from Admissions.models import *
from Admissions.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from Admissions import paginators, serializers
# Create your views here.
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, ]
    #permission_classes = [permissions.IsAuthenticated]

    """
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    """
    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(first_name__icontains=q)
        return queries

    @action(methods=['get'], detail=True)
    def comment(self, request, pk):
        comment = self.get_object().comments_set.filter(active=True).all()

        return Response(serializers.CommentsSerializer(comment, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def question(self, request, pk):
        question = self.get_object().questions_set.filter(active=True).all()

        return Response(serializers.QuestionsSerializer(question, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class FacultyViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView,):
    queryset = Faculty.objects.filter(active=True)
    serializer_class = FacultySerializer
    parser_classes = [MultiPartParser, ]

    """
    def get_permissions(self):
        #everyone has permission to see
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        #but other functions are not
        return [permissions.IsAuthenticated()]
    """

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(name__icontains=q)
        return queries

    @action(methods=['get'], detail=True)
    def major(self, request, pk):
        major = self.get_object().majors.filter(active=True).all()

        return Response(serializers.MajorSerializer(major, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.filter(active=True)
    serializer_class = MajorSerializer

    """
    def get_permissions(self):
        #everyone has permission to see
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    """

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(name__icontains=q)
        return queries

    @action(methods=['get'], detail=True)
    def mark(self, request, pk):
        mark = self.get_object().majorfk.filter(active=True).all()

        return Response(serializers.MarkSerializer(mark, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.filter(active=True)
    serializer_class = InformationSerializer
    pagination_class = paginators.InformationPagination

    """
    def get_permissions(self):
        #everyone has permission to see
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    """

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(title__icontains=q)
        return queries

    @action(methods=['get'], detail=True)
    def comment(self, request, pk):
        comment = self.get_object().comments_set.filter(active=True).all()

        return Response(serializers.CommentsSerializer(comment, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class InformationSecViewSet(viewsets.ModelViewSet):
    queryset = InformationSection.objects.filter(active=True)
    serializer_class = InformationSecSerializer

    """
    def get_permissions(self):
        #everyone has permission to see
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    """

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(name__icontains=q)
        return queries

    @action(methods=['get'], detail=True)
    def information(self, request, pk):
        information = self.get_object().infos.filter(active=True).all()

        return Response(serializers.InformationSerializer(information, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)


class CommentsViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Comments.objects.filter(active=True)
    serializer_class = CommentsSerializer

    def get_permissions(self):
        #everyone has permission to see
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class QuestionsViewSet(viewsets.ModelViewSet, generics.CreateAPIView):
    queryset = Questions.objects.filter(active=True)
    serializer_class = QuestionsSerializer
    pagination_class = paginators.QuestionPagination
    #permission_classes = [permissions.IsAuthenticated]

    """
    def get_permissions(self):
        #everyone has permission to see
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    """


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.filter(active=True)
    serializer_class = MarkSerializer

    def get_permissions(self):
        #everyone has permission to see
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class BannerViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = BannerImage.objects.filter(active=True)
    serializer_class = BannerSerializer

    def get_permissions(self):
        #everyone has permission to see
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = UniversityInfo.objects.all()
    serializer_class = UniversitySerializer

    def get_permissions(self):
        #everyone has permission to see
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class LivestreamViewSet(viewsets.ModelViewSet):
    queryset = Livestream.objects.filter(active=True)
    serializer_class = LivestreamSerializer

    """
    def get_permissions(self):
        #everyone has permission to see
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    """

    # def get_permissions(self):
    #     if self.action in ['add_question', 'hide_live']:
    #         return [permissions.IsAuthenticated()]
    #     return self.permission_classes

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(title__icontains=q)
        return queries

    @action(methods=['get'], detail=True)
    def question(self, request, pk):
        question = self.get_object().questions_set.filter(active=True).all()

        return Response(serializers.QuestionsSerializer(question, many=True, context={'request': request}).data,
                        status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True, url_name="hide-live")
    def hide_live(self, request, pk):
        try:
            l = Livestream.objects.get(pk=pk)
            l.active = False
            l.save()
        except Livestream.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=LivestreamSerializer(l, context={'request': request}).data, status=status.HTTP_200_OK)

    # @action(methods=['post'], url_path='question', detail=True)
    # def add_question(self, request, pk):
    #     q = Questions.objects.create(user=request.user, livestream=self.get_object(), content=request.data.get('content'))
    #
    #     return Response(serializers.QuestionsSerializer(q).data, status=status.HTTP_201_CREATED)