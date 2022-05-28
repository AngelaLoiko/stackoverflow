import requests


def get_question():
    # /2.3/questions?fromdate=1653609600&todate=1653696000&order=desc&sort=activity&tagged=python&site=stackoverflow
    url = 'https://api.stackexchange.com//2.3/questions?fromdate=1653609600&todate=1653696000' \
          '&order=desc&sort=activity&tagged=Python&site=stackoverflow'
    response = requests.get(url)
    listofquestios = []
    for item in response.json()['items']:
        listofquestios.append(item['question_id'])
       #  listofquestios.append(item['title'])
       #  listofquestios.append(item['link'])
    print(listofquestios)

if __name__ == '__main__':
    get_question()