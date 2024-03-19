import json


def main():
	f = open("blog-boilerplate.html", "r")
	
	page = f.read()
	
	f.close()
	f = open("currentArticles.js", "r")
	pageList = f.read()
	
	f.close()
	
	print("\n\n\n")
	name = "/blogging/" + input("What's the blog link to use for the page?\n>") + ".html"
	
	if pageList.find(name) != -1:
		print(i["name"] + " has the same link! uh ohhhhh")
		exit()
	
	tag = ""
	article = ""
	while tag != "q":
		tag = input("\nWhat tag? ('h1', 'h2', 'h3', 'p', 'br', 'img')")
		if tag == "img":
			article = article + "<img src='" + input("\n\nimg source? ") + "' alt=''" + input("alt? ") + "'>\n"
		elif tag == "br":
			article = article + "<br>"
		else:
			article = article + "<" + tag + ">" + input("\nenter text\n\n>") + "</" + tag + ">\n"
		print("\nq to quit...")
		tag = input(">")
	page = page.replace("$$$$$$$$", article)
	f = open(name.lstrip("/blogging/"), "w")
	f.write(page)
	f.close()


if __name__ == "__main__":
	main()

