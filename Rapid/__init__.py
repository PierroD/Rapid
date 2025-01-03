from .applications import Rapid as Rapid
from fastapi_crudrouter_mongodb import CRUDRouter as RapidCRUDRouter
from fastapi_crudrouter_mongodb import CRUDLookup as RapidCRUDLookup
from fastapi_crudrouter_mongodb import CRUDEmbed as RapidCRUDEmbed
from fastapi_crudrouter_mongodb import CRUDRouterService as RapidCRUDService

from fastapi_crudrouter_mongodb import MongoModel as MongoModel
from fastapi_crudrouter_mongodb import MongoObjectId as MongoObjectId
from fastapi_crudrouter_mongodb import ObjectId as ObjectId
from fastapi_crudrouter_mongodb import DeletedModelOut as DeletedModelOut

from fastapi_query_parameter_model import QueryParameterModel as QueryParameterModel  

__version__ = "0.0.0"
__author__ = "Pierre DUVEAU"
__credits__ = ["Pierre DUVEAU"]