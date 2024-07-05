import json


def main():
	f = open("blog-boilerplate.html", "r")
	page = f.read()
	f.close()

	f = open("currentArticles.js", "r")
	page_list = f.read()
	f.close()
	
	print("\n\n\n")
	name = input("What's the blog link to use for the page?\n>")

	if page_list.find("/blogging/" + name + ".html") != -1:
		print(i["name"] + " has the same link! uh ohhhhh")
		exit()
	page = page.replace("###", name)
	tag = ""
	article = ""
	while input("q to quit:") != "q":
		tag = input("\nWhat tag? ('h1', 'h2', 'h3', 'p', 'br', 'img') \n")
		article = add_tag(article, tag)
		print(article)
	page = page.replace("$$$$$$$$", article)
	f = open(name, "w")
	f.write(page)
	f.close()

def add_tag(article, tag):
	if tag == "img":
		return article + "<img src='" + input("\nImage Location: ") + "'>"
	if tag == "br":
		return article + "<br>"
	return article + "<" + tag + ">" + input("\nText: ") + "</" + tag + ">"

if __name__ == "__main__":
	main()

