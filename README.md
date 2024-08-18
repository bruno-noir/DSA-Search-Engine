# DSA-Search-Engine

The **DSA-Search-Engine** is a custom search engine project centered on data structures and algorithms. It consists of four major components, each serving a distinct role in building the search functionality:

1. **Web Scraping**  
   - Extract problem data from coding platforms (e.g., LeetCode, CodeChef, HackerRank, Codeforces).
   - Use Python's `BeautifulSoup` and `Selenium` to identify and scrape problem titles, URLs, and descriptions.
   - Customizable scraping logic for different platforms by adjusting HTML tag selection.

2. **TF-IDF Calculation**  
   - Generate a corpus of scraped data and extract relevant keywords using the `nltk` library.
   - Perform **Term Frequency (TF)** and **Inverse Document Frequency (IDF)** calculations to rank keywords by importance.
   - Output includes a matrix of TF-IDF values saved in files like `all_keywords.txt`, `tf_idf_matrix.txt`, and `idf.txt`.

3. **Data Storage in MongoDB**  
   - Store the scraped data and calculated TF-IDF results in a MongoDB database.
   - Use a Node.js server with Express.js to handle data storage and retrieval operations.
   - Define and structure database models in a `models` directory to ensure consistent and organized data storage.

4. **Web Application Interface**  
   - Use Express.js to build a user-friendly web interface for interacting with the search engine.
   - Enable users to search for algorithm problems based on keywords derived from TF-IDF calculations.
   - Display relevant problems with their corresponding metadata from the MongoDB database.

---

## How to Install and Run the Project Locally

### 1. Web Scraping

- Run the `webScrapping.py` script to scrape problems from your chosen platforms (default is LeetCode).
- If using a different platform, inspect the webpage to find the correct HTML tags for titles, URLs, and descriptions.
- Customize the scraping logic accordingly, and store the extracted data locally in text files.

### 2. Keyword Extraction and TF-IDF Calculation

- Run the `tf_idf.py` script to process the scraped data.
- This script uses the `nltk` library to filter stopwords and extract keywords from the corpus.
- The output will include keyword lists and a TF-IDF matrix, saved as text files (`all_keywords.txt`, `tf_idf_matrix.txt`, `idf.txt`).

### 3. Database Storage with MongoDB

- Use `server.js` to upload your locally generated data to a MongoDB server.
- Create a `models` directory to define the schema for each data model (problems, keywords, etc.).
- Configure MongoDB connection settings to ensure proper data storage on the server.

### 4. Running the Web Application

- Once the data is stored in MongoDB, run the Express.js server to launch the web application.
- Access the application via a browser to search for algorithm problems and view relevant results.
