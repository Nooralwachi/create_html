def create_html():
	items = ['first string', 'second string']
	html_str = '<ul>\n'
	for item in items:
		html_str += '<li>' + item +'</li>\n'
	html_str += '</ul>\n'
	print(html_str)
	
create_html()