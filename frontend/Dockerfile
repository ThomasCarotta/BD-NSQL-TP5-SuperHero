# # frontend/Dockerfile
# FROM node:18-alpine as build
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . .
# RUN npm run build

# FROM nginx:alpine
# COPY --from=build /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]

FROM node:latest

# 🔧 Solución para el error de OpenSSL
ENV NODE_OPTIONS=--openssl-legacy-provider

WORKDIR /frontreact
COPY . .

RUN npm install --silent
RUN npm install react-scripts@3.0.1 -g --silent



EXPOSE 3000

#RUN npm run build
CMD npm start