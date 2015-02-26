
from rest_framework import routers, serializers, viewsets, permissions

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from comments.serializers import CommentSerializer

from .models import  Category, Video

#HyperlinkedIdentityField

class CategoryUrlHyperlinkedIdentityField(serializers.HyperlinkedIdentityField):
	#lookup_field = 'slug'
	#pass

	def get_url(self, obj, view_name, request, format):
		kwargs = {
			'slug': obj.slug
		}
		return reverse(view_name, kwargs=kwargs, request=request, format=format)




class CategorySerializer(serializers.HyperlinkedModelSerializer):
	url = CategoryUrlHyperlinkedIdentityField(view_name='category_detail_api')
	class Meta:
		model = Category
		fields = [
			"url",
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
	category = CategorySerializer(many=False, read_only=True)
	comment_set = CommentSerializer(many=True, read_only=True)
	#category_title = serializers.CharField(source='category.title', read_only=True)
	#category_image = serializers.CharField(source='category.get_image_url', read_only=True)
	#category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
	class Meta:
		model = Video
		fields = [
			"url",
			'id',
			'slug',
			'title',
			'order',
			'embed_code',
			'share_message',
			'timestamp',
			"category",
			#"category_image",
			#"category_title",
			"comment_set",
		]


class VideoViewSet(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
	permission_classes = [permissions.IsAuthenticated, ]
	queryset = Video.objects.all()
	serializer_class = VideoSerializer
