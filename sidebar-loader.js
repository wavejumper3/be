
const toggleBtn = document.getElementById('toggleBtn');
const panel = document.querySelector('.panel');
const listOfLinks = document.getElementById('link-list');

currentLinks.forEach((article) => {
	var a = document.createElement("a");
	var link = document.createTextNode(article.name);
	a.appendChild(link);
	a.href = article.link;
	var li = document.createElement("li");
	li.appendChild(a);
	listOfLinks.appendChild(li);
});

toggleBtn.addEventListener('click', () => {
	if (panel.style.display == 'none') {panel.style.display = "inline";} else {panel.style.display = "none"}
});