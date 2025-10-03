# Build stage
FROM golang:1.21-alpine AS builder

WORKDIR /app

# Install git for fetching dependencies
RUN apk add --no-cache git

# Copy go.mod and go.sum files
COPY go.mod go.sum ./

# Download dependencies
RUN go mod download

# Copy source code
COPY . .

# Build the application
# CGO_ENABLED=0 creates a static binary
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o /app/stocks-data-sync

# Final stage
FROM gcr.io/distroless/static:nonroot

WORKDIR /app

# Copy the binary from builder
COPY --from=builder /app/stocks-data-sync /app/stocks-data-sync

# Use nonroot user
USER nonroot:nonroot

# Run the binary
ENTRYPOINT ["/app/stocks-data-sync"]