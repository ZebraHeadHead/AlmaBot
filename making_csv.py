import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def makingCSV(output_file):
    options = Options()
    options.add_argument("--headless")  # Run in the background

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get("https://monsterhunterwilds.wiki.fextralife.com/Materials")
        rows = driver.find_elements(
            By.XPATH, "//*[@id='wiki-content-block']/div[4]/table/tbody/tr")

        # Prepare data for CSV
        data = []
        for row in rows:
            try:
                # Extract the <a> text inside the first <td>
                link_element = row.find_element(By.XPATH, "./td[1]/h5/a")
                link_text = link_element.text.strip()
                print(link_text)
                # Append the extracted text as a list (for CSV row)
                data.append([link_text])
            except Exception as e:
                # If <a> is not found in this row
                data.append(["No link found"])

        # Write the data to a CSV file
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Link Text"])  # Header row
            writer.writerows(data)  # Write the data rows

        print(f"Data saved to {output_file}")
    finally:
        driver.quit()
    return None


makingCSV("G:\monhunBot/Material.csv")
