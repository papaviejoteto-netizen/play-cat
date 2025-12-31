# sv

Everything you need to build a Svelte project, powered by [`sv`](https://github.com/sveltejs/cli).

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```sh
# create a new project in the current directory
npx sv create

# create a new project in my-app
npx sv create my-app
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```sh
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.
> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.

## Despliegue usando Docker (sin `npm` en el host)

Si el servidor donde vas a desplegar no tiene `npm`/Node instalado, puedes construir y ejecutar la aplicación enteramente con Docker. Este repositorio ya incluye un `Dockerfile` multietapa que ejecuta `npm ci` y `npm run build` dentro de la imagen.

- Construir la imagen:
```bash
docker build -t playcatsdemo-app .
```

- Ejecutar el contenedor (mapea el puerto 3000):
```bash
docker run --rm -p 3000:3000 --name playcatsdemo playcatsdemo-app
```

- Usando Docker Compose (reconstruye y levanta los servicios):
```bash
docker compose up --build -d
docker compose logs -f
```

- Modo desarrollo desde un contenedor (edita archivos localmente, sin `npm` instalado en el host):
```bash
docker run --rm -it -v "$PWD":/app -w /app -p 3000:3000 node:18-alpine sh -c "npm ci && npm run dev -- --host"
```

Notas:
- El `Dockerfile` hace la compilación en una etapa `builder` y copia la salida a la imagen de runtime; no necesitas ejecutar `npm run build` en la máquina anfitriona.
- Ajusta el puerto y variables de entorno con `-e PORT=...` o en tu `docker-compose.yml` si lo requieres.

.
├── build/                      # ⬅️ Tu aplicación Svelte compilada (salida de 'npm run build')
│   ├── index.html
│   ├── assets/
│   └── ...
├── data/                       # ⬅️ Directorio para datos persistentes (certificados Let's Encrypt)
│   └── certbot/
│       ├── conf/               # Certificados finales (ej: live/TUDOMINIO.com/)
│       └── www/                # Archivos para el desafío de Certbot (.well-known/acme-challenge)
├── nginx-conf/                 # ⬅️ Archivos de configuración de Nginx
│   └── default.conf            # El archivo con las directivas HTTP y HTTPS
└── docker-compose.yml          # ⬅️ Define los servicios Nginx y Certbot