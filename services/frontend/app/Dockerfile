FROM node:18.19.0-slim

ENV PATH /app/node_modules/.bin:$PATH


# Install necessary build dependencies
RUN apt-get update && \
    apt-get install -y python3 build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*



#Create a working directory
WORKDIR /usr/src/app

RUN npm install -g @vue/cli@5.0.8

COPY package.*json ./

RUN npm install


CMD ["npm", "run", "serve"]
