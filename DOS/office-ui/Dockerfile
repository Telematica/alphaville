FROM mhart/alpine-node:16 AS builder
LABEL author="@telematica"

#ARG NODE_ENV
#ARG REACT_APP_HOST_API
#ARG REACT_APP_HOST_AUTH

WORKDIR /app
COPY . .
ENV GENERATE_SOURCEMAP=false
RUN npm install react-scripts -g --silent
RUN yarn install
RUN yarn run build

FROM mhart/alpine-node
RUN yarn global add serve
WORKDIR /app
COPY --from=builder /app/build .
CMD ["serve", "-p", "80", "-s", "."]doc
