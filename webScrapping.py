import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Set Chrome options
options = Options()
options.page_load_strategy = 'normal'
options.add_argument('--enable-automation')
options.headless = True
options.add_argument("window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
options.add_argument("--dns-prefetch-disable")
options.add_argument("--disable-gpu")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Initialize WebDriver with the service and options
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Tags to search
tags = ["array", "dynamic-programming", "string", "math", "hash-table", "linked-list", "two-pointers", "binary-search", "depth-first-search", "greedy", "graph", "binary-tree", "stack", "bit-manipulation", "backtracking", "recursion", "game-theory", "union-find", "counting", "combinatorics", "geometry", "heap-priority-queue", "sliding-window", "probability-and-statistics"]

cnt = 0
urls = []
titles = []
all_ques = []

# Scraping LeetCode problem links
for tag_name in tags:
    link = "https://leetcode.com/tag/" + tag_name
    driver.get(link)
    time.sleep(10)  # Better to use WebDriverWait
    html = driver.page_source
    soup = bs(html, 'html.parser')
    all_ques_div = soup.findAll("div", {"class": "title-cell__ZGos"})

    for ques in all_ques_div:
        if not ques.find("span"):
            if ques.find("a") not in all_ques:
                all_ques.append(ques.find("a"))

# Store problem URLs and titles
for ques in all_ques:
    urls.append("https://leetcode.com" + ques['href'])
    titles.append(ques.text)

with open("leetcode_prob_url.txt", "w+") as f:
    f.write('\n'.join(urls))

with open("leetcode_prob_titles.txt", "w+") as f:
    f.write('\n'.join(titles))

# Scrape problem descriptions
for url in urls:
    driver.get(url)
    cnt += 1
    time.sleep(5)  # Better to use WebDriverWait
    html = driver.page_source
    soup = bs(html, 'html.parser')

    # Extract the problem description
    try:
        problem_text = soup.find('div', {"class": "content__u3I1 question-content__JfgR"}).get_text()

        # Save the problem description to a file
        with open(f"leet_prob_{cnt}.txt", "w+", encoding="utf-8") as f:
            f.write(problem_text)
    except AttributeError:
        print(f"Problem not found at {url}")
        continue

# Clean up by closing the driver
driver.quit()
