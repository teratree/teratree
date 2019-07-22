FROM alpine:3.10 as base

RUN apk --no-cache add curl bash nodejs
RUN curl https://cli-assets.heroku.com/install.sh | sh

FROM base as run
ENTRYPOINT ["heroku"]
