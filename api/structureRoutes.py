from flask import Blueprint, jsonify, request
from structures.array import MyArray
from structures.bst import BinarySearchTree
from structures.doublyLinkedList import DoublyLinkedList
from structures.hashmap import Hashmap
from structures.myqueue import Queue
from structures.singlyLinkedList import SinglyLinkedList
from structures.stack import Stack

structureAPI = Blueprint("structures", __name__)

stackOps = {"push", "pop", "peek"}
arrayOps = {"append", "insert", "set"}
queueOps = {"enqueue", "dequeue", "front"}

@structureAPI.route("/array/<operation>", methods = ["POST"])
def array(operation):
    data = request.get_json(silent = True)
    if data is None:
        return jsonify({"error": "No data inputted"}), 400

    if operation not in arrayOps:
        return jsonify({"error": f"Unknown operation '{operation}'"}), 400

    values = data.get("values")

    if not isinstance(values, list):
        return jsonify({"error": "Values must be a list"}), 400

    arr = MyArray()
    for v in values:
        arr.append(v)

    if operation == "append":
        value = data.get("value")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        else:
            result = arr.append(value)
            if result == "Array is full":
                return jsonify({"error": "Array capacity reached"}), 400
            else: 
                return jsonify({"values": arr.arr[:arr.length], "result": result})
    elif operation == "insert":
        value = data.get("value")
        index = data.get("index")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        if not isinstance(index, int):
            return jsonify({"error": "Index must be an int"}), 400

        result = arr.insert(index, value)
        if result == "Index out of bounds": 
            return jsonify({"error": "Index out of bounds"}), 400
        elif result == "Array is full":
            return jsonify({"error": "Array is full"}), 400
        else: 
            return jsonify({"values": arr.arr[:arr.length], "result": result})
    elif operation == "set":
        value = data.get("value")
        index = data.get("index")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        if not isinstance(index, int):
            return jsonify({"error": "Index must be an int"}), 400

        result = arr.set(index, value)
        if result == "Index out of bounds": 
            return jsonify({"error": "Index out of bounds"}), 400
        else: 
            return jsonify({"values": arr.arr[:arr.length], "result": result})

@structureAPI.route("/bst/<operation>", methods = ["POST"])
def bst(operation):
    pass

@structureAPI.route("/dll/<operation>", methods = ["POST"])
def dll(operation):
    pass

@structureAPI.route("/hashmap/<operation>", methods = ["POST"])
def hashmap(operation):
    pass

@structureAPI.route("/queue/<operation>", methods = ["POST"])
def queue(operation):
    data = request.get_json(silent = True)
    if data is None: 
        return jsonify({"error": "No data inputted"}), 400

    if operation not in queueOps:
        return jsonify({"error": "No data inputted"}), 400

    values = data.get("values")
    q = Queue()

    if not isinstance(values, list):
        return jsonify({"error": "Values must be a list"}), 400

    for v in values:
        q.enqueue(v)

    if operation == "enqueue":
        pass

    if operation == "dequeue":
        pass

    if operation == "front":
        pass

@structureAPI.route("/sll/<operation>", methods = ["POST"])
def sll(operation):
    pass

@structureAPI.route("/stack/<operation>", methods = ["POST"])
def stack(operation):
    data = request.get_json(silent = True)
    if data is None:
        return jsonify({"error": "No data inputted"}), 400
    
    if operation not in stackOps: 
        return jsonify({"error": f"Unknown operation '{operation}'"}), 400

    values = data.get("values")
    s = Stack()
    
    if not isinstance(values, list):
        return jsonify({"error": "Values must be a list"}), 400
    for v in values:
        s.push(v)

    if operation == "push":
        value = data.get("value")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        else:
            result = s.push(value)
            if result == "Stack is Full":
                return jsonify({"error": "Stack capacity reached"}), 400
            else:
                return jsonify({"values": s.stack, "result": result})
    elif operation == "pop":
        result = s.pop()
        if result == None:
            return jsonify({"error": "Empty stack"}), 400
        else: 
            return jsonify({"values": s.stack, "result": result})
    elif operation == "peek":
        result = s.peek()
        if result == None:
            return jsonify({"error": "Empty stack"}), 400
        else: 
            return jsonify({"values": s.stack, "result": result})

