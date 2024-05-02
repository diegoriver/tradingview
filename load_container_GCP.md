## para hacer deploy en app engine
gcloud app deploy app.yaml --project "Nombre del proyecto"

## para subir a un contenedor a GCP

gcloud config set project tradingview2-420717
gcloud builds submit --tag gcr.io/tradingview2-420717/webapp:0.0.1


gcr.io/tradingview2-420717/webapp@sha256:6adf62ea77f320e1ec5abe237b79607ab16354199fce312fb2cb40c0a81a96cf
