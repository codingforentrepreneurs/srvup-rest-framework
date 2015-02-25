from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions


from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .models import  Category, Video



class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = [
			'id',
			'slug',
			'title',
			'description',
			'image',
		]


class CategoryViewSet(viewsets.ModelViewSet):
	#authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
	#permission_classes = [permissions.IsAuthenticated, ]
	queryset = Category.objects.all()
	serializer_class = CategorySerializer




class VideoSerializer(serializers.HyperlinkedModelSerializer):
	category_title = serializers.CharField(source='category.title', read_only=True)
	category_image = serializers.CharField(source='category.get_image_url', read_only=True)
	#category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
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
			"comment_set",
		]



class VideoViewSet(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
	permission_classes = [permissions.IsAuthenticated, ]
	queryset = Video.objects.all()
	serializer_class = VideoSerializer
