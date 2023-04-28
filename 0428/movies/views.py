from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_safe
from .models import Movie
from django.db.models import Max
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

@require_safe
def index(request):
    # 모든 영화 정보를 불러옴
    movies = get_list_or_404(Movie)
    context = {
        'movies': movies, 
    }
    return render(request, 'movies/index.html', context)

@require_safe
def detail(request, movie_pk):
    # 선택한 movie 정보 받아오기 
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 해당 movie에 대한 genre 전체 리스트 받아오기
    genres = movie.genres.all()
    context = {
        'movie' : movie,
        'genres' : genres,
    }
    return render(request, 'movies/detail.html', context)

def recommended(request, movie_pk):
    # 선택한 movie 정보 받아오기 
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 모든 영화 정보를 불러옴(id, title, overview, poster_path)
    movies = Movie.objects.values_list('id', 'title', 'overview', 'poster_path')
    
    # CountVectorizer 객체 생성 및 영화 개요 리스트 생성
    vectorizer = CountVectorizer()
    movie_overviews = [movie[2] for movie in movies]
    # 영화 개요 리스트를 이용해 벡터화된 matrix 생성
    vectors = vectorizer.fit_transform(movie_overviews)
    # 유사도 계산(cosine similarity)
    cosine_similarities = cosine_similarity(vectors)
    
    # 영화 id 최대값 구하기
    max_id = Movie.objects.all().aggregate(max_id=Max("id"))['max_id']
    recommended_movies = []
    cnt = 0
    while True:
        cnt += 1
        pk = random.randint(1, max_id)
        movie_idx = pk - 1
        # 선택한 영화와 가장 유사한 영화 10개 구하기
        sim_scores = list(enumerate(cosine_similarities[movie_idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        # 가장 유사한 영화 10개의 인덱스 추출
        movie_indices = [i[0] for i in sim_scores]
        # 추천 영화 리스트에 추가
        recommended_movies += [(movies[i][0], movies[i][1], movies[i][3], int(sim_scores[j][1]*100)) for j, i in enumerate(movie_indices)]
        # 추천 영화가 10개일 경우 반복문 종료
        if len(recommended_movies) == 10:
            break
    
    context = {
        'movie': movie,
        'movies': recommended_movies
    }

    return render(request, 'movies/recommended.html', context)
