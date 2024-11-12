from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    from_location = request.args.get('from')
    to_location = request.args.get('to')
    departure_date = request.args.get('departure')
    return_date = request.args.get('return')

    # Получение доступных билетов (примерный код)
    available_tickets = search_flights(from_location, to_location, departure_date, return_date)

    tickets = []
    if available_tickets:
        for idx, ticket in enumerate(available_tickets):
            tickets.append({
                'id': idx + 1,  # Уникальный идентификатор для каждого билета
                'airline': ticket['airline'],
                'price': ticket['price'],
                'departure_time': ticket['departure_time'],
                'arrival_time': ticket['arrival_time']
            })

    return jsonify({'tickets': tickets})

def search_flights(from_location, to_location, departure_date, return_date):
    # Ваш код для обращения к API и получения информации о билетах
    return [
        {'airline': 'S7 airlines', 'price': 53800, 'departure_time': '2023-10-25 10:00', 'arrival_time': '2023-10-25 12:00'},
        {'airline': 'Aэрофлот', 'price': 69990, 'departure_time': '2023-10-25 14:00', 'arrival_time': '2023-10-25 16:00'}
    ]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Здесь вы добавляете строку