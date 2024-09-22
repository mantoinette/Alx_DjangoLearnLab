from django.contrib.auth import get_user_model
from rest_framework import status, viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer, RegisterSerializer

CustomUser = get_user_model()

# Registration view using GenericAPIView
class RegisterView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user_id': user.pk,
            'username': user.username
        }, status=status.HTTP_201_CREATED)

# Custom token authentication view using GenericAPIView
class CustomAuthToken(generics.GenericAPIView):
    serializer_class = ObtainAuthToken.serializer_class

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

# ViewSet for handling user follows/unfollows
class FollowViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Action to follow a user
    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        user_to_follow = self.get_object()
        if request.user != user_to_follow:
            request.user.following.add(user_to_follow)
            return Response({"message": f"Successfully followed {user_to_follow.username}"}, status=status.HTTP_200_OK)
        return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    # Action to unfollow a user
    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user_to_unfollow = self.get_object()
        if request.user != user_to_unfollow:
            request.user.following.remove(user_to_unfollow)
            return Response({"message": f"Successfully unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
        return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    # Additional action to view the list of followed users
    @action(detail=False, methods=['get'])
    def following_list(self, request):
        following = request.user.following.all()
        serializer = self.get_serializer(following, many=True)
        return Response(serializer.data)
