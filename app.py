from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Endpoint de la API para obtener la lista de cocktails
API_URL = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail"

# Endpoint de la API para obtener detalles de un cocktail por ID
DETAILS_API_URL = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php"

# Ruta principal para mostrar la lista de cocktails
@app.route('/')
def cocktail_list():
    response = requests.get(API_URL)
    data = response.json()
    cocktails = data.get('drinks', [])
    return render_template('cocktail_list.html', cocktails=cocktails)

# Ruta para mostrar los detalles de un cocktail
@app.route('/cocktail/<int:cocktail_id>')
def cocktail_detail(cocktail_id):
    response = requests.get(f"{DETAILS_API_URL}?i={cocktail_id}")
    data = response.json()
    cocktail = data.get('drinks', [])[0] if data.get('drinks') else None
    return render_template('cocktail_detail.html', cocktail=cocktail)

if __name__ == '__main__':
    app.run(debug=True)
