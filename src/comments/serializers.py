
from django.contrib.auth import get_user_model

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions


from rest_framework_jwt.authentication import JSONWebTokenAuthentication



from .models import  Comment


User= get_user_model()

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
	class Meta:
		model = Comment
		fields = [
			'id',
			"parent",
			"user",
			'video',
			'text',
		]


class CommentViewSet(viewsets.ModelViewSet):
	#authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
	#permission_classes = [permissions.IsAuthenticated, ]
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

