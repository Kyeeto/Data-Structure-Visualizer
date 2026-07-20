from flask import Blueprint, jsonify, request
from structures.array import MyArray
from structures.bst import BinarySearchTree
from structures.doublyLinkedList import DoublyLinkedList
from structures.hashmap import Hashmap
from structures.myqueue import Queue
from structures.singlyLinkedList import SinglyLinkedList
from structures.stack import Stack

structureAPI = Blueprint("structures", __name__)

@structureAPI.route("/array/<operation>", methods = ["POST"])
def array(operation):
    pass

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
    pass

@structureAPI.route("/sll/<operation>", methods = ["POST"])
def sll(operation):
    pass

@structureAPI.route("/stack/<operation>", methods = ["POST"])
def stack(operation):
    pass