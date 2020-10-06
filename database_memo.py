from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global col

def connect_db():
	global con
	global db
	global col
	con = MongoClient('mongodb+srv://test:test@cluster0.kw4id.mongodb.net/nexus?retryWrites=true&w=majority')
	db = con.nexus
	

#icollection installation_companies
def get_installation_companies():
	global col
	connect_db()
	col = db.installation_companies
	install_comp_data_from_db = col.find({})
	return install_comp_data_from_db


def save_installation_companies(install_comapanies):
	global col
	connect_db()
	col = db.installation_companies
	col.insert_many(install_comapanies)
	return

#collection memo
def get_memo():
	global col
	connect_db()
	col = db.memo
	memo_data_from_db = col.find({})
	return memo_data_from_db


def save_memo(memo_data):
	global col
	connect_db()
	col = db.memo
	col.insert_many(memo_data)
	return

#collection token_map
def get_token_map():
	global col
	connect_db()
	col = db.token_map
	tokenmap_data_from_db = col.find({})
	return tokenmap_data_from_db


def save_token_map(token_map):
	global col
	connect_db()
	col = db.token_map
	col.insert_many(token_map)
	return
