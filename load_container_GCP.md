## para hacer deploy en app engine
gcloud app deploy app.yaml --project "Nombre del proyecto"

## para subir a un contenedor a GCP

gcloud config set project tradingview2-420717
gcloud builds submit --tag gcr.io/tradingview2-420717/webapp:0.0.1


gcr.io/tradingview2-420717/webapp@sha256:c39efb1455b5b707a3ea37c5cc44558d4285774c5f142d7bada2ebaefd25e9c9

SOURCE: gs://tradingview2-420717_cloudbuild/source/1714684651 590114-06bf02a937e94f6db574136b97f0fb34.tgz
IMAGES: gcr.io/tradingview2-420717/webapp:0.0.1


# listar proyectos
gcloud projects list --format="value(projectId)"

# listar servicios
gcloud iam service-accounts list --project tradingview2-420717

# desactivar un servicio
gcloud iam service-accounts disable 403177431120-compute@developer.gserviceaccount.com --project tradingview2-420717

# activar un servicio
gcloud services enable 403177431120-compute@developer.gserviceaccount.com --project tradingview2-420717


# eliminar un servicio
gcloud iam service-accounts delete tradingview2-420717@appspot.gserviceaccount.com --project tradingview2-420717

# eliminar un proyecto
gcloud projects delete fast-gateway-416821
