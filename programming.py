import requests

# Get the list of PRs in the free-programming-books repository
response = requests.get("https://api.github.com/repos/EbookFoundation/free-programming-books/pulls")

# Filter the PRs by category
filtered_prs = []
for pr in response.json():
    if pr["labels"][0]["name"] == "category:books":
        filtered_prs.append(pr)

# Print the title and URL of each PR
for pr in filtered_prs:
    print(f"{pr['title']} ({pr['html_url']})")
