import requests
import threading
import datetime

stamp1 = datetime.datetime.today()

print(">> App Started")

# FetchNewsTask IS-A Thread
class FetchNewsTask(threading.Thread):
    # run will contain what task should be done by FetchNewsTask Thread
    def run(self):
        url1 = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=7b950bb5fa384b3bb3b7b9b5d3b350cb"
        print(">> Fetching Response1 from URL1")
        response1 = requests.get(url1)
        print(response1.text)


# FetchBooksTask IS-A Thread
class FetchBooksTask(threading.Thread):
    # run will contain what task should be done by FetchBooksTask Thread
    def run(self):
        url2 = "http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2"
        print(">> Fetching Response2 from URL2")
        response2 = requests.get(url2)
        print(response2.text)
        


booksTask = FetchBooksTask()
newsTask = FetchNewsTask()

# start will internally execute run method (Parallel Execution)
newsTask.start()
booksTask.start()

for i in range(1, 11):
    print(">> i is:",i)



print(">> App Finished")
stamp2 = datetime.datetime.today()

print(">> Time Taken by Main Thread is:",stamp2-stamp1)

# Conclusion : We need Asynchronous Programing when main has burden