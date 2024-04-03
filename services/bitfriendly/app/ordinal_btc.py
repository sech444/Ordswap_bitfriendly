#from fastapi import FastAPI
import requests
import json
from bs4 import BeautifulSoup

#@app.get("/fetch_and_create_html")
def fetch_and_create_html():
    start = 63339
    end = 64301
    limit = 1000
l
    try:
        response = requests.get(f'ordapi.xyz/inscriptions/?start={start}&end={end}&limit={limit}')
        inscription_data = json.loads(response.text)
       

        with open('ids.txt', 'r') as file:
            id_list = file.read().split('\n')
            print(id_list)

            for index, id in enumerate(id_list):
                response = requests.get(f'https://ordinals.com/content/{id}')
                soup = BeautifulSoup(response.text, 'html.parser')

                container_div = soup.new_tag('div')
                container_div['class'] = 'inscription-item'

                image_container = soup.new_tag('div')
                image_container['class'] = 'image-container'

                image = soup.new_tag('img', src=f'https://ordinals.com/content/{id}', id=f'img{index}', class_=f'img{index}')
   
                link = soup.new_tag('a', href=f'../inscription?id={id}', id=f'link{index}', class_=f'link{index}')
         
                try:
                    title = soup.new_tag('title', href=f'../inscription?id={id}', id=f'title{index}', class_=f'title{index}')
                    title.string = inscription_data['title']
                except KeyError:
                    print("'title' not in dictionary")
                    pass
                except Exception as e:
                    print(f"Error: {e}")

                guid = soup.new_tag('a', href=f'../inscription?id={id}', id=f'guid{index}', class_=f'guid{index}')

                image_container.append(image)
                image_container.append(soup.new_tag('hr'))
                image_container.append(link)
                container_div.append(image_container)
                container_div.append(title)
                container_div.append(soup.new_tag('br'))
                container_div.append(guid)

                inscription_grid = soup.find(class_='inscription-grid')
                if inscription_grid is not None:
                    inscription_grid.append(container_div)
                else:
                    print("'inscription-grid' class not found in the HTML")


        return inscription_data

    except Exception as e:
        print(f"Error: {e}")


#print(fetch_and_create_html())


import requests as r

API_URL = "https://ordapi.xyz"
start_index = 1000
end_index = 1100
limit = 10
arguments = "?start={}&end={}&limit={}".format(start_index, end_index, limit)
content = r.get(API_URL+"/inscriptions/"+arguments).json()
print(content) # -> will show the JSON from the response


# import requests
# import json
# from bs4 import BeautifulSoup


# # #@app.get("/fetch_and_create_html")
# def fetch_and_create_html():
#     start = 63339
#     end = 64301
#     limit = 1000

#     try:
#         response = requests.get(f'https://ordapi.xyz/inscriptions/?start={start}&end={end}&limit={limit}')
#         inscription_data = json.loads(response.text)
#         print(response)

#         with open('ids.txt', 'r') as file:
#             id_list = file.read().split('\n')

#             for index, id in enumerate(id_list):
#                 response = requests.get(f'https://ordinals.com/content/{id}')
#                 soup = BeautifulSoup(response.text, 'html.parser')

#                 container_div = soup.new_tag('div')
#                 container_div['class'] = 'inscription-item'

#                 image_container = soup.new_tag('div')
#                 image_container['class'] = 'image-container'
            

#                 image = soup.new_tag('img', src=f'https://ordinals.com/content/{id}', id=f'img{index}', class_=f'img{index}')

#                 link = soup.new_tag('a', href=f'../inscription?id={id}', id=f'link{index}', class_=f'link{index}')
#                 try:
#                     title = soup.new_tag('title', href=f'../inscription?id={id}', id=f'title{index}', class_=f'title{index}')
#                     title.string = inscription_data['title']
#                 except KeyError:
#                     print("'title' not in dictionary")
#                     pass
#                 except Exception as e:
#                     print(f"Error: {e}")

#                 # title = soup.new_tag('title', href=f'../inscription?id={id}', id=f'title{index}', class_=f'title{index}')
#                 # title.string = inscription_data['title']
               

#                 guid = soup.new_tag('a', href=f'../inscription?id={id}', id=f'guid{index}', class_=f'guid{index}')
               

#                 image_container.append(image)
#                 image_container.append(soup.new_tag('hr'))
#                 image_container.append(link)
#                 container_div.append(image_container)
#                 container_div.append(title)
#                 container_div.append(soup.new_tag('br'))
#                 container_div.append(guid)

#                 inscription_grid = soup.find(class_='inscription-grid')
#                 if inscription_grid is not None:
#                     inscription_grid.append(container_div)
#                 else:
#                     print("'inscription-grid' class not found in the HTML")
#                     print(inscription_data)
#         return inscription_data

#     except Exception as e:
#         print(f"Error: {e}")


# print(fetch_and_create_html())
