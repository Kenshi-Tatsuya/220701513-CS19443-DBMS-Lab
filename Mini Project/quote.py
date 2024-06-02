import requests
from bs4 import BeautifulSoup

def getQuote():
    try:
        url = "https://www.brainyquote.com/quote_of_the_day"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        quote_element = soup.find("img", {"id": "qimage_0"})
        if quote_element:
            text = quote_element.get("alt")
            return text
        else:
            return "No quote available"
    except Exception as e:
        print("Error fetching quote:", e)
        return "Error fetching quote"

# Test the function
if __name__ == "__main__":
    print(getQuote())
