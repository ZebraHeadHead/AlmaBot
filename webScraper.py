import csv
import os
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def getList(website):
    # Set up headless Chrome browser
    options = Options()
    options.add_argument("--headless")  # Run in the background

    service = Service(ChromeDriverManager().install())
    # service.start()
    driver = webdriver.Chrome(service=service, options=options)
    # Open website

    driver.get(website)
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='row']/div[@class='col-sm-4']"))
    )
    cols = driver.find_elements(
        By.XPATH, "//div[@class='row']/div[@class='col-sm-4']")

    result = [cols[i].text for i in range(1, 4)]
    driver.quit()
    return result


def findItemNames(ui_entry, output_label):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "Material.csv")

    output_list = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        # Assuming data is in the first column (row[0])
        data = [row[0] for row in reader]

        while True:
            # Get user input
            user_input = ui_entry.strip()

            if user_input:
                # Find matches (case-insensitive partial match)
                matches = [item for item in data if user_input.lower()
                           in item.lower()]
                if len(matches) > 3:
                    output_label.config(
                        "Too vague, please try to be more specific")
                elif matches:
                    output_text = "Matching results:\n"
                    for match in matches:
                        output_text += f"- {match}\n"
                        output_list.append(match)
                    return output_list  # return the list that will be used for making websites

                else:
                    output_label.config("No matches found. Try again.")
            else:
                output_label.config("Please enter a valid search term.")


def namesIntoLinks(input: List[str]):
    links = []
    for i in input:
        encoded = i.replace(" ", "+")
        address = "https://monsterhunterwilds.wiki.fextralife.com/" + encoded
        links.append(address)
    # print(links)
    return links

# for testing


def runAll():
    for i in namesIntoLinks(findItemNames()):
        getList(i)
