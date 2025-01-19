{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "58cf410f-8935-4bc7-9100-75012727a998",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Current google-chrome version is 100.0.4896\n",
      "[WDM] - Get LATEST driver version for 100.0.4896\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Driver [C:\\Users\\danya\\.wdm\\drivers\\chromedriver\\win32\\100.0.4896.60\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.chrome.options import Options\n",
    "chrome_options = Options()\n",
    "chrome_options.add_argument(\"--headless\")\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c0aa03af-c87a-44d7-9333-e414dee35161",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "response = requests.get('https://techxplore.com/')\n",
    "html = response.text\n",
    "soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3bd43f52-e34b-4135-934b-aa08edee3921",
   "metadata": {
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "source": [
    "soup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ebaf49f7-e540-4c91-84f8-7faeaf03c24a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bs4.element.ResultSet"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(soup.find_all(['h4',['a']]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dc445c5d-b99a-4301-836d-d1744815dca7",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soup.find_all(['h4',['a']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "53bc7001-6d6f-4a78-8efe-049d8c86c768",
   "metadata": {},
   "outputs": [],
   "source": [
    "soup.h4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "04fc07bd-da14-42cd-9737-90ee8251f8fe",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "list1, l2 = [], []\n",
    "for h4 in soup.select(\"h4\")[:5]:\n",
    "    # if h4.a[\"href\"] is None:\n",
    "    #     print('ass')\n",
    "    #     break\n",
    "    # print(h4.a[\"href\"])\n",
    "    # print(h4.get_text(strip=True))\n",
    "    print(h4)\n",
    "    list1.append(h4.a[\"href\"])\n",
    "    l2.append(h4.get_text(strip=True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e67f9c6f-a986-41b9-9889-3a4e383ade4e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7dac12b9-4faf-4860-bd32-77deb3b140a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c9e23fef-dd5a-4af7-81c4-4c62c8939cd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "time_list = []\n",
    "table = soup.find_all('div',attrs={\"class\":\"article__info-item mr-auto\"})\n",
    "for x in table[2:6]:\n",
    "    time_list.append(x.find('p').text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "e03203d0-a68b-4f97-8372-77b8df8c464f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "time_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "951119cf-0853-4fcf-85a5-dfaddcd5cf85",
   "metadata": {},
   "outputs": [],
   "source": [
    "title_container = soup.find_all([\"h3\"], \n",
    "                               class_='text-large mt-2 mb-1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f7a71539-58f2-4ac5-9c84-4fd9bf5320e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "title_container"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6aecb9c2-0677-46c9-844a-38fdd3b6764c",
   "metadata": {},
   "outputs": [],
   "source": [
    "links_with_text = []\n",
    "for a in soup.find_all('a', href=True): \n",
    "    if a.text: \n",
    "        links_with_text.append(a['href'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "b181e869-fa71-4438-ba2e-db3ced28590b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "links_with_text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b3ded49e-03a4-4563-950f-929e9de4ad1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "link_container = [s for s in links_with_text if s.__contains__(\"https://techxplore.com/news/\")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "1d54bc0d-eaae-4ad5-8a51-c6cd158ba248",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "title_container"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "9637152f-35c7-48f8-8965-4985a6bf41ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "link_container"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bf532342-2687-4937-8126-bfd7e0545475",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "data = '' \n",
    "for data in soup.find_all(\"a\"): \n",
    "    print(data.get_text()) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "79bcea28-0c31-45c0-b71c-d740a1507dd6",
   "metadata": {},
   "outputs": [],
   "source": [
    "title_container = soup.find_all([\"h4\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "467e04bf-8cb2-46ea-9f7a-9dce2dcd73b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "bs4.element.ResultSet"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(title_container)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b6374782-df59-4b6c-8df3-c82a04a07991",
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.get(\"https://techxplore.com/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "04bd97a6-9e02-4e9a-815f-3b547eef9ed7",
   "metadata": {},
   "outputs": [],
   "source": [
    "for a in driver.find_elements_by_xpath('/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/article[1]/div[1]/h2[1]/a[1]'):\n",
    "    link = a.get_attribute('href')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "a3dcda53-165a-4eb3-8161-742629723c80",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://techxplore.com/news/2022-04-ai-technique-narrowed-candidate-molecules.html'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "link"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "cfd71499-b89f-4c7f-aef8-c11e6b9fcfa3",
   "metadata": {},
   "outputs": [],
   "source": [
    "first_row, first_row_l = [], []\n",
    "first_row.append(driver.find_element_by_xpath(\"/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/article[1]/div[1]/h2[1]/a[1]\").text)\n",
    "first_row.append(link)\n",
    "first_row.append(driver.find_element_by_xpath(\"//div[contains(@class,'col-lg-8')]//article[1]//figure[1]//figcaption[1]//p[1]\").text)\n",
    "first_row.append(driver.find_element_by_xpath(\"/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/article[1]/div[1]/div[1]/span[1]/p[1]\").text)\n",
    "first_row.append(driver.find_element_by_xpath(\"/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/article[1]/div[1]/div[1]/span[2]/p[1]/span[1]\").text)\n",
    "first_row.append(driver.find_element_by_xpath(\"/html[1]/body[1]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/article[1]/div[1]/div[1]/span[3]/p[1]/span[1]\").text)\n",
    "\n",
    "first_row_l.append(first_row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "8df17277-be67-4d84-917e-89070777b90b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>url</th>\n",
       "      <th>subcategory</th>\n",
       "      <th>time</th>\n",
       "      <th>comments</th>\n",
       "      <th>forwards</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AI technique narrowed to only propose candidat...</td>\n",
       "      <td>https://techxplore.com/news/2022-04-ai-techniq...</td>\n",
       "      <td>COMPUTER SCIENCES</td>\n",
       "      <td>3 HOURS AGO</td>\n",
       "      <td>0</td>\n",
       "      <td>64</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                               title  \\\n",
       "0  AI technique narrowed to only propose candidat...   \n",
       "\n",
       "                                                 url        subcategory  \\\n",
       "0  https://techxplore.com/news/2022-04-ai-techniq...  COMPUTER SCIENCES   \n",
       "\n",
       "          time comments forwards  \n",
       "0  3 HOURS AGO        0       64  "
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.DataFrame(first_row_l, columns = ['title', 'url', 'subcategory', 'time', 'comments', 'forwards'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "84220c52-0bf3-4d40-bd23-3686552e4794",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('out.csv', index=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b22a846-d227-459d-b938-4db7843df8d0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
