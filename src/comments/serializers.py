
from django.contrib.auth import get_user_model

from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse



from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .models import  Comment


User= get_user_model()


class CommentVideoUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
	def get_url(self, obj, view_name, request, format):
		video = None
		if obj.is_child:
			try:
				video = obj.parent.video
			except:
				video = None
		else:
			try:
				video = obj.video
			except:
				video = None
		if video:
			kwargs = {
				'cat_slug': video.category.slug,
				"vid_slug": video.slug
			}
			return reverse(view_name, kwargs=kwargs, request=request, format=format)
		else:
			return None




class CommentUpdateSerializer(serializers.ModelSerializer):
	user = serializers.CharField(source='user.username', read_only=True)
	class Meta:
		model = Comment
		fields = [
			"id",
			"user",
			'text'
		]

class CommentCreateSerializer(serializers.ModelSerializer):
	username = serializers.CharField(source='user.username', read_only=True)
	class Meta:
		model = Comment
		fields = [
			'id',
			'text',
			'user',
			'username'
			'video',
			'parent',
			]




class ChildCommentSerializer(serializers.HyperlinkedModelSerializer):
	#user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
	user = serializers.CharField(source='user.username', read_only=True)
	class Meta:
		model = Comment
		fields = [
			'id',
			"user",
			'text',
		]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField("comment_detail_api", lookup_field='id')
	#user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
	video = CommentVideoUrlHyperlinkedIdentityField("video_detail_api")
	user = serializers.CharField(source='user.username', read_only=True)
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
			#"parent",
			"user",
			'video',
			'text',
		]


class CommentViewSet(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
	permission_classes = [permissions.IsAuthenticated, ]
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

