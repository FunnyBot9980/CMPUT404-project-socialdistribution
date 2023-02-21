from rest_framework import serializers
from .models import *

# need to pip install rest_framework
# To convert your queries to or from a JSON object (useful when connecting with groups)

class PostSerializer(serializers.Serializer):
    pass

class AuthorSerializer(serializers.ModelSerializer):

    # get the author's information
    type = serializers.CharField(source = 'object_type')
    id = serializers.UUIDField(source = 'profile_url')
    url = serializers.URLField(source = 'profile_url')
    host = serializers.URLField(source = 'home_host')
    displayName = serializers.CharField(source = 'display_name')
    github = serializers.URLField(source = 'author_github')
    profileImage = serializers.URLField(source = 'profile_image')

    class Meta:
        model = Author
        fields = ['type', 'id', 'url', 'host', 'displayName', 'github', 'profileImage']


class CommentSerializer(serializers.ModelSerializer):

    type = serializers.CharField(default='comment')
    author = serializers.JSONField(source = 'author_json')
    comment = serializers.CharField(source = 'comment_content')
    contentType = serializers.CharField(source = 'content_type')
    published = serializers.DateTimeField(source='pub_date')
    id = serializers.URLField(source='comment_id')

    class Meta:
        model = Comment
        fields = ['type', 'author', 'comment', 'contentType', 'published', 'id']


class CommentsSerializer(serializers.ModelSerializer):

    type = serializers.CharField(default='comments')
    id = serializers.URLField(source='comments_id')
    comments_list = CommentSerializer(many=True)

    class Meta:
        model = Comments
        fields = ['type', 'page', 'size', 'post', 'id', 'comments_list']


    def create(self, validated_data):
        comments_info = validated_data.pop('comments_list')
        create_comments = Comments.objects.create(**validated_data)
        for comment in comments_info:
            Comment.objects.create(associated_author = create_comments, **comment)
        return create_comments

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return_data = {}
        return_data.update({
                'type': data['type'],
                'page': data['page'],
                'size': data['size'],
                'post': data['post'],
                'id': data['id'],
                'comments': data['comments_list']})
        return return_data

class LikeSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='object_type')
    summary = serializers.CharField(source = 'like_summary')
    author = serializers.JSONField(source = 'author_object') # the author who is the follower
    object = serializers.URLField(source = 'obj') # the post/comment that was liked

    class Meta:
        model = Like
        fields = ['context', 'type', 'summary', 'author', 'object']

    # Reference: https://stackoverflow.com/questions/51583756/django-rest-framework-modelserializer-fields-whose-names-are-invalid-python-iden
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return_data = {} # update how it's displayed after being serialized
        return_data.update({
                '@context': data['context'],
                'type': data['type'],
                'summary': data['summary'],
                'author': data['author'],
                'object': data['object']})
        return return_data

class AuthorLikesSerializer(serializers.ModelSerializer):
    type = serializers.CharField(default="Liked")
    liked_items = LikeSerializer(many=True)

    class Meta:
        model = Author
        fields = ['type', 'liked_items']

    def create(self, validated_data):
        likes_info = validated_data.pop('liked_items')
        create_author = Author.objects.create(**validated_data)
        for like in likes_info:
            Like.objects.create_like(like.context, like.author_object, like.obj)
        return create_author

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return_data = {}
        return_data.update({
                'type': data['type'],
                'items': data['liked_items']})
        return return_data


    def to_internal_value(self, data):
        type = data.get('type')
        liked_items = data.get('items')

        # data validation.
        if not type:
            raise serializers.ValidationError({
                'score': 'This field is required.'
            })
        if not liked_items:
            raise serializers.ValidationError({
                'player_name': 'This field is required.'
            })

        # returns the validated values
        return {
            'type': type,
            'liked_items': liked_items
        }
# ---------------------- Inbox Serializer ----------------------------------
class InboxItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = ['inbox_item']

class AuthorInboxSerializer(serializers.ModelSerializer):
    inbox_items = InboxItemSerializer(many=True)

    class Meta:
        model = Author
        fields = ['inbox_items']

    def create(self, validated_data):
        inbox_info = validated_data.pop('inbox_items')
        create_author = Author.objects.create(**validated_data)
        for item in inbox_info:
            Inbox.objects.create(associated_author = create_author, inbox_item = item.inbox_item)
        return create_author

    def to_representation(self, instance):
        items_list = []
        for item in instance.inbox.all():
            items_list.append(item.inbox_item) # add all the "notifications"
        return {
            'type': 'inbox',
            'author': instance.profile_url,
            'items': items_list
        }


class FollowSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source = 'follow_type')
    actor = serializers.JSONField(source = 'author_actor') # the author who is the follower
    object = serializers.JSONField(source = 'author_object') # the author who is being followed
    summary = serializers.CharField(source = 'following_summary')

    class Meta:
        model = Follow
        fields = ['type', 'actor', 'object', 'summary']

# ---------------------- Followers Serializer ----------------------------------
class AuthorFollowersSerializer(serializers.ModelSerializer):
    type = serializers.CharField(default="followers")
    followers_items = AuthorSerializer(many=True) # a list of the followers

    class Meta:
        model = Author
        fields = ['type', 'followers_items']

    def create(self, validated_data):
        followers_info = validated_data.pop('followers_items')
        create_author = Author.objects.create(**validated_data)
        for follower in followers_info:
            Followers.objects.create(follower_author = create_author,**follower)
        return create_author

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return_data = {}
        return_data.update({
                'type': data['type'],
                'items': data['followers_items']})
        return return_data