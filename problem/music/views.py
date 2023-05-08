from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import MusicListSerializer, MusicSerializer, MusicReviewCntSerializer, ReviewSerializer
from .models import Music, Review


@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        music_all = Music.objects.all()
        serializer = MusicListSerializer(music_all, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 문제 2. MusicSerializer를 이용하여 유효성 검사 후 음악 정보를 생성할 수 있도록 코드를 완성하시오.
    elif request.method == 'POST':
        serializer = MusicSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, music_pk):
    # 문제 3. 찾으려는 데이터가 없으면 404 상태 코드를 반환할 수 있도록 아래 코드를 완성하시오.
    music = get_object_or_404(Music, pk = music_pk)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    # 문제 4. 음악 데이터를 삭제하고 {'delete': 삭제되는음악pk} 형태의 JSON으로 반환하도록 코드를 완성하시오.
    if request.method == 'DELETE':
        music_pk = music_pk
        music.delete()
        result = {
            'delete': music_pk   
        }
        return Response(result)
    
    # 문제 5. 음악 데이터를 수정할 수 있도록 아래 코드를 완성하시오.
    # 수정이 정상적으로 완료되었다면 수정된 데이터를 JSON 형태로 반환합니다.
    if request.method == 'PUT':
        music = get_object_or_404(Music, pk=music.pk)
        serializer = MusicSerializer(music, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) 


# 문제 7. 모든 리뷰 정보를 반환하도록 review_list 코드를 완성하시오.
@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


# 문제 8. 리뷰를 생성할 수 있도록 아래 코드를 완성하시오.
# 유효성 검사를 통과하지 못하면 정보와 400 상태코드를 반환합니다.
# 작성된 리뷰의 JSON과 함께 201 상태 코드를 반환합니다.
@api_view(['POST'])
def review_create(request, music_pk):
    if request.method == 'POST':
        music = get_object_or_404(Music, pk=music_pk)
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(music = music)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'DELETE'])
def review_detail(request, review_pk):
    # 문제 9. 리뷰 정보를 조회할 수 있도록 아래 코드를 완성하시오.
    # 찾는 리뷰가 없으면 404 상태 코드를 반환합니다.
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    
    # 문제 10. DELETE 로 요청오는 경우 해당 리뷰가 삭제될 수 있도록 아래에 코드를 완성하시오.
    # 삭제하려는 리뷰가 없으면 404 상태 코드를 반환합니다.
    # 삭제가 정상적으로 완료되면 {'delete': 삭제된리뷰PK} 형태인 JSON이 204 상태코드와 함께 반환됩니다.

    if request.method == 'DELETE':
        review_pk = review_pk
        review.delete()
        result = {
            'delete': review_pk
        }
        return Response(result, status=status.HTTP_204_NO_CONTENT)