<template>
    <header class="header">
        <h1>Cartographie</h1>
    </header>
    <main class="main">
        <section id="map"></section>
        <article>
            <div class="popup" id="info">
                <h1>Informations</h1>
                <p>Cliquer sur un point pour afficher ses informations.</p>
            </div>
            <hr id="separatorHelp">
            <div class="help">
                <h1>Aide</h1>
                <ul>
                    <li>Utiliser la molette de la souris pour zoomer.</li>
                    <li>Utiliser le clic droit de la souris pour déplacer la carte.</li>
                    <li>Utiliser le clic gauche de la souris pour sélectionner un point.</li>
                    <li>Utiliser le clic molette de la souris pour réinitialiser la carte.</li>
                </ul>
            </div>
        </article>
    </main>
</template>

<script>
import mapboxgl from "mapbox-gl";

import data from "../../Dataset/dataset.json";

const FranceCenter = [2.2137, 46.2276] // Centre de la France
//const ParisCenter [2.3522, 48.8566] // Centre de Paris
const defaultZoom = 5.5

export default {
    mounted() {
        // Créer la carte en utilisant l'API de Mapbox GL
        mapboxgl.accessToken = "token" // todo: add token
        this.map = new mapboxgl.Map({
            container: "map",
            style: "mapbox://styles/mapbox/streets-v11",
            center: FranceCenter,
            zoom: defaultZoom,
            attributionControl: false
        });

        // Ajouter les données à la carte
        this.map.on("load", () => {
            this.map.addSource("points", {
                type: "geojson",
                data: data,
            });

            // Ajouter une couche de cercle pour les points
            this.map.addLayer({
                id: 'points',
                type: 'circle',
                source: 'points',
                paint: {
                    'circle-radius': 8,
                    'circle-color': '#ff0000'
                }
            });
        });

        // Ajouter un popup pour afficher les informations des points
        this.map.on('click', 'points', function (e) {

            let node = e.features[0].properties.node;
            let indicateur1 = e.features[0].properties.indicateur_1;
            let indicateur2 = e.features[0].properties.indicateur_2;
            let indicateur3 = e.features[0].properties.indicateur_3;

            // Créer le contenu du popup
            let popupContent = '<h1>' + node + '</h1>' +
                '<ul>' +
                '<li>Indicateur 1: ' + indicateur1 + '</li>' +
                '<li>Indicateur 2: ' + indicateur2 + '</li>' +
                '<li>Indicateur 3: ' + indicateur3 + '</li>' +
                '</ul>';

            let info = document.getElementById('info');
            info.innerHTML = popupContent;
        });

        // Changer le curseur de la souris lorsqu'elle survole les points
        this.map.on('mouseenter', 'points', function () {
            this.getCanvas().style.cursor = 'pointer';
        });

        // Changer le curseur de la souris lorsque la souris quitte les points
        this.map.on('mouseleave', 'points', function () {
            this.getCanvas().style.cursor = '';
        });

        // reset info et la map + rotation si click mollette
        this.map.on('mousedown', function (e) {
            if (e.originalEvent.button === 1) {
                // Réinitialiser l'info et la carte
                let info = document.getElementById('info');
                info.innerHTML = '<h1>Informations</h1>' +
                    '<p>Cliquer sur un point pour afficher ses informations.</p>';

                // Réinitialiser la carte
                this.flyTo({
                    center: FranceCenter,
                    zoom: defaultZoom,
                    bearing: 0,
                    pitch: 0,
                    speed: 0.5,
                    curve: 1
                });
                // Rotation de la carte
                this.once('moveend', function () {
                    this.rotateTo(0, {
                        duration: 2000
                    });
                });
            }
        });
    },
};
</script>

<style>

.header h1 {
    margin: 0;
    padding: 10px;
    background-color: #ffffff;
    border-radius: 5px;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 24px;
    line-height: 1.5;
    z-index: 1;
    text-align: center;
}

.main {
    position: relative;
    height: 90vh;
    width: 90vw;
    padding: 10px;
}

.main section {
    position: absolute;
    height: 100%;
    width: 100%;
}

.main article {
    position: absolute;
    top: 0;
    left: 0;
    margin: 15px;
    padding: 10px;
    background-color: #ffffff;
    border-radius: 5px;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 12px;
    line-height: 1.5;
    z-index: 1;
}


.popup {
    text-decoration-color: black;
}

.popup h1 {
    font-size: 18px;
    font-weight: bold;
    text-decoration-color: black;
}

.popup ul,p {
    font-size: 14px;
    text-decoration-color: black;
}


.help {
    text-decoration-color: gray;
}

.help h1 {
    font-size: 12px;
    font-weight: bold;
    text-decoration-color: gray;
}

.help ul,p {
    font-size: 10px;
    text-decoration-color: gray;
}

#separatorHelp {
    margin-top: 10px;
    margin-bottom: 10px;
    border: 1px solid black;
    width: 100%;

}

</style>
