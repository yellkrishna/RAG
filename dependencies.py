import os
import logging
import sys
import warnings
import json
from typing import Sequence, List
import nest_asyncio
import openai
from llama_index import Document, SimpleDirectoryReader, VectorStoreIndex, ServiceContext, LLMPredictor, SQLDatabase, load_index_from_storage, StorageContext
from llama_index.llms import OpenAI, ChatMessage
from llama_index.indices.struct_store import SQLTableRetrieverQueryEngine
from sqlalchemy import create_engine, MetaData
from llama_index.objects import SQLTableNodeMapping, ObjectIndex, SQLTableSchema
from llama_index.tools import BaseTool, FunctionTool
from llama_index.agent import OpenAIAgent
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart