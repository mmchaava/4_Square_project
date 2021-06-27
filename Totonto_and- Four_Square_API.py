{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "\n",
    "<h1 align=center><font size = 5>Toronto -  FourSquare API with Python</font></h1>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "## Assignment\n",
    "\n",
    "Making calls to the Foursquare API for different purposes.\n",
    "Constructing a URL to send a request to the API to search for a specific type of venues\n",
    "Exploring a particular venue, \n",
    "Exploring a Foursquare user, \n",
    "Exploring a geographical location\n",
    "Getting trending venues around a location.\n",
    "Using the visualization library, Folium, to visualize the results."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### Importing necessary Libraries\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Libraries imported.\n"
     ]
    }
   ],
   "source": [
    "import requests # library to handle requests\n",
    "import pandas as pd # library for data analsysis\n",
    "import numpy as np # library to handle data in a vectorized manner\n",
    "import random # library for random number generation\n",
    "\n",
    "print('Libraries imported.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Requirement already satisfied: geopy in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (2.1.0)\n",
      "Requirement already satisfied: geographiclib<2,>=1.49 in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (from geopy) (1.50)\n",
      "Libraries imported.\n"
     ]
    }
   ],
   "source": [
    "# Install libraries\n",
    "!pip install geopy\n",
    "from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values\n",
    "\n",
    "print('Libraries imported.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Libraries imported.\n"
     ]
    }
   ],
   "source": [
    "# libraries for displaying images\n",
    "from IPython.display import Image \n",
    "from IPython.core.display import HTML\n",
    "\n",
    "print('Libraries imported.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Requirement already satisfied: folium==0.5.0 in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (0.5.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (from folium==0.5.0) (2.11.3)\n",
      "Requirement already satisfied: branca in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (from folium==0.5.0) (0.4.2)\n",
      "Requirement already satisfied: six in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (from folium==0.5.0) (1.15.0)\n",
      "Requirement already satisfied: requests in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (from folium==0.5.0) (2.25.1)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (from jinja2->folium==0.5.0) (1.1.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (from requests->folium==0.5.0) (2020.12.5)\n",
      "Requirement already satisfied: chardet<5,>=3.0.2 in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (from requests->folium==0.5.0) (4.0.0)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (from requests->folium==0.5.0) (2.10)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\macdonald chaava\\anaconda3\\lib\\site-packages (from requests->folium==0.5.0) (1.26.4)\n",
      "Folium installed\n",
      "Libraries imported.\n"
     ]
    }
   ],
   "source": [
    "# tranforming json file into a pandas dataframe library\n",
    "from pandas.io.json import json_normalize\n",
    "\n",
    "! pip install folium==0.5.0\n",
    "import folium # plotting library\n",
    "\n",
    "print('Folium installed')\n",
    "print('Libraries imported.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### Define Foursquare Credentials and Version\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "##### Make sure that you have created a Foursquare developer account and have your credentials handy\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Obtain access token for the following steps.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Your credentails:\nCLIENT_ID: 0C2BD04A2V1DGSC4FXV5GIU01V2WURJBZ2XM044H3IGYJVRX\nCLIENT_SECRET:ILVXI2IA2FRQ5V2RKVBSEFDAG2NAAJNEXYODYFMGIZN1OXYJ\n"
     ]
    }
   ],
   "source": [
    "CLIENT_ID = '0C2BD04A2V1DGSC4FXV5GIU01V2WURJBZ2XM044H3IGYJVRX' # your Foursquare ID\n",
    "CLIENT_SECRET = 'ILVXI2IA2FRQ5V2RKVBSEFDAG2NAAJNEXYODYFMGIZN1OXYJ' # your Foursquare Secret\n",
    "ACCESS_TOKEN = '3DX01N4AZOQ0X2BRIR535EIDGLL1F1KR20ERF3KEP3RKFB2Z' # your FourSquare Access Token\n",
    "VERSION = '20180604'\n",
    "LIMIT = 30\n",
    "print('Your credentails:')\n",
    "print('CLIENT_ID: ' + CLIENT_ID)\n",
    "print('CLIENT_SECRET:' + CLIENT_SECRET)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Let's again assume that you are staying at the Ghalib Hotel, Toronto, ON. So let's start by converting the Contrad Hotel's address to its latitude and longitude coordinates.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In order to define an instance of the geocoder, we need to define a user_agent. We will name our agent <em>foursquare_agent</em>, as shown below.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "43.6503989 -79.38387458264332\n"
     ]
    }
   ],
   "source": [
    "address = '111 Richmond Street W. Toronto, ON'\n",
    "\n",
    "geolocator = Nominatim(user_agent=\"foursquare_agent\")\n",
    "location = geolocator.geocode(address)\n",
    "latitude = location.latitude\n",
    "longitude = location.longitude\n",
    "print(latitude, longitude)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "<a id=\"item1\"></a>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "## 1. Search for a specific venue category\n",
    "\n",
    "> `https://api.foursquare.com/v2/venues/`**search**`?client_id=`**CLIENT_ID**`&client_secret=`**CLIENT_SECRET**`&ll=`**LATITUDE**`,`**LONGITUDE**`&v=`**VERSION**`&query=`**QUERY**`&radius=`**RADIUS**`&limit=`**LIMIT**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Now, let's assume that it is lunch time, and you are craving Italian food. So, let's define a query to search for Italian food that is within 500 metres.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    },
    "scrolled": true
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "The Grill .... OK!\n"
     ]
    }
   ],
   "source": [
    "search_query = 'The Grill'\n",
    "radius = 500\n",
    "print(search_query + ' .... OK!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Define the corresponding URL\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "'https://api.foursquare.com/v2/venues/search?client_id=0C2BD04A2V1DGSC4FXV5GIU01V2WURJBZ2XM044H3IGYJVRX&client_secret=ILVXI2IA2FRQ5V2RKVBSEFDAG2NAAJNEXYODYFMGIZN1OXYJ&ll=43.6503989,-79.38387458264332&oauth_token=3DX01N4AZOQ0X2BRIR535EIDGLL1F1KR20ERF3KEP3RKFB2Z&v=20180604&query=The Grill&radius=500&limit=30'"
      ]
     },
     "metadata": {},
     "execution_count": 8
    }
   ],
   "source": [
    "url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&oauth_token={}&v={}&query={}&radius={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude,ACCESS_TOKEN, VERSION, search_query, radius, LIMIT)\n",
    "url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Send the GET Request and examine the results\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    },
    "scrolled": true
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "97c087f6d',\n",
       "    'name': 'Fresh West Grill',\n",
       "    'location': {'address': '200 Bay St.',\n",
       "     'crossStreet': 'In Royal Bank Plaza',\n",
       "     'lat': 43.650474402619714,\n",
       "     'lng': -79.38314617590946,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.650474402619714,\n",
       "       'lng': -79.38314617590946}],\n",
       "     'distance': 59,\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['200 Bay St. (In Royal Bank Plaza)',\n",
       "      'Toronto ON',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d153941735',\n",
       "      'name': 'Burrito Place',\n",
       "      'pluralName': 'Burrito Places',\n",
       "      'shortName': 'Burritos',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/burrito_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4bbfffca2a89ef3b480af088',\n",
       "    'name': 'Easy & The 5th',\n",
       "    'location': {'address': '225 Richmond St W',\n",
       "     'crossStreet': 'at Duncan St',\n",
       "     'lat': 43.64930252773556,\n",
       "     'lng': -79.38915153913439,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.64930252773556,\n",
       "       'lng': -79.38915153913439}],\n",
       "     'distance': 442,\n",
       "     'postalCode': 'M5V 1W2',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['225 Richmond St W (at Duncan St)',\n",
       "      'Toronto ON M5V 1W2',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d11f941735',\n",
       "      'name': 'Nightclub',\n",
       "      'pluralName': 'Nightclubs',\n",
       "      'shortName': 'Nightclub',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/nightlife/nightclub_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4af8da92f964a5204a1022e3',\n",
       "    'name': 'Blue Stone Grill & Bar',\n",
       "    'location': {'address': '372 Bay St.',\n",
       "     'crossStreet': 'at Richmond St.',\n",
       "     'lat': 43.65118713330148,\n",
       "     'lng': -79.38113925615237,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.65118713330148,\n",
       "       'lng': -79.38113925615237}],\n",
       "     'distance': 237,\n",
       "     'postalCode': 'M5H 1M7',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['372 Bay St. (at Richmond St.)',\n",
       "      'Toronto ON M5H 1M7',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d11b941735',\n",
       "      'name': 'Pub',\n",
       "      'pluralName': 'Pubs',\n",
       "      'shortName': 'Pub',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/nightlife/pub_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4ae0cf40f964a520bc8221e3',\n",
       "    'name': \"Jack Astor's Bar & Grill\",\n",
       "    'location': {'address': '144 Front St W',\n",
       "     'crossStreet': 'at University Ave',\n",
       "     'lat': 43.645315,\n",
       "     'lng': -79.383837,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.645315,\n",
       "       'lng': -79.383837}],\n",
       "     'distance': 565,\n",
       "     'postalCode': 'M5J 2L7',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['144 Front St W (at University Ave)',\n",
       "      'Toronto ON M5J 2L7',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d14e941735',\n",
       "      'name': 'American Restaurant',\n",
       "      'pluralName': 'American Restaurants',\n",
       "      'shortName': 'American',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/default_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '5234f22411d2754113a667cf',\n",
       "    'name': \"Moxie's Classic Grill\",\n",
       "    'location': {'address': '70 University Ave',\n",
       "     'lat': 43.64640825187707,\n",
       "     'lng': -79.38445921313797,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.64640825187707,\n",
       "       'lng': -79.38445921313797}],\n",
       "     'distance': 446,\n",
       "     'postalCode': 'M5J 2M4',\n",
       "     'cc': 'CA',\n",
       "     'neighborhood': 'Entertainment District',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['70 University Ave',\n",
       "      'Toronto ON M5J 2M4',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d14e941735',\n",
       "      'name': 'American Restaurant',\n",
       "      'pluralName': 'American Restaurants',\n",
       "      'shortName': 'American',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/default_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4bc3169e461576b0f81c7e32',\n",
       "    'name': 'The Bagg Group',\n",
       "    'location': {'address': '85 Richmond St. West',\n",
       "     'crossStreet': 'by Bay',\n",
       "     'lat': 43.650651,\n",
       "     'lng': -79.383076,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.650651,\n",
       "       'lng': -79.383076}],\n",
       "     'distance': 70,\n",
       "     'postalCode': 'M5H 2C9',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ONt',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['85 Richmond St. West (by Bay)',\n",
       "      'Toronto ONt M5H 2C9',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d124941735',\n",
       "      'name': 'Office',\n",
       "      'pluralName': 'Offices',\n",
       "      'shortName': 'Office',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/building/default_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4bba6e7f3db7b713a94e239a',\n",
       "    'name': 'Make Up For Ever Pro (The Bay)',\n",
       "    'location': {'crossStreet': 'Yonge Street & Queen Street',\n",
       "     'lat': 43.650995,\n",
       "     'lng': -79.383192,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.650995,\n",
       "       'lng': -79.383192}],\n",
       "     'distance': 86,\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['Yonge Street & Queen Street',\n",
       "      'Toronto ON',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d10c951735',\n",
       "      'name': 'Cosmetics Shop',\n",
       "      'pluralName': 'Cosmetics Shops',\n",
       "      'shortName': 'Cosmetics',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/beauty_cosmetic_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '5214e7c111d2a83379eae21f',\n",
       "    'name': 'The Chase',\n",
       "    'location': {'address': '10 Temperance St fl 5',\n",
       "     'crossStreet': 'Yonge St',\n",
       "     'lat': 43.650951982093595,\n",
       "     'lng': -79.37942201983014,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.650951982093595,\n",
       "       'lng': -79.37942201983014}],\n",
       "     'distance': 363,\n",
       "     'postalCode': 'M5H 1Y4',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['10 Temperance St fl 5 (Yonge St)',\n",
       "      'Toronto ON M5H 1Y4',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d157941735',\n",
       "      'name': 'New American Restaurant',\n",
       "      'pluralName': 'New American Restaurants',\n",
       "      'shortName': 'New American',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/newamerican_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4b828753f964a520d8d630e3',\n",
       "    'name': 'Grill It Up!',\n",
       "    'location': {'lat': 43.650838,\n",
       "     'lng': -79.3797,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.650838,\n",
       "       'lng': -79.3797}],\n",
       "     'distance': 339,\n",
       "     'cc': 'CA',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d143941735',\n",
       "      'name': 'Breakfast Spot',\n",
       "      'pluralName': 'Breakfast Spots',\n",
       "      'shortName': 'Breakfast',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/breakfast_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4bcf52fa77b29c74d8de8882',\n",
       "    'name': 'The Printing House',\n",
       "    'location': {'lat': 43.64888169503831,\n",
       "     'lng': -79.38515855038983,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.64888169503831,\n",
       "       'lng': -79.38515855038983}],\n",
       "     'distance': 198,\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['Toronto ON', 'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d130941735',\n",
       "      'name': 'Building',\n",
       "      'pluralName': 'Buildings',\n",
       "      'shortName': 'Building',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/building/default_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4b68aed1f964a520de862be3',\n",
       "    'name': 'The Rex Hotel Jazz & Blues Bar',\n",
       "    'location': {'address': '194 Queen St W',\n",
       "     'crossStreet': 'Queen & St. Patrick',\n",
       "     'lat': 43.65050475544005,\n",
       "     'lng': -79.38857723389897,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.65050475544005,\n",
       "       'lng': -79.38857723389897}],\n",
       "     'distance': 378,\n",
       "     'postalCode': 'M5V 1Z1',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['194 Queen St W (Queen & St. Patrick)',\n",
       "      'Toronto ON M5V 1Z1',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d1e7931735',\n",
       "      'name': 'Jazz Club',\n",
       "      'pluralName': 'Jazz Clubs',\n",
       "      'shortName': 'Jazz Club',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/arts_entertainment/musicvenue_jazzclub_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'venuePage': {'id': '62225795'},\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4ad4c062f964a520e5f720e3',\n",
       "    'name': 'Four Seasons Centre for the Performing Arts',\n",
       "    'location': {'address': '145 Queen St. W',\n",
       "     'crossStreet': 'at University Ave.',\n",
       "     'lat': 43.650592,\n",
       "     'lng': -79.385806,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.650592,\n",
       "       'lng': -79.385806}],\n",
       "     'distance': 157,\n",
       "     'postalCode': 'M5H 4G1',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['145 Queen St. W (at University Ave.)',\n",
       "      'Toronto ON M5H 4G1',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '5032792091d4c4b30a586d5c',\n",
       "      'name': 'Concert Hall',\n",
       "      'pluralName': 'Concert Halls',\n",
       "      'shortName': 'Concert Hall',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/arts_entertainment/musicvenue_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '5e711481c1b2850008240c83',\n",
       "    'name': 'The Source',\n",
       "    'location': {'address': '130 King St W, Unit CWW2',\n",
       "     'lat': 43.648448,\n",
       "     'lng': -79.383294,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.648448,\n",
       "       'lng': -79.383294}],\n",
       "     'distance': 222,\n",
       "     'postalCode': 'M5X 1B5',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['130 King St W, Unit CWW2',\n",
       "      'Toronto ON M5X 1B5',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d122951735',\n",
       "      'name': 'Electronics Store',\n",
       "      'pluralName': 'Electronics Stores',\n",
       "      'shortName': 'Electronics',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/technology_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4ccce9a1b571b60c1c03d665',\n",
       "    'name': 'Locked Out Of The Office',\n",
       "    'location': {'lat': 43.64953,\n",
       "     'lng': -79.384495,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.64953,\n",
       "       'lng': -79.384495}],\n",
       "     'distance': 108,\n",
       "     'cc': 'CA',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d17c941735',\n",
       "      'name': 'Casino',\n",
       "      'pluralName': 'Casinos',\n",
       "      'shortName': 'Casino',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/arts_entertainment/casino_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '5a2c551a95d986072897bb18',\n",
       "    'name': 'Christmas Fair In The Square',\n",
       "    'location': {'lat': 43.652734,\n",
       "     'lng': -79.383543,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.652734,\n",
       "       'lng': -79.383543}],\n",
       "     'distance': 261,\n",
       "     'postalCode': 'M5H 2N2',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['Toronto ON M5H 2N2', 'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d1f1931735',\n",
       "      'name': 'General Entertainment',\n",
       "      'pluralName': 'General Entertainment',\n",
       "      'shortName': 'Entertainment',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/arts_entertainment/default_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4bb0509df964a520b7403ce3',\n",
       "    'name': 'The Grange',\n",
       "    'location': {'address': '20 St. Patrick St.',\n",
       "     'crossStreet': 'at Queen St.',\n",
       "     'lat': 43.6508053511762,\n",
       "     'lng': -79.38890752503383,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.6508053511762,\n",
       "       'lng': -79.38890752503383}],\n",
       "     'distance': 407,\n",
       "     'postalCode': 'M5V 1Z1',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['20 St. Patrick St. (at Queen St.)',\n",
       "      'Toronto ON M5V 1Z1',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4d954b06a243a5684965b473',\n",
       "      'name': 'Residential Building (Apartment / Condo)',\n",
       "      'pluralName': 'Residential Buildings (Apartments / Condos)',\n",
       "      'shortName': 'Residential',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/building/apartment_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '5ca3c7d2c824ae002b99afaf',\n",
       "    'name': 'The Hunny Pot',\n",
       "    'location': {'address': '202 Queen St W',\n",
       "     'crossStreet': 'St Patrick',\n",
       "     'lat': 43.650411,\n",
       "     'lng': -79.389121,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.650411,\n",
       "       'lng': -79.389121}],\n",
       "     'distance': 422,\n",
       "     'postalCode': 'M5V 1Z2',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['202 Queen St W (St Patrick)',\n",
       "      'Toronto ON M5V 1Z2',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '52c71aaf3cf9994f4e043d17',\n",
       "      'name': 'Marijuana Dispensary',\n",
       "      'pluralName': 'Marijuana Dispensaries',\n",
       "      'shortName': 'Dispensary',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/shops/dispensary_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4ad4c062f964a520caf720e3',\n",
       "    'name': 'The Waterfall Stage',\n",
       "    'location': {'address': '1 First Canadian Place',\n",
       "     'lat': 43.64882465972433,\n",
       "     'lng': -79.3816781046333,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.64882465972433,\n",
       "       'lng': -79.3816781046333}],\n",
       "     'distance': 249,\n",
       "     'postalCode': 'M5X 1A9',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['1 First Canadian Place',\n",
       "      'Toronto ON M5X 1A9',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d171941735',\n",
       "      'name': 'Event Space',\n",
       "      'pluralName': 'Event Spaces',\n",
       "      'shortName': 'Event Space',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/building/eventspace_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '529fa999498ece612904193a',\n",
       "    'name': 'The Fifth Gastropub',\n",
       "    'location': {'address': '225 Richmond Street',\n",
       "     'crossStreet': 'at Duncan St.',\n",
       "     'lat': 43.64932984158663,\n",
       "     'lng': -79.3891708633644,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.64932984158663,\n",
       "       'lng': -79.3891708633644}],\n",
       "     'distance': 442,\n",
       "     'postalCode': 'M5V 1W2',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['225 Richmond Street (at Duncan St.)',\n",
       "      'Toronto ON M5V 1W2',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d11b941735',\n",
       "      'name': 'Pub',\n",
       "      'pluralName': 'Pubs',\n",
       "      'shortName': 'Pub',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/nightlife/pub_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4c0fc4167189c9280199dab6',\n",
       "    'name': 'Freshwest Grill',\n",
       "    'location': {'address': '100 Wellington Street West',\n",
       "     'lat': 43.647061428784056,\n",
       "     'lng': -79.38236459644109,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.647061428784056,\n",
       "       'lng': -79.38236459644109}],\n",
       "     'distance': 390,\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['100 Wellington Street West',\n",
       "      'Toronto ON',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d1c1941735',\n",
       "      'name': 'Mexican Restaurant',\n",
       "      'pluralName': 'Mexican Restaurants',\n",
       "      'shortName': 'Mexican',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/mexican_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '4ceecce5ecb66a31becd2c4c',\n",
       "    'name': 'the [clinic] Chiropractic Health Centre',\n",
       "    'location': {'address': '1210 - 401 Bay Street',\n",
       "     'crossStreet': 'Queen & Bay',\n",
       "     'lat': 43.64801821927537,\n",
       "     'lng': -79.38347057803215,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.64801821927537,\n",
       "       'lng': -79.38347057803215}],\n",
       "     'distance': 267,\n",
       "     'postalCode': 'M5H 2Y4',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['1210 - 401 Bay Street (Queen & Bay)',\n",
       "      'Toronto ON M5H 2Y4',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d104941735',\n",
       "      'name': 'Medical Center',\n",
       "      'pluralName': 'Medical Centers',\n",
       "      'shortName': 'Medical',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/building/medical_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'venuePage': {'id': '60613524'},\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '52607369498e7993d9089598',\n",
       "    'name': 'The Dream Cafe',\n",
       "    'location': {'lat': 43.650755,\n",
       "     'lng': -79.382269,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.650755,\n",
       "       'lng': -79.382269}],\n",
       "     'distance': 135,\n",
       "     'cc': 'CA',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d16d941735',\n",
       "      'name': 'Café',\n",
       "      'pluralName': 'Cafés',\n",
       "      'shortName': 'Café',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/cafe_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False},\n",
       "   {'id': '538bf897498e8301b31e1e65',\n",
       "    'name': 'The Porch',\n",
       "    'location': {'address': '250 Adelaide Street West',\n",
       "     'crossStreet': 'Duncan Street',\n",
       "     'lat': 43.64825063999569,\n",
       "     'lng': -79.38900157428692,\n",
       "     'labeledLatLngs': [{'label': 'display',\n",
       "       'lat': 43.64825063999569,\n",
       "       'lng': -79.38900157428692}],\n",
       "     'distance': 477,\n",
       "     'postalCode': 'M5H 1X6',\n",
       "     'cc': 'CA',\n",
       "     'city': 'Toronto',\n",
       "     'state': 'ON',\n",
       "     'country': 'Canada',\n",
       "     'formattedAddress': ['250 Adelaide Street West (Duncan Street)',\n",
       "      'Toronto ON M5H 1X6',\n",
       "      'Canada']},\n",
       "    'categories': [{'id': '4bf58dd8d48988d116941735',\n",
       "      'name': 'Bar',\n",
       "      'pluralName': 'Bars',\n",
       "      'shortName': 'Bar',\n",
       "      'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/nightlife/pub_',\n",
       "       'suffix': '.png'},\n",
       "      'primary': True}],\n",
       "    'referralId': 'v-1624756340',\n",
       "    'hasPerk': False}]}}"
      ]
     },
     "metadata": {},
     "execution_count": 9
    }
   ],
   "source": [
    "results = requests.get(url).json()\n",
    "results"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Get relevant part of JSON and transform it into a _pandas_ dataframe\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stderr",
     "text": [
      "<ipython-input-10-5acf500bf9ad>:5: FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead\n  dataframe = json_normalize(venues)\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "                         id                                    name  \\\n",
       "0  4ad69511f964a520e40721e3  The Keg Steakhouse + Bar - York Street   \n",
       "1  4c50d7d7250dd13a12fa377c                         City of Toronto   \n",
       "2  4ee117150cd686aafce847f4                     The Fifth & Terrace   \n",
       "3  5dfd2cd7227f9b000858fddc                               The Alley   \n",
       "4  5a9b3ef3d1a40244fc9e8373                      The Good Son Pizza   \n",
       "\n",
       "                                          categories    referralId  hasPerk  \\\n",
       "0  [{'id': '4bf58dd8d48988d1c4941735', 'name': 'R...  v-1624756340    False   \n",
       "1  [{'id': '50aa9e094b90af0d42d5de0d', 'name': 'C...  v-1624756340    False   \n",
       "2  [{'id': '52e81612bcbc57f1066b79f9', 'name': 'M...  v-1624756340    False   \n",
       "3  [{'id': '52e81612bcbc57f1066b7a0c', 'name': 'B...  v-1624756340    False   \n",
       "4  [{'id': '4bf58dd8d48988d1ca941735', 'name': 'P...  v-1624756340    False   \n",
       "\n",
       "                 location.address              location.crossStreet  \\\n",
       "0                     165 York St  btwn Richmond St. & Adelaide St.   \n",
       "1                             NaN                               NaN   \n",
       "2  225 Richmond St W., Suite 501b                               NaN   \n",
       "3               120 Adelaide St W                               NaN   \n",
       "4               111 Richmond St w                               NaN   \n",
       "\n",
       "   location.lat  location.lng  \\\n",
       "0     43.649987    -79.384103   \n",
       "1     43.650072    -79.383888   \n",
       "2     43.649250    -79.389320   \n",
       "3     43.650302    -79.383509   \n",
       "4     43.650696    -79.384149   \n",
       "\n",
       "                             location.labeledLatLngs  location.distance  \\\n",
       "0  [{'label': 'display', 'lat': 43.64998659318569...                 49   \n",
       "1                                                NaN                 36   \n",
       "2  [{'label': 'display', 'lat': 43.649249809335, ...                456   \n",
       "3  [{'label': 'display', 'lat': 43.650302, 'lng':...                 31   \n",
       "4  [{'label': 'display', 'lat': 43.650696, 'lng':...                 39   \n",
       "\n",
       "  location.postalCode location.cc location.city location.state  \\\n",
       "0             M5H 3R8          CA       Toronto             ON   \n",
       "1                 NaN          CA           NaN        Ontario   \n",
       "2             M5V 1W2          CA       Toronto             ON   \n",
       "3             M5H 1P9          CA       Toronto             ON   \n",
       "4             M5H 2G4          CA       Toronto             ON   \n",
       "\n",
       "  location.country                          location.formattedAddress  \\\n",
       "0           Canada  [165 York St (btwn Richmond St. & Adelaide St....   \n",
       "1           Canada                                  [Ontario, Canada]   \n",
       "2           Canada  [225 Richmond St W., Suite 501b, Toronto ON M5...   \n",
       "3           Canada    [120 Adelaide St W, Toronto ON M5H 1P9, Canada]   \n",
       "4           Canada    [111 Richmond St w, Toronto ON M5H 2G4, Canada]   \n",
       "\n",
       "  venuePage.id location.neighborhood  \n",
       "0   1359966175                   NaN  \n",
       "1          NaN                   NaN  \n",
       "2    401666972                   NaN  \n",
       "3          NaN                   NaN  \n",
       "4          NaN                   NaN  "
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>id</th>\n      <th>name</th>\n      <th>categories</th>\n      <th>referralId</th>\n      <th>hasPerk</th>\n      <th>location.address</th>\n      <th>location.crossStreet</th>\n      <th>location.lat</th>\n      <th>location.lng</th>\n      <th>location.labeledLatLngs</th>\n      <th>location.distance</th>\n      <th>location.postalCode</th>\n      <th>location.cc</th>\n      <th>location.city</th>\n      <th>location.state</th>\n      <th>location.country</th>\n      <th>location.formattedAddress</th>\n      <th>venuePage.id</th>\n      <th>location.neighborhood</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>4ad69511f964a520e40721e3</td>\n      <td>The Keg Steakhouse + Bar - York Street</td>\n      <td>[{'id': '4bf58dd8d48988d1c4941735', 'name': 'R...</td>\n      <td>v-1624756340</td>\n      <td>False</td>\n      <td>165 York St</td>\n      <td>btwn Richmond St. &amp; Adelaide St.</td>\n      <td>43.649987</td>\n      <td>-79.384103</td>\n      <td>[{'label': 'display', 'lat': 43.64998659318569...</td>\n      <td>49</td>\n      <td>M5H 3R8</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[165 York St (btwn Richmond St. &amp; Adelaide St....</td>\n      <td>1359966175</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>4c50d7d7250dd13a12fa377c</td>\n      <td>City of Toronto</td>\n      <td>[{'id': '50aa9e094b90af0d42d5de0d', 'name': 'C...</td>\n      <td>v-1624756340</td>\n      <td>False</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>43.650072</td>\n      <td>-79.383888</td>\n      <td>NaN</td>\n      <td>36</td>\n      <td>NaN</td>\n      <td>CA</td>\n      <td>NaN</td>\n      <td>Ontario</td>\n      <td>Canada</td>\n      <td>[Ontario, Canada]</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>4ee117150cd686aafce847f4</td>\n      <td>The Fifth &amp; Terrace</td>\n      <td>[{'id': '52e81612bcbc57f1066b79f9', 'name': 'M...</td>\n      <td>v-1624756340</td>\n      <td>False</td>\n      <td>225 Richmond St W., Suite 501b</td>\n      <td>NaN</td>\n      <td>43.649250</td>\n      <td>-79.389320</td>\n      <td>[{'label': 'display', 'lat': 43.649249809335, ...</td>\n      <td>456</td>\n      <td>M5V 1W2</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[225 Richmond St W., Suite 501b, Toronto ON M5...</td>\n      <td>401666972</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>5dfd2cd7227f9b000858fddc</td>\n      <td>The Alley</td>\n      <td>[{'id': '52e81612bcbc57f1066b7a0c', 'name': 'B...</td>\n      <td>v-1624756340</td>\n      <td>False</td>\n      <td>120 Adelaide St W</td>\n      <td>NaN</td>\n      <td>43.650302</td>\n      <td>-79.383509</td>\n      <td>[{'label': 'display', 'lat': 43.650302, 'lng':...</td>\n      <td>31</td>\n      <td>M5H 1P9</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[120 Adelaide St W, Toronto ON M5H 1P9, Canada]</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>5a9b3ef3d1a40244fc9e8373</td>\n      <td>The Good Son Pizza</td>\n      <td>[{'id': '4bf58dd8d48988d1ca941735', 'name': 'P...</td>\n      <td>v-1624756340</td>\n      <td>False</td>\n      <td>111 Richmond St w</td>\n      <td>NaN</td>\n      <td>43.650696</td>\n      <td>-79.384149</td>\n      <td>[{'label': 'display', 'lat': 43.650696, 'lng':...</td>\n      <td>39</td>\n      <td>M5H 2G4</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[111 Richmond St w, Toronto ON M5H 2G4, Canada]</td>\n      <td>NaN</td>\n      <td>NaN</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 10
    }
   ],
   "source": [
    "# assign relevant part of JSON to venues\n",
    "venues = results['response']['venues']\n",
    "\n",
    "# tranform venues into a dataframe\n",
    "dataframe = json_normalize(venues)\n",
    "dataframe.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Define information of interest and filter dataframe\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    },
    "scrolled": true
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "                                           name  \\\n",
       "0        The Keg Steakhouse + Bar - York Street   \n",
       "1                               City of Toronto   \n",
       "2                           The Fifth & Terrace   \n",
       "3                                     The Alley   \n",
       "4                            The Good Son Pizza   \n",
       "5                               Freshwest Grill   \n",
       "6                          Bulldog On The Block   \n",
       "7                              Fresh West Grill   \n",
       "8                                Easy & The 5th   \n",
       "9                        Blue Stone Grill & Bar   \n",
       "10                     Jack Astor's Bar & Grill   \n",
       "11                        Moxie's Classic Grill   \n",
       "12                               The Bagg Group   \n",
       "13               Make Up For Ever Pro (The Bay)   \n",
       "14                                    The Chase   \n",
       "15                                 Grill It Up!   \n",
       "16                           The Printing House   \n",
       "17               The Rex Hotel Jazz & Blues Bar   \n",
       "18  Four Seasons Centre for the Performing Arts   \n",
       "19                                   The Source   \n",
       "20                     Locked Out Of The Office   \n",
       "21                 Christmas Fair In The Square   \n",
       "22                                   The Grange   \n",
       "23                                The Hunny Pot   \n",
       "24                          The Waterfall Stage   \n",
       "25                          The Fifth Gastropub   \n",
       "26                              Freshwest Grill   \n",
       "27      the [clinic] Chiropractic Health Centre   \n",
       "28                               The Dream Cafe   \n",
       "29                                    The Porch   \n",
       "\n",
       "                                  categories                         address  \\\n",
       "0                                 Restaurant                     165 York St   \n",
       "1                                       City                             NaN   \n",
       "2                 Modern European Restaurant  225 Richmond St W., Suite 501b   \n",
       "3                            Bubble Tea Shop               120 Adelaide St W   \n",
       "4                                Pizza Place               111 Richmond St w   \n",
       "5                         Mexican Restaurant               120 Adelaide St W   \n",
       "6                                Coffee Shop               111 Richmond St W   \n",
       "7                              Burrito Place                     200 Bay St.   \n",
       "8                                  Nightclub               225 Richmond St W   \n",
       "9                                        Pub                     372 Bay St.   \n",
       "10                       American Restaurant                  144 Front St W   \n",
       "11                       American Restaurant               70 University Ave   \n",
       "12                                    Office            85 Richmond St. West   \n",
       "13                            Cosmetics Shop                             NaN   \n",
       "14                   New American Restaurant           10 Temperance St fl 5   \n",
       "15                            Breakfast Spot                             NaN   \n",
       "16                                  Building                             NaN   \n",
       "17                                 Jazz Club                  194 Queen St W   \n",
       "18                              Concert Hall                 145 Queen St. W   \n",
       "19                         Electronics Store        130 King St W, Unit CWW2   \n",
       "20                                    Casino                             NaN   \n",
       "21                     General Entertainment                             NaN   \n",
       "22  Residential Building (Apartment / Condo)              20 St. Patrick St.   \n",
       "23                      Marijuana Dispensary                  202 Queen St W   \n",
       "24                               Event Space          1 First Canadian Place   \n",
       "25                                       Pub             225 Richmond Street   \n",
       "26                        Mexican Restaurant      100 Wellington Street West   \n",
       "27                            Medical Center           1210 - 401 Bay Street   \n",
       "28                                      Café                             NaN   \n",
       "29                                       Bar        250 Adelaide Street West   \n",
       "\n",
       "                         crossStreet        lat        lng  \\\n",
       "0   btwn Richmond St. & Adelaide St.  43.649987 -79.384103   \n",
       "1                                NaN  43.650072 -79.383888   \n",
       "2                                NaN  43.649250 -79.389320   \n",
       "3                                NaN  43.650302 -79.383509   \n",
       "4                                NaN  43.650696 -79.384149   \n",
       "5                                NaN  43.650444 -79.383202   \n",
       "6                               York  43.650652 -79.384141   \n",
       "7                In Royal Bank Plaza  43.650474 -79.383146   \n",
       "8                       at Duncan St  43.649303 -79.389152   \n",
       "9                    at Richmond St.  43.651187 -79.381139   \n",
       "10                 at University Ave  43.645315 -79.383837   \n",
       "11                               NaN  43.646408 -79.384459   \n",
       "12                            by Bay  43.650651 -79.383076   \n",
       "13       Yonge Street & Queen Street  43.650995 -79.383192   \n",
       "14                          Yonge St  43.650952 -79.379422   \n",
       "15                               NaN  43.650838 -79.379700   \n",
       "16                               NaN  43.648882 -79.385159   \n",
       "17               Queen & St. Patrick  43.650505 -79.388577   \n",
       "18                at University Ave.  43.650592 -79.385806   \n",
       "19                               NaN  43.648448 -79.383294   \n",
       "20                               NaN  43.649530 -79.384495   \n",
       "21                               NaN  43.652734 -79.383543   \n",
       "22                      at Queen St.  43.650805 -79.388908   \n",
       "23                        St Patrick  43.650411 -79.389121   \n",
       "24                               NaN  43.648825 -79.381678   \n",
       "25                     at Duncan St.  43.649330 -79.389171   \n",
       "26                               NaN  43.647061 -79.382365   \n",
       "27                       Queen & Bay  43.648018 -79.383471   \n",
       "28                               NaN  43.650755 -79.382269   \n",
       "29                     Duncan Street  43.648251 -79.389002   \n",
       "\n",
       "                                       labeledLatLngs  distance postalCode  \\\n",
       "0   [{'label': 'display', 'lat': 43.64998659318569...        49    M5H 3R8   \n",
       "1                                                 NaN        36        NaN   \n",
       "2   [{'label': 'display', 'lat': 43.649249809335, ...       456    M5V 1W2   \n",
       "3   [{'label': 'display', 'lat': 43.650302, 'lng':...        31    M5H 1P9   \n",
       "4   [{'label': 'display', 'lat': 43.650696, 'lng':...        39    M5H 2G4   \n",
       "5   [{'label': 'display', 'lat': 43.65044403076172...        54    M5H 1T1   \n",
       "6   [{'label': 'display', 'lat': 43.65065218852629...        35    M5H 2G4   \n",
       "7   [{'label': 'display', 'lat': 43.65047440261971...        59        NaN   \n",
       "8   [{'label': 'display', 'lat': 43.64930252773556...       442    M5V 1W2   \n",
       "9   [{'label': 'display', 'lat': 43.65118713330148...       237    M5H 1M7   \n",
       "10  [{'label': 'display', 'lat': 43.645315, 'lng':...       565    M5J 2L7   \n",
       "11  [{'label': 'display', 'lat': 43.64640825187707...       446    M5J 2M4   \n",
       "12  [{'label': 'display', 'lat': 43.650651, 'lng':...        70    M5H 2C9   \n",
       "13  [{'label': 'display', 'lat': 43.650995, 'lng':...        86        NaN   \n",
       "14  [{'label': 'display', 'lat': 43.65095198209359...       363    M5H 1Y4   \n",
       "15  [{'label': 'display', 'lat': 43.650838, 'lng':...       339        NaN   \n",
       "16  [{'label': 'display', 'lat': 43.64888169503831...       198        NaN   \n",
       "17  [{'label': 'display', 'lat': 43.65050475544005...       378    M5V 1Z1   \n",
       "18  [{'label': 'display', 'lat': 43.650592, 'lng':...       157    M5H 4G1   \n",
       "19  [{'label': 'display', 'lat': 43.648448, 'lng':...       222    M5X 1B5   \n",
       "20  [{'label': 'display', 'lat': 43.64953, 'lng': ...       108        NaN   \n",
       "21  [{'label': 'display', 'lat': 43.652734, 'lng':...       261    M5H 2N2   \n",
       "22  [{'label': 'display', 'lat': 43.6508053511762,...       407    M5V 1Z1   \n",
       "23  [{'label': 'display', 'lat': 43.650411, 'lng':...       422    M5V 1Z2   \n",
       "24  [{'label': 'display', 'lat': 43.64882465972433...       249    M5X 1A9   \n",
       "25  [{'label': 'display', 'lat': 43.64932984158663...       442    M5V 1W2   \n",
       "26  [{'label': 'display', 'lat': 43.64706142878405...       390        NaN   \n",
       "27  [{'label': 'display', 'lat': 43.64801821927537...       267    M5H 2Y4   \n",
       "28  [{'label': 'display', 'lat': 43.650755, 'lng':...       135        NaN   \n",
       "29  [{'label': 'display', 'lat': 43.64825063999569...       477    M5H 1X6   \n",
       "\n",
       "    cc     city    state country  \\\n",
       "0   CA  Toronto       ON  Canada   \n",
       "1   CA      NaN  Ontario  Canada   \n",
       "2   CA  Toronto       ON  Canada   \n",
       "3   CA  Toronto       ON  Canada   \n",
       "4   CA  Toronto       ON  Canada   \n",
       "5   CA  Toronto       ON  Canada   \n",
       "6   CA  Toronto       ON  Canada   \n",
       "7   CA  Toronto       ON  Canada   \n",
       "8   CA  Toronto       ON  Canada   \n",
       "9   CA  Toronto       ON  Canada   \n",
       "10  CA  Toronto       ON  Canada   \n",
       "11  CA  Toronto       ON  Canada   \n",
       "12  CA  Toronto      ONt  Canada   \n",
       "13  CA  Toronto       ON  Canada   \n",
       "14  CA  Toronto       ON  Canada   \n",
       "15  CA      NaN      NaN  Canada   \n",
       "16  CA  Toronto       ON  Canada   \n",
       "17  CA  Toronto       ON  Canada   \n",
       "18  CA  Toronto       ON  Canada   \n",
       "19  CA  Toronto       ON  Canada   \n",
       "20  CA      NaN      NaN  Canada   \n",
       "21  CA  Toronto       ON  Canada   \n",
       "22  CA  Toronto       ON  Canada   \n",
       "23  CA  Toronto       ON  Canada   \n",
       "24  CA  Toronto       ON  Canada   \n",
       "25  CA  Toronto       ON  Canada   \n",
       "26  CA  Toronto       ON  Canada   \n",
       "27  CA  Toronto       ON  Canada   \n",
       "28  CA      NaN      NaN  Canada   \n",
       "29  CA  Toronto       ON  Canada   \n",
       "\n",
       "                                     formattedAddress            neighborhood  \\\n",
       "0   [165 York St (btwn Richmond St. & Adelaide St....                     NaN   \n",
       "1                                   [Ontario, Canada]                     NaN   \n",
       "2   [225 Richmond St W., Suite 501b, Toronto ON M5...                     NaN   \n",
       "3     [120 Adelaide St W, Toronto ON M5H 1P9, Canada]                     NaN   \n",
       "4     [111 Richmond St w, Toronto ON M5H 2G4, Canada]                     NaN   \n",
       "5     [120 Adelaide St W, Toronto ON M5H 1T1, Canada]                     NaN   \n",
       "6   [111 Richmond St W (York), Toronto ON M5H 2G4,...                     NaN   \n",
       "7   [200 Bay St. (In Royal Bank Plaza), Toronto ON...                     NaN   \n",
       "8   [225 Richmond St W (at Duncan St), Toronto ON ...                     NaN   \n",
       "9   [372 Bay St. (at Richmond St.), Toronto ON M5H...                     NaN   \n",
       "10  [144 Front St W (at University Ave), Toronto O...                     NaN   \n",
       "11    [70 University Ave, Toronto ON M5J 2M4, Canada]  Entertainment District   \n",
       "12  [85 Richmond St. West (by Bay), Toronto ONt M5...                     NaN   \n",
       "13  [Yonge Street & Queen Street, Toronto ON, Canada]                     NaN   \n",
       "14  [10 Temperance St fl 5 (Yonge St), Toronto ON ...                     NaN   \n",
       "15                                           [Canada]                     NaN   \n",
       "16                               [Toronto ON, Canada]                     NaN   \n",
       "17  [194 Queen St W (Queen & St. Patrick), Toronto...                     NaN   \n",
       "18  [145 Queen St. W (at University Ave.), Toronto...                     NaN   \n",
       "19  [130 King St W, Unit CWW2, Toronto ON M5X 1B5,...                     NaN   \n",
       "20                                           [Canada]                     NaN   \n",
       "21                       [Toronto ON M5H 2N2, Canada]                     NaN   \n",
       "22  [20 St. Patrick St. (at Queen St.), Toronto ON...                     NaN   \n",
       "23  [202 Queen St W (St Patrick), Toronto ON M5V 1...                     NaN   \n",
       "24  [1 First Canadian Place, Toronto ON M5X 1A9, C...                     NaN   \n",
       "25  [225 Richmond Street (at Duncan St.), Toronto ...                     NaN   \n",
       "26   [100 Wellington Street West, Toronto ON, Canada]                     NaN   \n",
       "27  [1210 - 401 Bay Street (Queen & Bay), Toronto ...                     NaN   \n",
       "28                                           [Canada]                     NaN   \n",
       "29  [250 Adelaide Street West (Duncan Street), Tor...                     NaN   \n",
       "\n",
       "                          id  \n",
       "0   4ad69511f964a520e40721e3  \n",
       "1   4c50d7d7250dd13a12fa377c  \n",
       "2   4ee117150cd686aafce847f4  \n",
       "3   5dfd2cd7227f9b000858fddc  \n",
       "4   5a9b3ef3d1a40244fc9e8373  \n",
       "5   53ce95d5498e0eac81256ecb  \n",
       "6   5a3a846af62e0960e9364d11  \n",
       "7   52f3db84498ed9797c087f6d  \n",
       "8   4bbfffca2a89ef3b480af088  \n",
       "9   4af8da92f964a5204a1022e3  \n",
       "10  4ae0cf40f964a520bc8221e3  \n",
       "11  5234f22411d2754113a667cf  \n",
       "12  4bc3169e461576b0f81c7e32  \n",
       "13  4bba6e7f3db7b713a94e239a  \n",
       "14  5214e7c111d2a83379eae21f  \n",
       "15  4b828753f964a520d8d630e3  \n",
       "16  4bcf52fa77b29c74d8de8882  \n",
       "17  4b68aed1f964a520de862be3  \n",
       "18  4ad4c062f964a520e5f720e3  \n",
       "19  5e711481c1b2850008240c83  \n",
       "20  4ccce9a1b571b60c1c03d665  \n",
       "21  5a2c551a95d986072897bb18  \n",
       "22  4bb0509df964a520b7403ce3  \n",
       "23  5ca3c7d2c824ae002b99afaf  \n",
       "24  4ad4c062f964a520caf720e3  \n",
       "25  529fa999498ece612904193a  \n",
       "26  4c0fc4167189c9280199dab6  \n",
       "27  4ceecce5ecb66a31becd2c4c  \n",
       "28  52607369498e7993d9089598  \n",
       "29  538bf897498e8301b31e1e65  "
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>categories</th>\n      <th>address</th>\n      <th>crossStreet</th>\n      <th>lat</th>\n      <th>lng</th>\n      <th>labeledLatLngs</th>\n      <th>distance</th>\n      <th>postalCode</th>\n      <th>cc</th>\n      <th>city</th>\n      <th>state</th>\n      <th>country</th>\n      <th>formattedAddress</th>\n      <th>neighborhood</th>\n      <th>id</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>The Keg Steakhouse + Bar - York Street</td>\n      <td>Restaurant</td>\n      <td>165 York St</td>\n      <td>btwn Richmond St. &amp; Adelaide St.</td>\n      <td>43.649987</td>\n      <td>-79.384103</td>\n      <td>[{'label': 'display', 'lat': 43.64998659318569...</td>\n      <td>49</td>\n      <td>M5H 3R8</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[165 York St (btwn Richmond St. &amp; Adelaide St....</td>\n      <td>NaN</td>\n      <td>4ad69511f964a520e40721e3</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>City of Toronto</td>\n      <td>City</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>43.650072</td>\n      <td>-79.383888</td>\n      <td>NaN</td>\n      <td>36</td>\n      <td>NaN</td>\n      <td>CA</td>\n      <td>NaN</td>\n      <td>Ontario</td>\n      <td>Canada</td>\n      <td>[Ontario, Canada]</td>\n      <td>NaN</td>\n      <td>4c50d7d7250dd13a12fa377c</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>The Fifth &amp; Terrace</td>\n      <td>Modern European Restaurant</td>\n      <td>225 Richmond St W., Suite 501b</td>\n      <td>NaN</td>\n      <td>43.649250</td>\n      <td>-79.389320</td>\n      <td>[{'label': 'display', 'lat': 43.649249809335, ...</td>\n      <td>456</td>\n      <td>M5V 1W2</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[225 Richmond St W., Suite 501b, Toronto ON M5...</td>\n      <td>NaN</td>\n      <td>4ee117150cd686aafce847f4</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>The Alley</td>\n      <td>Bubble Tea Shop</td>\n      <td>120 Adelaide St W</td>\n      <td>NaN</td>\n      <td>43.650302</td>\n      <td>-79.383509</td>\n      <td>[{'label': 'display', 'lat': 43.650302, 'lng':...</td>\n      <td>31</td>\n      <td>M5H 1P9</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[120 Adelaide St W, Toronto ON M5H 1P9, Canada]</td>\n      <td>NaN</td>\n      <td>5dfd2cd7227f9b000858fddc</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>The Good Son Pizza</td>\n      <td>Pizza Place</td>\n      <td>111 Richmond St w</td>\n      <td>NaN</td>\n      <td>43.650696</td>\n      <td>-79.384149</td>\n      <td>[{'label': 'display', 'lat': 43.650696, 'lng':...</td>\n      <td>39</td>\n      <td>M5H 2G4</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[111 Richmond St w, Toronto ON M5H 2G4, Canada]</td>\n      <td>NaN</td>\n      <td>5a9b3ef3d1a40244fc9e8373</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Freshwest Grill</td>\n      <td>Mexican Restaurant</td>\n      <td>120 Adelaide St W</td>\n      <td>NaN</td>\n      <td>43.650444</td>\n      <td>-79.383202</td>\n      <td>[{'label': 'display', 'lat': 43.65044403076172...</td>\n      <td>54</td>\n      <td>M5H 1T1</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[120 Adelaide St W, Toronto ON M5H 1T1, Canada]</td>\n      <td>NaN</td>\n      <td>53ce95d5498e0eac81256ecb</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Bulldog On The Block</td>\n      <td>Coffee Shop</td>\n      <td>111 Richmond St W</td>\n      <td>York</td>\n      <td>43.650652</td>\n      <td>-79.384141</td>\n      <td>[{'label': 'display', 'lat': 43.65065218852629...</td>\n      <td>35</td>\n      <td>M5H 2G4</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[111 Richmond St W (York), Toronto ON M5H 2G4,...</td>\n      <td>NaN</td>\n      <td>5a3a846af62e0960e9364d11</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Fresh West Grill</td>\n      <td>Burrito Place</td>\n      <td>200 Bay St.</td>\n      <td>In Royal Bank Plaza</td>\n      <td>43.650474</td>\n      <td>-79.383146</td>\n      <td>[{'label': 'display', 'lat': 43.65047440261971...</td>\n      <td>59</td>\n      <td>NaN</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[200 Bay St. (In Royal Bank Plaza), Toronto ON...</td>\n      <td>NaN</td>\n      <td>52f3db84498ed9797c087f6d</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Easy &amp; The 5th</td>\n      <td>Nightclub</td>\n      <td>225 Richmond St W</td>\n      <td>at Duncan St</td>\n      <td>43.649303</td>\n      <td>-79.389152</td>\n      <td>[{'label': 'display', 'lat': 43.64930252773556...</td>\n      <td>442</td>\n      <td>M5V 1W2</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[225 Richmond St W (at Duncan St), Toronto ON ...</td>\n      <td>NaN</td>\n      <td>4bbfffca2a89ef3b480af088</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Blue Stone Grill &amp; Bar</td>\n      <td>Pub</td>\n      <td>372 Bay St.</td>\n      <td>at Richmond St.</td>\n      <td>43.651187</td>\n      <td>-79.381139</td>\n      <td>[{'label': 'display', 'lat': 43.65118713330148...</td>\n      <td>237</td>\n      <td>M5H 1M7</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[372 Bay St. (at Richmond St.), Toronto ON M5H...</td>\n      <td>NaN</td>\n      <td>4af8da92f964a5204a1022e3</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>Jack Astor's Bar &amp; Grill</td>\n      <td>American Restaurant</td>\n      <td>144 Front St W</td>\n      <td>at University Ave</td>\n      <td>43.645315</td>\n      <td>-79.383837</td>\n      <td>[{'label': 'display', 'lat': 43.645315, 'lng':...</td>\n      <td>565</td>\n      <td>M5J 2L7</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[144 Front St W (at University Ave), Toronto O...</td>\n      <td>NaN</td>\n      <td>4ae0cf40f964a520bc8221e3</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>Moxie's Classic Grill</td>\n      <td>American Restaurant</td>\n      <td>70 University Ave</td>\n      <td>NaN</td>\n      <td>43.646408</td>\n      <td>-79.384459</td>\n      <td>[{'label': 'display', 'lat': 43.64640825187707...</td>\n      <td>446</td>\n      <td>M5J 2M4</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[70 University Ave, Toronto ON M5J 2M4, Canada]</td>\n      <td>Entertainment District</td>\n      <td>5234f22411d2754113a667cf</td>\n    </tr>\n    <tr>\n      <th>12</th>\n      <td>The Bagg Group</td>\n      <td>Office</td>\n      <td>85 Richmond St. West</td>\n      <td>by Bay</td>\n      <td>43.650651</td>\n      <td>-79.383076</td>\n      <td>[{'label': 'display', 'lat': 43.650651, 'lng':...</td>\n      <td>70</td>\n      <td>M5H 2C9</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ONt</td>\n      <td>Canada</td>\n      <td>[85 Richmond St. West (by Bay), Toronto ONt M5...</td>\n      <td>NaN</td>\n      <td>4bc3169e461576b0f81c7e32</td>\n    </tr>\n    <tr>\n      <th>13</th>\n      <td>Make Up For Ever Pro (The Bay)</td>\n      <td>Cosmetics Shop</td>\n      <td>NaN</td>\n      <td>Yonge Street &amp; Queen Street</td>\n      <td>43.650995</td>\n      <td>-79.383192</td>\n      <td>[{'label': 'display', 'lat': 43.650995, 'lng':...</td>\n      <td>86</td>\n      <td>NaN</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[Yonge Street &amp; Queen Street, Toronto ON, Canada]</td>\n      <td>NaN</td>\n      <td>4bba6e7f3db7b713a94e239a</td>\n    </tr>\n    <tr>\n      <th>14</th>\n      <td>The Chase</td>\n      <td>New American Restaurant</td>\n      <td>10 Temperance St fl 5</td>\n      <td>Yonge St</td>\n      <td>43.650952</td>\n      <td>-79.379422</td>\n      <td>[{'label': 'display', 'lat': 43.65095198209359...</td>\n      <td>363</td>\n      <td>M5H 1Y4</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[10 Temperance St fl 5 (Yonge St), Toronto ON ...</td>\n      <td>NaN</td>\n      <td>5214e7c111d2a83379eae21f</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>Grill It Up!</td>\n      <td>Breakfast Spot</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>43.650838</td>\n      <td>-79.379700</td>\n      <td>[{'label': 'display', 'lat': 43.650838, 'lng':...</td>\n      <td>339</td>\n      <td>NaN</td>\n      <td>CA</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>Canada</td>\n      <td>[Canada]</td>\n      <td>NaN</td>\n      <td>4b828753f964a520d8d630e3</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>The Printing House</td>\n      <td>Building</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>43.648882</td>\n      <td>-79.385159</td>\n      <td>[{'label': 'display', 'lat': 43.64888169503831...</td>\n      <td>198</td>\n      <td>NaN</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[Toronto ON, Canada]</td>\n      <td>NaN</td>\n      <td>4bcf52fa77b29c74d8de8882</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>The Rex Hotel Jazz &amp; Blues Bar</td>\n      <td>Jazz Club</td>\n      <td>194 Queen St W</td>\n      <td>Queen &amp; St. Patrick</td>\n      <td>43.650505</td>\n      <td>-79.388577</td>\n      <td>[{'label': 'display', 'lat': 43.65050475544005...</td>\n      <td>378</td>\n      <td>M5V 1Z1</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[194 Queen St W (Queen &amp; St. Patrick), Toronto...</td>\n      <td>NaN</td>\n      <td>4b68aed1f964a520de862be3</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>Four Seasons Centre for the Performing Arts</td>\n      <td>Concert Hall</td>\n      <td>145 Queen St. W</td>\n      <td>at University Ave.</td>\n      <td>43.650592</td>\n      <td>-79.385806</td>\n      <td>[{'label': 'display', 'lat': 43.650592, 'lng':...</td>\n      <td>157</td>\n      <td>M5H 4G1</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[145 Queen St. W (at University Ave.), Toronto...</td>\n      <td>NaN</td>\n      <td>4ad4c062f964a520e5f720e3</td>\n    </tr>\n    <tr>\n      <th>19</th>\n      <td>The Source</td>\n      <td>Electronics Store</td>\n      <td>130 King St W, Unit CWW2</td>\n      <td>NaN</td>\n      <td>43.648448</td>\n      <td>-79.383294</td>\n      <td>[{'label': 'display', 'lat': 43.648448, 'lng':...</td>\n      <td>222</td>\n      <td>M5X 1B5</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[130 King St W, Unit CWW2, Toronto ON M5X 1B5,...</td>\n      <td>NaN</td>\n      <td>5e711481c1b2850008240c83</td>\n    </tr>\n    <tr>\n      <th>20</th>\n      <td>Locked Out Of The Office</td>\n      <td>Casino</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>43.649530</td>\n      <td>-79.384495</td>\n      <td>[{'label': 'display', 'lat': 43.64953, 'lng': ...</td>\n      <td>108</td>\n      <td>NaN</td>\n      <td>CA</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>Canada</td>\n      <td>[Canada]</td>\n      <td>NaN</td>\n      <td>4ccce9a1b571b60c1c03d665</td>\n    </tr>\n    <tr>\n      <th>21</th>\n      <td>Christmas Fair In The Square</td>\n      <td>General Entertainment</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>43.652734</td>\n      <td>-79.383543</td>\n      <td>[{'label': 'display', 'lat': 43.652734, 'lng':...</td>\n      <td>261</td>\n      <td>M5H 2N2</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[Toronto ON M5H 2N2, Canada]</td>\n      <td>NaN</td>\n      <td>5a2c551a95d986072897bb18</td>\n    </tr>\n    <tr>\n      <th>22</th>\n      <td>The Grange</td>\n      <td>Residential Building (Apartment / Condo)</td>\n      <td>20 St. Patrick St.</td>\n      <td>at Queen St.</td>\n      <td>43.650805</td>\n      <td>-79.388908</td>\n      <td>[{'label': 'display', 'lat': 43.6508053511762,...</td>\n      <td>407</td>\n      <td>M5V 1Z1</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[20 St. Patrick St. (at Queen St.), Toronto ON...</td>\n      <td>NaN</td>\n      <td>4bb0509df964a520b7403ce3</td>\n    </tr>\n    <tr>\n      <th>23</th>\n      <td>The Hunny Pot</td>\n      <td>Marijuana Dispensary</td>\n      <td>202 Queen St W</td>\n      <td>St Patrick</td>\n      <td>43.650411</td>\n      <td>-79.389121</td>\n      <td>[{'label': 'display', 'lat': 43.650411, 'lng':...</td>\n      <td>422</td>\n      <td>M5V 1Z2</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[202 Queen St W (St Patrick), Toronto ON M5V 1...</td>\n      <td>NaN</td>\n      <td>5ca3c7d2c824ae002b99afaf</td>\n    </tr>\n    <tr>\n      <th>24</th>\n      <td>The Waterfall Stage</td>\n      <td>Event Space</td>\n      <td>1 First Canadian Place</td>\n      <td>NaN</td>\n      <td>43.648825</td>\n      <td>-79.381678</td>\n      <td>[{'label': 'display', 'lat': 43.64882465972433...</td>\n      <td>249</td>\n      <td>M5X 1A9</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[1 First Canadian Place, Toronto ON M5X 1A9, C...</td>\n      <td>NaN</td>\n      <td>4ad4c062f964a520caf720e3</td>\n    </tr>\n    <tr>\n      <th>25</th>\n      <td>The Fifth Gastropub</td>\n      <td>Pub</td>\n      <td>225 Richmond Street</td>\n      <td>at Duncan St.</td>\n      <td>43.649330</td>\n      <td>-79.389171</td>\n      <td>[{'label': 'display', 'lat': 43.64932984158663...</td>\n      <td>442</td>\n      <td>M5V 1W2</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[225 Richmond Street (at Duncan St.), Toronto ...</td>\n      <td>NaN</td>\n      <td>529fa999498ece612904193a</td>\n    </tr>\n    <tr>\n      <th>26</th>\n      <td>Freshwest Grill</td>\n      <td>Mexican Restaurant</td>\n      <td>100 Wellington Street West</td>\n      <td>NaN</td>\n      <td>43.647061</td>\n      <td>-79.382365</td>\n      <td>[{'label': 'display', 'lat': 43.64706142878405...</td>\n      <td>390</td>\n      <td>NaN</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[100 Wellington Street West, Toronto ON, Canada]</td>\n      <td>NaN</td>\n      <td>4c0fc4167189c9280199dab6</td>\n    </tr>\n    <tr>\n      <th>27</th>\n      <td>the [clinic] Chiropractic Health Centre</td>\n      <td>Medical Center</td>\n      <td>1210 - 401 Bay Street</td>\n      <td>Queen &amp; Bay</td>\n      <td>43.648018</td>\n      <td>-79.383471</td>\n      <td>[{'label': 'display', 'lat': 43.64801821927537...</td>\n      <td>267</td>\n      <td>M5H 2Y4</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[1210 - 401 Bay Street (Queen &amp; Bay), Toronto ...</td>\n      <td>NaN</td>\n      <td>4ceecce5ecb66a31becd2c4c</td>\n    </tr>\n    <tr>\n      <th>28</th>\n      <td>The Dream Cafe</td>\n      <td>Café</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>43.650755</td>\n      <td>-79.382269</td>\n      <td>[{'label': 'display', 'lat': 43.650755, 'lng':...</td>\n      <td>135</td>\n      <td>NaN</td>\n      <td>CA</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>Canada</td>\n      <td>[Canada]</td>\n      <td>NaN</td>\n      <td>52607369498e7993d9089598</td>\n    </tr>\n    <tr>\n      <th>29</th>\n      <td>The Porch</td>\n      <td>Bar</td>\n      <td>250 Adelaide Street West</td>\n      <td>Duncan Street</td>\n      <td>43.648251</td>\n      <td>-79.389002</td>\n      <td>[{'label': 'display', 'lat': 43.64825063999569...</td>\n      <td>477</td>\n      <td>M5H 1X6</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[250 Adelaide Street West (Duncan Street), Tor...</td>\n      <td>NaN</td>\n      <td>538bf897498e8301b31e1e65</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 11
    }
   ],
   "source": [
    "# keep only columns that include venue name, and anything that is associated with location\n",
    "filtered_columns = ['name', 'categories'] + [col for col in dataframe.columns if col.startswith('location.')] + ['id']\n",
    "dataframe_filtered = dataframe.loc[:, filtered_columns]\n",
    "\n",
    "# function that extracts the category of the venue\n",
    "def get_category_type(row):\n",
    "    try:\n",
    "        categories_list = row['categories']\n",
    "    except:\n",
    "        categories_list = row['venue.categories']\n",
    "        \n",
    "    if len(categories_list) == 0:\n",
    "        return None\n",
    "    else:\n",
    "        return categories_list[0]['name']\n",
    "\n",
    "# filter the category for each row\n",
    "dataframe_filtered['categories'] = dataframe_filtered.apply(get_category_type, axis=1)\n",
    "\n",
    "# clean column names by keeping only last term\n",
    "dataframe_filtered.columns = [column.split('.')[-1] for column in dataframe_filtered.columns]\n",
    "\n",
    "dataframe_filtered"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Let's visualize the Italian restaurants that are nearby\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "0          The Keg Steakhouse + Bar - York Street\n",
       "1                                 City of Toronto\n",
       "2                             The Fifth & Terrace\n",
       "3                                       The Alley\n",
       "4                              The Good Son Pizza\n",
       "5                                 Freshwest Grill\n",
       "6                            Bulldog On The Block\n",
       "7                                Fresh West Grill\n",
       "8                                  Easy & The 5th\n",
       "9                          Blue Stone Grill & Bar\n",
       "10                       Jack Astor's Bar & Grill\n",
       "11                          Moxie's Classic Grill\n",
       "12                                 The Bagg Group\n",
       "13                 Make Up For Ever Pro (The Bay)\n",
       "14                                      The Chase\n",
       "15                                   Grill It Up!\n",
       "16                             The Printing House\n",
       "17                 The Rex Hotel Jazz & Blues Bar\n",
       "18    Four Seasons Centre for the Performing Arts\n",
       "19                                     The Source\n",
       "20                       Locked Out Of The Office\n",
       "21                   Christmas Fair In The Square\n",
       "22                                     The Grange\n",
       "23                                  The Hunny Pot\n",
       "24                            The Waterfall Stage\n",
       "25                            The Fifth Gastropub\n",
       "26                                Freshwest Grill\n",
       "27        the [clinic] Chiropractic Health Centre\n",
       "28                                 The Dream Cafe\n",
       "29                                      The Porch\n",
       "Name: name, dtype: object"
      ]
     },
     "metadata": {},
     "execution_count": 12
    }
   ],
   "source": [
    "dataframe_filtered.name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    },
    "scrolled": true
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<folium.folium.Map at 0x273fc6fa430>"
      ],
      "text/html": "<div style=\"width:100%;\"><div style=\"position:relative;width:100%;height:0;padding-bottom:60%;\"><span style=\"color:#565656\">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src=\"about:blank\" style=\"position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;\" data-html=%3C%21DOCTYPE%20html%3E%0A%3Chead%3E%20%20%20%20%0A%20%20%20%20%3Cmeta%20http-equiv%3D%22content-type%22%20content%3D%22text/html%3B%20charset%3DUTF-8%22%20/%3E%0A%20%20%20%20%3Cscript%3EL_PREFER_CANVAS%20%3D%20false%3B%20L_NO_TOUCH%20%3D%20false%3B%20L_DISABLE_3D%20%3D%20false%3B%3C/script%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//cdn.jsdelivr.net/npm/leaflet%401.2.0/dist/leaflet.js%22%3E%3C/script%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js%22%3E%3C/script%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js%22%3E%3C/script%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js%22%3E%3C/script%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//cdn.jsdelivr.net/npm/leaflet%401.2.0/dist/leaflet.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//rawgit.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css%22/%3E%0A%20%20%20%20%3Cstyle%3Ehtml%2C%20body%20%7Bwidth%3A%20100%25%3Bheight%3A%20100%25%3Bmargin%3A%200%3Bpadding%3A%200%3B%7D%3C/style%3E%0A%20%20%20%20%3Cstyle%3E%23map%20%7Bposition%3Aabsolute%3Btop%3A0%3Bbottom%3A0%3Bright%3A0%3Bleft%3A0%3B%7D%3C/style%3E%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cstyle%3E%20%23map_6f7daff3e0df442abd0025b899c2d7de%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20position%20%3A%20relative%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20width%20%3A%20100.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20height%3A%20100.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20left%3A%200.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20top%3A%200.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%3C/style%3E%0A%20%20%20%20%20%20%20%20%0A%3C/head%3E%0A%3Cbody%3E%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22folium-map%22%20id%3D%22map_6f7daff3e0df442abd0025b899c2d7de%22%20%3E%3C/div%3E%0A%20%20%20%20%20%20%20%20%0A%3C/body%3E%0A%3Cscript%3E%20%20%20%20%0A%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20bounds%20%3D%20null%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20map_6f7daff3e0df442abd0025b899c2d7de%20%3D%20L.map%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%27map_6f7daff3e0df442abd0025b899c2d7de%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7Bcenter%3A%20%5B43.6503989%2C-79.38387458264332%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20zoom%3A%2013%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20maxBounds%3A%20bounds%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20layers%3A%20%5B%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20worldCopyJump%3A%20false%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20crs%3A%20L.CRS.EPSG3857%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20tile_layer_cbb25352e3b54e1f8943cfcd7c2ef14e%20%3D%20L.tileLayer%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%27https%3A//%7Bs%7D.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22attribution%22%3A%20null%2C%0A%20%20%22detectRetina%22%3A%20false%2C%0A%20%20%22maxZoom%22%3A%2018%2C%0A%20%20%22minZoom%22%3A%201%2C%0A%20%20%22noWrap%22%3A%20false%2C%0A%20%20%22subdomains%22%3A%20%22abc%22%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_9d881c0fc2264f5ba38467784a34561f%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.6503989%2C-79.38387458264332%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22red%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22red%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%2010%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_9624e6ba61284b9d89d80550c36df6ea%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_36ca5e3c83454b8296fdd6629ba9fff7%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_36ca5e3c83454b8296fdd6629ba9fff7%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EConrad%20Hotel%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_9624e6ba61284b9d89d80550c36df6ea.setContent%28html_36ca5e3c83454b8296fdd6629ba9fff7%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_9d881c0fc2264f5ba38467784a34561f.bindPopup%28popup_9624e6ba61284b9d89d80550c36df6ea%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_ab2368afd61147389e044e88716d4916%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64998659318569%2C-79.38410336664538%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_37e9dc44d930457e8b72904092a45975%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_bd647664bef64090bebed8c88bcde792%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_bd647664bef64090bebed8c88bcde792%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ERestaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_37e9dc44d930457e8b72904092a45975.setContent%28html_bd647664bef64090bebed8c88bcde792%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_ab2368afd61147389e044e88716d4916.bindPopup%28popup_37e9dc44d930457e8b72904092a45975%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_8668b36dcace4ec080cea2b788eab069%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.65007245086522%2C-79.38388845027751%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_e8e7da1bfbe24ac6909b319131d041ea%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_fee10565259149078f2f5b334a395517%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_fee10565259149078f2f5b334a395517%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ECity%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_e8e7da1bfbe24ac6909b319131d041ea.setContent%28html_fee10565259149078f2f5b334a395517%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_8668b36dcace4ec080cea2b788eab069.bindPopup%28popup_e8e7da1bfbe24ac6909b319131d041ea%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_033fdd62ccfb41a59eee598b8ddb0355%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.649249809335%2C-79.38931975675418%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_4ea4daef38a341ad8c061ca8cd39b904%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_aa1bab7d92c64976b1155c979a1d590c%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_aa1bab7d92c64976b1155c979a1d590c%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EModern%20European%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_4ea4daef38a341ad8c061ca8cd39b904.setContent%28html_aa1bab7d92c64976b1155c979a1d590c%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_033fdd62ccfb41a59eee598b8ddb0355.bindPopup%28popup_4ea4daef38a341ad8c061ca8cd39b904%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_0b61e14792fa436aac62c481cb644e00%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650302%2C-79.383509%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_023d75a3360b494db3e1cfaa496432ed%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_0407f7b3eb57473b8484c7664a9ae8c0%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_0407f7b3eb57473b8484c7664a9ae8c0%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EBubble%20Tea%20Shop%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_023d75a3360b494db3e1cfaa496432ed.setContent%28html_0407f7b3eb57473b8484c7664a9ae8c0%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_0b61e14792fa436aac62c481cb644e00.bindPopup%28popup_023d75a3360b494db3e1cfaa496432ed%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_367557d4cd5d489db25e9cfc7b5a3a82%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650696%2C-79.384149%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_5a38e3b728034c2caf02a9a8459b211a%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_34923dba54514e63a80f64405ffed616%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_34923dba54514e63a80f64405ffed616%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EPizza%20Place%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_5a38e3b728034c2caf02a9a8459b211a.setContent%28html_34923dba54514e63a80f64405ffed616%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_367557d4cd5d489db25e9cfc7b5a3a82.bindPopup%28popup_5a38e3b728034c2caf02a9a8459b211a%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_5d779088870f48958c25a17bfa711fbc%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.65044403076172%2C-79.3832015991211%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_a2fdd8d98db145f8b5ca433e0a979fd3%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_3747ec113db64da5ae442a371d3e2971%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_3747ec113db64da5ae442a371d3e2971%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EMexican%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_a2fdd8d98db145f8b5ca433e0a979fd3.setContent%28html_3747ec113db64da5ae442a371d3e2971%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_5d779088870f48958c25a17bfa711fbc.bindPopup%28popup_a2fdd8d98db145f8b5ca433e0a979fd3%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_5acba9368f3249c2a96e9ab1c374059b%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.65065218852629%2C-79.38414092873634%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_3bc16da6c5ef48f3b08950c212b6199f%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_6fdd598c3ca74f949e7080b4779dd431%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_6fdd598c3ca74f949e7080b4779dd431%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ECoffee%20Shop%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_3bc16da6c5ef48f3b08950c212b6199f.setContent%28html_6fdd598c3ca74f949e7080b4779dd431%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_5acba9368f3249c2a96e9ab1c374059b.bindPopup%28popup_3bc16da6c5ef48f3b08950c212b6199f%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_ec98a33346f64646be36c1de59d39ca7%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650474402619714%2C-79.38314617590946%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_8cee70cca07b40d3883f4b2d78f79682%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_b7efd00249b34f91976b6d6d7284f237%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_b7efd00249b34f91976b6d6d7284f237%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EBurrito%20Place%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_8cee70cca07b40d3883f4b2d78f79682.setContent%28html_b7efd00249b34f91976b6d6d7284f237%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_ec98a33346f64646be36c1de59d39ca7.bindPopup%28popup_8cee70cca07b40d3883f4b2d78f79682%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_97ff4101965a49b39b46824ea01bea0b%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64930252773556%2C-79.38915153913439%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_e37ca4144b2e4377b73ef68a5f93c66f%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_b7a2e2794f5548139b5cd0df31f3f341%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_b7a2e2794f5548139b5cd0df31f3f341%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ENightclub%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_e37ca4144b2e4377b73ef68a5f93c66f.setContent%28html_b7a2e2794f5548139b5cd0df31f3f341%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_97ff4101965a49b39b46824ea01bea0b.bindPopup%28popup_e37ca4144b2e4377b73ef68a5f93c66f%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_2f6b859c177547ec8145e0fa56b18ec8%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.65118713330148%2C-79.38113925615237%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_cfab005b3f144fd785a9debed53a945a%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_18b00f93d09a47c48dbf313acdb3e64b%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_18b00f93d09a47c48dbf313acdb3e64b%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EPub%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_cfab005b3f144fd785a9debed53a945a.setContent%28html_18b00f93d09a47c48dbf313acdb3e64b%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_2f6b859c177547ec8145e0fa56b18ec8.bindPopup%28popup_cfab005b3f144fd785a9debed53a945a%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_fd35b4f39a6540cc8aa80d46898f12a2%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.645315%2C-79.383837%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_24b78b6db28d403a82b9a50ec6db60c3%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_fe23faf074184e8c81342639eae9c3e3%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_fe23faf074184e8c81342639eae9c3e3%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EAmerican%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_24b78b6db28d403a82b9a50ec6db60c3.setContent%28html_fe23faf074184e8c81342639eae9c3e3%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_fd35b4f39a6540cc8aa80d46898f12a2.bindPopup%28popup_24b78b6db28d403a82b9a50ec6db60c3%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_d7f1b6719010455b93995c7be257714c%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64640825187707%2C-79.38445921313797%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_51a8735e361c48b79e5f105b370dafbe%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_ea3ca08c3fb5463082be6a7d41b5c4a8%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_ea3ca08c3fb5463082be6a7d41b5c4a8%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EAmerican%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_51a8735e361c48b79e5f105b370dafbe.setContent%28html_ea3ca08c3fb5463082be6a7d41b5c4a8%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_d7f1b6719010455b93995c7be257714c.bindPopup%28popup_51a8735e361c48b79e5f105b370dafbe%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_31d2707fecf24a12a9a9bf82e5b49d0a%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650651%2C-79.383076%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_cb71e2b79f624df79ee8bc21a20d6e21%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_5c39ebcba2e54a2e982cfa7c3407a4a1%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_5c39ebcba2e54a2e982cfa7c3407a4a1%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EOffice%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_cb71e2b79f624df79ee8bc21a20d6e21.setContent%28html_5c39ebcba2e54a2e982cfa7c3407a4a1%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_31d2707fecf24a12a9a9bf82e5b49d0a.bindPopup%28popup_cb71e2b79f624df79ee8bc21a20d6e21%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_2f5222f3912b440f9e166ab9e7d65c7d%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650995%2C-79.383192%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_751954b6f064479c91ac81211da2ceec%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_80848a2fc8a14af1a332267140e0155f%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_80848a2fc8a14af1a332267140e0155f%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ECosmetics%20Shop%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_751954b6f064479c91ac81211da2ceec.setContent%28html_80848a2fc8a14af1a332267140e0155f%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_2f5222f3912b440f9e166ab9e7d65c7d.bindPopup%28popup_751954b6f064479c91ac81211da2ceec%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_7a4265c8c7e241269217ca0c7f65e763%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650951982093595%2C-79.37942201983014%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_808967c0de3f4f2d95e2a1d638ace21a%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_fe8b05fee9d14b8b8b359eccf8f70b54%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_fe8b05fee9d14b8b8b359eccf8f70b54%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ENew%20American%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_808967c0de3f4f2d95e2a1d638ace21a.setContent%28html_fe8b05fee9d14b8b8b359eccf8f70b54%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_7a4265c8c7e241269217ca0c7f65e763.bindPopup%28popup_808967c0de3f4f2d95e2a1d638ace21a%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_22783c6a52694a838b3751570a47d23c%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650838%2C-79.3797%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_a1ae655a01b945a99dec0eba98d3a5d6%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_54e3434c560049aa8d4c32c2c15dcb1d%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_54e3434c560049aa8d4c32c2c15dcb1d%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EBreakfast%20Spot%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_a1ae655a01b945a99dec0eba98d3a5d6.setContent%28html_54e3434c560049aa8d4c32c2c15dcb1d%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_22783c6a52694a838b3751570a47d23c.bindPopup%28popup_a1ae655a01b945a99dec0eba98d3a5d6%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_bcdace90e6b64b4fa57ab6fc0c45a021%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64888169503831%2C-79.38515855038983%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_8e970302f79a46eeb8d7a871cff04eee%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_544f0eec40ff48cfacb1c1e5195bce31%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_544f0eec40ff48cfacb1c1e5195bce31%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EBuilding%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_8e970302f79a46eeb8d7a871cff04eee.setContent%28html_544f0eec40ff48cfacb1c1e5195bce31%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_bcdace90e6b64b4fa57ab6fc0c45a021.bindPopup%28popup_8e970302f79a46eeb8d7a871cff04eee%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_9b484ac712fa44a9a6052f4d6ff7211e%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.65050475544005%2C-79.38857723389897%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_94d6473131674f519e0423b51ce98da2%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_d40758f0ba1249c5b3daf0c602aa21e1%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_d40758f0ba1249c5b3daf0c602aa21e1%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EJazz%20Club%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_94d6473131674f519e0423b51ce98da2.setContent%28html_d40758f0ba1249c5b3daf0c602aa21e1%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_9b484ac712fa44a9a6052f4d6ff7211e.bindPopup%28popup_94d6473131674f519e0423b51ce98da2%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_4d7c0ca57f9d4b5c95e4960aa8b73e91%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650592%2C-79.385806%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_a8d777dc3e5e4d45915fc6a4c3ee5f3a%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_42ce6987ae46457e94f5e2c077021170%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_42ce6987ae46457e94f5e2c077021170%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EConcert%20Hall%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_a8d777dc3e5e4d45915fc6a4c3ee5f3a.setContent%28html_42ce6987ae46457e94f5e2c077021170%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_4d7c0ca57f9d4b5c95e4960aa8b73e91.bindPopup%28popup_a8d777dc3e5e4d45915fc6a4c3ee5f3a%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_499bd1d4bfa3469ea06ed44fe437d482%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.648448%2C-79.383294%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_87b07ce135bf4915af38e596b8cd99a1%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_d91ece23ba6b437c982e8376a0d3e3c7%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_d91ece23ba6b437c982e8376a0d3e3c7%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EElectronics%20Store%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_87b07ce135bf4915af38e596b8cd99a1.setContent%28html_d91ece23ba6b437c982e8376a0d3e3c7%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_499bd1d4bfa3469ea06ed44fe437d482.bindPopup%28popup_87b07ce135bf4915af38e596b8cd99a1%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_58a0908ca60041259ceb18129373542f%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64953%2C-79.384495%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_a379b15c52a24e8785d6bc480f08242d%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_261540a784f5480b96e130e0d264d96d%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_261540a784f5480b96e130e0d264d96d%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ECasino%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_a379b15c52a24e8785d6bc480f08242d.setContent%28html_261540a784f5480b96e130e0d264d96d%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_58a0908ca60041259ceb18129373542f.bindPopup%28popup_a379b15c52a24e8785d6bc480f08242d%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_9d85692a01d04d84a6cae911e7502b35%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.652734%2C-79.383543%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_eca4cab38e68499d9183698860f6bdc1%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_b0b030aada8a4d6692d37c7dca24c7a8%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_b0b030aada8a4d6692d37c7dca24c7a8%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EGeneral%20Entertainment%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_eca4cab38e68499d9183698860f6bdc1.setContent%28html_b0b030aada8a4d6692d37c7dca24c7a8%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_9d85692a01d04d84a6cae911e7502b35.bindPopup%28popup_eca4cab38e68499d9183698860f6bdc1%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_d0761799f2f34c8d9f12b9bb9da51cf6%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.6508053511762%2C-79.38890752503383%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_165a6f7a5ab3490b86ed91450c99f773%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_7e69fbee9e774aacb08746f7ef35295b%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_7e69fbee9e774aacb08746f7ef35295b%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EResidential%20Building%20%28Apartment%20/%20Condo%29%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_165a6f7a5ab3490b86ed91450c99f773.setContent%28html_7e69fbee9e774aacb08746f7ef35295b%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_d0761799f2f34c8d9f12b9bb9da51cf6.bindPopup%28popup_165a6f7a5ab3490b86ed91450c99f773%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_b0685010a6dd4b6cbf89b5c027ddd3ff%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650411%2C-79.389121%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_b3dfffc1a7da4a4287af72595772ebac%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_a021b8cc40f84f6e87d7942886f50268%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_a021b8cc40f84f6e87d7942886f50268%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EMarijuana%20Dispensary%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_b3dfffc1a7da4a4287af72595772ebac.setContent%28html_a021b8cc40f84f6e87d7942886f50268%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_b0685010a6dd4b6cbf89b5c027ddd3ff.bindPopup%28popup_b3dfffc1a7da4a4287af72595772ebac%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_f80c392d72f4420d84bf6abba52838e6%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64882465972433%2C-79.3816781046333%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_87730d17165d4d8a9bdbba8c4a7b2d1c%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_b7d31b9a11ca47cfb92b7b7b7b43a7b4%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_b7d31b9a11ca47cfb92b7b7b7b43a7b4%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EEvent%20Space%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_87730d17165d4d8a9bdbba8c4a7b2d1c.setContent%28html_b7d31b9a11ca47cfb92b7b7b7b43a7b4%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_f80c392d72f4420d84bf6abba52838e6.bindPopup%28popup_87730d17165d4d8a9bdbba8c4a7b2d1c%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_265c52036e43400a98f5ba8baedfb9cb%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64932984158663%2C-79.3891708633644%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_5af9b68dc0454124b0199efdbb0d3ddd%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_a54ac1b33ea04fbf8490b83146a1b36a%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_a54ac1b33ea04fbf8490b83146a1b36a%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EPub%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_5af9b68dc0454124b0199efdbb0d3ddd.setContent%28html_a54ac1b33ea04fbf8490b83146a1b36a%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_265c52036e43400a98f5ba8baedfb9cb.bindPopup%28popup_5af9b68dc0454124b0199efdbb0d3ddd%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_7eada6c0c8294d2f993c2fd9ba2bc5ea%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.647061428784056%2C-79.38236459644109%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_9493e473c3284501b22a2b26708b374a%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_83569da2d5d743eda590cea41c225978%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_83569da2d5d743eda590cea41c225978%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EMexican%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_9493e473c3284501b22a2b26708b374a.setContent%28html_83569da2d5d743eda590cea41c225978%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_7eada6c0c8294d2f993c2fd9ba2bc5ea.bindPopup%28popup_9493e473c3284501b22a2b26708b374a%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_a96089ccad7b4453b4dd5a49cbfc4ca9%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64801821927537%2C-79.38347057803215%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_3e8a82b3304440f79653ab1e3fc28081%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_fe5d05415fbc4015b0ab501f1fe2bb78%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_fe5d05415fbc4015b0ab501f1fe2bb78%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EMedical%20Center%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_3e8a82b3304440f79653ab1e3fc28081.setContent%28html_fe5d05415fbc4015b0ab501f1fe2bb78%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_a96089ccad7b4453b4dd5a49cbfc4ca9.bindPopup%28popup_3e8a82b3304440f79653ab1e3fc28081%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_5b45f1f0acb04f71b695a47d45926f1c%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650755%2C-79.382269%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_b1d2c657c59e4eb8942e14dcd6b40ba7%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_4d210fcef5f4406b8640da3a31cf193c%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_4d210fcef5f4406b8640da3a31cf193c%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ECaf%C3%A9%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_b1d2c657c59e4eb8942e14dcd6b40ba7.setContent%28html_4d210fcef5f4406b8640da3a31cf193c%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_5b45f1f0acb04f71b695a47d45926f1c.bindPopup%28popup_b1d2c657c59e4eb8942e14dcd6b40ba7%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_c673645e432846d3a4c71666ad124332%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64825063999569%2C-79.38900157428692%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_6f7daff3e0df442abd0025b899c2d7de%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_803307ded34144c4b3957a345a40c75a%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_37a89913a12a4130bca4e93213a55ba4%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_37a89913a12a4130bca4e93213a55ba4%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EBar%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_803307ded34144c4b3957a345a40c75a.setContent%28html_37a89913a12a4130bca4e93213a55ba4%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_c673645e432846d3a4c71666ad124332.bindPopup%28popup_803307ded34144c4b3957a345a40c75a%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%3C/script%3E onload=\"this.contentDocument.open();this.contentDocument.write(    decodeURIComponent(this.getAttribute('data-html')));this.contentDocument.close();\" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>"
     },
     "metadata": {},
     "execution_count": 13
    }
   ],
   "source": [
    "venues_map = folium.Map(location=[latitude, longitude], zoom_start=13) # generate map centred around the Conrad Hotel\n",
    "\n",
    "# add a red circle marker to represent the Conrad Hotel\n",
    "folium.CircleMarker(\n",
    "    [latitude, longitude],\n",
    "    radius=10,\n",
    "    color='red',\n",
    "    popup='Conrad Hotel',\n",
    "    fill = True,\n",
    "    fill_color = 'red',\n",
    "    fill_opacity = 0.6\n",
    ").add_to(venues_map)\n",
    "\n",
    "# add the Italian restaurants as blue circle markers\n",
    "for lat, lng, label in zip(dataframe_filtered.lat, dataframe_filtered.lng, dataframe_filtered.categories):\n",
    "    folium.CircleMarker(\n",
    "        [lat, lng],\n",
    "        radius=5,\n",
    "        color='blue',\n",
    "        popup=label,\n",
    "        fill = True,\n",
    "        fill_color='blue',\n",
    "        fill_opacity=0.6\n",
    "    ).add_to(venues_map)\n",
    "\n",
    "# display map\n",
    "venues_map"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "<a id=\"item2\"></a>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "## 2. Explore a Given Venue\n",
    "\n",
    "> `https://api.foursquare.com/v2/venues/`**VENUE_ID**`?client_id=`**CLIENT_ID**`&client_secret=`**CLIENT_SECRET**`&v=`**VERSION**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### A. Let's explore the closest \"The Grill\" restaurant -- The Keg Steakhouse and Bar on York Street._\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "'https://api.foursquare.com/v2/venues/4ad69511f964a520e40721e3?client_id=0C2BD04A2V1DGSC4FXV5GIU01V2WURJBZ2XM044H3IGYJVRX&client_secret=ILVXI2IA2FRQ5V2RKVBSEFDAG2NAAJNEXYODYFMGIZN1OXYJ&oauth_token=3DX01N4AZOQ0X2BRIR535EIDGLL1F1KR20ERF3KEP3RKFB2Z&v=20180604'"
      ]
     },
     "metadata": {},
     "execution_count": 14
    }
   ],
   "source": [
    "venue_id = '4ad69511f964a520e40721e3' # The Keg Steakhouse + Bar - York Street\n",
    "url = 'https://api.foursquare.com/v2/venues/{}?client_id={}&client_secret={}&oauth_token={}&v={}'.format(venue_id, CLIENT_ID, CLIENT_SECRET,ACCESS_TOKEN, VERSION)\n",
    "url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Send GET request for result\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "dict_keys(['id', 'name', 'contact', 'location', 'canonicalUrl', 'categories', 'verified', 'stats', 'url', 'price', 'hasMenu', 'likes', 'like', 'dislike', 'ok', 'rating', 'ratingColor', 'ratingSignals', 'menu', 'allowMenuUrlEdit', 'beenHere', 'specials', 'photos', 'venuePage', 'reasons', 'description', 'page', 'hereNow', 'createdAt', 'tips', 'shortUrl', 'timeZone', 'listed', 'hours', 'popular', 'seasonalHours', 'defaultHours', 'pageUpdates', 'inbox', 'attributes', 'bestPhoto', 'colors'])\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "{'id': '4ad69511f964a520e40721e3',\n",
       " 'name': 'The Keg Steakhouse + Bar - York Street',\n",
       " 'contact': {'phone': '4167031773',\n",
       "  'formattedPhone': '(416) 703-1773',\n",
       "  'twitter': 'thekeg'},\n",
       " 'location': {'address': '165 York St',\n",
       "  'crossStreet': 'btwn Richmond St. & Adelaide St.',\n",
       "  'lat': 43.64998659318569,\n",
       "  'lng': -79.38410336664538,\n",
       "  'labeledLatLngs': [{'label': 'display',\n",
       "    'lat': 43.64998659318569,\n",
       "    'lng': -79.38410336664538}],\n",
       "  'postalCode': 'M5H 3R8',\n",
       "  'cc': 'CA',\n",
       "  'city': 'Toronto',\n",
       "  'state': 'ON',\n",
       "  'country': 'Canada',\n",
       "  'formattedAddress': ['165 York St (btwn Richmond St. & Adelaide St.)',\n",
       "   'Toronto ON M5H 3R8',\n",
       "   'Canada']},\n",
       " 'canonicalUrl': 'https://foursquare.com/v/the-keg-steakhouse--bar--york-street/4ad69511f964a520e40721e3',\n",
       " 'categories': [{'id': '4bf58dd8d48988d1c4941735',\n",
       "   'name': 'Restaurant',\n",
       "   'pluralName': 'Restaurants',\n",
       "   'shortName': 'Restaurant',\n",
       "   'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/default_',\n",
       "    'suffix': '.png'},\n",
       "   'primary': True}],\n",
       " 'verified': True,\n",
       " 'stats': {'tipCount': 79},\n",
       " 'url': 'https://kegsteakhouse.com/en/locations/york-street',\n",
       " 'price': {'tier': 2, 'message': 'Moderate', 'currency': '$'},\n",
       " 'hasMenu': True,\n",
       " 'likes': {'count': 269,\n",
       "  'groups': [{'type': 'others', 'count': 269, 'items': []}],\n",
       "  'summary': '269 Likes'},\n",
       " 'like': False,\n",
       " 'dislike': False,\n",
       " 'ok': False,\n",
       " 'rating': 8.4,\n",
       " 'ratingColor': '73CF42',\n",
       " 'ratingSignals': 213,\n",
       " 'menu': {'type': 'Menu',\n",
       "  'label': 'Menu',\n",
       "  'anchor': 'View Menu',\n",
       "  'url': 'https://foursquare.com/v/the-keg-steakhouse--bar--york-street/4ad69511f964a520e40721e3/menu',\n",
       "  'mobileUrl': 'https://foursquare.com/v/4ad69511f964a520e40721e3/device_menu'},\n",
       " 'allowMenuUrlEdit': True,\n",
       " 'beenHere': {'count': 0,\n",
       "  'unconfirmedCount': 0,\n",
       "  'marked': False,\n",
       "  'lastCheckinExpiredAt': 0},\n",
       " 'specials': {'count': 0, 'items': []},\n",
       " 'photos': {'count': 258,\n",
       "  'groups': [{'type': 'venue',\n",
       "    'name': 'Venue photos',\n",
       "    'count': 258,\n",
       "    'items': [{'id': '4fabe3cce4b09eda9f3da2ef',\n",
       "      'createdAt': 1336665036,\n",
       "      'source': {'name': 'Foursquare for iOS',\n",
       "       'url': 'https://foursquare.com/download/#/iphone'},\n",
       "      'prefix': 'https://fastly.4sqi.net/img/general/',\n",
       "      'suffix': '/xEqh8d6KTm0N4Ij5hCHX7sw6n2I8xG1m3MUTEIgA4Nw.jpg',\n",
       "      'width': 540,\n",
       "      'height': 540,\n",
       "      'user': {'id': '7411288',\n",
       "       'firstName': 'Susan',\n",
       "       'lastName': 'Park',\n",
       "       'gender': 'female',\n",
       "       'countryCode': 'CA',\n",
       "       'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',\n",
       "        'suffix': '/ACYFRLOXLEKG3PX0.jpg'}},\n",
       "      'visibility': 'public'}]}]},\n",
       " 'venuePage': {'id': '1359966175'},\n",
       " 'reasons': {'count': 1,\n",
       "  'items': [{'summary': 'Lots of people like this place',\n",
       "    'type': 'general',\n",
       "    'reasonName': 'rawLikesReason'}]},\n",
       " 'description': 'The Keg Steakhouse + Bar is the perfect place to connect. Find a location near you, see our menus, and join us to unwind with friends and create great memories over delicious food.',\n",
       " 'page': {'user': {'id': '1359966175',\n",
       "   'firstName': 'The Keg Steakhouse + Bar - York Street',\n",
       "   'gender': 'none',\n",
       "   'countryCode': 'CA',\n",
       "   'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',\n",
       "    'suffix': '/1359966175_ASgjI7Ra_XrBVTO6XoyYl_o2BHMfE66cPIWALKbERn-Apk5JcOVz3ox85bZ9ByrIlx6s4APQk.png'},\n",
       "   'type': 'venuePage',\n",
       "   'venue': {'id': '4ad69511f964a520e40721e3'},\n",
       "   'tips': {'count': 0},\n",
       "   'lists': {'groups': [{'type': 'created', 'count': 2, 'items': []}]},\n",
       "   'homeCity': 'Toronto, ON',\n",
       "   'bio': '',\n",
       "   'contact': {}}},\n",
       " 'hereNow': {'count': 0, 'summary': 'Nobody here', 'groups': []},\n",
       " 'createdAt': 1255576849,\n",
       " 'tips': {'count': 79,\n",
       "  'groups': [{'type': 'following',\n",
       "    'name': 'Tips from people you follow',\n",
       "    'count': 0,\n",
       "    'items': []},\n",
       "   {'type': 'others',\n",
       "    'name': 'All tips',\n",
       "    'count': 79,\n",
       "    'items': [{'id': '4cba3fabdd41a35d3d37e7a0',\n",
       "      'createdAt': 1287274411,\n",
       "      'text': 'Go for the twice bake potato. You will not regret it!',\n",
       "      'type': 'user',\n",
       "      'canonicalUrl': 'https://foursquare.com/item/4cba3fabdd41a35d3d37e7a0',\n",
       "      'likes': {'count': 3,\n",
       "       'groups': [{'type': 'others',\n",
       "         'count': 3,\n",
       "         'items': [{'id': '1006811',\n",
       "           'firstName': 'Kerry',\n",
       "           'lastName': 'McKibbin',\n",
       "           'gender': 'female',\n",
       "           'countryCode': 'CA',\n",
       "           'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',\n",
       "            'suffix': '/1006811-JRGADW0PLXUTUKUD.jpg'}}]}],\n",
       "       'summary': '3 likes'},\n",
       "      'like': False,\n",
       "      'logView': True,\n",
       "      'agreeCount': 3,\n",
       "      'disagreeCount': 0,\n",
       "      'todo': {'count': 0},\n",
       "      'user': {'id': '65588',\n",
       "       'firstName': 'Emma',\n",
       "       'lastName': 'Brooks',\n",
       "       'gender': 'female',\n",
       "       'countryCode': 'CA',\n",
       "       'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',\n",
       "        'suffix': '/65588-XKZNX3TSRXJ2SZON.jpg'}}}]}]},\n",
       " 'shortUrl': 'http://4sq.com/5P27eM',\n",
       " 'timeZone': 'America/Toronto',\n",
       " 'listed': {'count': 92,\n",
       "  'groups': [{'type': 'others',\n",
       "    'name': 'Lists from other people',\n",
       "    'count': 92,\n",
       "    'items': [{'id': '4ee5e760722e08826104a20c',\n",
       "      'name': 'Toronto, Canada',\n",
       "      'description': '',\n",
       "      'type': 'others',\n",
       "      'user': {'id': '5381506',\n",
       "       'firstName': 'Rafal',\n",
       "       'lastName': 'W.',\n",
       "       'gender': 'male',\n",
       "       'countryCode': 'GB',\n",
       "       'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',\n",
       "        'suffix': '/5381506_LCFGtpCV_1BM68oakIKNCdVoAQzPv6_Gd5XC0cRnVwoWM2Py55eWYHITibvA9Guf7XSxuIikU.jpg'}},\n",
       "      'editable': False,\n",
       "      'public': True,\n",
       "      'collaborative': False,\n",
       "      'url': '/mycognitive/list/toronto-canada',\n",
       "      'canonicalUrl': 'https://foursquare.com/mycognitive/list/toronto-canada',\n",
       "      'createdAt': 1323689824,\n",
       "      'updatedAt': 1395807773,\n",
       "      'photo': {'id': '4e41d744a8092520554ea170',\n",
       "       'createdAt': 1312937796,\n",
       "       'prefix': 'https://fastly.4sqi.net/img/general/',\n",
       "       'suffix': '/PEN3YPP3ACRXTVKUYWEZMDM5L2JFJWMZWZ151UZH2TPYVKOH.jpg',\n",
       "       'width': 720,\n",
       "       'height': 537,\n",
       "       'user': {'id': '5080210',\n",
       "        'firstName': 'Ryan',\n",
       "        'lastName': 'Caligiuri',\n",
       "        'gender': 'male',\n",
       "        'countryCode': 'CA',\n",
       "        'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',\n",
       "         'suffix': '/5080210-VXYYWMKS5FZMBRWR.jpg'}},\n",
       "       'visibility': 'public'},\n",
       "      'followers': {'count': 124},\n",
       "      'listItems': {'count': 114,\n",
       "       'items': [{'id': 'v4ad69511f964a520e40721e3',\n",
       "         'createdAt': 1324342362}]}},\n",
       "     {'id': '4f16f045e4b0042059da1a18',\n",
       "      'name': 'Bars close to ACC.',\n",
       "      'description': \"Coming to a Leafs game? Sweet! Just thought we'd throw this list together of nearby bars and restaurants. Air Canada Centre is located at 40 Bay Street just south of Union Station.\",\n",
       "      'type': 'others',\n",
       "      'user': {'id': '16730536',\n",
       "       'firstName': 'Toronto Maple Leafs',\n",
       "       'gender': 'none',\n",
       "       'countryCode': 'CA',\n",
       "       'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',\n",
       "        'suffix': '/ELBJCZ1RARXDXGPS.png'},\n",
       "       'type': 'page'},\n",
       "      'editable': False,\n",
       "      'public': True,\n",
       "      'collaborative': False,\n",
       "      'url': '/mapleleafs/list/bars-close-to-acc',\n",
       "      'canonicalUrl': 'https://foursquare.com/mapleleafs/list/bars-close-to-acc',\n",
       "      'createdAt': 1326903365,\n",
       "      'updatedAt': 1326903769,\n",
       "      'photo': {'id': '4f0cc440e4b0cdfb03181804',\n",
       "       'createdAt': 1326236736,\n",
       "       'prefix': 'https://fastly.4sqi.net/img/general/',\n",
       "       'suffix': '/OKJXYZJT5OOAHIUNKLUJUZHOBRANN50DHAVB4QFOPECEAPXK.jpg',\n",
       "       'width': 461,\n",
       "       'height': 346,\n",
       "       'user': {'id': '546057',\n",
       "        'firstName': 'Daniel',\n",
       "        'lastName': 'Plaw',\n",
       "        'gender': 'male',\n",
       "        'countryCode': 'CA',\n",
       "        'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',\n",
       "         'suffix': '/LVC1ECAJGKMIN2K2.jpg'}},\n",
       "       'visibility': 'public'},\n",
       "      'logView': True,\n",
       "      'followers': {'count': 28},\n",
       "      'listItems': {'count': 8,\n",
       "       'items': [{'id': 'v4ad69511f964a520e40721e3',\n",
       "         'createdAt': 1326903534}]}}]}]},\n",
       " 'hours': {'status': 'Open until Midnight',\n",
       "  'richStatus': {'entities': [], 'text': 'Open until Midnight'},\n",
       "  'isOpen': True,\n",
       "  'isLocalHoliday': False,\n",
       "  'dayData': [],\n",
       "  'timeframes': [{'days': 'Mon–Wed',\n",
       "    'open': [{'renderedTime': 'Midnight–1:00 AM'},\n",
       "     {'renderedTime': '11:30 AM–Midnight'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Thu–Fri',\n",
       "    'open': [{'renderedTime': 'Midnight–2:00 AM'},\n",
       "     {'renderedTime': '11:30 AM–Midnight'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Sat',\n",
       "    'includesToday': True,\n",
       "    'open': [{'renderedTime': 'Midnight–2:00 AM'},\n",
       "     {'renderedTime': '4:00 PM–Midnight'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Sun',\n",
       "    'open': [{'renderedTime': '4:00 PM–Midnight'}],\n",
       "    'segments': []}]},\n",
       " 'popular': {'status': 'Likely open',\n",
       "  'richStatus': {'entities': [], 'text': 'Likely open'},\n",
       "  'isOpen': True,\n",
       "  'isLocalHoliday': False,\n",
       "  'timeframes': [{'days': 'Today',\n",
       "    'includesToday': True,\n",
       "    'open': [{'renderedTime': '5:00 PM–11:00 PM'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Sun',\n",
       "    'open': [{'renderedTime': '6:00 PM–10:00 PM'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Mon',\n",
       "    'open': [{'renderedTime': '5:00 PM–10:00 PM'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Tue',\n",
       "    'open': [{'renderedTime': 'Noon–1:00 PM'},\n",
       "     {'renderedTime': '5:00 PM–10:00 PM'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Wed',\n",
       "    'open': [{'renderedTime': 'Noon–1:00 PM'},\n",
       "     {'renderedTime': '5:00 PM–11:00 PM'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Thu',\n",
       "    'open': [{'renderedTime': 'Noon–1:00 PM'},\n",
       "     {'renderedTime': '3:00 PM–Midnight'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Fri',\n",
       "    'open': [{'renderedTime': 'Noon–11:00 PM'}],\n",
       "    'segments': []}]},\n",
       " 'seasonalHours': [],\n",
       " 'defaultHours': {'status': 'Open until Midnight',\n",
       "  'richStatus': {'entities': [], 'text': 'Open until Midnight'},\n",
       "  'isOpen': True,\n",
       "  'isLocalHoliday': False,\n",
       "  'dayData': [],\n",
       "  'timeframes': [{'days': 'Mon–Wed',\n",
       "    'open': [{'renderedTime': 'Midnight–1:00 AM'},\n",
       "     {'renderedTime': '11:30 AM–Midnight'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Thu–Fri',\n",
       "    'open': [{'renderedTime': 'Midnight–2:00 AM'},\n",
       "     {'renderedTime': '11:30 AM–Midnight'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Sat',\n",
       "    'includesToday': True,\n",
       "    'open': [{'renderedTime': 'Midnight–2:00 AM'},\n",
       "     {'renderedTime': '4:00 PM–Midnight'}],\n",
       "    'segments': []},\n",
       "   {'days': 'Sun',\n",
       "    'open': [{'renderedTime': '4:00 PM–Midnight'}],\n",
       "    'segments': []}]},\n",
       " 'pageUpdates': {'count': 0, 'items': []},\n",
       " 'inbox': {'count': 0, 'items': []},\n",
       " 'attributes': {'groups': [{'type': 'price',\n",
       "    'name': 'Price',\n",
       "    'summary': '$$',\n",
       "    'count': 1,\n",
       "    'items': [{'displayName': 'Price', 'displayValue': '$$', 'priceTier': 2}]},\n",
       "   {'type': 'payments',\n",
       "    'name': 'Credit Cards',\n",
       "    'summary': 'No Credit Cards',\n",
       "    'count': 5,\n",
       "    'items': [{'displayName': 'Credit Cards', 'displayValue': 'No'}]},\n",
       "   {'type': 'outdoorSeating',\n",
       "    'name': 'Outdoor Seating',\n",
       "    'summary': 'Outdoor Seating',\n",
       "    'count': 1,\n",
       "    'items': [{'displayName': 'Outdoor Seating', 'displayValue': 'Yes'}]},\n",
       "   {'type': 'wifi',\n",
       "    'name': 'Wi-Fi',\n",
       "    'summary': 'Wi-Fi',\n",
       "    'count': 1,\n",
       "    'items': [{'displayName': 'Wi-Fi', 'displayValue': 'Yes'}]},\n",
       "   {'type': 'serves',\n",
       "    'name': 'Menus',\n",
       "    'summary': 'Happy Hour, Dinner & more',\n",
       "    'count': 8,\n",
       "    'items': [{'displayName': 'Brunch', 'displayValue': 'Brunch'},\n",
       "     {'displayName': 'Dinner', 'displayValue': 'Dinner'},\n",
       "     {'displayName': 'Happy Hour', 'displayValue': 'Happy Hour'}]},\n",
       "   {'type': 'drinks',\n",
       "    'name': 'Drinks',\n",
       "    'summary': 'Wine, Full Bar & Cocktails',\n",
       "    'count': 5,\n",
       "    'items': [{'displayName': 'Wine', 'displayValue': 'Wine'},\n",
       "     {'displayName': 'Full Bar', 'displayValue': 'Full Bar'},\n",
       "     {'displayName': 'Cocktails', 'displayValue': 'Cocktails'}]}]},\n",
       " 'bestPhoto': {'id': '4fabe3cce4b09eda9f3da2ef',\n",
       "  'createdAt': 1336665036,\n",
       "  'source': {'name': 'Foursquare for iOS',\n",
       "   'url': 'https://foursquare.com/download/#/iphone'},\n",
       "  'prefix': 'https://fastly.4sqi.net/img/general/',\n",
       "  'suffix': '/xEqh8d6KTm0N4Ij5hCHX7sw6n2I8xG1m3MUTEIgA4Nw.jpg',\n",
       "  'width': 540,\n",
       "  'height': 540,\n",
       "  'visibility': 'public'},\n",
       " 'colors': {'highlightColor': {'photoId': '4fabe3cce4b09eda9f3da2ef',\n",
       "   'value': -13625320},\n",
       "  'highlightTextColor': {'photoId': '4fabe3cce4b09eda9f3da2ef', 'value': -1},\n",
       "  'algoVersion': 3}}"
      ]
     },
     "metadata": {},
     "execution_count": 15
    }
   ],
   "source": [
    "result = requests.get(url).json()\n",
    "print(result['response']['venue'].keys())\n",
    "result['response']['venue']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### B. Get the venue's overall rating\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "8.4\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    print(result['response']['venue']['rating'])\n",
    "except:\n",
    "    print('This venue has not been rated yet.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "That is very good rating. Let's check the rating of the second closest Grill restaurant.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "This venue has not been rated yet.\n"
     ]
    }
   ],
   "source": [
    "venue_id = '5a9b3ef3d1a40244fc9e8373' # The Good Son Restaurant\n",
    "url = 'https://api.foursquare.com/v2/venues/{}?client_id={}&client_secret={}&oauth_token={}&v={}'.format(venue_id, CLIENT_ID, CLIENT_SECRET,ACCESS_TOKEN, VERSION)\n",
    "\n",
    "result = requests.get(url).json()\n",
    "try:\n",
    "    print(result['response']['venue']['rating'])\n",
    "except:\n",
    "    print('This venue has not been rated yet.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Since this restaurant has no ratings, let's check the third restaurant.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "8.0\n"
     ]
    }
   ],
   "source": [
    "venue_id = '4ee117150cd686aafce847f4' # ID of Ecco\n",
    "url = 'https://api.foursquare.com/v2/venues/{}?client_id={}&client_secret={}&oauth_token={}&v={}'.format(venue_id, CLIENT_ID, CLIENT_SECRET,ACCESS_TOKEN, VERSION)\n",
    "\n",
    "result = requests.get(url).json()\n",
    "try:\n",
    "    print(result['response']['venue']['rating'])\n",
    "except:\n",
    "    print('This venue has not been rated yet.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Since this restaurant has a good rating, let's explore it further.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### C. Get the number of tips\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "metadata": {},
     "execution_count": 19
    }
   ],
   "source": [
    "result['response']['venue']['tips']['count']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### D. Get the venue's tips\n",
    "\n",
    "> `https://api.foursquare.com/v2/venues/`**VENUE_ID**`/tips?client_id=`**CLIENT_ID**`&client_secret=`**CLIENT_SECRET**`&v=`**VERSION**`&limit=`**LIMIT**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Create URL and send GET request. Make sure to set limit to get all tips\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "{'meta': {'code': 200, 'requestId': '60d7d07897cf8309c0f366eb'},\n",
       " 'notifications': [{'type': 'notificationTray', 'item': {'unreadCount': 0}}],\n",
       " 'response': {'tips': {'count': 7,\n",
       "   'items': [{'id': '5269d3ec11d2d17acc48297c',\n",
       "     'createdAt': 1382667244,\n",
       "     'text': 'Amazing service and lovely atmosphere. Get the steaks - one of the best in the city. Shared sides of brocollini , mushrooms and chive potatoes and it was all spectacular. Banana churros best dessert!',\n",
       "     'type': 'user',\n",
       "     'canonicalUrl': 'https://foursquare.com/item/5269d3ec11d2d17acc48297c',\n",
       "     'likes': {'count': 1,\n",
       "      'groups': [{'type': 'others', 'count': 1, 'items': []}],\n",
       "      'summary': '1 like'},\n",
       "     'like': False,\n",
       "     'logView': True,\n",
       "     'agreeCount': 1,\n",
       "     'disagreeCount': 0,\n",
       "     'todo': {'count': 0},\n",
       "     'user': {'id': '921748',\n",
       "      'firstName': 'Melissa',\n",
       "      'lastName': 'Alvares',\n",
       "      'gender': 'female',\n",
       "      'countryCode': 'CA',\n",
       "      'photo': {'prefix': 'https://fastly.4sqi.net/img/user/',\n",
       "       'suffix': '/JA5OJD5ISBIYB0Q4.jpg'}}}]}}}"
      ]
     },
     "metadata": {},
     "execution_count": 20
    }
   ],
   "source": [
    "## Ecco Tips\n",
    "limit = 10 # set limit to be greater than or equal to the total number of tips\n",
    "url = 'https://api.foursquare.com/v2/venues/{}/tips?client_id={}&client_secret={}&oauth_token={}&v={}&limit={}'.format(venue_id, CLIENT_ID, CLIENT_SECRET,ACCESS_TOKEN, VERSION, limit)\n",
    "\n",
    "results = requests.get(url).json()\n",
    "results"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Get tips and list of associated features\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "dict_keys(['id', 'createdAt', 'text', 'type', 'canonicalUrl', 'likes', 'like', 'logView', 'agreeCount', 'disagreeCount', 'todo', 'user'])"
      ]
     },
     "metadata": {},
     "execution_count": 21
    }
   ],
   "source": [
    "tips = results['response']['tips']['items']\n",
    "\n",
    "tip = results['response']['tips']['items'][0]\n",
    "tip.keys()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Format column width and display all tips\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stderr",
     "text": [
      "<ipython-input-22-252e55242536>:1: FutureWarning: Passing a negative integer is deprecated in version 1.0 and will not be supported in future version. Instead, use None to not limit the column width.\n  pd.set_option('display.max_colwidth', -1)\n<ipython-input-22-252e55242536>:3: FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead\n  tips_df = json_normalize(tips) # json normalize tips\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "                                                                                                                                                                                                      text  \\\n",
       "0  Amazing service and lovely atmosphere. Get the steaks - one of the best in the city. Shared sides of brocollini , mushrooms and chive potatoes and it was all spectacular. Banana churros best dessert!   \n",
       "\n",
       "   agreeCount  disagreeCount                        id user.firstName  \\\n",
       "0  1           0              5269d3ec11d2d17acc48297c  Melissa         \n",
       "\n",
       "  user.lastName user.id  \n",
       "0  Alvares       921748  "
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>text</th>\n      <th>agreeCount</th>\n      <th>disagreeCount</th>\n      <th>id</th>\n      <th>user.firstName</th>\n      <th>user.lastName</th>\n      <th>user.id</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Amazing service and lovely atmosphere. Get the steaks - one of the best in the city. Shared sides of brocollini , mushrooms and chive potatoes and it was all spectacular. Banana churros best dessert!</td>\n      <td>1</td>\n      <td>0</td>\n      <td>5269d3ec11d2d17acc48297c</td>\n      <td>Melissa</td>\n      <td>Alvares</td>\n      <td>921748</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 22
    }
   ],
   "source": [
    "pd.set_option('display.max_colwidth', -1)\n",
    "\n",
    "tips_df = json_normalize(tips) # json normalize tips\n",
    "\n",
    "# columns to keep\n",
    "filtered_columns = ['text', 'agreeCount', 'disagreeCount', 'id', 'user.firstName', 'user.lastName', 'user.id']\n",
    "tips_filtered = tips_df.loc[:, filtered_columns]\n",
    "\n",
    "# display tips\n",
    "tips_filtered.reindex()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Now remember that because we are using a personal developer account, then we can access only 2 of the restaurant's tips, instead of all 15 tips.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "<a id=\"item3\"></a>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "## 3. Search a Foursquare User\n",
    "\n",
    "> `https://api.foursquare.com/v2/users/`**USER_ID**`?client_id=`**CLIENT_ID**`&client_secret=`**CLIENT_SECRET**`&v=`**VERSION**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### Define URL, send GET request and display features associated with user\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stderr",
     "text": [
      "<ipython-input-23-eebeb823ce76>:11: FutureWarning: Passing a negative integer is deprecated in version 1.0 and will not be supported in future version. Instead, use None to not limit the column width.\n  pd.set_option('display.max_colwidth', -1)\n<ipython-input-23-eebeb823ce76>:13: FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead\n  users_df = json_normalize(user_data)\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "                         id                                prefix  \\\n",
       "0  536d6b28498edcdeb859bc6c  https://fastly.4sqi.net/img/general/   \n",
       "\n",
       "                                                    suffix  width  height  \n",
       "0  /921748_fm2S57waLTDtl65qFTBe0fSWDfjv2w30zcMr6Isp8GE.jpg  717    959     "
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>id</th>\n      <th>prefix</th>\n      <th>suffix</th>\n      <th>width</th>\n      <th>height</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>536d6b28498edcdeb859bc6c</td>\n      <td>https://fastly.4sqi.net/img/general/</td>\n      <td>/921748_fm2S57waLTDtl65qFTBe0fSWDfjv2w30zcMr6Isp8GE.jpg</td>\n      <td>717</td>\n      <td>959</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 23
    }
   ],
   "source": [
    "idnumber = '921748' # user ID with most agree counts and complete profile\n",
    "\n",
    "url = 'https://api.foursquare.com/v2/users/{}/?client_id={}&client_secret={}&oauth_token={}&v={}'.format(idnumber,CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN,VERSION) # define URL\n",
    "\n",
    "# send GET request\n",
    "results = requests.get(url).json()\n",
    "\n",
    "user_data=results['response']['user']['photos']['items']\n",
    "\n",
    "#results\n",
    "pd.set_option('display.max_colwidth', -1)\n",
    "\n",
    "users_df = json_normalize(user_data)\n",
    "#This mainly used later to display the photo of the user\n",
    "filtered_columns = ['id','prefix','suffix','width','height']\n",
    "tips_filtered = users_df.loc[:, filtered_columns]\n",
    "#url\n",
    "tips_filtered"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "0    First Name: Melissa\nName: user.firstName, dtype: object\n0    Last Name: Alvares\nName: user.lastName, dtype: object\n"
     ]
    }
   ],
   "source": [
    "\n",
    "g=tips_df.loc[tips_df['user.id'] == '484542633']\n",
    "print('First Name: ' + tips_df['user.firstName'])\n",
    "print('Last Name: ' + tips_df['user.lastName'])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Retrieve the User's Profile Image\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/html": "<img src=\"https://fastly.4sqi.net/img/general/921748_fm2S57waLTDtl65qFTBe0fSWDfjv2w30zcMr6Isp8GE.jpg\"/>",
      "text/plain": [
       "<IPython.core.display.Image object>"
      ]
     },
     "metadata": {},
     "execution_count": 25
    }
   ],
   "source": [
    "# 1. grab prefix of photo \n",
    "# 2. grab suffix of photo\n",
    "# 3. concatenate them using the image size  \n",
    "Image(url='https://fastly.4sqi.net/img/general/921748_fm2S57waLTDtl65qFTBe0fSWDfjv2w30zcMr6Isp8GE.jpg')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Wow! So, Mellisa is an active Foursquare user with 9 tips.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### Get User's tips\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stderr",
     "text": [
      "<ipython-input-26-42201c265818>:10: FutureWarning: Passing a negative integer is deprecated in version 1.0 and will not be supported in future version. Instead, use None to not limit the column width.\n  pd.set_option('display.max_colwidth', -1)\n<ipython-input-26-42201c265818>:12: FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead\n  tips_df = json_normalize(tips)\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "                                                                                                                                                                                                       text  \\\n",
       "0  High quality falafel that doesn’t come from a cart on the side of the road?! Yes, it exists, and it exists at Taim. Highly recommended - even if you’re new to falafel.                                    \n",
       "1  If you are in the West Village and you choose to go to a nationwide chain coffee shop instead of 11th Street Cafe, then you are everything that is wrong with the world. This place is AWESOME!!!          \n",
       "2  A+! The New Whitney is MUCH more accessible and easier to navigate than the city’s other famous museums like the Met. I’m a big fan. If you’re on a budget: there’s free admission on Friday nights        \n",
       "3  I had the wings and they blew my mind. Plus, Leah (the owner) is pretty awesome, so you should definitely check it out!                                                                                    \n",
       "4  Everything here is fantastic! I’ve ordered half the menu and never been disappointed. My favorite is the spaghetti & meatballs (only served on Sundays). The spicy sauce takes it to the next level!       \n",
       "5  THE spot for breakfast in the West Village. I recommend ordering the healthy treat. If you don’t like it, then you have no soul.                                                                           \n",
       "6  Get the vegan peanut butter bar. It’s like sex in your mouth.                                                                                                                                              \n",
       "7  My go-to for coffee and a breakfast sandwich in the mornings. That actually undersells this place - EVERYTHING is good. Lunch, pasta, desserts, wine. I’ve never been disappointed here.                   \n",
       "8  This is the real deal. Stuff like this is why I moved to NYC. I bet half of the guys who play here could have gone pro. Do NOT bring your cousin Jimmy (who never played before) unless you like losing!   \n",
       "9  The High Line is pretty cool. The only thing not to like is that it’s so good that everyone comes here and it gets too crowded. Check it out on a weekday morning or at night to dodge the crowds.         \n",
       "\n",
       "   agreeCount  disagreeCount                        id  \n",
       "0  6           0              5ab2771a7dc9e17930670085  \n",
       "1  3           0              5ab1daf0da5e5617d1da3c7d  \n",
       "2  5           0              5ab1d649464d655c24fc144f  \n",
       "3  1           0              5ab1d0a5c666662673a11799  \n",
       "4  6           0              5ab1cbe467f62b57ee6beaa9  \n",
       "5  5           0              5ab1af48f79faa4bc867de78  \n",
       "6  1           0              5ab1ad2847f8767a8ca88fc1  \n",
       "7  2           0              5ab1acbba6ec980645fd7512  \n",
       "8  1           0              5ab1a316a8eb606122a3b755  \n",
       "9  10          0              5ab19f6849281477a8be2dab  "
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>text</th>\n      <th>agreeCount</th>\n      <th>disagreeCount</th>\n      <th>id</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>High quality falafel that doesn’t come from a cart on the side of the road?! Yes, it exists, and it exists at Taim. Highly recommended - even if you’re new to falafel.</td>\n      <td>6</td>\n      <td>0</td>\n      <td>5ab2771a7dc9e17930670085</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>If you are in the West Village and you choose to go to a nationwide chain coffee shop instead of 11th Street Cafe, then you are everything that is wrong with the world. This place is AWESOME!!!</td>\n      <td>3</td>\n      <td>0</td>\n      <td>5ab1daf0da5e5617d1da3c7d</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>A+! The New Whitney is MUCH more accessible and easier to navigate than the city’s other famous museums like the Met. I’m a big fan. If you’re on a budget: there’s free admission on Friday nights</td>\n      <td>5</td>\n      <td>0</td>\n      <td>5ab1d649464d655c24fc144f</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>I had the wings and they blew my mind. Plus, Leah (the owner) is pretty awesome, so you should definitely check it out!</td>\n      <td>1</td>\n      <td>0</td>\n      <td>5ab1d0a5c666662673a11799</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Everything here is fantastic! I’ve ordered half the menu and never been disappointed. My favorite is the spaghetti &amp; meatballs (only served on Sundays). The spicy sauce takes it to the next level!</td>\n      <td>6</td>\n      <td>0</td>\n      <td>5ab1cbe467f62b57ee6beaa9</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>THE spot for breakfast in the West Village. I recommend ordering the healthy treat. If you don’t like it, then you have no soul.</td>\n      <td>5</td>\n      <td>0</td>\n      <td>5ab1af48f79faa4bc867de78</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Get the vegan peanut butter bar. It’s like sex in your mouth.</td>\n      <td>1</td>\n      <td>0</td>\n      <td>5ab1ad2847f8767a8ca88fc1</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>My go-to for coffee and a breakfast sandwich in the mornings. That actually undersells this place - EVERYTHING is good. Lunch, pasta, desserts, wine. I’ve never been disappointed here.</td>\n      <td>2</td>\n      <td>0</td>\n      <td>5ab1acbba6ec980645fd7512</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>This is the real deal. Stuff like this is why I moved to NYC. I bet half of the guys who play here could have gone pro. Do NOT bring your cousin Jimmy (who never played before) unless you like losing!</td>\n      <td>1</td>\n      <td>0</td>\n      <td>5ab1a316a8eb606122a3b755</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>The High Line is pretty cool. The only thing not to like is that it’s so good that everyone comes here and it gets too crowded. Check it out on a weekday morning or at night to dodge the crowds.</td>\n      <td>10</td>\n      <td>0</td>\n      <td>5ab19f6849281477a8be2dab</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 26
    }
   ],
   "source": [
    "# define tips URL\n",
    "user_id='484542633'\n",
    "url = 'https://api.foursquare.com/v2/users/{}/tips?client_id={}&client_secret={}&oauth_token={}&v={}&limit={}'.format(user_id, CLIENT_ID, CLIENT_SECRET,ACCESS_TOKEN,VERSION, limit)\n",
    "\n",
    "# send GET request and get user's tips\n",
    "results = requests.get(url).json()\n",
    "tips = results['response']['tips']['items']\n",
    "\n",
    "# format column width\n",
    "pd.set_option('display.max_colwidth', -1)\n",
    "\n",
    "tips_df = json_normalize(tips)\n",
    "\n",
    "# filter columns\n",
    "filtered_columns = ['text', 'agreeCount', 'disagreeCount', 'id']\n",
    "tips_filtered = tips_df.loc[:, filtered_columns]\n",
    "\n",
    "# display user's tips\n",
    "tips_filtered"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Let's get the venue for the tip with the greatest number of agree counts\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "The Fifth & Terrace\n{'address': '225 Richmond St W., Suite 501b', 'lat': 43.649249809335, 'lng': -79.38931975675418, 'labeledLatLngs': [{'label': 'display', 'lat': 43.649249809335, 'lng': -79.38931975675418}], 'postalCode': 'M5V 1W2', 'cc': 'CA', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada', 'formattedAddress': ['225 Richmond St W., Suite 501b', 'Toronto ON M5V 1W2', 'Canada']}\n"
     ]
    }
   ],
   "source": [
    "tip_id = '5ab19f6849281477a8be2dab' # tip id\n",
    "\n",
    "# define URL\n",
    "url = 'https://api.foursquare.com/v2/users/{}/tips?client_id={}&client_secret={}&oauth_token={}&v={}'.format(idnumber, CLIENT_ID, CLIENT_SECRET,ACCESS_TOKEN, VERSION) # define URL\n",
    "\n",
    "\n",
    "# send GET Request and examine results\n",
    "result = requests.get(url).json()\n",
    "print(result['response']['tips']['items'][0]['venue']['name'])\n",
    "print(result['response']['tips']['items'][0]['venue']['location'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "## 4. Explore a location\n",
    "\n",
    "> `https://api.foursquare.com/v2/venues/`**explore**`?client_id=`**CLIENT_ID**`&client_secret=`**CLIENT_SECRET**`&ll=`**LATITUDE**`,`**LONGITUDE**`&v=`**VERSION**`&limit=`**LIMIT**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### So, you just finished your gourmet dish at The Atley, and are just curious about the popular spots around the restaurant. In order to explore the area, let's start by getting the latitude and longitude values of The Atley.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": true
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "latitude = 43.64924\n",
    "longitude = -79.38931"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Define URL\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "'https://api.foursquare.com/v2/venues/explore?client_id=0C2BD04A2V1DGSC4FXV5GIU01V2WURJBZ2XM044H3IGYJVRX&client_secret=ILVXI2IA2FRQ5V2RKVBSEFDAG2NAAJNEXYODYFMGIZN1OXYJ&ll=43.64924,-79.38931&v=20180604&radius=500&limit=30'"
      ]
     },
     "metadata": {},
     "execution_count": 29
    }
   ],
   "source": [
    "url = 'https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&ll={},{}&v={}&radius={}&limit={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION, radius, LIMIT)\n",
    "url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Send GET request and examine results\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": true
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "'There are 30 around The Atley restaurant.'"
      ]
     },
     "metadata": {},
     "execution_count": 31
    }
   ],
   "source": [
    "results = requests.get(url).json()\n",
    "'There are {} around The Atley restaurant.'.format(len(results['response']['groups'][0]['items']))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Get relevant part of JSON\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "{'reasons': {'count': 0,\n",
       "  'items': [{'summary': 'This spot is popular',\n",
       "    'type': 'general',\n",
       "    'reasonName': 'globalInteractionReason'}]},\n",
       " 'venue': {'id': '5321f4d9e4b07946702e6e08',\n",
       "  'name': 'Byblos Toronto',\n",
       "  'location': {'address': '11 Duncan Street',\n",
       "   'lat': 43.647615054171766,\n",
       "   'lng': -79.3883810317138,\n",
       "   'labeledLatLngs': [{'label': 'display',\n",
       "     'lat': 43.647615054171766,\n",
       "     'lng': -79.3883810317138}],\n",
       "   'distance': 195,\n",
       "   'postalCode': 'M5V 3M2',\n",
       "   'cc': 'CA',\n",
       "   'city': 'Toronto',\n",
       "   'state': 'ON',\n",
       "   'country': 'Canada',\n",
       "   'formattedAddress': ['11 Duncan Street', 'Toronto ON M5V 3M2', 'Canada']},\n",
       "  'categories': [{'id': '4bf58dd8d48988d1c0941735',\n",
       "    'name': 'Mediterranean Restaurant',\n",
       "    'pluralName': 'Mediterranean Restaurants',\n",
       "    'shortName': 'Mediterranean',\n",
       "    'icon': {'prefix': 'https://ss3.4sqi.net/img/categories_v2/food/mediterranean_',\n",
       "     'suffix': '.png'},\n",
       "    'primary': True}],\n",
       "  'photos': {'count': 0, 'groups': []}},\n",
       " 'referralId': 'e-0-5321f4d9e4b07946702e6e08-0'}"
      ]
     },
     "metadata": {},
     "execution_count": 32
    }
   ],
   "source": [
    "items = results['response']['groups'][0]['items']\n",
    "items[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Process JSON and convert it to a clean dataframe\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stderr",
     "text": [
      "<ipython-input-33-b7321e367fed>:1: FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead\n  dataframe = json_normalize(items) # flatten JSON\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "                    name                  categories  \\\n",
       "0  Byblos Toronto         Mediterranean Restaurant     \n",
       "1  YYoga                  Yoga Studio                  \n",
       "2  Pai                    Thai Restaurant              \n",
       "3  Umbra Concept Store    Furniture / Home Store       \n",
       "4  Omg! Oh My Gyro!       Souvlaki Shop                \n",
       "5  JaBistro               Sushi Restaurant             \n",
       "6  Civello Salon & Spa    Salon / Barbershop           \n",
       "7  Hakata Ikkousha Ramen  Ramen Restaurant             \n",
       "8  The Fifth & Terrace    Modern European Restaurant   \n",
       "9  Daily Press Juicery    Juice Bar                    \n",
       "\n",
       "                          address        lat        lng  \\\n",
       "0  11 Duncan Street                43.647615 -79.388381   \n",
       "1  327-333 Queen St W              43.649725 -79.391983   \n",
       "2  18 Duncan St                    43.647923 -79.388579   \n",
       "3  165 John St.                    43.650417 -79.391136   \n",
       "4  155 John St.                    43.650064 -79.391104   \n",
       "5  222 Richmond St W               43.649687 -79.388090   \n",
       "6  269 Queen St W                  43.650020 -79.389400   \n",
       "7  249 Queen Street West           43.650299 -79.388753   \n",
       "8  225 Richmond St W., Suite 501b  43.649250 -79.389320   \n",
       "9  200 Queen St W                  43.650388 -79.388792   \n",
       "\n",
       "                                                                labeledLatLngs  \\\n",
       "0  [{'label': 'display', 'lat': 43.647615054171766, 'lng': -79.3883810317138}]   \n",
       "1  [{'label': 'display', 'lat': 43.64972499320129, 'lng': -79.39198265471717}]   \n",
       "2  [{'label': 'display', 'lat': 43.64792310735613, 'lng': -79.38857932631602}]   \n",
       "3  [{'label': 'display', 'lat': 43.650417, 'lng': -79.391136}]                   \n",
       "4  [{'label': 'display', 'lat': 43.6500639687058, 'lng': -79.39110371201055}]    \n",
       "5  [{'label': 'display', 'lat': 43.64968685893743, 'lng': -79.38809001547467}]   \n",
       "6  [{'label': 'display', 'lat': 43.6500197743058, 'lng': -79.38940017059696}]    \n",
       "7  [{'label': 'display', 'lat': 43.650299, 'lng': -79.388753}]                   \n",
       "8  [{'label': 'display', 'lat': 43.649249809335, 'lng': -79.38931975675418}]     \n",
       "9  [{'label': 'display', 'lat': 43.65038785952372, 'lng': -79.38879174332155}]   \n",
       "\n",
       "   distance postalCode  cc     city state country  \\\n",
       "0  195       M5V 3M2    CA  Toronto  ON    Canada   \n",
       "1  221       M5V 2A4    CA  Toronto  ON    Canada   \n",
       "2  157       M5H 3G6    CA  Toronto  ON    Canada   \n",
       "3  196       M5T 1X3    CA  Toronto  ON    Canada   \n",
       "4  171       M5T 1X3    CA  Toronto  ON    Canada   \n",
       "5  110       M5V 1W4    CA  Toronto  ON    Canada   \n",
       "6  87        NaN        CA  Toronto  ON    Canada   \n",
       "7  126       M5V 1Z4    CA  Toronto  ON    Canada   \n",
       "8  1         M5V 1W2    CA  Toronto  ON    Canada   \n",
       "9  134       M5V 1Z2    CA  Toronto  ON    Canada   \n",
       "\n",
       "                                                         formattedAddress  \\\n",
       "0  [11 Duncan Street, Toronto ON M5V 3M2, Canada]                           \n",
       "1  [327-333 Queen St W (Beverley St), Toronto ON M5V 2A4, Canada]           \n",
       "2  [18 Duncan St (Adelaide and Duncan), Toronto ON M5H 3G6, Canada]         \n",
       "3  [165 John St. (at Queen St. W), Toronto ON M5T 1X3, Canada]              \n",
       "4  [155 John St. (Queen St. & John St.), Toronto ON M5T 1X3, Canada]        \n",
       "5  [222 Richmond St W, Toronto ON M5V 1W4, Canada]                          \n",
       "6  [269 Queen St W (at Duncan St.), Toronto ON, Canada]                     \n",
       "7  [249 Queen Street West (Queen/University), Toronto ON M5V 1Z4, Canada]   \n",
       "8  [225 Richmond St W., Suite 501b, Toronto ON M5V 1W2, Canada]             \n",
       "9  [200 Queen St W (at St. Patrick St), Toronto ON M5V 1Z2, Canada]         \n",
       "\n",
       "            crossStreet            neighborhood                        id  \n",
       "0  NaN                   NaN                     5321f4d9e4b07946702e6e08  \n",
       "1  Beverley St           NaN                     526ef67311d27290a9ec9c8a  \n",
       "2  Adelaide and Duncan   Entertainment District  529612de11d2ab526191ccc9  \n",
       "3  at Queen St. W        NaN                     4ae734bef964a5205ea921e3  \n",
       "4  Queen St. & John St.  NaN                     595d4380c876c841c08f1959  \n",
       "5  NaN                   NaN                     509bb871e4b09c7ac93f6642  \n",
       "6  at Duncan St.         NaN                     4b44bd18f964a520cafa25e3  \n",
       "7  Queen/University      NaN                     5c9aaa3f66f3cd002c95bd58  \n",
       "8  NaN                   NaN                     4ee117150cd686aafce847f4  \n",
       "9  at St. Patrick St     NaN                     5548cfb6498ec3e4bdfde59a  "
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>name</th>\n      <th>categories</th>\n      <th>address</th>\n      <th>lat</th>\n      <th>lng</th>\n      <th>labeledLatLngs</th>\n      <th>distance</th>\n      <th>postalCode</th>\n      <th>cc</th>\n      <th>city</th>\n      <th>state</th>\n      <th>country</th>\n      <th>formattedAddress</th>\n      <th>crossStreet</th>\n      <th>neighborhood</th>\n      <th>id</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Byblos Toronto</td>\n      <td>Mediterranean Restaurant</td>\n      <td>11 Duncan Street</td>\n      <td>43.647615</td>\n      <td>-79.388381</td>\n      <td>[{'label': 'display', 'lat': 43.647615054171766, 'lng': -79.3883810317138}]</td>\n      <td>195</td>\n      <td>M5V 3M2</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[11 Duncan Street, Toronto ON M5V 3M2, Canada]</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>5321f4d9e4b07946702e6e08</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>YYoga</td>\n      <td>Yoga Studio</td>\n      <td>327-333 Queen St W</td>\n      <td>43.649725</td>\n      <td>-79.391983</td>\n      <td>[{'label': 'display', 'lat': 43.64972499320129, 'lng': -79.39198265471717}]</td>\n      <td>221</td>\n      <td>M5V 2A4</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[327-333 Queen St W (Beverley St), Toronto ON M5V 2A4, Canada]</td>\n      <td>Beverley St</td>\n      <td>NaN</td>\n      <td>526ef67311d27290a9ec9c8a</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Pai</td>\n      <td>Thai Restaurant</td>\n      <td>18 Duncan St</td>\n      <td>43.647923</td>\n      <td>-79.388579</td>\n      <td>[{'label': 'display', 'lat': 43.64792310735613, 'lng': -79.38857932631602}]</td>\n      <td>157</td>\n      <td>M5H 3G6</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[18 Duncan St (Adelaide and Duncan), Toronto ON M5H 3G6, Canada]</td>\n      <td>Adelaide and Duncan</td>\n      <td>Entertainment District</td>\n      <td>529612de11d2ab526191ccc9</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Umbra Concept Store</td>\n      <td>Furniture / Home Store</td>\n      <td>165 John St.</td>\n      <td>43.650417</td>\n      <td>-79.391136</td>\n      <td>[{'label': 'display', 'lat': 43.650417, 'lng': -79.391136}]</td>\n      <td>196</td>\n      <td>M5T 1X3</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[165 John St. (at Queen St. W), Toronto ON M5T 1X3, Canada]</td>\n      <td>at Queen St. W</td>\n      <td>NaN</td>\n      <td>4ae734bef964a5205ea921e3</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Omg! Oh My Gyro!</td>\n      <td>Souvlaki Shop</td>\n      <td>155 John St.</td>\n      <td>43.650064</td>\n      <td>-79.391104</td>\n      <td>[{'label': 'display', 'lat': 43.6500639687058, 'lng': -79.39110371201055}]</td>\n      <td>171</td>\n      <td>M5T 1X3</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[155 John St. (Queen St. &amp; John St.), Toronto ON M5T 1X3, Canada]</td>\n      <td>Queen St. &amp; John St.</td>\n      <td>NaN</td>\n      <td>595d4380c876c841c08f1959</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>JaBistro</td>\n      <td>Sushi Restaurant</td>\n      <td>222 Richmond St W</td>\n      <td>43.649687</td>\n      <td>-79.388090</td>\n      <td>[{'label': 'display', 'lat': 43.64968685893743, 'lng': -79.38809001547467}]</td>\n      <td>110</td>\n      <td>M5V 1W4</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[222 Richmond St W, Toronto ON M5V 1W4, Canada]</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>509bb871e4b09c7ac93f6642</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Civello Salon &amp; Spa</td>\n      <td>Salon / Barbershop</td>\n      <td>269 Queen St W</td>\n      <td>43.650020</td>\n      <td>-79.389400</td>\n      <td>[{'label': 'display', 'lat': 43.6500197743058, 'lng': -79.38940017059696}]</td>\n      <td>87</td>\n      <td>NaN</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[269 Queen St W (at Duncan St.), Toronto ON, Canada]</td>\n      <td>at Duncan St.</td>\n      <td>NaN</td>\n      <td>4b44bd18f964a520cafa25e3</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>Hakata Ikkousha Ramen</td>\n      <td>Ramen Restaurant</td>\n      <td>249 Queen Street West</td>\n      <td>43.650299</td>\n      <td>-79.388753</td>\n      <td>[{'label': 'display', 'lat': 43.650299, 'lng': -79.388753}]</td>\n      <td>126</td>\n      <td>M5V 1Z4</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[249 Queen Street West (Queen/University), Toronto ON M5V 1Z4, Canada]</td>\n      <td>Queen/University</td>\n      <td>NaN</td>\n      <td>5c9aaa3f66f3cd002c95bd58</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>The Fifth &amp; Terrace</td>\n      <td>Modern European Restaurant</td>\n      <td>225 Richmond St W., Suite 501b</td>\n      <td>43.649250</td>\n      <td>-79.389320</td>\n      <td>[{'label': 'display', 'lat': 43.649249809335, 'lng': -79.38931975675418}]</td>\n      <td>1</td>\n      <td>M5V 1W2</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[225 Richmond St W., Suite 501b, Toronto ON M5V 1W2, Canada]</td>\n      <td>NaN</td>\n      <td>NaN</td>\n      <td>4ee117150cd686aafce847f4</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Daily Press Juicery</td>\n      <td>Juice Bar</td>\n      <td>200 Queen St W</td>\n      <td>43.650388</td>\n      <td>-79.388792</td>\n      <td>[{'label': 'display', 'lat': 43.65038785952372, 'lng': -79.38879174332155}]</td>\n      <td>134</td>\n      <td>M5V 1Z2</td>\n      <td>CA</td>\n      <td>Toronto</td>\n      <td>ON</td>\n      <td>Canada</td>\n      <td>[200 Queen St W (at St. Patrick St), Toronto ON M5V 1Z2, Canada]</td>\n      <td>at St. Patrick St</td>\n      <td>NaN</td>\n      <td>5548cfb6498ec3e4bdfde59a</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 33
    }
   ],
   "source": [
    "dataframe = json_normalize(items) # flatten JSON\n",
    "\n",
    "# filter columns\n",
    "filtered_columns = ['venue.name', 'venue.categories'] + [col for col in dataframe.columns if col.startswith('venue.location.')] + ['venue.id']\n",
    "dataframe_filtered = dataframe.loc[:, filtered_columns]\n",
    "\n",
    "# filter the category for each row\n",
    "dataframe_filtered['venue.categories'] = dataframe_filtered.apply(get_category_type, axis=1)\n",
    "\n",
    "# clean columns\n",
    "dataframe_filtered.columns = [col.split('.')[-1] for col in dataframe_filtered.columns]\n",
    "\n",
    "dataframe_filtered.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Let's visualize these items on the map around our location\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    },
    "scrolled": true
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "<folium.folium.Map at 0x273fc685940>"
      ],
      "text/html": "<div style=\"width:100%;\"><div style=\"position:relative;width:100%;height:0;padding-bottom:60%;\"><span style=\"color:#565656\">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe src=\"about:blank\" style=\"position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;\" data-html=%3C%21DOCTYPE%20html%3E%0A%3Chead%3E%20%20%20%20%0A%20%20%20%20%3Cmeta%20http-equiv%3D%22content-type%22%20content%3D%22text/html%3B%20charset%3DUTF-8%22%20/%3E%0A%20%20%20%20%3Cscript%3EL_PREFER_CANVAS%20%3D%20false%3B%20L_NO_TOUCH%20%3D%20false%3B%20L_DISABLE_3D%20%3D%20false%3B%3C/script%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//cdn.jsdelivr.net/npm/leaflet%401.2.0/dist/leaflet.js%22%3E%3C/script%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js%22%3E%3C/script%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js%22%3E%3C/script%3E%0A%20%20%20%20%3Cscript%20src%3D%22https%3A//cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js%22%3E%3C/script%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//cdn.jsdelivr.net/npm/leaflet%401.2.0/dist/leaflet.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css%22/%3E%0A%20%20%20%20%3Clink%20rel%3D%22stylesheet%22%20href%3D%22https%3A//rawgit.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css%22/%3E%0A%20%20%20%20%3Cstyle%3Ehtml%2C%20body%20%7Bwidth%3A%20100%25%3Bheight%3A%20100%25%3Bmargin%3A%200%3Bpadding%3A%200%3B%7D%3C/style%3E%0A%20%20%20%20%3Cstyle%3E%23map%20%7Bposition%3Aabsolute%3Btop%3A0%3Bbottom%3A0%3Bright%3A0%3Bleft%3A0%3B%7D%3C/style%3E%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cstyle%3E%20%23map_07c22b5046d844a8989c4a1f20650829%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20position%20%3A%20relative%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20width%20%3A%20100.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20height%3A%20100.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20left%3A%200.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20top%3A%200.0%25%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%3C/style%3E%0A%20%20%20%20%20%20%20%20%0A%3C/head%3E%0A%3Cbody%3E%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cdiv%20class%3D%22folium-map%22%20id%3D%22map_07c22b5046d844a8989c4a1f20650829%22%20%3E%3C/div%3E%0A%20%20%20%20%20%20%20%20%0A%3C/body%3E%0A%3Cscript%3E%20%20%20%20%0A%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20bounds%20%3D%20null%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20map_07c22b5046d844a8989c4a1f20650829%20%3D%20L.map%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%27map_07c22b5046d844a8989c4a1f20650829%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7Bcenter%3A%20%5B43.64924%2C-79.38931%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20zoom%3A%2015%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20maxBounds%3A%20bounds%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20layers%3A%20%5B%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20worldCopyJump%3A%20false%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20crs%3A%20L.CRS.EPSG3857%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20tile_layer_63a7bfe7d9ea4c20becbca4a2952fb7d%20%3D%20L.tileLayer%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%27https%3A//%7Bs%7D.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22attribution%22%3A%20null%2C%0A%20%20%22detectRetina%22%3A%20false%2C%0A%20%20%22maxZoom%22%3A%2018%2C%0A%20%20%22minZoom%22%3A%201%2C%0A%20%20%22noWrap%22%3A%20false%2C%0A%20%20%22subdomains%22%3A%20%22abc%22%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_b52b9660348c4b89a777197cf2185a19%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64924%2C-79.38931%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22red%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22red%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%2010%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_801f9b969b004df5b9279598c6832159%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_8ac82f44e17a4455ae8d4133794633ea%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_8ac82f44e17a4455ae8d4133794633ea%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EEcco%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_801f9b969b004df5b9279598c6832159.setContent%28html_8ac82f44e17a4455ae8d4133794633ea%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_b52b9660348c4b89a777197cf2185a19.bindPopup%28popup_801f9b969b004df5b9279598c6832159%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_6458a35dd7e2473795b534a4f26272cb%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.647615054171766%2C-79.3883810317138%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_8442537b95864dc682edf1a6ac711a9e%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_d7d619cc9aec475f9baa4d693cb60ec3%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_d7d619cc9aec475f9baa4d693cb60ec3%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EMediterranean%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_8442537b95864dc682edf1a6ac711a9e.setContent%28html_d7d619cc9aec475f9baa4d693cb60ec3%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_6458a35dd7e2473795b534a4f26272cb.bindPopup%28popup_8442537b95864dc682edf1a6ac711a9e%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_89deac66a55a4c35bfed385342a9414c%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64972499320129%2C-79.39198265471717%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_059d02fcf72d46b19cadd537f160d889%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_a7d83b0201ce47018a466d83cccee469%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_a7d83b0201ce47018a466d83cccee469%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EYoga%20Studio%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_059d02fcf72d46b19cadd537f160d889.setContent%28html_a7d83b0201ce47018a466d83cccee469%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_89deac66a55a4c35bfed385342a9414c.bindPopup%28popup_059d02fcf72d46b19cadd537f160d889%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_b18892362797434cb2a94e8b92a97626%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64792310735613%2C-79.38857932631602%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_b405d331d9284444b30178f071d4e665%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_2e335a7adbeb4678b8ff44d45cba25f0%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_2e335a7adbeb4678b8ff44d45cba25f0%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EThai%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_b405d331d9284444b30178f071d4e665.setContent%28html_2e335a7adbeb4678b8ff44d45cba25f0%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_b18892362797434cb2a94e8b92a97626.bindPopup%28popup_b405d331d9284444b30178f071d4e665%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_e54f982e80464739a1d8f383d19ea640%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650417%2C-79.391136%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_e005af38811e453fb27530f08c743f81%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_180bd90886384033abdb506ca2565f94%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_180bd90886384033abdb506ca2565f94%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EFurniture%20/%20Home%20Store%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_e005af38811e453fb27530f08c743f81.setContent%28html_180bd90886384033abdb506ca2565f94%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_e54f982e80464739a1d8f383d19ea640.bindPopup%28popup_e005af38811e453fb27530f08c743f81%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_ee2eee2126ff406991fde3c49c391781%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.6500639687058%2C-79.39110371201055%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_c85e1a0a0e71423a850ce102897006b0%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_4f6a7005ade542079064c3642d1661b6%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_4f6a7005ade542079064c3642d1661b6%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ESouvlaki%20Shop%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_c85e1a0a0e71423a850ce102897006b0.setContent%28html_4f6a7005ade542079064c3642d1661b6%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_ee2eee2126ff406991fde3c49c391781.bindPopup%28popup_c85e1a0a0e71423a850ce102897006b0%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_1c42cf63214e40f3bd17f0838607b408%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64968685893743%2C-79.38809001547467%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_059c2a8fdeaf49a7acbb81011145275d%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_cc86029375b2468bac833ff6c37acd5f%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_cc86029375b2468bac833ff6c37acd5f%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ESushi%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_059c2a8fdeaf49a7acbb81011145275d.setContent%28html_cc86029375b2468bac833ff6c37acd5f%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_1c42cf63214e40f3bd17f0838607b408.bindPopup%28popup_059c2a8fdeaf49a7acbb81011145275d%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_f30391ee714641c5ab20081694ef0591%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.6500197743058%2C-79.38940017059696%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_b24fdeed7e4b44de9aee0919332df341%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_d02cd5933af5415bbf6a876994ff71a8%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_d02cd5933af5415bbf6a876994ff71a8%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ESalon%20/%20Barbershop%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_b24fdeed7e4b44de9aee0919332df341.setContent%28html_d02cd5933af5415bbf6a876994ff71a8%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_f30391ee714641c5ab20081694ef0591.bindPopup%28popup_b24fdeed7e4b44de9aee0919332df341%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_3d649048ca5d4b8a963a90fd2c846979%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650299%2C-79.388753%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_28499c45963a43d6a84c9a1e72dd2c12%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_585d075b8db6485f9a74ec90056d75a3%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_585d075b8db6485f9a74ec90056d75a3%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ERamen%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_28499c45963a43d6a84c9a1e72dd2c12.setContent%28html_585d075b8db6485f9a74ec90056d75a3%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_3d649048ca5d4b8a963a90fd2c846979.bindPopup%28popup_28499c45963a43d6a84c9a1e72dd2c12%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_402f45398761453fbc783374c32f2295%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.649249809335%2C-79.38931975675418%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_e6713db23b1c4ab8bb47d6240e43c27a%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_20fc99745d284e26beba42497df24896%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_20fc99745d284e26beba42497df24896%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EModern%20European%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_e6713db23b1c4ab8bb47d6240e43c27a.setContent%28html_20fc99745d284e26beba42497df24896%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_402f45398761453fbc783374c32f2295.bindPopup%28popup_e6713db23b1c4ab8bb47d6240e43c27a%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_ed6dece2f5484546a26ba9d5651b23bd%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.65038785952372%2C-79.38879174332155%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_b5a541c3a8b049c38cc1ffe94da16871%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_3859ec720b8e452ab5088dc218b77c77%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_3859ec720b8e452ab5088dc218b77c77%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EJuice%20Bar%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_b5a541c3a8b049c38cc1ffe94da16871.setContent%28html_3859ec720b8e452ab5088dc218b77c77%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_ed6dece2f5484546a26ba9d5651b23bd.bindPopup%28popup_b5a541c3a8b049c38cc1ffe94da16871%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_0618322f8be04b55b68750e0957102a8%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64912919417502%2C-79.3865566853963%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_430f29dc3ea34b378bffea9b0db990f5%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_c6ddca0c8e724937a3669062c1c11357%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_c6ddca0c8e724937a3669062c1c11357%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EHotel%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_430f29dc3ea34b378bffea9b0db990f5.setContent%28html_c6ddca0c8e724937a3669062c1c11357%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_0618322f8be04b55b68750e0957102a8.bindPopup%28popup_430f29dc3ea34b378bffea9b0db990f5%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_2a2337ea727d47a99103de0a19bb943c%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.65030427070834%2C-79.38892664709715%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_a3f06ac0542a4bb59649a1a54c155b8d%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_e8efeb8407864c92975549e79d9e185c%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_e8efeb8407864c92975549e79d9e185c%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EClothing%20Store%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_a3f06ac0542a4bb59649a1a54c155b8d.setContent%28html_e8efeb8407864c92975549e79d9e185c%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_2a2337ea727d47a99103de0a19bb943c.bindPopup%28popup_a3f06ac0542a4bb59649a1a54c155b8d%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_2201793c27c943e8aac068224a8d7ed8%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.65051219841103%2C-79.38812570541256%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_75cbb8d47ae243a4b685e0b4c497c453%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_9263f317401b48cbbf01a12601c265c1%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_9263f317401b48cbbf01a12601c265c1%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ERecord%20Shop%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_75cbb8d47ae243a4b685e0b4c497c453.setContent%28html_9263f317401b48cbbf01a12601c265c1%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_2201793c27c943e8aac068224a8d7ed8.bindPopup%28popup_75cbb8d47ae243a4b685e0b4c497c453%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_159639e8f08040e595e1e2a30c279c82%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.6499881760459%2C-79.39079046249388%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_26091917d6cf45ba94c6c3ff92562ece%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_f21c69fefe074fff9b36d0d3f9a56174%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_f21c69fefe074fff9b36d0d3f9a56174%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EShoe%20Store%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_26091917d6cf45ba94c6c3ff92562ece.setContent%28html_f21c69fefe074fff9b36d0d3f9a56174%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_159639e8f08040e595e1e2a30c279c82.bindPopup%28popup_26091917d6cf45ba94c6c3ff92562ece%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_f9003942f4684c69b421e630b33198d2%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.65036434800487%2C-79.38866907575726%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_53cb37774e6148b6b964608338a9c737%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_49e4b922115643319492f41ea67d81d9%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_49e4b922115643319492f41ea67d81d9%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ECoffee%20Shop%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_53cb37774e6148b6b964608338a9c737.setContent%28html_49e4b922115643319492f41ea67d81d9%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_f9003942f4684c69b421e630b33198d2.bindPopup%28popup_53cb37774e6148b6b964608338a9c737%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_bd087040d6014c73a71ae5f47727270d%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.647595917807365%2C-79.38641938975012%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_468ebbe475d14284b35b107bb8945885%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_3e98049c9ce74357a2a625c0052922c4%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_3e98049c9ce74357a2a625c0052922c4%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ECaf%C3%A9%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_468ebbe475d14284b35b107bb8945885.setContent%28html_3e98049c9ce74357a2a625c0052922c4%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_bd087040d6014c73a71ae5f47727270d.bindPopup%28popup_468ebbe475d14284b35b107bb8945885%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_5b1ba7e38cd94ca5abcba19d7a4d9a63%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650139555584936%2C-79.3903774023056%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_3eb6944d8a7e4491922ac5b2b0a0b57f%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_1598e2eaa22246f3a66f878b5c858ebd%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_1598e2eaa22246f3a66f878b5c858ebd%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EChocolate%20Shop%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_3eb6944d8a7e4491922ac5b2b0a0b57f.setContent%28html_1598e2eaa22246f3a66f878b5c858ebd%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_5b1ba7e38cd94ca5abcba19d7a4d9a63.bindPopup%28popup_3eb6944d8a7e4491922ac5b2b0a0b57f%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_b79b73b26612471489aff9231f43e236%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64634159071232%2C-79.39006297129853%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_c9239907b18149a58859bb23bffa6d70%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_2d43e1c0044544a7bbc74ab8644d67ed%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_2d43e1c0044544a7bbc74ab8644d67ed%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EMovie%20Theater%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_c9239907b18149a58859bb23bffa6d70.setContent%28html_2d43e1c0044544a7bbc74ab8644d67ed%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_b79b73b26612471489aff9231f43e236.bindPopup%28popup_c9239907b18149a58859bb23bffa6d70%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_cb1e529efee049b2a20be677c6068c57%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64829161679981%2C-79.39039040155937%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_5c2ea151e1e34c1db331ef0314b40bd6%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_5d2e8e5049dd41c6b20ffb523aea06af%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_5d2e8e5049dd41c6b20ffb523aea06af%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ECoffee%20Shop%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_5c2ea151e1e34c1db331ef0314b40bd6.setContent%28html_5d2e8e5049dd41c6b20ffb523aea06af%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_cb1e529efee049b2a20be677c6068c57.bindPopup%28popup_5c2ea151e1e34c1db331ef0314b40bd6%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_5fc76d548bf842fa84c9e8897e6e2962%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64915499986854%2C-79.38654574367817%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_bfb53ea754994a22afe157307382fe10%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_3207648db25b49a2aa959e2094f81167%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_3207648db25b49a2aa959e2094f81167%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ELounge%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_bfb53ea754994a22afe157307382fe10.setContent%28html_3207648db25b49a2aa959e2094f81167%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_5fc76d548bf842fa84c9e8897e6e2962.bindPopup%28popup_bfb53ea754994a22afe157307382fe10%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_449441d2ed5b4250bdd06cdf25b2e8f5%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64873430659662%2C-79.38654117564838%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_f516fc6b2bbb4bdeb29f9ffb66bd06ad%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_c17c8d77ff5949b1b1d82658d816ac19%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_c17c8d77ff5949b1b1d82658d816ac19%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ESpeakeasy%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_f516fc6b2bbb4bdeb29f9ffb66bd06ad.setContent%28html_c17c8d77ff5949b1b1d82658d816ac19%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_449441d2ed5b4250bdd06cdf25b2e8f5.bindPopup%28popup_f516fc6b2bbb4bdeb29f9ffb66bd06ad%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_f85489bca55040aa9d026e5a8a4fed0a%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.647326115934106%2C-79.39304291907733%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_8a2d9151ed7245679eb3011f1238ab7a%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_0016f693980045bbaca6b5d42cf92f21%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_0016f693980045bbaca6b5d42cf92f21%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EPizza%20Place%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_8a2d9151ed7245679eb3011f1238ab7a.setContent%28html_0016f693980045bbaca6b5d42cf92f21%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_f85489bca55040aa9d026e5a8a4fed0a.bindPopup%28popup_8a2d9151ed7245679eb3011f1238ab7a%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_285dcb50f1cc43f7aef2368d122ffcf4%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64833259480477%2C-79.3881514766071%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_981790f69b734bfb82ee696c6ee4c58b%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_1d8bb49e111a47069064ca2a682607fd%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_1d8bb49e111a47069064ca2a682607fd%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EBrazilian%20Restaurant%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_981790f69b734bfb82ee696c6ee4c58b.setContent%28html_1d8bb49e111a47069064ca2a682607fd%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_285dcb50f1cc43f7aef2368d122ffcf4.bindPopup%28popup_981790f69b734bfb82ee696c6ee4c58b%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_18c18cd78e9e4c82938e623367dbc407%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.650592%2C-79.385806%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_b96cb2773fd649fa94908059c7030cb8%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_8c7f12fb7ab9473bb1f05a99d3cf86f7%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_8c7f12fb7ab9473bb1f05a99d3cf86f7%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EConcert%20Hall%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_b96cb2773fd649fa94908059c7030cb8.setContent%28html_8c7f12fb7ab9473bb1f05a99d3cf86f7%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_18c18cd78e9e4c82938e623367dbc407.bindPopup%28popup_b96cb2773fd649fa94908059c7030cb8%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_57e0c830109b4c63a4248bac0711b936%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.648146672800344%2C-79.38921873094012%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_6e7079377f6f44819e174dba9e9c48da%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_b244154e174c43569adc0520d9efae38%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_b244154e174c43569adc0520d9efae38%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EBurrito%20Place%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_6e7079377f6f44819e174dba9e9c48da.setContent%28html_b244154e174c43569adc0520d9efae38%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_57e0c830109b4c63a4248bac0711b936.bindPopup%28popup_6e7079377f6f44819e174dba9e9c48da%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_7f1e0dbe1c5a431d9c99843d3a88752e%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64654315405365%2C-79.38910030187289%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_c30df3e6de99416082e9cbcd6f334407%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_058dec86c88e4f6397708881b7be7f7b%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_058dec86c88e4f6397708881b7be7f7b%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ETheater%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_c30df3e6de99416082e9cbcd6f334407.setContent%28html_058dec86c88e4f6397708881b7be7f7b%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_7f1e0dbe1c5a431d9c99843d3a88752e.bindPopup%28popup_c30df3e6de99416082e9cbcd6f334407%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_52596bb22e5f4990a0e1be89269b82ac%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64701650155176%2C-79.38814275495332%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_becc1fed6ddf43a9a1e88095c3050c5d%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_1a862d211c5c419aa5fc37b5bf228efe%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_1a862d211c5c419aa5fc37b5bf228efe%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EGym%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_becc1fed6ddf43a9a1e88095c3050c5d.setContent%28html_1a862d211c5c419aa5fc37b5bf228efe%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_52596bb22e5f4990a0e1be89269b82ac.bindPopup%28popup_becc1fed6ddf43a9a1e88095c3050c5d%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_2389e501680f4e9e9fed2d36a85f0d08%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.646317516225395%2C-79.39094024700876%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_db0e78712f354c608e01f7a562f98de0%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_02a761dac0364a0f822a759f500285a4%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_02a761dac0364a0f822a759f500285a4%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3EGym%20/%20Fitness%20Center%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_db0e78712f354c608e01f7a562f98de0.setContent%28html_02a761dac0364a0f822a759f500285a4%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_2389e501680f4e9e9fed2d36a85f0d08.bindPopup%28popup_db0e78712f354c608e01f7a562f98de0%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_f951b59f66784212a8552756b6c4e88d%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.648059%2C-79.389791%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_d0bd8410b9af445f91e3f0abdfb7bfd8%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_33ca69590d1647c8803812a49abff043%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_33ca69590d1647c8803812a49abff043%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ECaf%C3%A9%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_d0bd8410b9af445f91e3f0abdfb7bfd8.setContent%28html_33ca69590d1647c8803812a49abff043%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_f951b59f66784212a8552756b6c4e88d.bindPopup%28popup_d0bd8410b9af445f91e3f0abdfb7bfd8%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20circle_marker_eb91d46eca85487abc01dcab24f51aaf%20%3D%20L.circleMarker%28%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%5B43.64736939566164%2C-79.39183955161323%5D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%22bubblingMouseEvents%22%3A%20true%2C%0A%20%20%22color%22%3A%20%22blue%22%2C%0A%20%20%22dashArray%22%3A%20null%2C%0A%20%20%22dashOffset%22%3A%20null%2C%0A%20%20%22fill%22%3A%20true%2C%0A%20%20%22fillColor%22%3A%20%22blue%22%2C%0A%20%20%22fillOpacity%22%3A%200.6%2C%0A%20%20%22fillRule%22%3A%20%22evenodd%22%2C%0A%20%20%22lineCap%22%3A%20%22round%22%2C%0A%20%20%22lineJoin%22%3A%20%22round%22%2C%0A%20%20%22opacity%22%3A%201.0%2C%0A%20%20%22radius%22%3A%205%2C%0A%20%20%22stroke%22%3A%20true%2C%0A%20%20%22weight%22%3A%203%0A%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%29.addTo%28map_07c22b5046d844a8989c4a1f20650829%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20var%20popup_ab98f1bcd59f4929af308a85811edde1%20%3D%20L.popup%28%7BmaxWidth%3A%20%27300%27%7D%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20var%20html_9833df840a534915b68bdded69ff0df6%20%3D%20%24%28%27%3Cdiv%20id%3D%22html_9833df840a534915b68bdded69ff0df6%22%20style%3D%22width%3A%20100.0%25%3B%20height%3A%20100.0%25%3B%22%3ESoup%20Place%3C/div%3E%27%29%5B0%5D%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20popup_ab98f1bcd59f4929af308a85811edde1.setContent%28html_9833df840a534915b68bdded69ff0df6%29%3B%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20circle_marker_eb91d46eca85487abc01dcab24f51aaf.bindPopup%28popup_ab98f1bcd59f4929af308a85811edde1%29%3B%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%0A%3C/script%3E onload=\"this.contentDocument.open();this.contentDocument.write(    decodeURIComponent(this.getAttribute('data-html')));this.contentDocument.close();\" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>"
     },
     "metadata": {},
     "execution_count": 34
    }
   ],
   "source": [
    "venues_map = folium.Map(location=[latitude, longitude], zoom_start=15) # generate map centred around The Atley.\n",
    "\n",
    "\n",
    "# add Ecco as a red circle mark\n",
    "folium.CircleMarker(\n",
    "    [latitude, longitude],\n",
    "    radius=10,\n",
    "    popup='Ecco',\n",
    "    fill=True,\n",
    "    color='red',\n",
    "    fill_color='red',\n",
    "    fill_opacity=0.6\n",
    "    ).add_to(venues_map)\n",
    "\n",
    "\n",
    "# add popular spots to the map as blue circle markers\n",
    "for lat, lng, label in zip(dataframe_filtered.lat, dataframe_filtered.lng, dataframe_filtered.categories):\n",
    "    folium.CircleMarker(\n",
    "        [lat, lng],\n",
    "        radius=5,\n",
    "        popup=label,\n",
    "        fill=True,\n",
    "        color='blue',\n",
    "        fill_color='blue',\n",
    "        fill_opacity=0.6\n",
    "        ).add_to(venues_map)\n",
    "\n",
    "# display map\n",
    "venues_map"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "<a id=\"item5\"></a>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "## 5. Explore Trending Venues\n",
    "\n",
    "> `https://api.foursquare.com/v2/venues/`**trending**`?client_id=`**CLIENT_ID**`&client_secret=`**CLIENT_SECRET**`&ll=`**LATITUDE**`,`**LONGITUDE**`&v=`**VERSION**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "#### Now, instead of simply exploring the area around The Atley, you are interested in knowing the venues that are trending at the time you are done with your lunch, meaning the places with the highest foot traffic. So let's do that and get the trending venues around The Atley.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "{'meta': {'code': 200, 'requestId': '60d7d07d11af0c62679e1c76'},\n",
       " 'response': {'venues': []}}"
      ]
     },
     "metadata": {},
     "execution_count": 35
    }
   ],
   "source": [
    "# define URL\n",
    "url = 'https://api.foursquare.com/v2/venues/trending?client_id={}&client_secret={}&ll={},{}&v={}'.format(CLIENT_ID, CLIENT_SECRET, latitude, longitude, VERSION)\n",
    "\n",
    "# send GET request and get trending venues\n",
    "results = requests.get(url).json()\n",
    "results"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### Check if any venues are trending at this time\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": true
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "if len(results['response']['venues']) == 0:\n",
    "    trending_venues_df = 'No trending venues are available at the moment!'\n",
    "    \n",
    "else:\n",
    "    trending_venues = results['response']['venues']\n",
    "    trending_venues_df = json_normalize(trending_venues)\n",
    "\n",
    "    # filter columns\n",
    "    columns_filtered = ['name', 'categories'] + ['location.distance', 'location.city', 'location.postalCode', 'location.state', 'location.country', 'location.lat', 'location.lng']\n",
    "    trending_venues_df = trending_venues_df.loc[:, columns_filtered]\n",
    "\n",
    "    # filter the category for each row\n",
    "    trending_venues_df['categories'] = trending_venues_df.apply(get_category_type, axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "'No trending venues are available at the moment!'"
      ]
     },
     "metadata": {},
     "execution_count": 37
    }
   ],
   "source": [
    "# display trending venues\n",
    "trending_venues_df"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "Now, depending on when you run the above code, you might get different venues since the venues with the highest foot traffic are fetched live. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "### Visualize trending venues\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "outputs": [],
   "source": [
    "if len(results['response']['venues']) == 0:\n",
    "    venues_map = 'Cannot generate visual as no trending venues are available at the moment!'\n",
    "\n",
    "else:\n",
    "    venues_map = folium.Map(location=[latitude, longitude], zoom_start=15) # generate map centred around Ecco\n",
    "\n",
    "\n",
    "    # add Ecco as a red circle mark\n",
    "    folium.CircleMarker(\n",
    "        [latitude, longitude],\n",
    "        radius=10,\n",
    "        popup='Ecco',\n",
    "        fill=True,\n",
    "        color='red',\n",
    "        fill_color='red',\n",
    "        fill_opacity=0.6\n",
    "    ).add_to(venues_map)\n",
    "\n",
    "\n",
    "    # add the trending venues as blue circle markers\n",
    "    for lat, lng, label in zip(trending_venues_df['location.lat'], trending_venues_df['location.lng'], trending_venues_df['name']):\n",
    "        folium.CircleMarker(\n",
    "            [lat, lng],\n",
    "            radius=5,\n",
    "            poup=label,\n",
    "            fill=True,\n",
    "            color='blue',\n",
    "            fill_color='blue',\n",
    "            fill_opacity=0.6\n",
    "        ).add_to(venues_map)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "button": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "new_sheet": false,
    "run_control": {
     "read_only": false
    },
    "scrolled": true
   },
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "'Cannot generate visual as no trending venues are available at the moment!'"
      ]
     },
     "metadata": {},
     "execution_count": 39
    }
   ],
   "source": [
    "# display map\n",
    "venues_map"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "<a id=\"item6\"></a>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "button": false,
    "new_sheet": false,
    "run_control": {
     "read_only": false
    }
   },
   "source": [
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.8.8 64-bit ('base': conda)"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "metadata": {
   "interpreter": {
    "hash": "63fd5069d213b44bf678585dea6b12cceca9941eaf7f819626cde1f2670de90d"
   }
  },
  "widgets": {
   "state": {},
   "version": "1.1.2"
  },
  "interpreter": {
   "hash": "0d6ee3a53993161da897d5274caa6061e78baeaa656a70c10e4c2269304362b6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}