## para hacer deploy en app engine
gcloud app deploy app.yaml --project "Nombre del proyecto"

## para subir un contenedor a GCP

gcloud config set project tradingview2-420717
gcloud config set project tradingview3

gcloud builds submit --tag gcr.io/tradingview2-420717/webapp:0.0.1
gcloud builds submit --tag gcr.io/tradingview3/webapp:0.0.1


gcr.io/tradingview2-420717/webapp@sha256:c39efb1455b5b707a3ea37c5cc44558d4285774c5f142d7bada2ebaefd25e9c9

SOURCE: gs://tradingview2-420717_cloudbuild/source/1714684651 590114-06bf02a937e94f6db574136b97f0fb34.tgz
IMAGES: gcr.io/tradingview2-420717/webapp:0.0.1

SOURCE: gs://tradingview3_cloudbuild/source/1715827294.342371-a29fb9ea404742099ec974e92b4f9fca.tgz
IMAGES: gcr.io/tradingview3/webapp:0.0.1
STATUS: SUCCESS

gcr.io/tradingview3/webapp@sha256:4d534c9ac1b8f42a69cb27b0543a37140d441db85862ac1a815fded7ee48ed80


# listar proyectos
gcloud projects list --format="value(projectId)"

# listar servicios
gcloud iam service-accounts list --project tradingview2-420717
gcloud iam service-accounts list --project tradingview3

# desactivar un servicio
gcloud iam service-accounts disable 743927460834-compute@developer.gserviceaccount.com --project tradingview3

gcloud iam service-accounts disable tradingview@tradingview3.iam.gserviceaccount.com --project tradingview3


# activar un servicio
gcloud services enable 743927460834-compute@developer.gserviceaccount.com--project tradingview3


# eliminar un servicio

gcloud iam service-accounts delete tradingview@tradingview3.iam.gserviceaccount.com --project tradingview3

# eliminar un proyecto
gcloud projects delete fast-gateway-416821


# subir una imgen de docker a GCP
## Etiquetar la imagen
docker tag [NOMBRE_IMAGEN] gcr.io/[TU_PROYECTO_ID]/[NOMBRE_IMAGEN]

## Subir la imagen
docker push gcr.io/[TU_PROYECTO_ID]/[NOMBRE_IMAGEN]




