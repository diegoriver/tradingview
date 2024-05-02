## para hacer deploy en app engine
gcloud app deploy app.yaml --project "Nombre del proyecto"

## para subir a un contenedor a GCP

gcloud config set project tradingview2-420717
gcloud builds submit --tag gcr.io/tradingview2-420717/webapp:0.0.1


