<template>
  <div id="map"></div>
</template>

<script>
import mapboxgl from "mapbox-gl";

export default {
  mounted() {
    // Créer la carte en utilisant l'API de Mapbox GL
    mapboxgl.accessToken = "votre_access_token";
    this.map = new mapboxgl.Map({
      container: "map",
      style: "mapbox://styles/mapbox/streets-v11",
      center: [2.3522, 48.8566], // Centre de Paris
      zoom: 12,
    });

    // Ajouter les données à la carte
    this.map.on("load", () => {
      this.map.addSource("points", {
        type: "geojson",
        data: "url_vers_votre_fichier_geojson",
      });

      this.map.addLayer({
        id: "points",
        type: "circle",
        source: "points",
        paint: {
          "circle-color": "#007cbf",
          "circle-radius": 8,
        },
      });
    });
  },
};
</script>

<style>
#map {
  height: 100vh;
  width: 100%;
}
</style>