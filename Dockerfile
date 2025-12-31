## Multi-stage Dockerfile for building and running the SvelteKit app
# Uses adapter-node output (server entry: `build/index.js`).

FROM node:20-alpine AS builder
WORKDIR /app

# install dependencies (including dev deps for the build)
COPY package*.json ./
RUN npm ci

# Dar permisos de ejecución
RUN chmod -R +x node_modules/.bin

# copy source and build
COPY . .
RUN npm run build

## runtime image
FROM node:20-alpine AS runtime
WORKDIR /app

# copy only production deps and build output
COPY package*.json ./
RUN npm ci --omit=dev
COPY --from=builder /app/build ./build

ENV PORT=3000
EXPOSE 3000

# Start the adapter-node server (entrypoint produced in build/index.js)
CMD ["node", "build/index.js"]
