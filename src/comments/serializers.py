
from django.contrib.auth import get_user_model

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions


from rest_framework_jwt.authentication import JSONWebTokenAuthentication



from .models import  Comment


User= get_user_model()


class CommentCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = [
			'text',
			'user',
			'video',
			]




class ChildCommentSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
	class Meta:
		model = Comment
		fields = [
			'id',
			"user",
			'text',
		]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField("comment_detail_api", lookup_field='id')
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
	children = serializers.SerializerMethodField(read_only=True)

	def get_children(self, instance):
		#queryset = instance.get_children()
		queryset = Comment.objects.filter(parent__pk=instance.pk)
		serializer = ChildCommentSerializer(queryset, context={"request": instance}, many=True)
		return serializer.data


	class Meta:
		model = Comment
		fields = [
			"url",
			'id',
			"children",
			"parent",
			"user",
			'video',
			'text',
		]


class CommentViewSet(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
	permission_classes = [permissions.IsAuthenticated, ]
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

