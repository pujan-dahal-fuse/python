from re import search
from flask import Flask, jsonify, request
from exceptions import ValueDuplicate, ValueNotFound
from tmdb_api_key import API_KEY # api key for my account in TMDB database, the file is gitignored
from api_creation_assign import jprint
import urllib.request, json


app = Flask(__name__)


# get list of top-movies in tmdb database and write into example.json file
@app.route('/api/load-movies/', methods=['GET'])
def load_movies():
    # will load first 10 pages of record only
    i = 1
    results = []
    while i < 11:
        url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page={i}"
        response = urllib.request.urlopen(url)
        data = json.load(response)
        # we need only results field from the data that is loaded
        results.extend(data['results']) # extend is used because results is in the form of a list itself rather than a dictionary
        i += 1
    
    # this results has to be written into example.json file
    with open('example.json', mode='w', encoding='utf-8') as file_to_write:
        file_to_write.write(json.dumps(results, indent=4))
    
    return jsonify({
        'status': 200,
        'message': 'Movies load successful',
        'data': {
            'number_of_results': len(results),
            'results': results, 
        },
    })


# get title and rating of all top movies
@app.route('/api/movies', methods=['GET'])
def get_movies():
    with open('example.json', mode='r', encoding='utf-8') as file:
        movies = json.load(file)
        response = []
        for movie in movies:
            movie_dict = dict()
            movie_dict['title'] = movie['title']
            movie_dict['rating'] = movie['vote_average']
            response.append(movie_dict)
    
    return jsonify({
        'status': 200,
        'message': 'Movies retrieval successful',
        'data': {
            'number_of_results': len(response),
            'results': response,
        }
    })

# get title, overview, release date, rating of movies with given keyword
@app.route('/api/search/<keyword>', methods=['GET'])
def search_movies(keyword):
    with open('example.json', mode='r', encoding='utf-8') as read_file:
        movies = json.load(read_file)
        response = []
        try:
            for movie in movies:
                if keyword.lower() in movie['title'].lower():
                    movie_dict = dict()
                    movie_dict['title'] = movie['title']
                    movie_dict['release_date'] = movie['release_date']
                    movie_dict['rating'] = movie['vote_average']
                    movie_dict['overview'] = movie['overview']
                    response.append(movie_dict)
            if len(response) == 0:
                raise ValueNotFound
            else:
                return jsonify({
                    'status': 200,
                    'message': 'Movies retrieval successful',
                    'data': {
                        'number_of_results': len(response),
                        'results': response,
                    },
                })

        except ValueNotFound:
            return jsonify({
                'status': 404,
                'message': 'Movies for keyword not found',
                'data': {},
            })

# delete movie with given id
@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_movie(id):
    try:
        with open('example.json', mode='r', encoding='utf-8') as read_file:
            movies = json.load(read_file)
            new_movies = []
            id_found = False
            for movie in movies:
                if movie['id'] == id:
                    id_found = True
                    movie_dict = movie
                    continue
                new_movies.append(movie)
            if not id_found:
                raise ValueNotFound
        
        with open('example.json', mode='w', encoding = 'utf-8') as write_file:
            write_file.write(json.dumps(new_movies, indent=4))
            return jsonify({
                'status': 200,
                'message': 'Movie deletion successful',
                'data': movie_dict,
            })
    
    except ValueNotFound:
        return jsonify({
            'status': 404,
            'message': 'Movie with given id not found',
            'data': {},
        })
            


# update movie rating with given id to given rating
@app.route('/api/update/<int:id>', methods=['PATCH'])
def update_movie(id):
    input_json = request.get_json()
    try:
        with open('example.json', mode='r', encoding='utf-8') as read_file:
            movies = json.load(read_file)
            id_found = False
            movie_dict = dict()
            for movie in movies:
                if movie['id'] == id:
                    movie['vote_average'] = input_json['rating']
                    movie_dict = movie
                    id_found = True
                    break
            if not id_found:
                raise ValueNotFound
        with open('example.json', mode='w', encoding='utf-8') as write_file:
            write_file.write(json.dumps(movies, indent=4))
        
        return jsonify({
            'status': 200,
            'message': 'Movie update successful',
            'data': movie_dict,
        })
    
    except ValueNotFound:
        return jsonify({
            'status': 404,
            'message': 'Movie with given id not found',
            'data': {}
        })

# insert a movie into the database
@app.route('/api/insert/', methods=['POST'])
def insert_movie():
    input_json = request.get_json()
    try:
        with open('example.json', mode = 'r', encoding = 'utf-8') as read_file:
            movies = json.load(read_file)
            for movie in movies:
                if movie['id'] == input_json['id']:
                    raise ValueDuplicate # duplicate id is not allowed
        with open('example.json', mode = 'a', encoding = 'utf-8') as append_file:
            append_file.write(json.dumps(input_json, indent=4))

        return jsonify({
            'status': 200,
            'message': 'Movie insertion successful',
            'data': input_json,
        })
    
    except ValueDuplicate:
        return jsonify({
            'status': 400,
            'message': 'Cannot insert: duplicate id',
            'data': {},
        })
        


if __name__ == "__main__":
    app.run(debug=True)
