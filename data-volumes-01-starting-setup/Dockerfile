FROM node

WORKDIR /tempp

COPY package.json  /tempp/

RUN npm install

COPY . /tempp/

EXPOSE 80

CMD [ "node", "server.js" ]