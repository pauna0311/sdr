from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import AddItemProperty, SetItemValues, AddPurchase
from recombee_api_client.api_requests import RecommendItemsToItem, SearchItems, Batch, ResetDatabase
import random
import csv


client = RecombeeClient(
  'pauna-filme', 'y71BMuz9oFej8p311yaoPD1SBTIyPQUIMvnXKhdtIRKM68y8FvKhh0wXa9Rps63b',
  region=Region.EU_WEST
)

# Clear the entire database
#client.send(ResetDatabase())

# Add properties of items
client.send(AddItemProperty('title', 'string'))
client.send(AddItemProperty('genre', 'string'))
client.send(AddItemProperty('premiere', 'string'))
client.send(AddItemProperty('runtime', 'int'))
client.send(AddItemProperty('score', 'double'))
client.send(AddItemProperty('languages', 'string'))
