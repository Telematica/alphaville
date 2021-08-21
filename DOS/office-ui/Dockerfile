FROM mhart/alpine-node:14
LABEL author="@telematica"

ARG NODE_ENV
ARG REACT_APP_HOST_API
ARG REACT_APP_HOST_AUTH

ENV APP_DIR=/app
WORKDIR $APP_DIR

COPY . .

RUN yarn global add react-scripts

RUN yarn install

RUN yarn run build

RUN yarn global add serve

COPY scripts/run_service.sh $APP_DIR

CMD ["/app/run_service.sh"]
