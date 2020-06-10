import requests


def get_movie_data(movie_id, keyword):
    res_movie = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=f08b72164e664e909b4d099429fb4593&language=en-US').json()
    return res_movie[keyword]


def get_movie_poster(movie_id):
    res_movie = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=f08b72164e664e909b4d099429fb4593&language=en-US').json()
    path = res_movie['poster_path']
    return f'https://image.tmdb.org/t/p/w600_and_h900_bestv2{path}'


def get_movie_video(movie_id):
    res_movie = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=f08b72164e664e909b4d099429fb4593&language=en-US').json()
    try:
        video_key = res_movie['results'][1]['key']
    except (IndexError, UnboundLocalError):
        video_key = res_movie['results'][0]['key']
    finally:
        return video_key
