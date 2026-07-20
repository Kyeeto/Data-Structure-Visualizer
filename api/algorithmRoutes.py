from flask import Blueprint, jsonify, request
from algorithms.bubbleSort import bubbleSort
from algorithms.insertionSort import insertionSort
from algorithms.mergeSort import mergeSort
from algorithms.quickSort import quickSort
from algorithms.selectionSort import selectionSort

algorithmAPI = Blueprint("algorithms", __name__)

algorithms = {
    "bubble": bubbleSort,
    "insertion": insertionSort,
    "merge": mergeSort, 
    "quick": quickSort, 
    "selection": selectionSort
}

@algorithmAPI.route("/sort/<algorithm>", methods = ["POST"])
def sort(algorithm):
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Request body must be a valid JSON"}), 400
    
    if algorithm not in algorithms:
        return jsonify({"error": "Not a sorting method"}), 400
    
    array = data.get("array")
    if array is None:
        return jsonify({"error": "No data provided"}), 400
    
    if not isinstance(array, list):
        return jsonify({"error": "Not a list"}), 400
    
    steps = algorithms[algorithm](array)
    return jsonify({"steps": steps})