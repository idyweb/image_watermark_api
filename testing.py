url = '<img src="https://res.cloudinary.com/asakas/image/upload/l_text:montserrat_55:bruno/af4nk6h7uycz9z6x8cmg"/>'

url = url.strip('<img src="').strip('"/>')
print(url)
