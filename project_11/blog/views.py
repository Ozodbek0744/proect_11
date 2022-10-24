from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import BlogModel, Comment, Izoh
from .serializers import BlogModelSerializer, BlogModelDetailSerializer, \
    CommentSerializer, CommentUpdateSerializer, \
    CommentListSerializer, IzohSerializer
from account.models import Account


@api_view(('GET',))
def blog_list_view(request):
    blog_posts = BlogModel.objects.all()
    serializer = BlogModelSerializer(blog_posts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(('GET',))
def blog_detail_view(request, slug):
    try:
        blog = BlogModel.objects.get(slug=slug)
    except BlogModel.DoesNotExist:
        return Response({"message": "This blog does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BlogModelDetailSerializer(blog)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('POST',))
@permission_classes([IsAuthenticated])
def blog_post(request):
    account = request.user

    blog_post = BlogModel(author=account)

    serializer = BlogModelSerializer(blog_post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('PUT', 'DELETE'))
@permission_classes([IsAuthenticated])
def update_delete_blog_post(request, slug):
    print(request.user)
    account = request.user
    try:
        blog = BlogModel.objects.get(slug=slug)
    except BlogModel.DoesNotExist:
        return Response({'message':'kechirasiz bu blog mavjud emas'}, status=status.HTTP_404_NOT_FOUND)

    if account != blog.author:
        return Response({'message':'siz blog egasi emassiz'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = BlogModelDetailSerializer(instance=blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        blog.delete()
        return Response({"message": "blog mufaqqiyatli o'chirildi"}, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @api_view(('DELETE',))
# @permission_classes([IsAuthenticated])
# def delete_blog(request, slug):
#     account = request.user
#     try:
#         blog = BlogModel.objects.get(slug= slug)
#
#     except BlogModel.DoesNotExist:
#         return Response({'message':'kechirasiz bunday blog mavjud emas'}, status=status.HTTP_404_NOT_FOUND)
#
#     if account != blog.author:
#         return Response({'message':'siz bu blogning egasi emassiz'}, status=status.HTTP_403_FORBIDDEN)
#
#     blog.delete()
#     return Response({"message": "blog mufaqqiyatli o'chirildi"}, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def post_comment(request, pk):
    account = request.user

    try:
        blog = BlogModel.objects.get(id=pk)
    except BlogModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    comment = Comment(author=account, blog=blog)

    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        obj = serializer.save()
        obj.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
def comment_list_view(request):
    comment_posts = Comment.objects.all()
    serializer = CommentListSerializer(comment_posts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('PUT',))
@permission_classes([IsAuthenticated])
def update_comment_post(request, pk):
    print(request.user)
    account = request.user
    try:
        comment = Comment.objects.get(id=pk)
    except Comment.DoesNotExist:
        return Response({'message' : 'kechirasiz bu comment mavjud emas'}, status=status.HTTP_404_NOT_FOUND)

    if account != comment.author:
        return Response({'message' : 'siz comment egasi emassiz'}, status=status.HTTP_403_FORBIDDEN)

    serializer = CommentUpdateSerializer(instance=comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('DELETE',))
@permission_classes([IsAuthenticated])
def delete_comment(request, pk):
    account = request.user
    try:
        comment = Comment.objects.get(id=pk)

    except Comment.DoesNotExist:
        return Response({'message': 'kechirasiz bunday comment mavjud emas'}, status=status.HTTP_404_NOT_FOUND)

    if account != comment.author:
        return Response({'message': 'siz bu commentning egasi emassiz'}, status=status.HTTP_403_FORBIDDEN)

    comment.delete()
    return Response({"message": "comment mufaqqiyatli o'chirildi"}, status=status.HTTP_202_ACCEPTED)


@api_view(('GET',))
def author_list_view(request):
    account = request.user
    author_posts = BlogModel.objects.filter(author=account)
    serializer = BlogModelSerializer(author_posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('GET',))
def author_list_comment(request):
    account = request.user
    author_comment = Comment.objects.filter(author=account)
    serializer = CommentListSerializer(author_comment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(('POST',))
@permission_classes([IsAuthenticated])
def comment_izoh(request, pk):
    account = request.user

    try:
        comment = Comment.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    izoh = Izoh(author=account, comment=comment)

    serialezer = IzohSerializer(izoh, data=request.data)
    if serialezer.is_valid():
        obj = serialezer.save()
        obj.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)




