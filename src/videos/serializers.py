from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions

from .models import Video


class VideoSerializer(serializers.HyperlinkedModelSerializer):
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
		]



class VideoViewSet(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [permissions.IsAuthenticated, ]
	queryset = Video.objects.all()
	serializer_class = VideoSerializer