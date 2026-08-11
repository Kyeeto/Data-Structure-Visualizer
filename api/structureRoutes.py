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
sllOps = {"append", "prepend", "insert", "pop", "remove"}
dllOps = {"append", "prepend", "insert", "pop", "pop_first", "remove", "remove_at", "set"}
bstOps = {}
hashOps = {"insert", "get", "delete"}

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
    data = request.get_json(silent = True)
    if data is None:
        return jsonify({"error": "No data inputted"}), 400

    if operation not in dllOps: 
        return jsonify({"error": f"Unknown operation '{operation}'"}), 400

    values = data.get("values")
    dll = DoublyLinkedList()

    if not isinstance(values, list):
        return jsonify({"error": "Values must be a list"}), 400
    for v in values:
        dll.append(v)

    if operation == "append":
        value = data.get("value")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        else: 
            result = dll.append(value)
            return jsonify({"values": dll.to_list(), "result": result})

    elif operation == "prepend":
        value = data.get("value")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        else: 
            result = dll.prepend(value)
            return jsonify({"values": dll.to_list(), "result": result})
    elif operation == "insert":
        value = data.get("value")
        index = data.get("index")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        elif not isinstance(index, int):
            return jsonify({"error": "Index must be an int"}), 400
        else: 
            result = dll.insert(index, value)
            if result == "Index does not exist":
                return jsonify({"error": "Please use an existing index"}), 400
            return jsonify({"values": dll.to_list(), "result": result})
    elif operation == "pop":
        result = dll.pop()
        if result == None:
            return jsonify({"error": "Empty list"}), 400
        else: 
            return jsonify({"values": dll.to_list(), "result": result})
    elif operation == "pop_first":
        result = dll.pop_first()
        if result == None:
            return jsonify({"error": "Empty list"}), 400
        else: 
            return jsonify({"values": dll.to_list(), "result": result})
    elif operation == "remove":
            value = data.get("value")
            if not isinstance(value, int):
                return jsonify({"error": "Value must be an int"}), 400
            else:
                result = dll.remove(value)
                if result == None:
                    return jsonify({"error": "Empty List"}), 400
                elif result == -1:
                    return jsonify({"error": "Value not found"}), 400
                else:
                    return jsonify({"values": dll.to_list(), "result": result})
    elif operation == "remove_at":
        index = data.get("index")
        if not isinstance(index, int):
            return jsonify({"error": "Index must be an int"}), 400
        else:
            result = dll.remove_at(index)
            if result == "Index does not exist":
                return jsonify({"error": "Please use an existing index"}), 400
            else: 
                return jsonify({"values": dll.to_list(), "result": result})
    elif operation == "set":
        value = data.get("value")
        index = data.get("index")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        elif not isinstance(index, int):
            return jsonify({"error": "Index must be an int"}), 400
        else: 
            result = dll.set(index, value)
            if result == "Index does not exist":
                return jsonify({"error": "Please use an existing index"}), 400
            else:
                return jsonify({"values": dll.to_list(), "result": result}) 

@structureAPI.route("/hashmap/<operation>", methods = ["POST"])
def hashmap(operation):
    data = request.get_json(silent = True)
    if data is None: 
        return jsonify({"error": "No data inputted"}), 400

    if operation not in hashOps:
        return jsonify({"error": f"Unknown operation '{operation}'"}), 400

    pairs = data.get("pairs")
    hm = Hashmap()

    if not isinstance(pairs, dict):
        return jsonify({"error": "Pairs must be an object"}), 400
    for key, val in pairs.items():
        hm.insert(key, val)

    if operation == "insert":
        value = data.get("value")
        key = data.get("key")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        if not isinstance(key, str):
            return jsonify({"error": "Key must be a string"}), 400
        else: 
            result = hm.insert(key, value)
            if result == "Map is full":
                return jsonify({"error": "Map is full"}), 400
            else:
                return jsonify({"buckets": hm.to_buckets(), "result": None})
    elif operation == "get":
        key = data.get("key")
        if not isinstance(key, str):
            return jsonify({"error": "Key must be a string"}), 400
        else:
            result = hm.get(key)
            if result == None:
                return jsonify({"error": "No values stored at this key"}), 400
            else: 
                return jsonify({"buckets": hm.to_buckets(), "result": result})

    elif operation == "delete":
        key = data.get("key")
        if not isinstance(key, str):
            return jsonify({"error": "Key must be a string"}), 400
        else:
            result = hm.delete(key)
            return jsonify({"buckets": hm.to_buckets(), "result": result})

@structureAPI.route("/queue/<operation>", methods = ["POST"])
def queue(operation):
    data = request.get_json(silent = True)
    if data is None: 
        return jsonify({"error": "No data inputted"}), 400

    if operation not in queueOps:
        return jsonify({"error": f"Unknown operation '{operation}'"}), 400

    values = data.get("values")
    q = Queue()

    if not isinstance(values, list):
        return jsonify({"error": "Values must be a list"}), 400
    for v in values:
        q.enqueue(v)

    if operation == "enqueue":
        value = data.get("value")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        else:
            result = q.enqueue(value)
            if result == "Queue is Full":
                return jsonify({"error": "Queue capacity reached"}), 400
            else:
                jsonify({"values": q.queue, "result": result})

    if operation == "dequeue":
        result = q.dequeue()
        if result == None:
            return jsonify({"error": "Empty queue"}), 400
        else:
            return jsonify({"values": q.queue, "result": result})

    if operation == "front":
        result = q.front()
        if result == None:
            return jsonify({"error": "Empty queue"})
        else:
            return jsonify({"values": q.queue, "result": result})

@structureAPI.route("/sll/<operation>", methods = ["POST"])
def sll(operation):
    data = request.get_json(silent = True)
    if data is None:
        return jsonify({"error": "No data inputted"}), 400
    
    if operation not in sllOps: 
        return jsonify({"error": f"Unknown operation '{operation}'"}), 400

    values = data.get("values")
    sll = SinglyLinkedList()

    if not isinstance(values, list):
        return jsonify({"error": "Values must be a list"}), 400
    for v in values:
        sll.append(v)

    if operation == "append":
        value = data.get("value")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        else: 
            result = sll.append(value)
            return jsonify({"values": sll.to_list(), "result": result})
    elif operation == "prepend":
        value = data.get("value")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        else: 
            result = sll.prepend(value)
            return jsonify({"values": sll.to_list(), "result": result})
    elif operation == "insert":
        value = data.get("value")
        index = data.get("index")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        elif not isinstance(index, int):
            return jsonify({"error": "Index must be an int"}), 400
        else: 
            result = sll.insert(index, value)
            if result == "Index does not exist":
                return jsonify({"error": "Please use an existing index"}), 400
            return jsonify({"values": sll.to_list(), "result": result})
    elif operation == "pop":
        result = sll.pop()
        if result == None:
            return jsonify({"error": "Empty list"}), 400
        else: 
            return jsonify({"values": sll.to_list(), "result": result})
    elif operation == "remove":
        value = data.get("value")
        if not isinstance(value, int):
            return jsonify({"error": "Value must be an int"}), 400
        else:
            result = sll.remove(value)
            if result == None:
                return jsonify({"error": "Empty List"}), 400
            elif result == -1:
                return jsonify({"error": "Value not found"}), 400
            else:
                return jsonify({"values": sll.to_list(), "result": result})

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

