import React from 'react';
import {createRoot} from 'react-dom/client';
import {APIProvider, Map} from '@vis.gl/react-google-maps';

const App = () => (
  <APIProvider apiKey={AIzaSyB6lBBQu2yrWdLZ4qOgWtIx7iCMtRcAeeM}>
    <Map
      style={{width: '100vw', height: '100vh'}}
      defaultCenter={{lat: 22.54992, lng: 0}}
      defaultZoom={3}
      gestureHandling={'greedy'}
      disableDefaultUI={true}
    />
  </APIProvider>
);

const root = createRoot(document.querySelector('#app'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);