import math
from flask import Flask, request
import json
from scipy.optimize import linprog
app = Flask(__name__)

# def calculate_profit(bus_slots, car_slots, parking_charges, buses, cars, bikes):
#     bus_profit = min(bus_slots, buses) * parking_charges['Bus']
#     car_profit = min(car_slots, cars) * parking_charges['Car']
#     bike_profit = min(car_slots * 5, cars * 5 + bikes) * parking_charges['Bike']
#     total_profit = bus_profit + car_profit + bike_profit

#     bus_rejections = max(0, buses - bus_slots)
#     car_rejections = max(0, cars - car_slots)
#     bike_rejections = max(0, cars * 5 + bikes - car_slots * 5)

#     return {
#         "Profit": total_profit,
#         "BusRejections": bus_rejections,
#         "CarRejections": car_rejections,
#         "BikeRejections": bike_rejections
#     }

@app.route('/parking-lot', methods=['POST'])
def parking_lot():
    return 0 