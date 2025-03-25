import requests
from bs4 import BeautifulSoup
import os
from zipfile import ZipFile


# function to download pdfs
def download_pdf(url: str, folder: str):

    # gets pdf from url
    response = requests.get(url)

    # checks if function was able to request to url
    if response.status_code != 200:
        return None
    
    # creates string to represent where the file will be saved and it's name
    file_name = os.path.join(folder, url.split('/')[-1])

    # opens or creates file to save pdf content
    with open(file_name, 'wb') as file:
        file.write(response.content)

    return file_name


# function to get content from page
def get_data(url: str, folder: str, zip_file_name: str):

    # gets data from url
    response = requests.get(url)

    # checks if function was able to request to url
    if response.status_code != 200:
        raise Exception("Unable to request to url")
    
    # uses BeatifulSoup to parse html content
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')


    pdf_links = []

    # iterates over all <a> html elements
    for link in soup.find_all('a', href=True):

        # gets text from <a> html element
        text = link.text.lower()

        # checks if the href value of the current <a> html element points to a pdf and if it's an anexo
        if link['href'].endswith('.pdf') and "anexo" in text:

            # process the pdf link in case it is a relative link
            full_url = link['href'] if link['href'].startswith('http') else 'https://www.gov.br' + link['href']
            pdf_links.append(full_url)

    # checks if at least one pdf was found
    if not pdf_links:
        print("No PDFs found")
        return
    
    # creates a folder to save the pdf's found
    if not os.path.exists(folder):
        os.makedirs(folder)


    downloaded_files = []

    # download pdfs found
    for pdf_url in pdf_links:
        
        # uses function to download pdf
        downloaded_file = download_pdf(pdf_url, folder)

        # checks if pdf was downloaded and saves it's name
        if downloaded_file:
            downloaded_files.append(downloaded_file)

    # zip pdfs in one file
    if downloaded_files:

        # creates string to represent where the file will be saved and it's name
        zip_file_name = os.path.join(folder, zip_file_name)

        # creates zip file from string
        with ZipFile(zip_file_name, 'w') as zipf:

            # adds each pdf downloaded
            for file in downloaded_files:
                zipf.write(file, os.path.basename(file))


if __name__ == "__main__":

    # url to get content from
    site_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    # folder to save pdfs
    folder = "pdfs"

    # name of final zip file
    zip_file_name = "anexos.zip"

    try:
        get_data(site_url, folder, zip_file_name)
    except Exception as e:
        print(f"Error: {str(e)}")
        