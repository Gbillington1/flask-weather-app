FROM nikolaik/python-nodejs

# set a directory for the app
WORKDIR /usr/src/flask-weather

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# build tailwind css
RUN npm run build

# define the port number the container should expose
EXPOSE 5000

# start the app
CMD ["flask", "run", "--host=0.0.0.0"]
