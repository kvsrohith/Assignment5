import json
from flask import Flask, jsonify, render_template, request, Response

app = Flask(__name__)


with open('movies.json') as json_data:
    movie_json = json.load(json_data)
    list_of_movies = []
    for movie in movie_json['movies']:
    	list_of_movies.append(movie)

@app.route('/movies', methods =['GET'])
def movies():
	return render_template("movies.html",list_data=list_of_movies)
	
@app.route('/movies/<string:movie_id>', methods =['GET'])
def movie_info(movie_id):
	list_movie_id = [movie for movie in list_of_movies if movie['id'] == movie_id]
	return render_template("movies.html",list_data=list_movie_id)

@app.route('/movies/<movie_id>/sales', methods =['GET'])
def sales(movie_id):
	list_movie_id = [movie for movie in list_of_movies if movie['id'] == movie_id]
	sale_details=list_movie_id[0]['sales']
	print(sale_details)
	return render_template("sales.html",list_data=sale_details)

@app.route('/movies/<movie_id>/sales/<sale_id>', methods =['GET'])
def sale_info(movie_id, sale_id):
	list_movie_id = [movie for movie in list_of_movies if movie['id'] == movie_id]
	sale_id = [sales for sales in list_movie_id[0]['sales'] if sales['sale_id'] == sale_id]
	return render_template("sales.html",list_data=sale_id)

if __name__ == '__main__':
	 app.run(host='0.0.0.0', port =8000)
