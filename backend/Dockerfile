FROM golang:1.18

WORKDIR /

COPY server/go.mod server/go.sum ./
RUN go mod download && go mod verify

COPY server/ .
EXPOSE 8080
RUN go build

CMD ["./somedude"]
