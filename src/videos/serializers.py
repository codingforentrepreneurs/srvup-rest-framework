from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions


from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .models import Video, Category


class VideoSerializer(serializers.HyperlinkedModelSerializer):
	# category_url = serializers.CharField(source='category.get_absolute_url', read_only=True)
	category_title = serializers.CharField(source='category.title', read_only=True)
	category_image = serializers.CharField(source='category.get_image_url', read_only=True)
	category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
	class Meta:
		model = Video
		fields = [
			'id',
			'slug',
			'title',
			'order',
			'embed_code',
			'share_message',
			'timestamp',
			"category",
			"category_image",
			"category_title",
			# "category_url",
		]



class VideoViewSet(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
	permission_classes = [permissions.IsAuthenticated, ]
	queryset = Video.objects.all()
	serializer_class = VideoSerializer